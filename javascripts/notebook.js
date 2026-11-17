// Notebook pages: a button that hides the code and keeps the markdown, plots and tables.
// The choice is remembered per browser. document$ is Material's page-load stream.
document$.subscribe(function () {
  var btn = document.querySelector(".notebook-actions .toggle-code");
  if (!btn) return;
  var label = btn.querySelector("span");
  function set(hide) {
    document.body.classList.toggle("hide-code", hide);
    label.textContent = hide ? "Show code" : "Hide code";
    try { localStorage.setItem("notebook-hide-code", hide ? "1" : "0"); } catch (e) {}
  }
  var hide = false;
  try { hide = localStorage.getItem("notebook-hide-code") === "1"; } catch (e) {}
  set(hide);
  btn.addEventListener("click", function () {
    set(!document.body.classList.contains("hide-code"));
  });
});
