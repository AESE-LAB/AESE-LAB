# -*- coding: utf-8 -*-
from common import head, header, FOOTER, page_hero, write_page

# ---------------- Facilities ----------------
fac_body = header("facilities.html") + page_hero(
    "연구시설", "Facilities",
    "AESE 연구실이 보유한 주요 분석 장비를 소개합니다.",
    "Major analytical instruments of the AESE Laboratory."
) + '''
<section>
  <div class="container">
    <h2 class="section-title"><span class="ko">주요 장비</span><span class="en">Major Equipment</span></h2>
    <div class="grid-3">
      <div class="card facility-card">
        <img class="f-img" src="assets/equip-placeholder.svg" alt="micro-GC">
        <h3>Micro-GC (TCD + TCD)</h3>
        <p><span class="ko">열분해·가스화 공정에서 생성되는 합성가스(H<sub>2</sub>, CO, CO<sub>2</sub>, CH<sub>4</sub> 등)의 조성을 신속하게 정량 분석합니다.</span>
        <span class="en">Rapid quantitative analysis of syngas composition (H<sub>2</sub>, CO, CO<sub>2</sub>, CH<sub>4</sub>, etc.) generated from pyrolysis and gasification processes.</span></p>
      </div>
      <div class="card facility-card">
        <img class="f-img" src="assets/equip-placeholder.svg" alt="valve GC">
        <h3>Valve GC (TCD + MTN-FID + FID)</h3>
        <p><span class="ko">고정가스와 탄화수소를 동시에 분석할 수 있는 밸브 시스템 GC로, 열화학 반응 생성가스의 정밀 분석에 활용합니다.</span>
        <span class="en">A valve-system GC capable of simultaneous analysis of fixed gases and hydrocarbons, used for precise characterization of gaseous products from thermochemical reactions.</span></p>
      </div>
      <div class="card facility-card">
        <img class="f-img" src="assets/equip-placeholder.svg" alt="BET">
        <h3>BET Surface Area Analyzer</h3>
        <p><span class="ko">촉매, 바이오차, 흡착제 등 다공성 소재의 비표면적과 기공 특성을 분석하여 소재 설계와 성능 평가에 활용합니다.</span>
        <span class="en">Analysis of specific surface area and pore characteristics of porous materials — catalysts, biochar, and adsorbents — for material design and performance evaluation.</span></p>
      </div>
    </div>
    <p class="notice" style="margin-top:26px;">
      <span class="ko">장비 사진은 추후 실제 사진으로 교체될 예정입니다. 장비 이용 문의는 이메일로 연락해 주세요.</span>
      <span class="en">Equipment photos will be updated soon. For equipment use inquiries, please contact us by email.</span>
    </p>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title"><span class="ko">연구실 위치</span><span class="en">Location</span></h2>
    <div class="grid-2">
      <div>
        <img src="assets/lab-photo-placeholder.svg" alt="AESE Lab" style="width:100%;border-radius:12px;border:1px solid #dfe6ec;">
      </div>
      <div class="contact-box">
        <h3 style="color:#0e3a5d;margin-bottom:12px;"><span class="ko">대기 공학 및 지속가능 에너지 연구실</span><span class="en">Atmospheric Engineering and Sustainable Energy Lab.</span></h3>
        <dl class="info-list">
          <dt><span class="ko">위치</span><span class="en">Address</span></dt>
          <dd><span class="ko">제주대학교 해양과학대학 3호관<br>제주특별자치도 제주시 제주대학로 102</span><span class="en">College of Ocean Science, 3rd Building,<br>Jeju National University, 102 Jejudaehak-ro, Jeju-si, Jeju</span></dd>
          <dt>Email</dt><dd>taewoolee@jejunu.ac.kr</dd>
          <dt>Tel</dt><dd>064-754-3444</dd>
        </dl>
      </div>
    </div>
  </div>
</section>
''' + FOOTER

write_page("../facilities.html", head("연구시설", "Facilities",
    "AESE Lab facilities: micro-GC, valve GC, BET surface area analyzer.", "facilities") + fac_body)

# ---------------- News ----------------
news_body = header("news.html") + page_hero(
    "소식", "News",
    "연구실의 논문 게재, 학회 발표, 수상, 연구과제 소식을 전합니다.",
    "Updates on publications, conference presentations, awards, and research projects."
) + '''
<section>
  <div class="container">
    <h2 class="section-title">2026</h2>

    <div class="news-item">
      <div class="news-date">2026.08</div>
      <div>
        <span class="news-cat lab"><span class="ko">연구실</span><span class="en">Lab</span></span>
        <div class="news-title"><span class="ko">AESE 연구실 홈페이지 오픈</span><span class="en">AESE Lab website launched</span></div>
        <div class="news-body"><span class="ko">연구실 공식 홈페이지를 오픈했습니다.</span><span class="en">Our official lab website is now open.</span></div>
      </div>
    </div>

    <div class="news-item">
      <div class="news-date">2026.07</div>
      <div>
        <span class="news-cat conf"><span class="ko">연구과제</span><span class="en">Project</span></span>
        <div class="news-title"><span class="ko">축산환경관리원 연구용역 착수</span><span class="en">New project launched with the Livestock Environment Management Institute</span></div>
        <div class="news-body"><span class="ko">가축분 바이오차 수처리용 담체 활용 기술개발 및 상용화 기반 구축 연구를 시작했습니다.</span><span class="en">Development of livestock manure biochar as water-treatment media and its commercialization.</span></div>
      </div>
    </div>

    <div class="news-item">
      <div class="news-date">2026.04</div>
      <div>
        <span class="news-cat paper"><span class="ko">특허</span><span class="en">Patent</span></span>
        <div class="news-title"><span class="ko">기능성 바이오차 제조 조건 결정 방법 특허 등록</span><span class="en">Patent registered: engineered biochar manufacturing conditions</span></div>
        <div class="news-body"><span class="ko">바이오매스 종류에 따른 기능성 바이오차 제조 조건 결정 방법이 특허 등록되었습니다 (등록번호 1029572690000).</span><span class="en">KR Registration No. 1029572690000 (Apr. 21, 2026).</span></div>
      </div>
    </div>

    <div class="news-item">
      <div class="news-date">2026.04</div>
      <div>
        <span class="news-cat conf"><span class="ko">연구과제</span><span class="en">Project</span></span>
        <div class="news-title"><span class="ko">국가 NDC 달성 기여 토양기반 환경기술개발(R&amp;D) 과제 참여</span><span class="en">Joined the national R&amp;D project on soil-based environmental technology for NDC achievement</span></div>
        <div class="news-body"><span class="ko">기후에너지환경부/한국환경산업기술원 과제에 공동연구자로 참여합니다 (2026.04 – 2030.12).</span><span class="en">Ministry of Climate, Energy and Environment / KEITI (Apr. 2026 – Dec. 2030), as co-researcher.</span></div>
      </div>
    </div>

    <div class="news-item">
      <div class="news-date">2026.03</div>
      <div>
        <span class="news-cat lab"><span class="ko">연구실</span><span class="en">Lab</span></span>
        <div class="news-title"><span class="ko">이태우 교수, 제주대학교 환경공학과 부임 — AESE 연구실 출범</span><span class="en">Prof. Taewoo Lee joined Jeju National University — AESE Lab established</span></div>
        <div class="news-body"><span class="ko">대기 공학 및 지속가능 에너지 연구실이 제주대학교 환경공학과에서 출범했습니다.</span><span class="en">The Atmospheric Engineering and Sustainable Energy Laboratory was established in the Department of Environmental Engineering.</span></div>
      </div>
    </div>

    <div class="news-item">
      <div class="news-date">2026.02</div>
      <div>
        <span class="news-cat award"><span class="ko">수상</span><span class="en">Award</span></span>
        <div class="news-title"><span class="ko">한양대학교 신진연구자 우수연구성과(논문분야) 수상</span><span class="en">Outstanding Research Achievement by Early-Career Researcher, Hanyang University</span></div>
        <div class="news-body"><span class="ko">2년 연속(2025, 2026) 신진연구자 우수연구성과에 선정되었습니다.</span><span class="en">Selected for two consecutive years (2025, 2026).</span></div>
      </div>
    </div>

    <div class="news-item">
      <div class="news-date">2026</div>
      <div>
        <span class="news-cat paper"><span class="ko">논문</span><span class="en">Paper</span></span>
        <div class="news-title"><span class="ko">Energy Conversion and Management 논문 게재</span><span class="en">Paper published in Energy Conversion and Management</span></div>
        <div class="news-body">CO2-assisted control of H2/CO ratio in plastic waste pyrolysis (IF 11.8, JCR 98.1%)</div>
      </div>
    </div>

    <div class="news-item">
      <div class="news-date">2026</div>
      <div>
        <span class="news-cat conf"><span class="ko">학회</span><span class="en">Conference</span></span>
        <div class="news-title"><span class="ko">국내외 학회 발표</span><span class="en">Conference presentations</span></div>
        <div class="news-body"><span class="ko">춘계 폐기물자원순환학회(평창, 구두), 춘계 청정기술학회(부산, 포스터), CMEE(발리, 구두), 추계 폐기물자원순환학회 신진연구자 세션(여수, 구두)에서 연구 성과를 발표했습니다.</span><span class="en">Presented at the KSWM Spring Conference (Pyeongchang, oral), KSCT Spring Conference (Busan, poster), CMEE (Bali, oral), and the KSWM Fall Conference Early-Career Researcher Session (Yeosu, oral).</span></div>
      </div>
    </div>

  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title">2025</h2>
    <div class="news-item">
      <div class="news-date">2025</div>
      <div>
        <span class="news-cat paper"><span class="ko">논문</span><span class="en">Paper</span></span>
        <div class="news-title"><span class="ko">Progress in Energy and Combustion Science 리뷰 논문 게재</span><span class="en">Review published in Progress in Energy and Combustion Science</span></div>
        <div class="news-body">Recovery of chemicals and energy through thermo-chemical processing of plastic waste (IF 41.3, JCR 99.7%)</div>
      </div>
    </div>
    <div class="news-item">
      <div class="news-date">2025.02</div>
      <div>
        <span class="news-cat award"><span class="ko">수상</span><span class="en">Award</span></span>
        <div class="news-title"><span class="ko">한양대학교 신진연구자 우수연구성과(논문분야) 수상</span><span class="en">Outstanding Research Achievement by Early-Career Researcher, Hanyang University</span></div>
      </div>
    </div>
  </div>
</section>
''' + FOOTER

write_page("../news.html", head("소식", "News",
    "News from AESE Lab: publications, awards, conferences, and projects.", "news") + news_body)

# ---------------- Join ----------------
join_body = header("join.html") + page_hero(
    "모집 안내", "Join Us",
    "폐기물 에너지화와 대기오염제어 연구에 함께할 열정적인 인재를 찾습니다.",
    "We are looking for passionate students to join our research on waste-to-energy and air pollution control."
) + '''
<section>
  <div class="container">
    <div class="join-highlight" style="margin-bottom:40px;">
      <h3><span class="ko">대학원생 및 학부연구생 상시 모집</span><span class="en">Graduate &amp; Undergraduate Researchers — Open Recruitment</span></h3>
      <p><span class="ko">지원 전 반드시 이메일로 사전 연락해 주세요. 관심 분야와 간단한 자기소개(이력서, 성적표 등)를 함께 보내주시면 좋습니다.</span>
      <span class="en">Please email me in advance before applying. Including your research interests and a brief introduction (CV, transcript) is appreciated.</span></p>
      <a class="btn" href="mailto:taewoolee@jejunu.ac.kr"><span class="ko">이메일 보내기</span><span class="en">Send Email</span></a>
    </div>

    <h2 class="section-title"><span class="ko">모집 분야</span><span class="en">Research Areas for Recruitment</span></h2>
    <div class="chips" style="margin-bottom:40px;">
      <span class="chip"><span class="ko">폐기물 에너지화</span><span class="en">Waste-to-Energy</span></span>
      <span class="chip"><span class="ko">열분해 · 열화학 공정</span><span class="en">Pyrolysis · Thermochemical Process</span></span>
      <span class="chip"><span class="ko">CO<sub>2</sub> 활용</span><span class="en">CO<sub>2</sub> Utilization</span></span>
      <span class="chip"><span class="ko">바이오리파이너리 · 바이오차</span><span class="en">Biorefinery · Biochar</span></span>
      <span class="chip"><span class="ko">대기오염제어 · 열촉매</span><span class="en">Air Pollution Control · Thermocatalysis</span></span>
      <span class="chip"><span class="ko">VOC 산화</span><span class="en">VOC Oxidation</span></span>
    </div>

    <h2 class="section-title"><span class="ko">모집 대상</span><span class="en">Who Can Apply</span></h2>
    <div class="grid-3" style="margin-bottom:40px;">
      <div class="card">
        <h3><span class="ko">석사 · 박사과정</span><span class="en">M.S. / Ph.D. Students</span></h3>
        <p><span class="ko">환경공학, 화학공학, 에너지공학 등 관련 전공의 대학원 진학 희망자</span><span class="en">Prospective graduate students in environmental, chemical, or energy engineering and related fields.</span></p>
      </div>
      <div class="card">
        <h3><span class="ko">학부연구생</span><span class="en">Undergraduate Researchers</span></h3>
        <p><span class="ko">연구 경험을 쌓고 싶은 학부생 (전공·학년 무관, 관심과 열정 중시)</span><span class="en">Undergraduates who want research experience — motivation matters more than major or year.</span></p>
      </div>
      <div class="card">
        <h3><span class="ko">연구원 · 공동연구</span><span class="en">Researchers &amp; Collaboration</span></h3>
        <p><span class="ko">박사후연구원 및 공동연구 제안도 언제든 환영합니다.</span><span class="en">Postdoctoral researchers and collaboration proposals are always welcome.</span></p>
      </div>
    </div>

    <h2 class="section-title"><span class="ko">지원 방법</span><span class="en">How to Apply</span></h2>
    <ul class="timeline" style="max-width:640px;">
      <li>
        <div class="t-title"><span class="ko">1. 이메일 사전 연락</span><span class="en">1. Email in advance</span></div>
        <div class="t-meta"><span class="ko">taewoolee@jejunu.ac.kr 로 관심 분야와 자기소개를 보내주세요.</span><span class="en">Send your research interests and a brief introduction to taewoolee@jejunu.ac.kr.</span></div>
      </li>
      <li>
        <div class="t-title"><span class="ko">2. 면담</span><span class="en">2. Meeting</span></div>
        <div class="t-meta"><span class="ko">연구 주제와 대학원 생활에 대해 충분히 이야기를 나눕니다.</span><span class="en">We will discuss research topics and graduate life in depth.</span></div>
      </li>
      <li>
        <div class="t-title"><span class="ko">3. 지원 및 합류</span><span class="en">3. Apply &amp; Join</span></div>
        <div class="t-meta"><span class="ko">제주대학교 대학원 모집 일정에 맞추어 지원합니다.</span><span class="en">Apply according to the JNU graduate admissions schedule.</span></div>
      </li>
    </ul>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title"><span class="ko">연락처</span><span class="en">Contact</span></h2>
    <div class="grid-2">
      <div class="contact-box">
        <dl class="info-list">
          <dt><span class="ko">지도교수</span><span class="en">PI</span></dt>
          <dd><span class="ko">이태우 조교수</span><span class="en">Prof. Taewoo Lee</span></dd>
          <dt>Email</dt><dd><a href="mailto:taewoolee@jejunu.ac.kr" style="color:#1a6fae;">taewoolee@jejunu.ac.kr</a></dd>
          <dt>Tel</dt><dd>064-754-3444</dd>
          <dt><span class="ko">위치</span><span class="en">Location</span></dt>
          <dd><span class="ko">제주대학교 해양과학대학 3호관</span><span class="en">College of Ocean Science, 3rd Building, Jeju National University</span></dd>
        </dl>
      </div>
      <div class="contact-box">
        <h3 style="color:#0e3a5d;margin-bottom:10px;"><span class="ko">이런 분과 함께하고 싶습니다</span><span class="en">We look for students who…</span></h3>
        <p style="color:#4b5966;font-size:0.92rem;">
          <span class="ko">에너지·환경 문제 해결에 관심이 있고, 실험과 데이터 분석을 통해 성장하고 싶은 분이라면 전공과 무관하게 환영합니다. 신생 연구실인 만큼 연구 주제 선정부터 논문 작성까지 밀착 지도를 받을 수 있습니다.</span>
          <span class="en">Anyone interested in solving energy and environmental problems and growing through experiments and data analysis is welcome, regardless of major. As a newly established lab, students receive close, hands-on mentoring from topic selection to publication.</span>
        </p>
      </div>
    </div>
  </div>
</section>
''' + FOOTER

write_page("../join.html", head("모집 안내", "Join Us",
    "Join AESE Lab — graduate and undergraduate researcher recruitment. Please email in advance.", "join") + join_body)

# ---------------- 404 ----------------
notfound = head("페이지를 찾을 수 없습니다", "Page Not Found", "Page not found", "404") + header("") + '''
<section style="text-align:center;padding:100px 0;">
  <div class="container">
    <h1 style="font-size:4rem;color:#0e3a5d;font-weight:800;">404</h1>
    <p style="color:#4b5966;margin:14px 0 26px;"><span class="ko">요청하신 페이지를 찾을 수 없습니다.</span><span class="en">The page you are looking for could not be found.</span></p>
    <a class="btn btn-primary" href="index.html"><span class="ko">홈으로 돌아가기</span><span class="en">Back to Home</span></a>
  </div>
</section>
''' + FOOTER
write_page("../404.html", notfound)
