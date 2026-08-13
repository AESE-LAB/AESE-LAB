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

    // Tabs (e.g. Publications page)
    var tabBtns = document.querySelectorAll(".tab-btn[data-tab]");
    if (tabBtns.length) {
      function activateTab(id, updateHash) {
        var panel = document.getElementById("panel-" + id);
        if (!panel) return;
        tabBtns.forEach(function (b) {
          b.classList.toggle("active", b.getAttribute("data-tab") === id);
        });
        document.querySelectorAll(".tab-panel").forEach(function (p) {
          p.classList.toggle("active", p === panel);
        });
        if (updateHash && window.history && window.history.replaceState) {
          window.history.replaceState(null, "", "#" + id);
        }
      }
      tabBtns.forEach(function (btn) {
        btn.addEventListener("click", function () {
          activateTab(btn.getAttribute("data-tab"), true);
        });
      });
      var hash = window.location.hash.replace("#", "");
      if (hash) activateTab(hash, false);
      window.addEventListener("hashchange", function () {
        var h = window.location.hash.replace("#", "");
        if (h) activateTab(h, false);
      });
    }
  });
})();
