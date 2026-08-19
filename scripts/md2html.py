#!/usr/bin/env python3
"""Minimal markdown to HTML. No dependencies, so the hub builds anywhere."""
import re, sys, html, pathlib

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', lambda m: '<code>%s</code>' % m.group(1), t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
               lambda m: '<a href="%s">%s</a>' % (m.group(2).replace('.md','.html'), m.group(1)), t)
    return t

def convert(md):
    out, i, lines = [], 0, md.split('\n')
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('```'):
            lang = ln[3:].strip(); i += 1; buf = []
            while i < len(lines) and not lines[i].startswith('```'):
                buf.append(html.escape(lines[i])); i += 1
            i += 1
            out.append('<pre><code>%s</code></pre>' % '\n'.join(buf)); continue
        if re.match(r'^\|.*\|\s*$', ln) and i+1 < len(lines) and re.match(r'^\|[\s:|-]+\|\s*$', lines[i+1]):
            hdr = [c.strip() for c in ln.strip().strip('|').split('|')]
            i += 2; rows = []
            while i < len(lines) and re.match(r'^\|.*\|\s*$', lines[i]):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
            t = '<div class="tw"><table><thead><tr>' + ''.join('<th>%s</th>' % inline(c) for c in hdr) + '</tr></thead><tbody>'
            for r in rows:
                t += '<tr>' + ''.join('<td>%s</td>' % inline(c) for c in r) + '</tr>'
            out.append(t + '</tbody></table></div>'); continue
        m = re.match(r'^(#{1,6})\s+(.*)$', ln)
        if m:
            lvl = len(m.group(1)); out.append('<h%d>%s</h%d>' % (lvl, inline(m.group(2)), lvl)); i += 1; continue
        if ln.startswith('>'):
            buf = []
            while i < len(lines) and lines[i].startswith('>'):
                buf.append(lines[i].lstrip('>').strip()); i += 1
            out.append('<blockquote>%s</blockquote>' % inline(' '.join(buf))); continue
        if re.match(r'^\s*[-*+]\s+', ln):
            buf = []
            while i < len(lines) and re.match(r'^\s*[-*+]\s+', lines[i]):
                buf.append(re.sub(r'^\s*[-*+]\s+', '', lines[i])); i += 1
            out.append('<ul>' + ''.join('<li>%s</li>' % inline(b) for b in buf) + '</ul>'); continue
        if re.match(r'^\s*\d+\.\s+', ln):
            buf = []
            while i < len(lines) and re.match(r'^\s*\d+\.\s+', lines[i]):
                buf.append(re.sub(r'^\s*\d+\.\s+', '', lines[i])); i += 1
            out.append('<ol>' + ''.join('<li>%s</li>' % inline(b) for b in buf) + '</ol>'); continue
        if re.match(r'^\s*---+\s*$', ln):
            i += 1; continue
        if ln.strip() == '':
            i += 1; continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,6}\s|\||>|```|\s*[-*+]\s|\s*\d+\.\s|\s*---+\s*$)', lines[i]):
            buf.append(lines[i]); i += 1
        if not buf:
            # Nothing matched and nothing consumed. Emit the line verbatim and
            # move on, so a malformed block can never hang the build.
            out.append('<p>%s</p>' % inline(lines[i])); i += 1
            continue
        out.append('<p>%s</p>' % inline(' '.join(buf)))
    return '\n'.join(out)

PAGE = """<title>{title}</title>
<link rel="stylesheet" href="../styles/hub.css">
<div class="strip">KRISEVA ATTEST &middot; synthetic data only &middot; research stage &middot; no customer or entity data</div>
<div class="wrap">{body}
<a class="backlink" href="../index.html">&larr; back to the submission hub</a>
<footer>Kriseva AI Private Limited &middot; GIFT IFIH Young Builders' Program 2026 &middot; all data synthetic</footer>
</div>"""

src, dst, title = sys.argv[1], sys.argv[2], sys.argv[3]
md = pathlib.Path(src).read_text()
pathlib.Path(dst).write_text(PAGE.format(title=html.escape(title), body=convert(md)))
print('wrote', dst)
