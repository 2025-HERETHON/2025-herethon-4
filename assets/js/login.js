document.addEventListener("DOMContentLoaded", function () {
  const clickBoxes = document.querySelectorAll(".click-box");

  clickBoxes.forEach((box) => {
    box.addEventListener("click", () => {
      clickBoxes.forEach((b) => {
        b.classList.remove("clicked");
        const img = b.querySelector(".checkImage");
        if (img) img.src = "../assets/images/none-checkBtn.svg";
      });
      box.classList.add("clicked");

      const checkImg = box.querySelector(".checkImage");
      if (checkImg) checkImg.src = "../assets/images/checkBtn.svg";
    });
  });
});
