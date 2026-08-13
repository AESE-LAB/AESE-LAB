# -*- coding: utf-8 -*-
from common import head, header, FOOTER, page_hero, write_page

PUBS = [
    ("T. Lee, G. Moon, Y.-M. Kim, E.E. Kwon.",
     "CO2-assisted control of H2/CO ratio in plastic waste pyrolysis",
     "Energy Conversion and Management", "350 (2026) 120997",
     "10.1016/j.enconman.2025.120997", "IF 11.8 · JCR 98.1%"),
    ("T. Lee, D. Kwon, S. Lee, Y. Kim, J.Y. Kim, H. Song, et al.",
     "Recovery of chemicals and energy through thermo-chemical processing of plastic waste",
     "Progress in Energy and Combustion Science", "108 (2025) 101219",
     "10.1016/j.pecs.2025.101219", "IF 41.3 · JCR 99.7%"),
    ("T. Lee, G. Park, H. Cha, H. Nam, H.W. Kim, E.E. Kwon.",
     "Biochar utilization in thermochemical biodiesel production from perilla seed",
     "Chemical Engineering Journal", "525 (2025) 170661",
     "10.1016/j.cej.2025.170661", "IF 12.5 · JCR 96.0%"),
    ("T. Lee, H. Cha, J.Y. Kim, H. Choi, J. Lee, S. Yun, et al.",
     "Modifying carbon feedback by transforming arctic soil into biochar",
     "Renewable and Sustainable Energy Reviews", "216 (2025) 115712",
     "10.1016/j.rser.2025.115712", "IF 18.0 · JCR 96.9%"),
    ("T. Lee, S. Lee, Y.F. Tsang, E.E. Kwon.",
     "Carbon-negative power generation using syngas produced from CO2-cofeeding pyrolysis of lignocellulosic biomass",
     "Energy", "325 (2025) 136215",
     "10.1016/j.energy.2025.136215", "IF 10.1 · JCR 96.8%"),
    ("T. Lee, J.-H. Kim, H. Choi, Y. Kim, S.-J. Park, E.E. Kwon.",
     "Pyrolytic conversion of polyimide into carbon-based CO2 adsorbent with in-situ suppression of toxic byproducts",
     "Polymer Degradation and Stability", "234 (2025) 111193",
     "10.1016/j.polymdegradstab.2025.111193", "IF 8.1 · JCR 93.2%"),
    ("T. Lee, H. Cha, S. Lee, J. Lee, E.E. Kwon.",
     "Production of CO-rich syngas through CO2-Mediated pyrolysis of plastic waste and its practical use for power generation",
     "Energy", "319 (2025) 135053",
     "10.1016/j.energy.2025.135053", "IF 10.1 · JCR 96.8%"),
    ("T. Lee, J. Park, Y. Kim, W.-H. Chen, E.E. Kwon.",
     "Comparison of toxic pyrogenic compounds derived from conventional cigarettes and heated tobacco products",
     "Journal of Hazardous Materials", "493 (2025) 138357",
     "10.1016/j.jhazmat.2025.138357", "IF 10.6 · JCR 93.0%"),
    ("T. Lee, D. Choi, J. Park, Y.F. Tsang, K.Y. Andrew Lin, S. Jung, et al.",
     "Valorizing spent mushroom substrate into syngas by the thermo-chemical process",
     "Bioresource Technology", "391 (2024) 130007",
     "10.1016/j.biortech.2023.130007", "IF 8.2 · JCR 97.7%"),
    ("T. Lee, S. Jung, S. Lee, Y.F. Tsang, K.H. Lee, E.E. Kwon.",
     "Production of aviation fuel via thermal cracking of plastic waste",
     "Energy Conversion and Management", "315 (2024) 118827",
     "10.1016/j.enconman.2024.118827", "IF 11.8 · JCR 98.1%"),
]

pub_items = ""
for authors, title, journal, volinfo, doi, ifjcr in PUBS:
    pub_items += f'''      <li class="pub-item">
        <span class="pub-no"></span>
        <div>
          <div class="pub-title">{title}</div>
          <div class="pub-meta">{authors} <span class="journal">{journal}</span>, {volinfo}.</div>
          <span class="pub-if">{ifjcr}</span>
        </div>
        <a class="doi-btn" href="https://doi.org/{doi}" target="_blank" rel="noopener">DOI</a>
      </li>
'''

body = header("publications.html") + page_hero(
    "연구성과", "Publications",
    "대표 논문, 특허, 학술발표 등 연구 성과를 소개합니다. 전체 논문 목록은 Google Scholar에서 확인할 수 있습니다.",
    "Selected publications, patents, and presentations. The full publication list is available on Google Scholar."
) + f'''
<section>
  <div class="container">
    <h2 class="section-title"><span class="ko">논문 요약</span><span class="en">Publication Summary</span></h2>
    <div class="stats">
      <div class="stat"><div class="num">69</div><div class="label"><span class="ko">전체 논문</span><span class="en">Total Publications</span></div></div>
      <div class="stat"><div class="num">38</div><div class="label"><span class="ko">제1저자·교신저자 논문</span><span class="en">First/Corresponding Author</span></div></div>
      <div class="stat"><div class="num">20</div><div class="label">H-index</div></div>
      <div class="stat"><div class="num">1,296<small>+</small></div><div class="label"><span class="ko">피인용 횟수</span><span class="en">Citations</span></div></div>
    </div>
    <p style="margin-top:14px;font-size:0.8rem;color:#8aa5ba;">
      <span class="ko">* Google Scholar 기준 (2026년 7월 기준) · 교신저자 1편, 제1저자 37편, 공저자 32편</span>
      <span class="en">* Based on Google Scholar (as of Jul. 2026) · Corresponding author: 1, first author: 37, co-author: 32</span>
    </p>
    <div class="btn-row" style="margin-top:18px;">
      <a class="btn btn-primary" href="https://scholar.google.co.kr/citations?user=AMC3wKoAAAAJ" target="_blank" rel="noopener">Google Scholar</a>
      <a class="btn btn-outline" href="https://orcid.org/0000-0002-0017-3716" target="_blank" rel="noopener">ORCID</a>
      <a class="btn btn-outline" href="https://www.scopus.com/authid/detail.uri?authorId=57194348573" target="_blank" rel="noopener">Scopus</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title"><span class="ko">대표 논문</span><span class="en">Selected Publications</span></h2>
    <ol class="pub-list">
{pub_items}    </ol>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-title"><span class="ko">북챕터</span><span class="en">Book Chapter</span></h2>
    <ul class="plain-list">
      <li><strong>Ecological Impacts of Microplastics on Marine Organisms.</strong><br>
      Lee, T., Kim, J. Y., &amp; Kwon, E. E. (2027). In <em>Handbook of Microplastics and Associated Chemicals</em> (pp. 199–221). CRC Press.</li>
    </ul>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title"><span class="ko">특허</span><span class="en">Patents</span></h2>
    <ul class="plain-list">
      <li><span class="tag reg"><span class="ko">등록</span><span class="en">Registered</span></span>
        <strong><span class="ko">제조되는 기능성 바이오차의 수율 및 흡착 성능을 향상시키기 위한 바이오매스의 종류에 따른 기능성 바이오차 제조 조건을 결정하는 방법</span><span class="en">Method for determining engineered biochar manufacturing conditions according to types of biomass to improve yield and adsorption performance</span></strong><br>
        <span class="ko">권일한, 이태우, 이상윤, 정성엽 · 세종대학교 산학협력단 · 등록번호 1029572690000 (2026.04.21)</span>
        <span class="en">E.E. Kwon; T. Lee; S. Lee; S. Jung · Sejong University IUCF · KR Registration No. 1029572690000 (Apr. 21, 2026)</span></li>
      <li><span class="tag reg"><span class="ko">등록</span><span class="en">Registered</span></span>
        <strong><span class="ko">이산화탄소의 연료화 방법</span><span class="en">Method of converting carbon dioxide to fuels</span></strong><br>
        <span class="ko">권일한, 이태우, 정성엽 · 세종대학교 산학협력단 · 등록번호 1025358490000 (2023.05.18)</span>
        <span class="en">E.E. Kwon; T. Lee; S. Jung · Sejong University IUCF · KR Registration No. 1025358490000 (May 18, 2023)</span></li>
      <li><span class="tag reg"><span class="ko">등록</span><span class="en">Registered</span></span>
        <strong><span class="ko">혐기성소화조의 중간생성물을 이용한 바이오알코올의 제조방법</span><span class="en">Method for producing bio-alcohol from intermediate products of anaerobic digestion tank</span></strong><br>
        <span class="ko">권일한, 정종민, 조성헌, 최동호, 이태우 외 · 세종대학교 산학협력단 · 등록번호 1022720120000 (2021.06.28)</span>
        <span class="en">E.E. Kwon; J.M. Jung; S.H. Cho; D. Choi; T. Lee et al. · Sejong University IUCF · KR Registration No. 1022720120000 (Jun. 28, 2021)</span></li>
      <li><span class="tag reg"><span class="ko">등록</span><span class="en">Registered</span></span>
        <strong><span class="ko">중력 보상 기반 자립형 휠체어</span><span class="en">Passive self-standable wheelchair with weight compensation unit</span></strong><br>
        <span class="ko">곽관웅, 이태우, 김경진, 최이주 · 세종대학교 산학협력단 · 등록번호 1018956790000 (2018.08.31)</span>
        <span class="en">K.W. Gwak; T. Lee; K. Kim; I. Choi · Sejong University IUCF · KR Registration No. 1018956790000 (Aug. 31, 2018)</span></li>
      <li><span class="tag app"><span class="ko">출원</span><span class="en">Application</span></span>
        <strong><span class="ko">조리흄 포집 및 분석 장치와 조리흄 포집 및 분석 방법</span><span class="en">Cooking fume collection and analysis method</span></strong><br>
        <span class="ko">권일한, 김민영, 최동호, 이태우 외 · 한양대학교 산학협력단 · 출원번호 1020240136090 (2024.10.07)</span>
        <span class="en">E.E. Kwon; M. Kim; D. Choi; T. Lee et al. · Hanyang University IUCF · KR Application No. 1020240136090 (Oct. 7, 2024)</span></li>
    </ul>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-title"><span class="ko">학술발표</span><span class="en">Conference Presentations</span></h2>
    <ul class="plain-list">
      <li><strong><span class="ko">춘계 폐기물자원순환학회</span><span class="en">Korea Society of Waste Management, Spring Conference</span></strong> — <span class="ko">구두발표, 평창 알펜시아</span><span class="en">Oral presentation, Alpensia, Pyeongchang</span></li>
      <li><strong><span class="ko">춘계 청정기술학회</span><span class="en">Korean Society of Clean Technology, Spring Conference</span></strong> — <span class="ko">포스터, 부산 벡스코</span><span class="en">Poster, BEXCO, Busan</span></li>
      <li><strong>CMEE</strong> — <span class="ko">구두발표, 발리</span><span class="en">Oral presentation, Bali</span></li>
      <li><strong><span class="ko">추계 폐기물자원순환학회 신진연구자 세션</span><span class="en">Korea Society of Waste Management, Fall Conference (Early-Career Researcher Session)</span></strong> — <span class="ko">구두발표, 여수 소노캄</span><span class="en">Oral presentation, Sono Calm, Yeosu</span></li>
    </ul>
  </div>
</section>
''' + FOOTER

html = head("연구성과", "Publications",
            "Selected publications, patents, and conference presentations of AESE Lab, Jeju National University.",
            "publications") + body
write_page("../publications.html", html)
