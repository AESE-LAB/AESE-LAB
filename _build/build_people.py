# -*- coding: utf-8 -*-
from common import head, header, FOOTER, page_hero, write_page

body = header("people.html") + page_hero(
    "구성원", "People",
    "대기 공학 및 지속가능 에너지 연구실의 구성원을 소개합니다.",
    "Meet the members of the Atmospheric Engineering and Sustainable Energy Laboratory."
) + '''
<section>
  <div class="container">
    <h2 class="section-title"><span class="ko">지도교수</span><span class="en">Principal Investigator</span></h2>
    <div class="profile-grid">
      <div>
        <img class="profile-photo" src="assets/profile-placeholder.svg" alt="Prof. Taewoo Lee">
      </div>
      <div>
        <div class="profile-name"><span class="ko">이태우</span><span class="en">Taewoo Lee, Ph.D.</span></div>
        <div class="profile-role"><span class="ko">조교수, 제주대학교 환경공학과</span><span class="en">Assistant Professor, Dept. of Environmental Engineering, Jeju National University</span></div>
        <div class="profile-links">
          <a href="https://scholar.google.co.kr/citations?user=AMC3wKoAAAAJ" target="_blank" rel="noopener">Google Scholar</a>
          <a href="https://orcid.org/0000-0002-0017-3716" target="_blank" rel="noopener">ORCID</a>
          <a href="https://www.scopus.com/authid/detail.uri?authorId=57194348573" target="_blank" rel="noopener">Scopus</a>
          <a href="mailto:taewoolee@jejunu.ac.kr">Email</a>
        </div>
        <dl class="info-list">
          <dt>Email</dt><dd>taewoolee@jejunu.ac.kr</dd>
          <dt>Tel</dt><dd>064-754-3444</dd>
          <dt><span class="ko">연구실</span><span class="en">Office</span></dt>
          <dd><span class="ko">제주대학교 해양과학대학 3호관</span><span class="en">College of Ocean Science, 3rd Building, Jeju National University</span></dd>
        </dl>
      </div>
    </div>

    <div class="grid-2" style="margin-top:40px;">
      <div>
        <h3 style="color:#0e3a5d;margin-bottom:16px;"><span class="ko">학력</span><span class="en">Education</span></h3>
        <ul class="timeline">
          <li>
            <div class="t-title"><span class="ko">한양대학교 자원환경공학과 박사</span><span class="en">Ph.D., Earth Resources and Environmental Engineering, Hanyang University</span></div>
            <div class="t-meta">2024</div>
          </li>
          <li>
            <div class="t-title"><span class="ko">세종대학교 환경에너지학과 석사</span><span class="en">M.S., Environment and Energy, Sejong University</span></div>
            <div class="t-meta">2019</div>
          </li>
          <li>
            <div class="t-title"><span class="ko">세종대학교 환경에너지학과 학사</span><span class="en">B.S., Environment and Energy, Sejong University</span></div>
            <div class="t-meta">2016</div>
          </li>
        </ul>
      </div>
      <div>
        <h3 style="color:#0e3a5d;margin-bottom:16px;"><span class="ko">주요 경력</span><span class="en">Professional Experience</span></h3>
        <ul class="timeline">
          <li>
            <div class="t-title"><span class="ko">제주대학교 환경공학과 조교수</span><span class="en">Assistant Professor, Dept. of Environmental Engineering, Jeju National University</span></div>
            <div class="t-meta"><span class="ko">2026.03 – 현재</span><span class="en">Mar. 2026 – Present</span></div>
          </li>
          <li>
            <div class="t-title"><span class="ko">한양대학교 자원환경공학과 박사후연구원</span><span class="en">Postdoctoral Researcher, Dept. of Earth Resources and Environmental Engineering, Hanyang University</span></div>
            <div class="t-meta"><span class="ko">2024.03 – 2026.02</span><span class="en">Mar. 2024 – Feb. 2026</span></div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title"><span class="ko">수상 및 활동</span><span class="en">Awards &amp; Activities</span></h2>
    <div class="grid-2">
      <div class="card">
        <h3><span class="ko">수상</span><span class="en">Awards</span></h3>
        <ul class="plain-list">
          <li><strong><span class="ko">신진연구자 우수연구성과 (논문분야)</span><span class="en">Outstanding Research Achievement by Early-Career Researcher</span></strong><br><span class="ko">한양대학교 (2026.02)</span><span class="en">Hanyang University (Feb. 2026)</span></li>
          <li><strong><span class="ko">신진연구자 우수연구성과 (논문분야)</span><span class="en">Outstanding Research Achievement by Early-Career Researcher</span></strong><br><span class="ko">한양대학교 (2025.02)</span><span class="en">Hanyang University (Feb. 2025)</span></li>
          <li><strong><span class="ko">박사학위 우수논문상</span><span class="en">Outstanding Doctoral Dissertation Award</span></strong><br><span class="ko">한양대학교 산업과학연구소 (2024.02)</span><span class="en">The Research Institute of Industrial Science, Hanyang University (Feb. 2024)</span></li>
          <li><strong><span class="ko">박사학위 우수논문상</span><span class="en">Outstanding Doctoral Dissertation Award</span></strong><br><span class="ko">한양대학교 (2024.02)</span><span class="en">Hanyang University (Feb. 2024)</span></li>
        </ul>
      </div>
      <div class="card">
        <h3><span class="ko">학회 및 사회 활동</span><span class="en">Academic Service</span></h3>
        <ul class="plain-list">
          <li><strong><span class="ko">폐기물자원순환학회 학술위원회 위원</span><span class="en">Academic Committee Member, Korea Society of Waste Management</span></strong><br><span class="ko">2026 – 현재</span><span class="en">2026 – Present</span></li>
          <li><strong><span class="ko">폐기물자원순환학회 무기물및바이오차위원회 위원</span><span class="en">Inorganics and Biochar Committee Member, Korea Society of Waste Management</span></strong><br><span class="ko">2026 – 현재</span><span class="en">2026 – Present</span></li>
          <li><strong><span class="ko">서귀포시 남부환경관리센터 산남주민지원협의체 위원</span><span class="en">Advisory Committee Member, Seogwipo Southern Environmental Management Center</span></strong><br><span class="ko">2026.02 – 2028.02</span><span class="en">Feb. 2026 – Feb. 2028</span></li>
          <li><strong><span class="ko">자격: 수질환경기사 (2015.11), 대기환경기사 (2015.12)</span><span class="en">Licenses: Engineer, Water Pollution Environmental (Nov. 2015); Engineer, Air Pollution Environmental (Dec. 2015)</span></strong><br><span class="ko">한국산업인력공단</span><span class="en">Human Resources Development Service of Korea</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-title"><span class="ko">연구실 구성원</span><span class="en">Lab Members</span></h2>
    <div class="grid-3">
      <div class="card member-card">
        <img class="avatar" src="assets/member-placeholder.svg" alt="Jisu Jang">
        <div class="m-name"><span class="ko">장지수</span><span class="en">Jisu Jang</span></div>
        <div class="m-role"><span class="ko">석사과정</span><span class="en">M.S. Student</span></div>
        <div class="m-topic"><span class="ko">폐기물 연료화 및 연소특성 평가</span><span class="en">Waste-to-fuel conversion and combustion characteristics</span></div>
      </div>
      <div class="card member-card" style="border-style:dashed;background:#fbfdfe;">
        <img class="avatar" src="assets/member-placeholder.svg" alt="">
        <div class="m-name"><span class="ko">당신의 이름</span><span class="en">Your Name Here</span></div>
        <div class="m-role"><span class="ko">대학원생 · 학부연구생</span><span class="en">Graduate / Undergraduate</span></div>
        <div class="m-topic"><a href="join.html" style="color:#2e8b6e;font-weight:700;"><span class="ko">모집 안내 보기 →</span><span class="en">See Join Us →</span></a></div>
      </div>
    </div>
    <h3 style="color:#0e3a5d;margin:34px 0 10px;"><span class="ko">졸업생</span><span class="en">Alumni</span></h3>
    <p style="color:#4b5966;font-size:0.92rem;"><span class="ko">2026년에 출범한 신생 연구실로, 아직 졸업생이 없습니다.</span><span class="en">As a newly established lab (2026), we do not yet have alumni.</span></p>
  </div>
</section>
''' + FOOTER

html = head("구성원", "People",
            "AESE Lab members: Prof. Taewoo Lee and graduate students, Department of Environmental Engineering, Jeju National University.",
            "people") + body
write_page("../people.html", html)
