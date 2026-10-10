document.querySelectorAll(".site-nav-toggle").forEach((toggle) => {
  const navigation = document.getElementById(toggle.getAttribute("aria-controls"));

  if (!navigation) {
    return;
  }

  toggle.addEventListener("click", () => {
    const isExpanded = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", String(!isExpanded));
    navigation.classList.toggle("is-open", !isExpanded);
  });
});
