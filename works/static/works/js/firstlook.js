(() => {
    const toggle = document.getElementById("add-firstlove-toggle");
    const panel = document.getElementById("add-firstlove");

    if (toggle && panel) {
        toggle.addEventListener("click", () => {
            const isOpening = panel.hidden;
            panel.hidden = !isOpening;
            toggle.setAttribute("aria-expanded", String(isOpening));

            if (isOpening) {
                panel.scrollIntoView({ behavior: "smooth", block: "start" });
                panel.querySelector("input, textarea, button")?.focus({ preventScroll: true });
            }
        });
    }

    const dialog = document.getElementById("story-dialog");
    const dialogTitle = document.getElementById("story-dialog-title");
    const dialogText = document.getElementById("story-dialog-text");
    const dialogImage = document.getElementById("story-dialog-image");
    const closeButton = dialog?.querySelector(".story-dialog-close");

    if (!dialog || !dialogTitle || !dialogText || !dialogImage || !closeButton) {
        return;
    }

    document.querySelectorAll(".story-card-trigger").forEach((card) => {
        card.addEventListener("click", () => {
            dialogTitle.textContent = card.dataset.storyTitle || "";
            dialogText.textContent = card.dataset.story || "";

            const image = card.querySelector("img");
            if (image) {
                dialogImage.src = image.src;
                dialogImage.alt = image.alt || card.dataset.storyTitle || "";
                dialogImage.hidden = false;
            } else {
                dialogImage.removeAttribute("src");
                dialogImage.alt = "";
                dialogImage.hidden = true;
            }

            dialog.showModal();
        });
    });

    closeButton.addEventListener("click", () => dialog.close());
    dialog.addEventListener("click", (event) => {
        if (event.target === dialog) {
            dialog.close();
        }
    });
})();
