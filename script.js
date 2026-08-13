/* AESE Lab website — language toggle & mobile nav */
(function () {
  var KEY = "aese-lang";

  function getLang() {
    try {
      return localStorage.getItem(KEY) || "ko";
    } catch (e) {
      return "ko";
    }
  }

  function setLang(lang) {
    document.documentElement.setAttribute("data-lang", lang);
    document.documentElement.setAttribute("lang", lang === "ko" ? "ko" : "en");
    try {
      localStorage.setItem(KEY, lang);
    } catch (e) {}
    var btn = document.getElementById("langToggle");
    if (btn) btn.textContent = lang === "ko" ? "ENG" : "한국어";
  }

  // Apply saved language as early as possible
  setLang(getLang());

  document.addEventListener("DOMContentLoaded", function () {
    setLang(getLang());

    var btn = document.getElementById("langToggle");
    if (btn) {
      btn.addEventListener("click", function () {
        setLang(getLang() === "ko" ? "en" : "ko");
      });
    }

    var menuBtn = document.getElementById("menuBtn");
    var nav = document.getElementById("mainNav");
    if (menuBtn && nav) {
      menuBtn.addEventListener("click", function () {
        nav.classList.toggle("open");
      });
      nav.addEventListener("click", function (e) {
        if (e.target.tagName === "A") nav.classList.remove("open");
      });
    }
  });
})();
