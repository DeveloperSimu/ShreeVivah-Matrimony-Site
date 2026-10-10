document.addEventListener("DOMContentLoaded", () => {
  const dialog = document.querySelector(".story-dialog");
  const dialogPhoto = document.querySelector(".story-dialog-photo");
  const dialogTitle = document.querySelector("#story-dialog-title");
  const dialogDate = document.querySelector(".story-dialog-date");
  const dialogDateValue = dialogDate?.querySelector("span");
  const dialogMessage = document.querySelector(".story-dialog-message");
  const closeButton = document.querySelector(".story-dialog-close");

  if (
    !(dialog instanceof HTMLDialogElement) ||
    !(dialogPhoto instanceof HTMLImageElement) ||
    !(dialogTitle instanceof HTMLHeadingElement) ||
    !(dialogDate instanceof HTMLParagraphElement) ||
    !(dialogDateValue instanceof HTMLSpanElement) ||
    !(dialogMessage instanceof HTMLParagraphElement) ||
    !(closeButton instanceof HTMLButtonElement)
  ) {
    return;
  }

  let activeStory = null;
  let previousScrollPosition = { left: 0, top: 0 };

  const restoreScrollPosition = () => {
    window.requestAnimationFrame(() => {
      window.scrollTo(previousScrollPosition.left, previousScrollPosition.top);
    });
  };

  const placeDialogNearCard = (card) => {
    const bounds = card.getBoundingClientRect();
    const margin = 16;
    const maxTop = Math.max(margin, window.innerHeight - dialog.offsetHeight - margin);
    const top = Math.min(Math.max(bounds.top, margin), maxTop);
    const maxLeft = Math.max(margin, window.innerWidth - dialog.offsetWidth - margin);
    const left = Math.min(
      Math.max(bounds.left + bounds.width / 2 - dialog.offsetWidth / 2, margin),
      maxLeft,
    );

    dialog.style.setProperty("--story-dialog-top", `${top}px`);
    dialog.style.setProperty("--story-dialog-left", `${left}px`);
  };

  const openStory = (card) => {
    const photo = card.querySelector("img");
    const title = card.querySelector("h3");
    const date = card.querySelector(".date");
    const message = card.querySelector(".msg");

    if (
      !(photo instanceof HTMLImageElement) ||
      !(title instanceof HTMLHeadingElement) ||
      !(date instanceof HTMLParagraphElement) ||
      !(message instanceof HTMLParagraphElement)
    ) {
      return;
    }

    activeStory = card;
    previousScrollPosition = { left: window.scrollX, top: window.scrollY };
    dialogPhoto.src = photo.src;
    dialogPhoto.alt = photo.alt;
    dialogTitle.textContent = title.textContent.trim();
    dialogDateValue.textContent = date.textContent.replace(/^Marriage Date\s*=\s*/i, "").trim();
    dialogMessage.textContent = message.textContent.trim();
    dialog.showModal();
    placeDialogNearCard(card);
    closeButton.focus({ preventScroll: true });
    restoreScrollPosition();
  };

  document.querySelectorAll(".story-card").forEach((card) => {
    card.addEventListener("click", () => openStory(card));
    card.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        openStory(card);
      }
    });
  });

  window.addEventListener("resize", () => {
    if (dialog.open && activeStory) {
      placeDialogNearCard(activeStory);
    }
  });

  window.addEventListener("scroll", () => {
    if (dialog.open && activeStory) {
      placeDialogNearCard(activeStory);
    }
  });

  closeButton.addEventListener("click", () => dialog.close());
  dialog.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      event.preventDefault();
      dialog.close();
    }
  });
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) {
      dialog.close();
    }
  });
  dialog.addEventListener("close", () => {
    activeStory?.focus({ preventScroll: true });
    restoreScrollPosition();
  });
});