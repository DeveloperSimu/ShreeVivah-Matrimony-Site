function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

 (function(){
    const cards = document.querySelectorAll('.wc-card');

    if (!("IntersectionObserver" in window)) {
        cards.forEach((card) => card.classList.add("revealed"));
        return;
    }

    const io = new IntersectionObserver((entries)=>{
        entries.forEach(e=>{
            if(e.isIntersecting) {
                e.target.classList.add('revealed');
                io.unobserve(e.target);
            }
        });
    }, {threshold: 0.15});
    cards.forEach(c => io.observe(c));
})();

// WhatsApp Button click action
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("whatsapp-btn");

  btn?.addEventListener("click", () => {
    console.log("WhatsApp button clicked ✅");
  });

  const searchForm = document.querySelector(".search-bar");
  const searchInput = searchForm?.querySelector('input[name="q"]');
  const suggestions = document.getElementById("profile-search-suggestions");
  if (!searchForm || !searchInput || !suggestions) return;

  let activeRequest;
  let debounceTimer;

  const closeSuggestions = () => {
    suggestions.hidden = true;
    suggestions.replaceChildren();
    searchInput.setAttribute("aria-expanded", "false");
  };

  const showMessage = (message) => {
    const item = document.createElement("div");
    item.className = "search-suggestion-message";
    item.setAttribute("role", "status");
    item.textContent = message;
    suggestions.replaceChildren(item);
    suggestions.hidden = false;
    searchInput.setAttribute("aria-expanded", "true");
  };

  searchInput.addEventListener("input", () => {
    const query = searchInput.value.trim();
    window.clearTimeout(debounceTimer);
    activeRequest?.abort();

    if (!query) {
      closeSuggestions();
      return;
    }

    debounceTimer = window.setTimeout(async () => {
      activeRequest = new AbortController();
      try {
        const url = new URL(searchForm.dataset.suggestionsUrl, window.location.origin);
        url.searchParams.set("q", query);
        const response = await fetch(url, { signal: activeRequest.signal });
        if (!response.ok) throw new Error(`Profile search failed: ${response.status}`);

        const data = await response.json();
        if (!Array.isArray(data.profiles)) throw new Error("Invalid profile search response");
        if (searchInput.value.trim() !== query) return;

        if (!data.profiles.length) {
          showMessage("No matching profiles found.");
          return;
        }

        const list = document.createElement("ul");
        list.className = "search-suggestion-list";
        list.setAttribute("role", "presentation");
        data.profiles.forEach((profile) => {
          const item = document.createElement("li");
          const link = document.createElement("a");
          link.href = profile.url;
          link.setAttribute("role", "option");
          link.textContent = `${profile.name} — ${profile.gender === "bride" ? "Bride" : "Groom"}${profile.location ? ` · ${profile.location}` : ""}`;
          item.append(link);
          list.append(item);
        });
        suggestions.replaceChildren(list);
        suggestions.hidden = false;
        searchInput.setAttribute("aria-expanded", "true");
      } catch (error) {
        if (error.name === "AbortError") return;
        showMessage("Unable to load profiles. Please try again.");
        console.error(error);
      }
    }, 150);
  });

  searchInput.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeSuggestions();
  });

  document.addEventListener("click", (event) => {
    if (!searchForm.contains(event.target)) closeSuggestions();
  });
});
