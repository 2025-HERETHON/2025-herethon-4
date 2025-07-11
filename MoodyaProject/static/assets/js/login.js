document.addEventListener("DOMContentLoaded", function () {
  const clickBoxes = document.querySelectorAll(".click-box");

  clickBoxes.forEach((box) => {
    box.addEventListener("click", () => {
      // 모든 박스 초기화
      clickBoxes.forEach((b) => {
        b.classList.remove("clicked");

        // const img = b.querySelector(".checkImage");
        // if (img) {
        //   img.src = "../assets/img/none-checkBtn.svg";
        // }
      });

      // 현재 박스 클릭 처리
      box.classList.add("clicked");

      // const checkImg = box.querySelector(".checkImage");
      // if (checkImg) {
      //   checkImg.src = "../assets/img/checkBtn.svg";
      // }
    });
  });
});
