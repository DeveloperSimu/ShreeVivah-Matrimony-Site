(() => {
    const filterButtons = document.querySelectorAll(".filter-btn");
    const designCards = document.querySelectorAll(".design-card");
    const designCount = document.querySelector(".design-count");

    const updateDesigns = (filter) => {
        let visibleCount = 0;

        designCards.forEach((card) => {
            const isVisible = filter === "all" || card.dataset.category === filter;
            card.hidden = !isVisible;
            if (isVisible) {
                visibleCount += 1;
            }
        });

        if (designCount) {
            designCount.textContent = `${visibleCount} ${visibleCount === 1 ? "design" : "designs"}`;
        }
    };

    filterButtons.forEach((button) => {
        button.addEventListener("click", () => {
            filterButtons.forEach((filterButton) => {
                const isActive = filterButton === button;
                filterButton.classList.toggle("active", isActive);
                filterButton.setAttribute("aria-pressed", String(isActive));
            });

            updateDesigns(button.dataset.filter || "all");
        });
    });

    const lightbox = document.querySelector(".mehendi-lightbox");

    if (lightbox) {
        const lightboxImage = lightbox.querySelector(".lightbox-image");
        const lightboxCaption = lightbox.querySelector(".lightbox-caption");
        const closeButton = lightbox.querySelector(".lightbox-close");

        document.querySelectorAll(".design-image-trigger").forEach((trigger) => {
            trigger.addEventListener("click", () => {
                const image = trigger.querySelector("img");
                lightboxImage.src = image.currentSrc || image.src;
                lightboxImage.alt = image.alt;
                lightboxCaption.textContent = image.alt;
                lightbox.showModal();
            });
        });

        closeButton.addEventListener("click", () => lightbox.close());
        lightbox.addEventListener("click", (event) => {
            if (event.target === lightbox) {
                lightbox.close();
            }
        });
    }

    const toggle = document.getElementById("add-design-toggle");
    const formPanel = document.getElementById("add-design");

    if (toggle && formPanel) {
        toggle.addEventListener("click", () => {
            const isOpening = formPanel.hidden;
            formPanel.hidden = !isOpening;
            toggle.setAttribute("aria-expanded", String(isOpening));

            if (isOpening) {
                formPanel.scrollIntoView({ behavior: "smooth", block: "start" });
                formPanel.querySelector("input, select, textarea, button")?.focus({
                    preventScroll: true,
                });
            }
        });
    }
})();
