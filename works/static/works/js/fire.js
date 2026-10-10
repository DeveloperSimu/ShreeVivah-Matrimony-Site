(() => {
    const dialog = document.querySelector(".fire-dialog");

    if (!dialog) {
        return;
    }

    const title = dialog.querySelector("#fire-dialog-title");
    const description = dialog.querySelector(".fire-dialog-copy");
    const closeButton = dialog.querySelector(".fire-dialog-close");

    document.querySelectorAll(".read-more").forEach((button) => {
        button.addEventListener("click", () => {
            title.textContent = button.dataset.title || "";
            description.textContent = button.dataset.description || "";
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
