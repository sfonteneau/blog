(function(){
  const STORAGE_KEY = "theme";
  const root = document.documentElement;

  function apply(theme){
    if(theme === "light" || theme === "dark"){
      root.setAttribute("data-theme", theme);
    } else {
      root.removeAttribute("data-theme");
    }
  }

  // Initial: saved preference, else system preference
  const saved = localStorage.getItem(STORAGE_KEY);
  if(saved){
    apply(saved);
  } else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches){
    apply("light");
  } else {
    apply("dark");
  }

  function toggle(){
    const current = root.getAttribute("data-theme") || "dark";
    const next = current === "dark" ? "light" : "dark";
    apply(next);
    localStorage.setItem(STORAGE_KEY, next);
  }

  document.addEventListener("click", function(e){
    const btn = e.target.closest && e.target.closest(".theme-toggle");
    if(btn) toggle();
  });
})();
