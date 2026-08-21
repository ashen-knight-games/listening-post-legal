#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the privacy policy Markdown sources to standalone HTML pages.

Usage:  python3 build.py
Needs:  pip install markdown

Every .html file in this repo is generated. Edit the .md sources, re-run this,
and commit both. Never hand-edit the .html.
"""
import io
import os
import re
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))

# slug -> (source file, <html lang>, menu label, page description)
PAGES = {
    "en": ("privacy-policy.en.md", "en", "English", "Privacy Policy"),
    "zh-TW": ("privacy-policy.zh-TW.md", "zh-Hant-TW", "繁體中文", "隱私權政策"),
    "zh-CN": ("privacy-policy.zh-CN.md", "zh-Hans-CN", "简体中文", "隐私政策"),
}
ORDER = ["en", "zh-TW", "zh-CN"]

CSS = """
:root{
  --bg:#fbfaf8; --fg:#23201c; --muted:#6b645b; --rule:#e2ddd5;
  --accent:#7a5c2e; --chip:#f2ede4; --chip-on:#23201c; --chip-on-fg:#fbfaf8;
}
@media (prefers-color-scheme: dark){
  :root{
    --bg:#16150f; --fg:#e9e4da; --muted:#a19889; --rule:#332f26;
    --accent:#d3b077; --chip:#252217; --chip-on:#e9e4da; --chip-on-fg:#16150f;
  }
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; padding:0 1.25rem 5rem; background:var(--bg); color:var(--fg);
  font-family:"Iowan Old Style","Palatino Linotype",Georgia,"Songti TC","Noto Serif CJK TC","Noto Serif CJK SC","Microsoft JhengHei",serif;
  font-size:17px; line-height:1.75;
}
main{max-width:44rem; margin:0 auto}
nav{
  max-width:44rem; margin:0 auto; padding:1.5rem 0 0;
  display:flex; gap:.5rem; flex-wrap:wrap; align-items:center;
  font-family:system-ui,-apple-system,"Segoe UI",sans-serif; font-size:.85rem;
}
nav .brand{margin-right:auto; color:var(--muted); letter-spacing:.02em}
nav a{
  text-decoration:none; color:var(--fg); background:var(--chip);
  padding:.3rem .7rem; border-radius:999px; border:1px solid transparent;
}
nav a:hover{border-color:var(--rule)}
nav a[aria-current="page"]{background:var(--chip-on); color:var(--chip-on-fg)}
h1{font-size:2rem; line-height:1.25; margin:2rem 0 .5rem; letter-spacing:-.01em}
h2{font-size:1.25rem; margin:2.75rem 0 .75rem; padding-top:1.25rem; border-top:1px solid var(--rule)}
h3{font-size:1rem; margin:1.75rem 0 .5rem; color:var(--accent); letter-spacing:.02em}
p,li{margin:.6rem 0}
ul{padding-left:1.25rem}
li::marker{color:var(--muted)}
strong{font-weight:600}
hr{border:0; border-top:1px solid var(--rule); margin:2.5rem 0}
code{
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:.85em;
  background:var(--chip); padding:.1em .35em; border-radius:4px;
}
a{color:var(--accent)}
em{color:var(--muted)}
blockquote{margin:1rem 0; padding-left:1rem; border-left:2px solid var(--rule); color:var(--muted)}
footer{
  max-width:44rem; margin:4rem auto 0; padding-top:1.25rem; border-top:1px solid var(--rule);
  color:var(--muted); font-size:.8rem;
  font-family:system-ui,-apple-system,"Segoe UI",sans-serif;
}
"""

SHELL = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — ListenPost</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<style>{css}</style>
</head>
<body>
<nav>
  <span class="brand">Ashen Knight Games</span>
  {menu}
</nav>
<main>
{body}
</main>
<footer>{footer}</footer>
</body>
</html>
"""

FOOTER = ('Ashen Knight Games · <a href="mailto:support@ashenknightgames.com">'
          'support@ashenknightgames.com</a> · '
          'Source and revision history: '
          '<a href="https://github.com/ashen-knight-games/listening-post-legal">GitHub</a>')


def menu(current):
    out = []
    for slug in ORDER:
        label = PAGES[slug][2]
        mark = ' aria-current="page"' if slug == current else ""
        out.append('<a href="./{s}.html"{m}>{l}</a>'.format(s=slug, m=mark, l=label))
    return "\n  ".join(out)


def render(slug):
    src, lang, _, desc = PAGES[slug]
    text = io.open(os.path.join(HERE, src), encoding="utf-8").read()
    # nl2br keeps the header block (Applies to / Studio / Version / Contact)
    # on separate lines, the way it reads in the Markdown source.
    html = markdown.markdown(text, extensions=["extra", "sane_lists", "nl2br"])
    # the first H1 doubles as the <title>
    m = re.search(r"<h1>(.*?)</h1>", html, re.S)
    title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else desc
    page = SHELL.format(lang=lang, title=title, desc=desc, css=CSS,
                        menu=menu(slug), body=html, footer=FOOTER)
    out = os.path.join(HERE, slug + ".html")
    io.open(out, "w", encoding="utf-8", newline="\n").write(page)
    return out, len(page)


INDEX_BODY = """<h1>ListenPost — Privacy Policy</h1>
<p>Ashen Knight Games. Choose a language / 選擇語言 / 选择语言:</p>
<ul>
<li><a href="./en.html"><strong>English</strong></a> — the authoritative version.</li>
<li><a href="./zh-TW.html"><strong>繁體中文</strong></a> — 譯本，僅供參考。</li>
<li><a href="./zh-CN.html"><strong>简体中文</strong></a> — 译本，仅供参考。</li>
</ul>
<hr>
<p><em>Where the translations differ from the English version, the English version applies.</em></p>
"""


def render_index():
    page = SHELL.format(lang="en", title="Privacy Policy", css=CSS,
                        desc="Privacy Policy for ListenPost by Ashen Knight Games",
                        menu=menu(None), body=INDEX_BODY, footer=FOOTER)
    out = os.path.join(HERE, "index.html")
    io.open(out, "w", encoding="utf-8", newline="\n").write(page)
    return out, len(page)


if __name__ == "__main__":
    for slug in ORDER:
        p, n = render(slug)
        print("wrote %-14s %6d bytes" % (os.path.basename(p), n))
    p, n = render_index()
    print("wrote %-14s %6d bytes" % (os.path.basename(p), n))
