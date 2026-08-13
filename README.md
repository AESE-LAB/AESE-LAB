# 대기 공학 및 지속가능 에너지 연구실 (AESE Lab) 홈페이지

제주대학교 환경공학과 이태우 교수 연구실 홈페이지입니다.
공식 주소: **https://aese-lab.github.io**

## 공식 파일 목록 (이 목록에 없는 파일은 저장소에서 삭제하세요)

```
├─ index.html          # 홈
├─ people.html         # 지도교수 (프로필·학력·경력·수상·활동)
├─ member.html         # 구성원 (학생·졸업생)  ※ members.html 아님!
├─ research.html       # 연구분야 + 연구과제
├─ publications.html   # 연구성과 (5개 탭: 논문요약/전체논문/북챕터/특허/학술발표)
├─ facilities.html     # 연구시설 (장비)
├─ news.html           # 소식
├─ join.html           # 모집 안내 + 연구실 위치(지도)
├─ 404.html            # 없는 주소 안내 페이지
├─ styles.css          # 전체 디자인
├─ script.js           # 언어 전환 + 연구성과 탭 기능
├─ robots.txt / sitemap.xml / site.webmanifest
├─ README.md           # 이 파일
└─ assets/             # 사진·로고·아이콘
```

`_build/` 폴더는 제작용 도구이므로 업로드하지 않아도 됩니다.

## 업로드 원칙 (중요)

1. **항상 최신 zip 하나에서 꺼낸 파일만 사용**하세요. 다운로드 폴더에 쌓인 예전 파일을 올리면 사이트가 과거 버전으로 되돌아갑니다.
2. 같은 이름의 파일을 올리면 자동으로 덮어쓰기됩니다. **미리 삭제할 필요가 없습니다.**
3. 파일 이름 뒤에 `(1)` 이 붙어 있으면 이름을 고친 뒤 올리거나, 그 파일을 버리고 zip에서 다시 꺼내세요.
4. 위 목록에 없는 파일(`members.html`, `index (1).html` 등)이 저장소에 보이면: 파일 클릭 → ⋯ → **Delete file** → Commit changes.

## 사진 교체 (남은 작업)

- 장비 사진: `assets/equip-placeholder.svg` 자리에 micro-GC / valve GC / BET 실물 사진
- 구성원 사진: `assets/member-placeholder.svg` 자리에 장지수 학생 사진
- 로고: 제주대 공식 UI 다운로드 페이지 자료로 `assets/logo.svg` 교체 가능
- 사진 파일을 Claude 대화창에 올리면 알맞은 자리에 넣은 수정본을 받을 수 있습니다.

## 내용 수정 방법

모든 글은 국문/영문 한 쌍으로 되어 있습니다. 두 곳 모두 수정해야 언어 전환이 올바르게 동작합니다.

```html
<span class="ko">국문 내용</span><span class="en">English content</span>
```

- 새 소식: news.html의 `news-item` 블록 복사
- 새 구성원: member.html의 `member-card` 블록 복사
- 새 논문: publications.html 전체논문 탭의 `pub-row` 블록 복사 (또는 Claude에게 목록 전달)
- GitHub 웹에서 파일 클릭 → 연필(✏) 아이콘으로 바로 수정 가능

## 검색엔진 등록 (배포 후 1회)

- Google Search Console (search.google.com/search-console): 사이트 등록 → sitemap.xml 제출
- 네이버 서치어드바이저 (searchadvisor.naver.com): 사이트 등록 → sitemap.xml 제출
