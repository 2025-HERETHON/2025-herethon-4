document.addEventListener("DOMContentLoaded", function () {
  const clickBoxes = document.querySelectorAll(".click-box");

  clickBoxes.forEach((box) => {
    box.addEventListener("click", () => {
      // 모든 박스 초기화
      clickBoxes.forEach((b) => {
        b.classList.remove("clicked");

        const img = b.querySelector(".checkImage");
        if (img) {
          img.src = "../assets/images/none-checkBtn.svg";
        }
      });

      // 현재 박스 클릭 처리
      box.classList.add("clicked");

      const checkImg = box.querySelector(".checkImage");
      if (checkImg) {
        checkImg.src = "../assets/images/checkBtn.svg";
      }
    });
  });

  // 감정 설정 (mypageFirst.html)
  if (window.location.pathname.includes("mypageFirst")) {
    const form = document.getElementById("settingForm");
    form?.addEventListener("submit", function (e) {
      e.preventDefault();
      const selected = document.querySelector('input[name="emotion"]:checked');
      if (!selected) {
        alert("감정을 선택해주세요!");
        return;
      }
      const value = selected.value;
      window.location.href = `mypage.html?emotion=${encodeURIComponent(value)}`;
    });
  }

  // 활동 역량 설정 (mypageSecond.html)
  if (window.location.pathname.includes("mypageSecond")) {
    const form = document.getElementById("settingForm");
    form?.addEventListener("submit", function (e) {
      e.preventDefault();
      const selected = document.querySelector('input[name="activity"]:checked');
      if (!selected) {
        alert("외출 레벨을 선택해주세요!");
        return;
      }
      const value = selected.value;
      window.location.href = `mypage.html?activity=${encodeURIComponent(value)}`;
    });
  }

  // 선호 지역 설정 (mypageThird.html)
  if (window.location.pathname.includes("mypageThird")) {
    const form = document.getElementById("settingForm");
    form?.addEventListener("submit", function (e) {
      e.preventDefault();
      const selected = document.querySelector('input[name="region"]:checked');
      if (!selected) {
        alert("지역을 선택해주세요!");
        return;
      }
      const value = selected.value;
      window.location.href = `mypage.html?region=${encodeURIComponent(value)}`;
    });
  }
});
