# 대기 공학 및 지속가능 에너지 연구실 (AESE Lab) 홈페이지

제주대학교 환경공학과 이태우 교수 연구실 홈페이지입니다.
순수 HTML/CSS/JS로 만들어져 서버 없이 GitHub Pages에 바로 배포할 수 있습니다.

## 파일 구조

```
├─ index.html          # 홈
├─ research.html       # 연구분야 + 연구과제
├─ people.html         # 구성원 (교수 프로필, 학생)
├─ publications.html   # 연구성과 (논문, 특허, 발표)
├─ facilities.html     # 연구시설 (장비, 위치)
├─ news.html           # 소식
├─ join.html           # 모집 안내
├─ 404.html
├─ styles.css          # 전체 스타일
├─ script.js           # 국문/영문 전환, 모바일 메뉴
├─ robots.txt / sitemap.xml / site.webmanifest
├─ assets/             # 로고, 아이콘, 플레이스홀더 이미지
└─ _build/             # (선택) 페이지 생성 스크립트 — 배포 시 없어도 됨
```

## 배포 방법 (GitHub Pages)

1. https://github.com 에서 연구실 계정을 만듭니다 (예: `aese-lab`).
2. `계정이름.github.io` 라는 이름으로 새 Repository를 만듭니다 (Public).
3. 이 폴더의 파일 전체를 Repository에 업로드합니다 (`_build` 폴더는 올리지 않아도 됩니다).
   - 웹에서: Repository → **Add file → Upload files** 로 드래그 앤 드롭
4. 몇 분 후 `https://계정이름.github.io` 에서 홈페이지가 열립니다.

## 배포 전 해야 할 일

- [ ] **사진 교체**
  - `assets/profile-placeholder.svg` → 교수님 사진 (`assets/profile.jpg` 등으로 저장 후 `people.html`에서 경로 수정)
  - `assets/lab-photo-placeholder.svg` → 연구실 사진
  - `assets/equip-placeholder.svg` → 장비 사진 (micro-GC, valve GC, BET)
  - `assets/member-placeholder.svg` → 구성원 사진
- [ ] **제주대학교 공식 로고**: 제주대 공식 UI 다운로드 페이지에서 받은 자료로 `assets/logo.svg` 교체 가능 (인터넷 이미지 검색 사용 금지)
- [ ] **도메인 주소 반영**: `sitemap.xml`, `robots.txt` 안의 `YOUR-ACCOUNT` 를 실제 계정 이름으로 변경

## 검색엔진 등록 (배포 후)

- Google Search Console: https://search.google.com/search-console — 사이트 등록 후 `sitemap.xml` 제출
- 네이버 서치어드바이저: https://searchadvisor.naver.com — 사이트 등록 후 `sitemap.xml` 제출

## 내용 수정 방법

각 HTML 파일을 직접 수정하면 됩니다. 국문/영문 병기는 다음 구조를 사용합니다.

```html
<span class="ko">국문 내용</span><span class="en">English content</span>
```

- 새 구성원 추가: `people.html`의 `member-card` 블록을 복사해 수정
- 새 논문 추가: `publications.html`의 `pub-item` 블록을 복사해 수정 (DOI 링크 포함)
- 새 소식 추가: `news.html`의 `news-item` 블록을 복사해 수정
  (카테고리: `paper`=논문/특허, `award`=수상, `conf`=학회/과제, `lab`=연구실)

`_build/` 폴더의 파이썬 스크립트로도 페이지를 다시 생성할 수 있습니다
(`cd _build && python3 build_home.py ...`). 직접 HTML을 수정하는 경우 스크립트는 무시해도 됩니다.
