 const REVEAL_SELECTOR = "[data-reveal]";
    const obs = new IntersectionObserver((entries)=>{
      entries.forEach(e=>{
        if(e.isIntersecting){ e.target.classList.add("show"); obs.unobserve(e.target); }
      })
    }, {threshold:.12});
    document.querySelectorAll(REVEAL_SELECTOR).forEach(el=>obs.observe(el));