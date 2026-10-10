(() => {
  const lightbox = document.querySelector(".memory-lightbox");

  if (!lightbox) {
    return;
  }

  const imageView = lightbox.querySelector(".lightbox-image");
  const caption = lightbox.querySelector(".lightbox-caption");
  const closeButton = lightbox.querySelector(".lightbox-close");

  document.querySelectorAll(".memory-photo").forEach((button) => {
    button.addEventListener("click", () => {
      const image = button.querySelector("img");
      imageView.src = image.currentSrc || image.src;
      imageView.alt = image.alt;
      caption.textContent = image.alt;
      lightbox.showModal();
    });
  });

  closeButton.addEventListener("click", () => lightbox.close());
  lightbox.addEventListener("click", (event) => {
    if (event.target === lightbox) {
      lightbox.close();
    }
  });
})();
