# -*- coding: utf-8 -*-
"""Shared header/footer templates for AESE Lab static site build."""

NAV_ITEMS = [
    ("index.html", "홈", "Home"),
    ("people.html", "구성원", "People"),
    ("research.html", "연구분야", "Research"),
    ("publications.html", "연구성과", "Publications"),
    ("facilities.html", "연구시설", "Facilities"),
    ("news.html", "소식", "News"),
    ("join.html", "모집", "Join Us"),
]


def head(title_ko, title_en, desc, page):
    return f'''<!DOCTYPE html>
<html lang="ko" data-lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_ko} | AESE Lab - Jeju National University</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<script src="script.js"></script>
</head>
<body>
'''


def header(active):
    links = ""
    for href, ko, en in NAV_ITEMS:
        cls = ' class="active"' if href == active else ""
        links += f'    <a href="{href}"{cls}><span class="ko">{ko}</span><span class="en">{en}</span></a>\n'
    return f'''<header class="site-header">
  <div class="nav-wrap">
    <a class="brand" href="index.html">
      <img src="assets/logo.svg" alt="AESE Lab logo">
      <span class="brand-text">
        <span class="brand-name">AESE Lab</span><br>
        <span class="brand-sub"><span class="ko">제주대학교 환경공학과</span><span class="en">Dept. of Environmental Engineering, JNU</span></span>
      </span>
    </a>
    <nav class="main-nav" id="mainNav">
{links}    </nav>
    <div style="display:flex;align-items:center;gap:8px;">
      <button class="lang-toggle" id="langToggle" aria-label="Switch language">ENG</button>
      <button class="menu-btn" id="menuBtn" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
'''


FOOTER = '''<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div>
        <h4><span class="ko">대기 공학 및 지속가능 에너지 연구실</span><span class="en">Atmospheric Engineering and Sustainable Energy Lab.</span></h4>
        <p><span class="ko">제주대학교 환경공학과<br>제주특별자치도 제주시 제주대학로 102, 해양과학대학 3호관</span><span class="en">Department of Environmental Engineering, Jeju National University<br>College of Ocean Science, 3rd Building, 102 Jejudaehak-ro, Jeju-si, Jeju, Republic of Korea</span></p>
      </div>
      <div>
        <h4><span class="ko">바로가기</span><span class="en">Quick Links</span></h4>
        <ul>
          <li><a href="research.html"><span class="ko">연구분야</span><span class="en">Research</span></a></li>
          <li><a href="publications.html"><span class="ko">연구성과</span><span class="en">Publications</span></a></li>
          <li><a href="join.html"><span class="ko">대학원생 모집</span><span class="en">Join Us</span></a></li>
          <li><a href="https://scholar.google.co.kr/citations?user=AMC3wKoAAAAJ" target="_blank" rel="noopener">Google Scholar</a></li>
        </ul>
      </div>
      <div>
        <h4><span class="ko">연락처</span><span class="en">Contact</span></h4>
        <ul>
          <li><a href="mailto:taewoolee@jejunu.ac.kr">taewoolee@jejunu.ac.kr</a></li>
          <li>Tel. 064-754-3444</li>
        </ul>
      </div>
    </div>
    <div class="copyright">&copy; 2026 Atmospheric Engineering and Sustainable Energy Laboratory, Jeju National University. All rights reserved.</div>
  </div>
</footer>
</body>
</html>
'''


def page_hero(t_ko, t_en, s_ko, s_en):
    return f'''<div class="page-hero">
  <div class="container">
    <h1><span class="ko">{t_ko}</span><span class="en">{t_en}</span></h1>
    <p><span class="ko">{s_ko}</span><span class="en">{s_en}</span></p>
  </div>
</div>
'''


def write_page(path, html):
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)
