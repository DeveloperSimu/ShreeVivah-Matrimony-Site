(() => {
  const storageKey = `profile-list-scroll:${window.location.pathname}`;

  if ("scrollRestoration" in window.history) {
    window.history.scrollRestoration = "manual";
  }

  window.addEventListener("pagehide", () => {
    window.sessionStorage.setItem(storageKey, String(window.scrollY));
  });

  window.addEventListener("pageshow", () => {
    const savedScrollPosition = window.sessionStorage.getItem(storageKey);
    if (savedScrollPosition === null) return;

    window.sessionStorage.removeItem(storageKey);
    window.requestAnimationFrame(() => {
      window.scrollTo(0, Number(savedScrollPosition));
    });
  });
})();
