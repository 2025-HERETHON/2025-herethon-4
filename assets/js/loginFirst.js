const clickBoxs = document.querySelectorAll(".click-box");

clickBoxs.forEach((box) => {
  box.addEventListener("click", () => {
    clickBoxs.forEach((b) => b.classList.remove("clicked"));
    box.classList.add("clicked");
  });
});
