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
org_count = count_by('org')
org_count.pop('未标注', None)
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
            out.append('<a class="plink" href="./%s" target="_blank" rel="noopener" '
                       'title="%s">%s</a>' % (quote(p['file']), esc(p['title']), esc(nm)))
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
    '论文名可直接点击打开 PDF（未匹配到的以粗体展示）</div>'
    + path_grid + '</div>') if path_blocks else ''

# ---------------------------------------------------------------- 条形图
def bars_html(obj, n, max_label=170, colors=None, order=None):
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
        out.append(
            '<div class="bar"><div class="lbl" title="%s">%s</div>'
            '<div class="track"><div class="fill" style="width:%.1f%%;background:%s"></div></div>'
            '<div class="val">%d</div></div>' % (esc(k), esc(k), w, col, v))
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
            g.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s">'
                     '<title>%s · %s: %d</title></rect>'
                     % (x, yy, bw, max(h - 1.2, 1), cmap.get(c, '#8a8f9e'),
                        esc(y), esc(c), v))
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
        segs.append('<path d="%s" fill="%s"><title>%s: %d (%.1f%%)</title></path>'
                    % (d, CAT_COLOR[c], esc(c), v, v * 100.0 / tot))
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
    arx = (' · <a href="%s" target="_blank" rel="noopener">arXiv</a>' % esc(p['arxiv'])) if p['arxiv'] else ''
    blob = (p['title'] + ' ' + p['note'] + ' ' + p['org'] + ' ' + p['cat'] + ' '
            + p['task'] + ' ' + p['type']).lower()
    tc = TASK_COLOR.get(p['task'], '#8a8f9e')
    yc = TYPE_COLOR.get(p['type'], '#8a8f9e')
    cc = CAT_COLOR.get(p['cat'], '#4f7cf3')
    return ('<tr class="prow" data-cat="%s" data-org="%s" data-year="%s" data-task="%s" data-type="%s" data-s="%s">'
            '<td><div class="ttl">%s</div></td>'
            '<td class="nowrap">%s</td>'
            '<td class="yr">%s</td>'
            '<td><span class="tag" style="color:%s;background:%s22">%s</span></td>'
            '<td><span class="tag" style="color:%s;background:%s22">%s</span></td>'
            '<td><span class="tag" style="color:%s;background:%s22">%s</span></td>'
            '<td class="note">%s</td>'
            '<td class="nowrap"><a href="%s" target="_blank" rel="noopener">PDF</a>%s</td>'
            '</tr>'
            % (esc(p['cat']), esc(p['org']), esc(p['year']), esc(p['task']), esc(p['type']), esc(blob),
               esc(p['title']), esc(p['org']), esc(p['year']),
               tc, tc, esc(p['task']),
               yc, yc, esc(p['type']),
               cc, cc, esc(p['cat']),
               esc(p['note']), esc(pdf), arx))

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

charts = {
    'cat': bars_html(cat_count, 20, colors=[CAT_COLOR[c] for c in cats_present]),
    'year': bars_html(year_count, 20, order=years_sorted),
    'org': bars_html(org_count, 12, colors=ORG_COLOR),
    'tt': ('<div class="minihd">任务</div>' + bars_html(task_count, 10, colors=TASK_COLOR)
           + '<div class="minihd">学术 / 工业</div>' + bars_html(type_count, 10, colors=TYPE_COLOR)),
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
<title>生成式推荐论文库</title>
<style>
  *{box-sizing:border-box}
  html{overflow-y:scroll;scrollbar-gutter:stable}
  body{margin:0;font-family:-apple-system,"PingFang SC","Microsoft YaHei",Helvetica,Arial,sans-serif;
       background:#f4f6fa;color:#1f2a44;-webkit-font-smoothing:antialiased}
  a{color:#2f6fed;text-decoration:none}
  a:hover{text-decoration:underline}
  .wrap{max-width:1180px;margin:0 auto;padding:22px 20px 60px}
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
  th,td{text-align:left;padding:10px 12px;font-size:13px;border-bottom:1px solid #eef1f7;vertical-align:top}
  th{background:#f7f9fd;color:#4a5878;font-weight:600;white-space:nowrap}
  tr:hover td{background:#fafbff}
  td.nowrap{white-space:nowrap}
  .ttl{font-weight:600;color:#1f2a44;line-height:1.45}
  .tag{display:inline-block;font-size:11px;padding:2px 9px;border-radius:20px;
       background:#eaf0ff;color:#2f6fed;white-space:nowrap}
  .yr{color:#7a869f}
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
</style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <h1>生成式推荐论文库</h1>
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
    <input id="q" placeholder="搜索标题 / 关键词 / 机构 / 分类 / 作者 ..." autocomplete="off">
    <select id="f_task">__OPT_TASK__</select>
    <select id="f_type">__OPT_TYPE__</select>
    <select id="f_cat">__OPT_CAT__</select>
    <select id="f_org">__OPT_ORG__</select>
    <select id="f_year">__OPT_YEAR__</select>
  </div>
  <div class="pcount" id="cnt">共 __NPAPERS__ 篇</div>

  <table>
    <colgroup>
      <col style="width:30%"><col style="width:9%"><col style="width:5%"><col style="width:6%">
      <col style="width:8%"><col style="width:13%"><col style="width:22%"><col style="width:7%">
    </colgroup>
    <thead><tr><th>标题</th><th>机构</th><th>年份</th><th>任务</th><th>学术/工业</th><th>分类</th><th>说明</th><th>链接</th></tr></thead>
    <tbody id="tb">__ROWS__</tbody>
  </table>

  __PATHS__
</div>
<script>
(function(){
  var PAPERS = __DATA__;
  var q = document.getElementById('q'),
      ftask = document.getElementById('f_task'),
      ftype = document.getElementById('f_type'),
      fc = document.getElementById('f_cat'),
      fo = document.getElementById('f_org'),
      fy = document.getElementById('f_year'),
      tb = document.getElementById('tb'),
      cnt = document.getElementById('cnt');
  var rows = tb.getElementsByTagName('tr');
  var total = 0;
  for (var k = 0; k < rows.length; k++){ if (!rows[k].classList.contains('absrow')) total++; }
  function apply(){
    var s = (q.value || '').toLowerCase().trim(),
        tk = ftask.value, ty = ftype.value,
        c = fc.value, o = fo.value, y = fy.value, n = 0;
    for (var i = 0; i < rows.length; i++){
      var tr = rows[i];
      if (tr.classList.contains('absrow')){ tr.classList.remove('show'); continue; }
      var ok = (!s || (tr.getAttribute('data-s') || '').indexOf(s) !== -1)
            && (!tk || tr.getAttribute('data-task') === tk)
            && (!ty || tr.getAttribute('data-type') === ty)
            && (!c || tr.getAttribute('data-cat') === c)
            && (!o || tr.getAttribute('data-org') === o)
            && (!y || tr.getAttribute('data-year') === y);
      tr.classList.remove('open');
      if (ok){ tr.classList.remove('hide'); n++; } else { tr.classList.add('hide'); }
    }
    cnt.textContent = '共 ' + n + ' 篇' + (n === total ? '' : '（已筛选，共 ' + total + ' 篇）');
  }
  [q, ftask, ftype, fc, fo, fy].forEach(function(el){
    el.addEventListener('input', apply);
    el.addEventListener('change', apply);
  });
  tb.addEventListener('click', function(e){
    if (e.target.closest('a')) return;
    var tr = e.target.closest('tr');
    if (!tr || tr.classList.contains('absrow')) return;
    var nx = tr.nextElementSibling;
    if (nx && nx.classList.contains('absrow')){
      var open = nx.classList.toggle('show');
      tr.classList.toggle('open', open);
    }
  });
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
    HTML = HTML.replace('max-width:1180px', 'max-width:560px')
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
