# -*- coding: utf-8 -*-
from common import head, header, FOOTER, page_hero, write_page

body = header("research.html") + page_hero(
    "연구분야", "Research",
    "대기오염물질의 발생을 원천적으로 줄이는 사전 제어 기술과 배출가스를 효율적으로 저감하는 사후 공학적 처리 기술을 포괄적으로 연구합니다.",
    "We conduct comprehensive research on source reduction technologies to minimize the generation of air pollutants and advanced treatment technologies to remove air pollutants from exhaust gases."
) + '''
<section>
  <div class="container">
    <h2 class="section-title"><span class="ko">연구실 소개</span><span class="en">About Our Research</span></h2>
    <p style="max-width:860px;color:#4b5966;">
      <span class="ko">대기 공학 및 지속가능 에너지 연구실은 열화학적 공정을 활용한 폐기물 에너지화를 통해 연료 특성과 연소 효율을 개선하고, 이를 바탕으로 대기오염물질의 발생을 선제적으로 줄이는 기술을 개발합니다. 또한, 연소시설에서 배출되는 휘발성유기화합물(VOCs)을 비롯한 다양한 오염물질의 제거 효율을 높이기 위해 촉매 처리 공정의 설계 및 운전 기술을 연구합니다.</span>
      <span class="en">The AESE Laboratory develops thermochemical conversion platforms for waste-to-energy to enhance fuel properties and combustion efficiency, thereby mitigating the formation of air pollutants. Additionally, our laboratory designs catalytic treatment processes to improve the removal efficiency of various air pollutants, including volatile organic compounds (VOCs).</span>
    </p>
    <div style="margin-top:30px;text-align:center;">
      <img src="assets/hero-diagram.svg" alt="Research process diagram" style="max-width:560px;width:100%;">
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title"><span class="ko">세부 연구 주제</span><span class="en">Research Topics</span></h2>
    <div class="grid-2">
      <div class="card">
        <img class="icon" src="assets/research-thermochemical.svg" alt="">
        <h3><span class="ko">폐기물 에너지화 · 열분해</span><span class="en">Waste-to-Energy &amp; Pyrolysis</span></h3>
        <p><span class="ko">플라스틱 폐기물, 바이오매스 등 폐자원의 열화학적 처리(열분해)를 통해 합성가스(syngas), 항공유 등 고부가가치 연료와 화학물질을 회수하는 기술을 연구합니다.</span>
        <span class="en">We recover high-value fuels and chemicals — such as syngas and aviation fuel — through thermochemical processing (pyrolysis) of plastic waste and biomass.</span></p>
      </div>
      <div class="card">
        <img class="icon" src="assets/research-co2.svg" alt="">
        <h3><span class="ko">CO<sub>2</sub> 활용</span><span class="en">CO<sub>2</sub> Utilization</span></h3>
        <p><span class="ko">CO<sub>2</sub>를 반응 매체로 활용하는 열분해 공정을 통해 H<sub>2</sub>/CO 비율 제어, CO-rich 합성가스 생산 등 탄소중립·탄소네거티브 에너지 전환 기술을 개발합니다.</span>
        <span class="en">Using CO<sub>2</sub> as a reaction medium in pyrolysis, we develop carbon-neutral and carbon-negative energy conversion technologies, including H<sub>2</sub>/CO ratio control and CO-rich syngas production.</span></p>
      </div>
      <div class="card">
        <img class="icon" src="assets/research-biochar.svg" alt="">
        <h3><span class="ko">바이오리파이너리 · 바이오차</span><span class="en">Biorefinery &amp; Biochar</span></h3>
        <p><span class="ko">바이오매스 기반 연료 생산(바이오디젤 등)과 기능성 바이오차 제조·활용 기술을 연구하여 탄소 저감과 자원순환에 기여합니다.</span>
        <span class="en">We study biomass-based fuel production (e.g., biodiesel) and the synthesis and application of engineered biochar, contributing to carbon reduction and resource circulation.</span></p>
      </div>
      <div class="card">
        <img class="icon" src="assets/research-voc.svg" alt="">
        <h3><span class="ko">열촉매 반응 · VOC 산화</span><span class="en">Thermocatalysis &amp; VOC Oxidation</span></h3>
        <p><span class="ko">연소시설 배출가스 중 VOCs 등 대기오염물질을 효율적으로 제거하기 위한 촉매 소재 및 촉매 처리 공정의 설계·운전 기술을 연구합니다.</span>
        <span class="en">We design catalytic materials and processes for the efficient removal of VOCs and other air pollutants from combustion exhaust gases.</span></p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-title"><span class="ko">연구 과제</span><span class="en">Research Projects</span></h2>
    <h3 style="color:#0e3a5d;margin-bottom:12px;"><span class="ko">진행 중 과제</span><span class="en">Ongoing Projects</span></h3>
    <ul class="plain-list">
      <li><span class="tag pi">PI</span><strong><span class="ko">세종과학펠로우십(국내트랙)</span><span class="en">Sejong Science Fellowship (Domestic Track)</span></strong> — <span class="ko">한국연구재단 개인기초연구</span><span class="en">National Research Foundation of Korea</span> (2024.05 – 2029.04)</li>
      <li><span class="tag co">Co-PI</span><strong><span class="ko">국가 NDC 달성 기여를 위한 토양기반 환경기술 개발(R&amp;D)</span><span class="en">Soil-based Environmental Technology Development for National NDC Achievement (R&amp;D)</span></strong> — <span class="ko">기후에너지환경부/한국환경산업기술원</span><span class="en">Ministry of Climate, Energy and Environment / KEITI</span> (2026.04 – 2030.12)</li>
      <li><span class="tag co">Co-PI</span><strong><span class="ko">(탄소중립공학 트랙) 전략산업 생태계 육성 및 미래 혁신산업 강화사업</span><span class="en">(Carbon-Neutral Engineering Track) Strategic Industry Ecosystem &amp; Future Innovation Program</span></strong> — <span class="ko">RISE 산학공동연구(R&amp;D)</span><span class="en">RISE Industry-Academia Joint Research (R&amp;D)</span> (– 2027.02)</li>
      <li><span class="tag co">Co-PI</span><strong><span class="ko">폐자원특성화대학</span><span class="en">Waste Resource Specialization University Program</span></strong> — <span class="ko">수도권매립지공사 폐자원에너지과</span><span class="en">Sudokwon Landfill Site Management Corp.</span> (2026.03 – 2027.02)</li>
      <li><span class="tag co">Co-PI</span><strong><span class="ko">가축분 바이오차 수처리용 담체 활용 기술개발 및 상용화 기반 구축 연구</span><span class="en">Livestock Manure Biochar as Water-Treatment Media: Technology Development &amp; Commercialization</span></strong> — <span class="ko">축산환경관리원</span><span class="en">Livestock Environment Management Institute</span> (2026.07 – 2026.12)</li>
      <li><span class="tag pi">PI</span><strong><span class="ko">2026 RISE 런케이션 프로그램 지원사업</span><span class="en">2026 RISE Learncation Program</span></strong> (2026.08 – 2027.01)</li>
      <li><span class="tag pi">PI</span><strong><span class="ko">2026 신진연구자 연구생태계 조성사업</span><span class="en">2026 Early-Career Researcher Ecosystem Program</span></strong> — <span class="ko">제주대학교</span><span class="en">Jeju National University</span> (2026.09 – 2027.01)</li>
    </ul>
    <h3 style="color:#0e3a5d;margin:26px 0 12px;"><span class="ko">종료된 과제</span><span class="en">Completed Projects</span></h3>
    <ul class="plain-list">
      <li><span class="tag pi">PI</span><strong><span class="ko">글로벌박사펠로우십</span><span class="en">Global Ph.D. Fellowship</span></strong> — <span class="ko">한국연구재단</span><span class="en">National Research Foundation of Korea</span> (2019.03 – 2022.02)</li>
    </ul>
  </div>
</section>
''' + FOOTER

html = head("연구분야", "Research",
            "AESE Lab research: waste-to-energy, pyrolysis, CO2 utilization, biorefinery, biochar, thermocatalysis, VOC oxidation, air pollution control.",
            "research") + body
write_page("../research.html", html)
