#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 paper_index.md 生成自包含的文献整理网页 (gr_doc/paper/index.html)。

无外部依赖。所有图表 / 表格在生成时就静态预渲染进 HTML（不依赖 JS），
JS 仅作为搜索 / 筛选的交互增强（无 JS 时表格依然完整可见）。
"""
import json
import re
import os
import sys
import html
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data') if os.path.isdir(os.path.join(HERE, 'data')) else '/tmp'
SRC = os.path.join(HERE, 'index.md')
OUT = os.path.join(HERE, 'index.html')
# 预览模式(仅自查用): full(默认) / sheets(只看图表) / tbl(只看表格) / short(图表+前8行)
MODE = sys.argv[1] if len(sys.argv) > 1 else 'full'

esc = lambda s: html.escape(str(s if s is not None else ''), quote=True)

lines = open(SRC, encoding='utf-8').read().split('\n')

papers = []
arxiv = {}          # 编号 -> url
section = None
sec_order = []
in_arxiv_block = False
in_reading = False
reading_lines = []  # §9 阅读路径建议 的原始行
READING_SEC = '阅读路径建议'
num_re = re.compile(r'^##\s*(\d+)\.\s*(.+?)\s*$')

for ln in lines:
    m = num_re.match(ln)
    if m:
        section = m.group(2).strip()
        if section not in sec_order:
            sec_order.append(section)
        in_arxiv_block = False
        in_reading = (section == READING_SEC)
        continue
    if ln.startswith('## 附'):
        in_arxiv_block = True
        section = None
        in_reading = False
        continue
    if ln.startswith('## '):
        in_reading = False
        continue
    if in_reading:
        reading_lines.append(ln)
        continue
    if not ln.strip().startswith('|'):
        continue
    cells = [c.strip() for c in ln.strip().strip('|').split('|')]
    if all(re.fullmatch(r':?-{2,}:?', c) for c in cells if c) or not cells:
        continue
    if cells[0] in ('文件', '编号'):
        continue
    # arxiv 表: | 编号 | 论文 | arxiv |
    if in_arxiv_block:
        if len(cells) >= 3 and cells[0].isdigit():
            url = re.search(r'https?://\S+', cells[2])
            if url:
                arxiv[cells[0].zfill(2)] = url.group(0)
        continue
    if section is None:
        continue
    # 论文表: 6列(文件|机构|年份|任务|类型|说明) / 4列(文件|机构|年份|说明) / 3列(文件|年份|说明)
    if len(cells) >= 6:
        f, org, year, task, typ = cells[0], cells[1], cells[2], cells[3], cells[4]
        note = ' | '.join(cells[5:])
    elif len(cells) >= 4:
        f, org, year, note = cells[0], cells[1], cells[2], ' | '.join(cells[3:])
        task = typ = '-'
    elif len(cells) == 3:
        f, org, year, note = cells[0], '-', cells[1], cells[2]
        task = typ = '-'
    else:
        continue
    for fname in re.split(r'\s*/\s*', f):
        fname = fname.strip().strip('`').strip()
        if not fname.lower().endswith('.pdf'):
            continue
        y = re.search(r'\d{4}', year)
        papers.append({
            'file': fname,
            'title': re.sub(r'\.pdf$', '', fname),
            'org': org if org and org != '-' else '未标注',
            'year': y.group(0) if y else '未知',
            'task': task if task and task != '-' else '—',
            'type': typ if typ and typ != '-' else '—',
            'cat': section,
            'note': note.strip(),
            'arxiv': None,
        })

# arxiv 表里的"论文"是简称(TIGER/P5/...), 而文件名是完整标题 -> 用标题关键字匹配
ARXIV_KW = {
    '02': 'Recommender Systems with Generative Retrieval',
    '03': 'Recommendation as Language Processing',
    '07': 'GPT4Rec',
    '08': 'TALLRec',
    '09': 'LLaRA',
    '10': 'Adapting Large Language Models by Integrating Collaborative Semantics',
    '11': 'Learning Vector-Quantized Item Representation',
}
for p in papers:
    for num, kw in ARXIV_KW.items():
        if kw.lower() in p['file'].lower():
            p['arxiv'] = arxiv.get(num)
            break

# 直接按标题关键字给的 arxiv 链接(2026-09 A 会新增批次)
ARXIV_DIRECT = {
    'Text Is All You Need': 'https://arxiv.org/abs/2305.13731',
    'IDGenRec': 'https://arxiv.org/abs/2403.19021',
    'Bridging Items and Language': 'https://arxiv.org/abs/2310.06491',
    'A Neural Corpus Indexer': 'https://arxiv.org/abs/2206.02743',
    'Generative Retrieval as Multi-Vector Dense Retrieval': 'https://arxiv.org/abs/2404.00684',
    'Learning to Rank in Generative Retrieval': 'https://arxiv.org/abs/2306.15222',
    'Generative Recommender with End-to-End Learnable Item Tokenization': 'https://arxiv.org/abs/2409.05546',
    'Semantic Convergence': 'https://arxiv.org/abs/2412.13771',
    'Towards Universal Sequence Representation Learning': 'https://arxiv.org/abs/2206.05941',
    'Representation Learning with Large Language Models for Recommendation': 'https://arxiv.org/abs/2310.15950',
    'Customizing Language Models with Instance-wise LoRA': 'https://arxiv.org/abs/2408.10159',
    'RecGPT': 'https://arxiv.org/abs/2405.12715',
    'SLMRec': 'https://arxiv.org/abs/2405.17890',
    'Scaling Transformers for Discriminative Recommendation': 'https://arxiv.org/abs/2506.03699',
    'EAGER-LLM': 'https://arxiv.org/abs/2502.14735',
    'Leveraging Passage Embeddings for Efficient Listwise Reranking': 'https://arxiv.org/abs/2406.14848',
    'Wukong': 'https://arxiv.org/abs/2403.02545',
    'LLM-ESR': 'https://arxiv.org/abs/2405.20646',
    'E4SRec': 'https://arxiv.org/abs/2312.02443',
    'RecRanker': 'https://arxiv.org/abs/2312.16018',
    'Molar: Multimodal LLMs': 'https://arxiv.org/abs/2412.18176',
    'Sparse Meets Dense': 'https://arxiv.org/abs/2503.02453',
}
for p in papers:
    if p.get('arxiv'):
        continue
    for kw, url in ARXIV_DIRECT.items():
        if kw.lower() in p['file'].lower():
            p['arxiv'] = url
            break

# 2026-09 扩充批次的 arxiv 链接（按文件名直接映射）
try:
    _na = json.load(open(os.path.join(DATA, 'new_arxiv.json'), encoding='utf-8'))
except Exception:
    _na = {}
for p in papers:
    if not p.get('arxiv') and p['file'] in _na:
        p['arxiv'] = _na[p['file']]

# 去重(按 file, 保留首次出现 = 更靠前的分类)
seen = {}
for p in papers:
    seen.setdefault(p['file'], p)
papers = list(seen.values())

# 年份回退: 从文件名里找 20xx
for p in papers:
    if p['year'] == '未知':
        y = re.search(r'(20\d{2})', p['file'])
        if y:
            p['year'] = y.group(1)

# 图表用的短分类名
for p in papers:
    p['catShort'] = re.sub(r'[（(].*?[)）]', '', p['cat']).strip()

# 稳定 id（供阅读路径跳转）+ 新增批次日期（data/added.json: file -> "YYYY-MM-DD"）
for _i, p in enumerate(papers):
    p['pid'] = _i
try:
    ADDED = json.load(open(os.path.join(DATA, 'added.json'), encoding='utf-8'))
except Exception:
    ADDED = {}
LATEST_ADD = max(ADDED.values()) if ADDED else ''
for p in papers:
    p['added'] = ADDED.get(p['file'], '')

# 机构归一：把同一实体的不同写法/子品牌/地区合并（用于展示、筛选、图表的机构维度）
ORG_MERGE = {
    # 公司子品牌 / 地区分部
    '阿里国际': '阿里', '华为爱尔兰': '华为', '腾讯微信': '腾讯',
    '抖音': '字节', '字节（国际电商）': '字节',
    'Google Cloud': 'Google', 'Google DeepMind': 'Google',
    # 简称 / 中英文写法
    '港中文': '香港中文大学', '港大': '香港大学', '港科大': '香港科技大学',
    '北航': '北京航空', '华科': '华中科技',
    'Glasgow': 'University of Glasgow', 'Leiden': 'Leiden University',
    'Queensland': 'The University of Queensland', 'Yonsei': 'Yonsei University',
}
def _norm_org(s):
    parts = [ORG_MERGE.get(x.strip(), x.strip()) for x in re.split(r'\s*/\s*', s)]
    return ' / '.join(dict.fromkeys([x for x in parts if x]))
for p in papers:
    p['org'] = _norm_org(p['org'])

# ---------------------------------------------------------------- 摘要（英文 + 中文）
ABS_EN, ABS_ZH = {}, {}
try:
    ABS_EN = json.load(open(os.path.join(DATA, 'abstracts_en.json'), encoding='utf-8'))
except Exception:
    pass
for _f in [os.path.join(DATA, 'abs_zh_%d.json' % _i) for _i in (1, 2, 3, 4)] + [os.path.join(DATA, 'abs_zh_fix.json')]:
    try:
        ABS_ZH.update(json.load(open(_f, encoding='utf-8')))
    except Exception:
        pass

AUTHORS = {}
for _f in (os.path.join(DATA, 'authors_A.json'), os.path.join(DATA, 'authors_B.json')):
    try:
        for _k, _v in json.load(open(_f, encoding='utf-8')).items():
            if _v and str(_v).strip():
                AUTHORS[_k] = str(_v).strip()
    except Exception:
        pass

def abs_block(p):
    """每篇论文后的可展开行：英文作者 + 英文摘要 + 中文翻译。"""
    en = (ABS_EN.get(p['file']) or '').strip()
    zh = (ABS_ZH.get(p['file']) or '').strip()
    au = (AUTHORS.get(p['file']) or '').strip()
    if not en and not zh and not au:
        return ''
    body = ''
    if au:
        body += '<div class="absau"><span class="abslbl">Authors</span>%s</div>' % esc(au)
    if en:
        body += '<div class="abslbl">Abstract (EN)</div><div class="absen">%s</div>' % esc(en)
    if zh:
        body += '<div class="abslbl">摘要 (中文)</div><div class="abszh">%s</div>' % esc(zh)
    return ('<tr class="absrow"><td colspan="8"><div class="absbox">%s</div></td></tr>' % body)

# ---------------------------------------------------------------- 统计
def count_by(key):
    m = {}
    for p in papers:
        k = p.get(key) or '未知'
        m[k] = m.get(k, 0) + 1
    return m

cat_count = count_by('cat')
year_count = count_by('year')
# 机构按「独立单位」拆分：多机构("新加坡国立 / USTC")拆成可单独筛选/搜索的单位
for p in papers:
    p['orgUnits'] = [u for u in (x.strip() for x in re.split(r'\s*/\s*', p['org']))
                     if u and u != '未标注']
org_count = {}
for p in papers:
    for u in set(p['orgUnits']):
        org_count[u] = org_count.get(u, 0) + 1
task_count = count_by('task')
type_count = count_by('type')

years_asc = sorted(y for y in year_count if y != '未知')
years_desc = list(reversed(years_asc))                      # 2026 → 2022
years_sorted = years_desc + (['未知'] if '未知' in year_count else [])
orgs_sorted = sorted(org_count.items(), key=lambda kv: -kv[1])
cats_present = [c for c in sec_order if cat_count.get(c)]
org_named = len(org_count)

PALETTE = ['#4f7cf3', '#7c6ee6', '#e06c75', '#e5a03c', '#3aa76d',
           '#4bb3c4', '#b06ce0', '#8a8f9e', '#d98cb3', '#6c9e5a']
CAT_COLOR = {c: PALETTE[i % len(PALETTE)] for i, c in enumerate(cats_present)}
TASK_COLOR = {'推荐': '#4f7cf3', '搜索': '#3aa76d', '推荐+搜索': '#7c6ee6', '通用': '#8a8f9e', '—': '#c2c9d6'}
TYPE_COLOR = {'工业': '#e5a03c', '学术': '#3aa76d', '—': '#c2c9d6'}
ORG_COLOR = ['#3f5aa6', '#4f7cf3', '#6a8ff5', '#86a5f8', '#a2bcfb',
             '#bed2fd', '#d6e2fe', '#e6edff']

# ---------------------------------------------------------------- §9 阅读路径建议
def _name_cands(name):
    """把路径里写的论文名(含 ... 省略、.pdf 后缀)拆成候选匹配串。"""
    n = name.strip().strip('`').strip()
    n = re.sub(r'\.pdf$', '', n, flags=re.I).strip()
    segs = [x.strip() for x in re.split(r'\.\.\.+', n) if x.strip()]
    return [x for x in dict.fromkeys([n] + segs) if x]

def match_paper(name):
    """论文名 -> papers 中的条目(尽量宽松匹配: 精确 / 前缀 / 子串)。"""
    for key in _name_cands(name):
        k = key.lower()
        for p in papers:
            if p['title'].lower() == k:
                return p
        for p in papers:
            t = p['title'].lower()
            if t.startswith(k) or k.startswith(t):
                return p
        if len(k) >= 8:
            for p in papers:
                if k in p['title'].lower():
                    return p
    return None

def rich(text):
    """把 `论文名` 反引号渲染成可点链接(能匹配到则链到 PDF)，其余文本转义。"""
    out, pos = [], 0
    for m in re.finditer(r'`([^`]+)`', text):
        out.append(esc(text[pos:m.start()]))
        nm = m.group(1)
        p = match_paper(nm)
        if p:
            out.append('<a class="plink jump" href="#row-%d" data-pid="%d" title="定位到表格中该行：%s">%s</a>'
                       '<a class="pdfmini" href="./%s" target="_blank" rel="noopener" title="打开 PDF">↗</a>'
                       % (p['pid'], p['pid'], esc(p['title']), esc(nm), quote(p['file'])))
        else:
            out.append('<span class="pchip">%s</span>' % esc(nm))
        pos = m.end()
    out.append(esc(text[pos:]))
    return ''.join(out)

# 解析 §9: ### 子块标题 + 有序列表项 / 2列表格(问题|参考论文)
path_blocks = []
_cur = None
for _ln in reading_lines:
    _s = _ln.strip()
    _m = re.match(r'^###\s+(.*)$', _s)
    if _m:
        _cur = {'title': _m.group(1).strip(), 'items': [], 'rows': [], 'kind': 'list'}
        path_blocks.append(_cur)
        continue
    if _cur is None:
        continue
    _m = re.match(r'^\d+[.、]\s+(.*)$', _s)
    if _m:
        _cur['items'].append(_m.group(1).strip())
        continue
    if _s.startswith('|'):
        _cells = [c.strip() for c in _s.strip('|').split('|')]
        if all(re.fullmatch(r':?-{2,}:?', c) for c in _cells if c):
            continue
        _cur['rows'].append(_cells)
        _cur['kind'] = 'table'

def _block_inner(b):
    if b['kind'] == 'table' and b['rows']:
        head = ''.join('<th>%s</th>' % esc(c) for c in b['rows'][0])
        body = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % rich(c) for c in r)
                       for r in b['rows'][1:])
        return ('<table class="ptbl"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>'
                % (head, body))
    return ('<ol class="plist">%s</ol>'
            % ''.join('<li>%s</li>' % rich(x) for x in b['items']))

path_grid = ('<div class="grid">%s</div>'
             % ''.join('<div class="card pathcard"><h3>%s</h3>%s</div>'
                       % (esc(b['title']), _block_inner(b)) for b in path_blocks))
paths_section = (
    '<div class="paths">'
    '<h2 class="secttl">阅读路径建议</h2>'
    '<div class="psub">按目标挑一条主线，2–3 小时可覆盖核心工作；'
    '点论文名可<b>定位到下方表格对应行</b>（会高亮），点其右侧 ↗ 打开 PDF</div>'
    + path_grid + '</div>') if path_blocks else ''

# ---------------------------------------------------------------- 条形图
def bars_html(obj, n, max_label=170, colors=None, order=None, facet=None):
    if order:
        ent = [(k, obj[k]) for k in order if k in obj][:n]
    else:
        ent = sorted(obj.items(), key=lambda kv: -kv[1])[:n]
    if not ent:
        return '<div class="empty">无数据</div>'
    mx = max(v for _, v in ent) or 1
    out = []
    for i, (k, v) in enumerate(ent):
        w = v / mx * 100
        if isinstance(colors, dict):
            col = colors.get(k, '#4f7cf3')
        elif colors:
            col = colors[i % len(colors)]
        else:
            col = '#4f7cf3'
        fac = (' data-facet="%s" data-val="%s"' % (esc(facet), esc(k))) if facet else ''
        cls = 'bar clickable' if facet else 'bar'
        out.append(
            '<div class="%s"%s><div class="lbl" title="%s">%s</div>'
            '<div class="track"><div class="fill" style="width:%.1f%%;background:%s"></div></div>'
            '<div class="val">%d</div></div>' % (cls, fac, esc(k), esc(k), w, col, v))
    return ''.join(out)

# ---------------------------------------------------------------- 堆叠柱状图
def stacked_svg(key='cat', groups=None, cmap=None, counts=None):
    ys = years_desc
    cs = cats_present if groups is None else groups
    cmap = CAT_COLOR if cmap is None else cmap
    counts = cat_count if counts is None else counts
    if not ys or not cs:
        return '<div class="empty">无数据</div>'
    totals = [sum(1 for p in papers if p['year'] == y) for y in ys]
    mx = max(totals) or 1
    W, H = 560, 240
    padL, padR, padT, padB = 34, 12, 16, 34
    plotW = W - padL - padR
    plotH = H - padT - padB
    step = plotW / max(len(ys), 1)
    bw = min(step * 0.58, 54)
    g = []
    # y 轴刻度（挑 4 条水平参考线）
    gridn = 4
    for i in range(gridn + 1):
        val = mx * i / gridn
        yy = padT + plotH - plotH * i / gridn
        g.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#e9edf6" stroke-width="1"/>'
                 % (padL, yy, W - padR, yy))
        g.append('<text x="%d" y="%.1f" font-size="9.5" fill="#9aa5bd" text-anchor="end">%d</text>'
                 % (padL - 6, yy + 3.2, round(val)))
    for i, y in enumerate(ys):
        cx = padL + step * i + step / 2
        x = cx - bw / 2
        acc = 0.0
        for c in cs:
            v = sum(1 for p in papers if p['year'] == y and p.get(key) == c)
            if not v:
                continue
            h = v / mx * plotH
            yy = padT + plotH - acc - h
            g.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" '
                     'data-facet="%s" data-val="%s" data-year="%s">'
                     '<title>%s · %s: %d（点击筛选）</title></rect>'
                     % (x, yy, bw, max(h - 1.2, 1), cmap.get(c, '#8a8f9e'),
                        esc(key), esc(c), esc(y), esc(y), esc(c), v))
            acc += h
        g.append('<text x="%.1f" y="%d" font-size="11" fill="#6b7794" text-anchor="middle">%s</text>'
                 % (cx, H - 12, esc(y)))
        g.append('<text x="%.1f" y="%.1f" font-size="10" fill="#9aa5bd" text-anchor="middle">%d</text>'
                 % (cx, padT + plotH - acc - 5, sum(1 for p in papers if p['year'] == y)))
    legend = ''.join(
        '<span class="lg"><i style="background:%s"></i>%s <b>%d</b></span>'
        % (cmap.get(c, '#8a8f9e'), esc(c), counts.get(c, 0))
        for c in cs if counts.get(c, 0) > 0)
    return ('<svg viewBox="0 0 %d %d" class="chart" preserveAspectRatio="xMidYMid meet">%s</svg>'
            '<div class="legend">%s</div>' % (W, H, ''.join(g), legend))

# ---------------------------------------------------------------- 环形图
def donut_svg():
    cs = cats_present
    tot = sum(cat_count.get(c, 0) for c in cs)
    if not cs or not tot:
        return '<div class="empty">无数据</div>'
    W = H = 240
    cx = cy = 120
    R, r = 88, 52
    import math
    a0 = -math.pi / 2
    segs = []
    for c in cs:
        v = cat_count.get(c, 0)
        if not v:
            continue
        a1 = a0 + 2 * math.pi * v / tot
        large = 1 if (a1 - a0) > math.pi else 0
        p0 = (cx + R * math.cos(a0), cy + R * math.sin(a0))
        p1 = (cx + R * math.cos(a1), cy + R * math.sin(a1))
        q0 = (cx + r * math.cos(a0), cy + r * math.sin(a0))
        q1 = (cx + r * math.cos(a1), cy + r * math.sin(a1))
        # 整圆（只有一个分类）特殊处理
        if v == tot:
            d = ('M %f %f A %d %d 0 1 1 %f %f A %d %d 0 1 1 %f %f Z '
                 'M %f %f A %d %d 0 1 0 %f %f A %d %d 0 1 0 %f %f Z'
                 % (cx, cy - R, R, R, cx - 0.01, cy - R, R, R, cx, cy - R,
                    cx, cy - r, r, r, cx - 0.01, cy - r, r, r, cx, cy - r))
        else:
            d = ('M %f %f A %d %d 0 %d 1 %f %f L %f %f A %d %d 0 %d 0 %f %f Z'
                 % (p0[0], p0[1], R, R, large, p1[0], p1[1],
                    q1[0], q1[1], r, r, large, q0[0], q0[1]))
        segs.append('<path d="%s" fill="%s" data-facet="cat" data-val="%s">'
                    '<title>%s: %d (%.1f%%)（点击筛选）</title></path>'
                    % (d, CAT_COLOR[c], esc(c), esc(c), v, v * 100.0 / tot))
        a0 = a1
    center = ('<text x="%d" y="%d" text-anchor="middle" font-size="26" font-weight="700" fill="#2b3a67">%d</text>'
              '<text x="%d" y="%d" text-anchor="middle" font-size="11" fill="#8894ae">篇论文</text>'
              % (cx, cy + 2, tot, cx, cy + 18))
    legend = ''.join(
        '<span class="lg"><i style="background:%s"></i>%s <b>%d</b></span>'
        % (CAT_COLOR[c], esc(c), cat_count.get(c, 0))
        for c in cs if cat_count.get(c, 0) > 0)
    return ('<svg viewBox="0 0 %d %d" class="chart" style="max-width:%dpx;margin:0 auto">%s%s</svg>'
            '<div class="legend">%s</div>' % (W, H, W, ''.join(segs), center, legend))

# ---------------------------------------------------------------- 表格（静态）
def row_html(p):
    pdf = './' + quote(p['file'])
    links = ['<a href="%s" target="_blank" rel="noopener">PDF</a>' % esc(pdf)]
    if p['arxiv']:
        links.append('<a href="%s" target="_blank" rel="noopener">arXiv</a>' % esc(p['arxiv']))
    else:
        links.append('<span class="nolink" title="未登记在线链接">无链接</span>')
    links.append('<a href="#" class="bibbtn" title="复制 BibTeX">BibTeX</a>')
    blob = (p['title'] + ' ' + p['note'] + ' ' + p['org'] + ' ' + p['cat'] + ' '
            + p['task'] + ' ' + p['type']).lower()
    orgkey = '|' + '|'.join(p['orgUnits']) + '|'
    au = AUTHORS.get(p['file'], '')
    tc = TASK_COLOR.get(p['task'], '#8a8f9e')
    yc = TYPE_COLOR.get(p['type'], '#8a8f9e')
    cc = CAT_COLOR.get(p['cat'], '#4f7cf3')
    newb = ('<span class="newbadge" title="本批新增 %s">NEW</span> ' % esc(p['added'])
            if (p['added'] and p['added'] == LATEST_ADD) else '')
    return ('<tr class="prow" id="row-%d" data-cat="%s" data-org="%s" data-year="%s" data-task="%s" '
            'data-type="%s" data-s="%s" data-title="%s" data-notes="%s" data-authors="%s" '
            'data-arxiv="%s" data-added="%s">'
            '<td data-l="标题"><div class="ttl">%s%s</div></td>'
            '<td data-l="机构">%s</td>'
            '<td data-l="年份" class="yr">%s</td>'
            '<td data-l="任务"><span class="tag" style="color:%s;background:%s22">%s</span></td>'
            '<td data-l="学术/工业"><span class="tag" style="color:%s;background:%s22">%s</span></td>'
            '<td data-l="分类"><span class="tag tagc" style="color:%s;background:%s22">%s</span></td>'
            '<td data-l="说明" class="note">%s</td>'
            '<td data-l="链接" class="links">%s</td>'
            '</tr>'
            % (p['pid'], esc(p['cat']), esc(orgkey), esc(p['year']), esc(p['task']),
               esc(p['type']), esc(blob), esc(p['title']), esc(p['note']), esc(au),
               esc(p['arxiv'] or ''), esc(p['added']),
               newb, esc(p['title']),
               esc(p['org']), esc(p['year']),
               tc, tc, esc(p['task']),
               yc, yc, esc(p['type']),
               cc, cc, esc(p['cat']),
               esc(p['note']), ''.join(links)))

# 明细清单排序：年份倒序(2026 最上) → 分类顺序
_cat_idx = {c: i for i, c in enumerate(cats_present)}
def _yr(p):
    y = str(p.get('year', ''))
    return int(y) if y.isdigit() else -1
ordered = sorted(papers, key=lambda p: (-_yr(p), _cat_idx.get(p['cat'], 99)))
rows_src = ordered[:8] if MODE == 'short' else ordered
rows = ''.join(row_html(p) + abs_block(p) for p in rows_src)

# 筛选下拉（预渲染 option）
def options(vals, label):
    return ('<option value="">%s</option>' % esc(label)
            + ''.join('<option value="%s">%s</option>' % (esc(v), esc(v)) for v in vals))

opt_task = options([t for t in ['推荐', '搜索', '推荐+搜索', '通用', '—'] if t in task_count], '全部任务')
opt_type = options([t for t in ['工业', '学术', '—'] if t in type_count], '学术/工业')
opt_cat = options(cats_present, '全部分类')
opt_org = options([o for o, _ in orgs_sorted], '全部机构')
opt_year = options(years_sorted, '全部年份')

# 统计卡（年份跨度按升序取端点）
yr_span = ('%s–%s' % (years_asc[0], years_asc[-1])) if years_asc else '-'
year_span_txt = ('%s 至 %s' % (years_asc[0], years_asc[-1])) if years_asc else '未知'
stat_html = (
    '<div><b>%d</b><span>篇论文</span></div>'
    '<div><b>%d</b><span>个分类</span></div>'
    '<div><b>%s</b><span>年份跨度</span></div>'
    '<div><b>%d</b><span>家机构</span></div>'
    % (len(papers), len(cats_present), esc(yr_span), org_named))
newtoggle = (('<label class="sw" title="只看最近一批新增 · %s"><input type="checkbox" id="fnew">只看新增</label>'
              % esc(LATEST_ADD)) if LATEST_ADD else '')

charts = {
    'cat': bars_html(cat_count, 20, colors=[CAT_COLOR[c] for c in cats_present], facet='cat'),
    'year': bars_html(year_count, 20, order=years_sorted, facet='year'),
    'org': bars_html(org_count, 12, colors=ORG_COLOR, facet='org'),
    'tt': ('<div class="minihd">任务</div>' + bars_html(task_count, 10, colors=TASK_COLOR, facet='task')
           + '<div class="minihd">学术 / 工业</div>' + bars_html(type_count, 10, colors=TYPE_COLOR, facet='type')),
}

# 供 JS 增强用的轻量数据集（页面静态内容已完整，JS 关闭也能看全）
data = json.dumps([{'title': p['title'], 'org': p['org'], 'year': p['year'],
                    'cat': p['cat'], 'note': p['note'], 'file': p['file'],
                    'arxiv': p['arxiv']} for p in papers], ensure_ascii=False)

HTML = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>生成式搜推论文库</title>
<style>
  *{box-sizing:border-box}
  html{overflow-y:scroll;scrollbar-gutter:stable}
  body{margin:0;font-family:-apple-system,"PingFang SC","Microsoft YaHei",Helvetica,Arial,sans-serif;
       background:#f4f6fa;color:#1f2a44;-webkit-font-smoothing:antialiased}
  a{color:#2f6fed;text-decoration:none}
  a:hover{text-decoration:underline}
  .wrap{max-width:1320px;margin:0 auto;padding:22px 20px 60px}
  .hero{background:#2b3a67;background:-webkit-linear-gradient(135deg,#2b3a67,#3f5aa6);
        background:linear-gradient(135deg,#2b3a67,#3f5aa6);color:#fff;border-radius:14px;padding:26px 28px}
  .hero h1{margin:0 0 6px;font-size:26px;font-weight:700}
  .hero .sub{opacity:.86;font-size:13px;line-height:1.6}
  .stat{display:flex;gap:30px;margin-top:18px;flex-wrap:wrap}
  .stat b{font-size:30px;font-weight:700;display:block;line-height:1.15}
  .stat span{font-size:12px;opacity:.82}
  .grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px}
  .grid.three{grid-template-columns:1fr 1fr 1fr}
  @media(max-width:900px){.grid,.grid.three{grid-template-columns:1fr}}
  .card{background:#fff;border-radius:12px;padding:16px 18px;box-shadow:0 1px 3px rgba(20,40,90,.07)}
  .card h3{margin:0 0 14px;font-size:14px;color:#33415c;font-weight:600}
  .bar{display:flex;align-items:center;gap:8px;margin:6px 0;font-size:12px}
  .bar .lbl{width:158px;flex:0 0 158px;color:#4a5878;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .bar .track{flex:1;background:#eef1f7;border-radius:4px;height:15px;overflow:hidden}
  .bar .fill{height:100%;background:#4f7cf3;border-radius:4px}
  .bar .val{width:30px;text-align:right;color:#33415c;font-variant-numeric:tabular-nums}
  .chart{width:100%;height:auto;display:block}
  .legend{display:flex;flex-wrap:wrap;gap:6px 14px;margin-top:10px;font-size:11.5px;color:#5a6683}
  .legend .lg{display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
  .legend .lg i{width:9px;height:9px;border-radius:2px;display:inline-block}
  .legend .lg b{color:#33415c}
  .empty{color:#9aa5bd;font-size:12px;padding:10px 0}
  .filters{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0 10px}
  select,input{font-size:13px;padding:8px 10px;border:1px solid #d6dced;border-radius:8px;
               background:#fff;color:#1f2a44;outline:none}
  select:focus,input:focus{border-color:#8fb0f5;box-shadow:0 0 0 3px rgba(79,124,243,.12)}
  #q{flex:1;min-width:200px}
  .pcount{color:#7a869f;font-size:12px;margin:8px 2px}
  table{width:100%;table-layout:fixed;border-collapse:collapse;background:#fff;border-radius:12px;overflow:hidden;
        box-shadow:0 1px 3px rgba(20,40,90,.07)}
  th,td{text-align:left;padding:10px 12px;font-size:13px;border-bottom:1px solid #eef1f7;vertical-align:top;
        overflow-wrap:anywhere}
  th{background:#f7f9fd;color:#4a5878;font-weight:600;white-space:nowrap}
  tr:hover td{background:#fafbff}
  td.nowrap{white-space:nowrap}
  td.links{white-space:normal;line-height:1.85}
  td.links a,td.links .nolink{display:block;white-space:nowrap}
  .ttl{font-weight:600;color:#1f2a44;line-height:1.45}
  .tag{display:inline-block;font-size:11px;padding:2px 9px;border-radius:20px;
       background:#eaf0ff;color:#2f6fed;white-space:nowrap}
  .tagc{white-space:normal;overflow-wrap:anywhere;max-width:100%}
  .yr{color:#7a869f;white-space:nowrap}
  .note{color:#43506b;font-size:12.5px;line-height:1.55}
  tr.hide{display:none}
  tr.prow{cursor:pointer}
  tr.prow .ttl::before{content:"▸";display:inline-block;width:14px;color:#a7b2cc;font-size:11px}
  tr.prow.open .ttl::before{content:"▾"}
  tr.absrow{display:none}
  tr.absrow.show{display:table-row}
  tr.absrow td{background:#f7faff;padding:0;border-bottom:1px solid #eef1f7}
  .absbox{padding:12px 16px 14px;border-left:3px solid #cddcfb;overflow-wrap:anywhere}
  .abslbl{font-size:10.5px;letter-spacing:.5px;color:#8894ae;font-weight:600;margin:2px 0 5px}
  .absen{font-size:12.5px;line-height:1.72;color:#5c6885;font-family:Georgia,"Times New Roman",serif;margin:0 0 12px}
  .abszh{font-size:12.5px;line-height:1.85;color:#2b3550;margin:0}
  .absau{font-size:12.5px;line-height:1.65;color:#33415c;margin:0 0 12px}
  .absau .abslbl{display:inline-block;margin:0 8px 0 0;vertical-align:1.5px}
  .minihd{font-size:12px;font-weight:600;color:#4a5878;margin:12px 0 6px}
  .minihd:first-child{margin-top:0}
  .paths{margin-top:26px}
  .secttl{margin:0 0 4px;font-size:18px;font-weight:700;color:#2b3a67}
  .psub{color:#6b7794;font-size:12.5px;margin-bottom:12px}
  .pathcard h3{margin:0 0 10px;font-size:14px;color:#2b3a67;font-weight:600}
  .plist{margin:0;padding-left:20px}
  .plist li{font-size:12.5px;line-height:1.75;color:#43506b;margin:2px 0}
  .plink{font-weight:600;color:#2f6fed;border-bottom:1px solid #cddcfb}
  .pchip{font-weight:600;color:#3f4b67}
  .ptbl{width:100%;border-collapse:collapse;background:#fff;border-radius:0;box-shadow:none}
  .ptbl th,.ptbl td{padding:7px 10px;font-size:12.5px;border-bottom:1px solid #eef1f7}
  .ptbl th{background:#f7f9fd;color:#4a5878;font-weight:600;white-space:nowrap}
  .ptbl tr:hover td{background:#fafbff}
  @media print{body{background:#fff}.card,table{box-shadow:none;border:1px solid #e6eaf3}}
  /* 图表可点联动 */
  .bar.clickable{cursor:pointer;border-radius:6px;padding:1px 5px;margin-left:-5px}
  .bar.clickable:hover{background:#f2f6ff}
  .chart [data-facet]{cursor:pointer}
  .chart [data-facet]:hover{opacity:.82}
  /* 吸顶表头 + 排序 */
  thead th{position:sticky;top:0;z-index:3;box-shadow:inset 0 -1px 0 #e6ebf5}
  th.sortable{cursor:pointer;user-select:none}
  th.sortable:hover{color:#2f6fed}
  th .arw{color:#aab4c8;font-size:10px}
  /* 高亮 / 新增标记 / 链接 */
  mark{background:#fff2a8;color:inherit;padding:0 1px;border-radius:2px}
  .newbadge{display:inline-block;font-size:10px;font-weight:700;color:#fff;background:#e0603c;
            border-radius:4px;padding:1px 5px;margin-right:6px;vertical-align:1.5px}
  .nolink{color:#b3bccd}
  .bibbtn{color:#8a94ad;font-size:12px}
  .prow.flash td{background:#fff6d2 !important}
  .prow.flash td{transition:background .5s}
  .pdfmini{font-size:11px;color:#9aa5bd;margin-left:3px;border-bottom:none}
  .pdfmini:hover{color:#2f6fed}
  /* 只看新增 开关 + 清空 */
  .filters label.sw{display:inline-flex;align-items:center;gap:6px;font-size:13px;color:#4a5878;
                    padding:8px 11px;border:1px solid #d6dced;border-radius:8px;background:#fff;cursor:pointer}
  .filters label.sw input{margin:0}
  #clr{font-size:13px;padding:8px 13px;border:1px solid #d6dced;border-radius:8px;background:#fff;
       color:#4a5878;cursor:pointer}
  #clr:hover{border-color:#8fb0f5;color:#2f6fed}
  /* 窄屏：表格 -> 卡片 */
  @media(max-width:700px){
    .wrap{padding:14px 12px 40px}
    thead{display:none}
    table,tbody,tr,td{display:block;width:auto;table-layout:auto}
    tr.prow{padding:8px 12px 10px;border-bottom:8px solid #eef1f7}
    tr.prow td{border:0;padding:2px 0;display:flex;gap:8px;overflow-wrap:anywhere}
    tr.prow td::before{content:attr(data-l);flex:0 0 60px;color:#95a0b8;font-size:11px;padding-top:2px}
    td.nowrap{white-space:normal}
    tr.absrow td{display:block;padding:0}
    tr.absrow td::before{display:none}
  }
</style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <h1>生成式搜推论文库</h1>
    <div class="sub">统计 __NPAPERS__ 篇论文，__YEARSPAN__，定期更新。</div>
    <div class="stat">__STAT__</div>
  </div>

  <div class="grid three">
    <div class="card"><h3>任务 × 年份</h3>__C_CY_TASK__</div>
    <div class="card"><h3>学术 / 工业 × 年份</h3>__C_CY_TYPE__</div>
    <div class="card"><h3>分类 × 年份</h3>__C_CY__</div>
  </div>

  <div class="grid three">
    <div class="card"><h3>机构 Top 12</h3>__C_ORG__</div>
    <div class="card"><h3>任务 · 学术 / 工业 分布</h3>__C_TT__</div>
    <div class="card"><h3>分类占比</h3>__C_DONUT__</div>
  </div>

  <div class="filters">
    <input id="q" placeholder="搜索标题 / 关键词 / 机构 / 分类 / 作者 …（按 / 聚焦）" autocomplete="off">
    <select id="f_task">__OPT_TASK__</select>
    <select id="f_type">__OPT_TYPE__</select>
    <select id="f_cat">__OPT_CAT__</select>
    <select id="f_org">__OPT_ORG__</select>
    <select id="f_year">__OPT_YEAR__</select>
    __NEWTOGGLE__
    <button id="clr" type="button" title="清空全部筛选（Esc）">清空</button>
  </div>
  <div class="pcount" id="cnt">共 __NPAPERS__ 篇</div>

  <table>
    <colgroup>
      <col style="width:25%"><col style="width:8%"><col style="width:5%"><col style="width:6%">
      <col style="width:7%"><col style="width:15%"><col style="width:24%"><col style="width:10%">
    </colgroup>
    <thead><tr>
      <th class="sortable" data-sort="title">标题 <span class="arw"></span></th>
      <th class="sortable" data-sort="org">机构 <span class="arw"></span></th>
      <th class="sortable" data-sort="year">年份 <span class="arw"></span></th>
      <th class="sortable" data-sort="task">任务 <span class="arw"></span></th>
      <th class="sortable" data-sort="type">学术/工业 <span class="arw"></span></th>
      <th class="sortable" data-sort="cat">分类 <span class="arw"></span></th>
      <th>说明</th><th>链接</th></tr></thead>
    <tbody id="tb">__ROWS__</tbody>
  </table>

  __PATHS__
</div>
<script>
(function(){
  var PAPERS = __DATA__;
  var q = document.getElementById('q'), ftask = document.getElementById('f_task'),
      ftype = document.getElementById('f_type'), fc = document.getElementById('f_cat'),
      fo = document.getElementById('f_org'), fy = document.getElementById('f_year'),
      fnew = document.getElementById('fnew'), clr = document.getElementById('clr'),
      tb = document.getElementById('tb'), cnt = document.getElementById('cnt');
  var LATEST = "__LATEST__";
  var FCTL = {cat: fc, org: fo, year: fy, task: ftask, type: ftype};
  var pairs = [], total = 0;
  (function(){
    var trs = tb.getElementsByTagName('tr');
    for (var i = 0; i < trs.length; i++){
      var tr = trs[i];
      if (!tr.classList.contains('prow')) continue;
      var nx = tr.nextElementSibling;
      pairs.push([tr, (nx && nx.classList.contains('absrow')) ? nx : null]);
    }
    total = pairs.length;
  })();

  function readURL(){
    try{
      var u = new URLSearchParams(location.search);
      if (u.get('q')) q.value = u.get('q');
      ['task','type','cat','org','year'].forEach(function(k){ var v=u.get(k); if(v) FCTL[k].value=v; });
      if (u.get('new')==='1' && fnew) fnew.checked = true;
    }catch(e){}
  }
  function writeURL(){
    try{
      var u = new URLSearchParams();
      if (q.value.trim()) u.set('q', q.value.trim());
      ['task','type','cat','org','year'].forEach(function(k){ if(FCTL[k].value) u.set(k, FCTL[k].value); });
      if (fnew && fnew.checked) u.set('new','1');
      var s = u.toString();
      history.replaceState(null, '', s ? ('?'+s) : location.pathname);
    }catch(e){}
  }
  function escHtml(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
  function hlSpan(text, q){
    if (!q) return escHtml(text);
    var low = text.toLowerCase(), ql = q.toLowerCase(), out = '', i = 0;
    while (true){
      var k = low.indexOf(ql, i);
      if (k < 0){ out += escHtml(text.slice(i)); break; }
      out += escHtml(text.slice(i,k)) + '<mark>' + escHtml(text.slice(k, k+ql.length)) + '</mark>';
      i = k + ql.length;
    }
    return out;
  }
  function mark(tr, s){
    var tw = tr.querySelector('.ttl'), nw = tr.querySelector('.note');
    var t1 = tr.getAttribute('data-title') || '', t2 = tr.getAttribute('data-notes') || '';
    if (tw) tw.innerHTML = hlSpan(t1, s);
    if (nw) nw.innerHTML = hlSpan(t2, s);
  }
  var sortKey = null, sortDir = 1;
  function val(tr, k){
    if (k === 'year') return parseInt(tr.getAttribute('data-year'), 10) || 0;
    if (k === 'title') return (tr.getAttribute('data-title') || '').toLowerCase();
    return (tr.getAttribute('data-' + k) || '').toLowerCase();
  }
  function order(){
    var s = (q.value || '').toLowerCase().trim();
    var vis = pairs.slice();
    if (sortKey){
      vis.sort(function(a,b){ var x=val(a[0],sortKey), y=val(b[0],sortKey);
        if (x < y) return -sortDir; if (x > y) return sortDir; return 0; });
    } else if (s){
      vis.sort(function(a,b){
        var ta=(a[0].getAttribute('data-title')||'').toLowerCase().indexOf(s)>=0?0:1;
        var tb2=(b[0].getAttribute('data-title')||'').toLowerCase().indexOf(s)>=0?0:1;
        return ta - tb2; });
    } else { return; }
    for (var i=0;i<vis.length;i++){ tb.appendChild(vis[i][0]); if (vis[i][1]) tb.appendChild(vis[i][1]); }
  }
  function apply(){
    var s = (q.value || '').toLowerCase().trim(), n = 0, nw = fnew && fnew.checked;
    for (var i=0;i<pairs.length;i++){
      var tr=pairs[i][0], ab=pairs[i][1];
      var ok = (!s || (tr.getAttribute('data-s')||'').indexOf(s) !== -1)
            && (!ftask.value || tr.getAttribute('data-task') === ftask.value)
            && (!ftype.value || tr.getAttribute('data-type') === ftype.value)
            && (!fc.value   || tr.getAttribute('data-cat')  === fc.value)
            && (!fo.value   || (tr.getAttribute('data-org')||'').indexOf('|'+fo.value+'|') !== -1)
            && (!fy.value   || tr.getAttribute('data-year') === fy.value)
            && (!nw || tr.getAttribute('data-added') === LATEST);
      tr.classList.remove('open'); if (ab) ab.classList.remove('show');
      if (ok){ tr.classList.remove('hide'); tr.style.display=''; n++; }
      else { tr.classList.add('hide'); tr.style.display='none'; }
      mark(tr, s);
    }
    order();
    writeURL();
    cnt.textContent = '共 ' + n + ' 篇' + (n === total ? '' : '（已筛选，共 ' + total + ' 篇）');
  }

  [q,ftask,ftype,fc,fo,fy].forEach(function(el){ el.addEventListener('input',apply); el.addEventListener('change',apply); });
  if (fnew) fnew.addEventListener('change', apply);
  if (clr) clr.addEventListener('click', function(){
    q.value=''; ftask.value=''; ftype.value=''; fc.value=''; fo.value=''; fy.value='';
    if (fnew) fnew.checked=false; apply(); q.focus();
  });
  document.addEventListener('keydown', function(e){
    if (e.key === '/' && document.activeElement !== q){ e.preventDefault(); q.focus(); }
    else if (e.key === 'Escape' && q.value){ q.value=''; apply(); }
  });
  document.addEventListener('click', function(e){
    var seg = e.target.closest('[data-facet]');
    if (seg){
      var f = seg.getAttribute('data-facet'), v = seg.getAttribute('data-val'), yr = seg.getAttribute('data-year');
      var ctl = FCTL[f]; if (!ctl) return;
      var already = (ctl.value === v);
      ctl.value = already ? '' : v;
      if (yr && FCTL.year && f !== 'year'){ FCTL.year.value = (already && FCTL.year.value === yr) ? '' : yr; }
      apply(); return;
    }
    var b = e.target.closest('.bibbtn');
    if (b){ e.preventDefault(); copyBib(b); return; }
    if (e.target.closest('a')) return;
    var tr = e.target.closest('tr.prow'); if (!tr) return;
    var nx = tr.nextElementSibling;
    if (nx && nx.classList.contains('absrow')){ var o = nx.classList.toggle('show'); tr.classList.toggle('open', o); }
  });
  Array.prototype.forEach.call(document.querySelectorAll('a.jump'), function(a){
    a.addEventListener('click', function(ev){
      ev.preventDefault();
      var tr = document.getElementById(a.getAttribute('href').slice(1)); if (!tr) return;
      if (tr.classList.contains('hide')){ if (clr) clr.click(); }
      tr.scrollIntoView({behavior:'smooth', block:'center'});
      tr.classList.add('flash'); setTimeout(function(){ tr.classList.remove('flash'); }, 1400);
    });
  });
  Array.prototype.forEach.call(document.querySelectorAll('th.sortable'), function(th){
    th.addEventListener('click', function(){
      var k = th.getAttribute('data-sort');
      if (sortKey === k) sortDir = -sortDir; else { sortKey = k; sortDir = 1; }
      Array.prototype.forEach.call(document.querySelectorAll('th.sortable .arw'), function(a){ a.textContent=''; });
      th.querySelector('.arw').textContent = sortDir > 0 ? '▲' : '▼';
      apply();
    });
  });
  function bibtex(tr){
    var NL = String.fromCharCode(10);
    var t = tr.getAttribute('data-title') || '', au = tr.getAttribute('data-authors') || '';
    var y = tr.getAttribute('data-year') || '', u = tr.getAttribute('data-arxiv') || '';
    var ep = '', k = u.indexOf('arxiv.org/abs/');
    if (k >= 0) ep = u.slice(k + 14).replace(/[^0-9.]/g, '');
    var auGS = (au ? au.split(',') : []).map(function(x){
        x = x.trim(); if (!x) return '';
        if (/^et al/i.test(x)) return 'others';
        var p = x.split(' '), last = p.pop();
        return p.length ? last + ', ' + p.join(' ') : last;
      }).filter(Boolean).join(' and ');
    var SUR = ((au.split(',')[0] || 'anon').trim().split(' ').pop() || 'anon').replace(/[^A-Za-z]/g, '').toLowerCase();
    var W = (t.split(' ')[0] || '').replace(/[^A-Za-z]/g, '').toLowerCase();
    var L = ['@' + (ep ? 'article' : 'misc') + '{' + SUR + y + W + ',', '  title={' + t + '},'];
    if (auGS) L.push('  author={' + auGS + '},');
    if (ep) L.push('  journal={arXiv preprint arXiv:' + ep + '},');
    else if (u) L.push('  url={' + u + '},');
    L.push('  year={' + y + '}');
    return L.join(NL) + NL + '}';
  }
  function copyBib(btn){
    var s = bibtex(btn.closest('tr.prow'));
    var done = function(){ btn.textContent = '已复制✓'; setTimeout(function(){ btn.textContent='BibTeX'; }, 1200); };
    if (navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(s).then(done, function(){ window.prompt('复制 BibTeX:', s); });
    } else { window.prompt('复制 BibTeX:', s); }
  }

  readURL();
  apply();
})();
</script>
</body>
</html>'''

HTML = (HTML
        .replace('__STAT__', stat_html)
        .replace('__C_CAT__', charts['cat'])
        .replace('__C_YEAR__', charts['year'])
        .replace('__C_YEAR2__', charts['year'])
        .replace('__C_ORG__', charts['org'])
        .replace('__C_CY__', stacked_svg())
        .replace('__C_CY_TASK__', stacked_svg('task', ['推荐', '搜索', '推荐+搜索', '通用', '—'], TASK_COLOR, task_count))
        .replace('__C_CY_TYPE__', stacked_svg('type', ['工业', '学术', '—'], TYPE_COLOR, type_count))
        .replace('__C_TT__', charts['tt'])
        .replace('__C_DONUT__', donut_svg())
        .replace('__OPT_TASK__', opt_task)
        .replace('__OPT_TYPE__', opt_type)
        .replace('__OPT_CAT__', opt_cat)
        .replace('__OPT_ORG__', opt_org)
        .replace('__OPT_YEAR__', opt_year)
        .replace('__NEWTOGGLE__', newtoggle)
        .replace('__LATEST__', LATEST_ADD)
        .replace('__ROWS__', rows)
        .replace('__PATHS__', paths_section)
        .replace('__NPAPERS__', str(len(papers)))
        .replace('__YEARSPAN__', year_span_txt)
        .replace('__DATA__', data))

# 预览裁剪（仅自查用，不影响默认 full 输出）
if MODE == 'sheets':
    a = HTML.index('<div class="filters">')
    b = HTML.index('</table>') + len('</table>')
    HTML = HTML[:a] + HTML[b:]
elif MODE == 'tbl':
    a = HTML.index('<div class="hero">')
    b = HTML.index('<div class="filters">')
    HTML = HTML[:a] + HTML[b:]
elif MODE in ('cy', 'org', 'cat', 'donut'):
    body = {
        'cy': ('分类 × 年份', stacked_svg()),
        'org': ('机构 Top 12', charts['org']),
        'cat': ('分类分布', charts['cat']),
        'donut': ('分类占比', donut_svg()),
    }[MODE]
    a = HTML.index('<div class="hero">')
    b = HTML.index('<div class="filters">')
    card = '<div class="card"><h3>%s</h3>%s</div>' % body
    HTML = (HTML[:a] + '<div class="grid">' + card + '</div>' + HTML[b:])
    HTML = HTML.replace('max-width:1320px', 'max-width:560px')
elif MODE == 'paths':
    st = HTML[HTML.index('<style>') + len('<style>'):HTML.index('</style>')]
    HTML = ('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">'
            '<style>%s</style></head><body><div class="wrap" style="max-width:860px">%s</div>'
            '</body></html>' % (st, paths_section))

open(OUT, 'w', encoding='utf-8').write(HTML)
print('papers:', len(papers), '| cats:', len(cats_present), '| years:',
      years_sorted, '| orgs:', org_named)
print('arxiv mapped:', sum(1 for p in papers if p['arxiv']))
print('paths:', len(path_blocks), 'blocks |',
      [len(b['items']) or len(b['rows']) - 1 for b in path_blocks])
print('out:', OUT, os.path.getsize(OUT), 'bytes')
