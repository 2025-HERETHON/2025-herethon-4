document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("reviewModal");
  const submitBtn = document.getElementById("submitBtn");
  const reviewText = document.getElementById("review-text");
  const ratingInput = document.getElementById("rating");
  const stars = document.querySelectorAll(".star");
  const dropdown = document.querySelector(".dropdown");
  const selected = document.querySelector(".dropdown-selected");
  const options = document.querySelector(".dropdown-options");
  const hiddenInput = document.getElementById("feeling");

  let currentRating = 0;

  // ⭐️ 별점 클릭
  stars.forEach((star, index) => {
    star.addEventListener("click", () => {
      currentRating = index + 1;
      ratingInput.value = currentRating;

      stars.forEach((s, i) => {
        s.src =
          i <= index
            ? "/static/assets/img/star-full.svg"
            : "/static/assets/img/star-outline2.svg";
      });

      checkConditions();
    });
  });

  // 여정 후기 입력 시
  reviewText.addEventListener("input", checkConditions);

  // 감정 선택 드롭다운 열기/닫기
  dropdown.addEventListener("click", (e) => {
    e.stopPropagation();
    options.classList.toggle("show");
    options.classList.toggle("hidden");
  });

  // 감정 선택 시 텍스트 반영 및 클래스 적용
  options.querySelectorAll("li").forEach((item) => {
    item.addEventListener("click", (e) => {
      e.stopPropagation();
      selected.textContent = item.textContent;
      hiddenInput.value = item.dataset.value;

      options
        .querySelectorAll("li")
        .forEach((li) => li.classList.remove("selected"));
      item.classList.add("selected");

      options.classList.remove("show");
      options.classList.add("hidden");

      checkConditions();
    });
  });

  // 드롭다운 외부 클릭 시 닫기
  document.addEventListener("click", (e) => {
    if (!dropdown.contains(e.target)) {
      options.classList.remove("show");
      options.classList.add("hidden");
    }
  });

  // 조건 체크 함수 (세 항목 모두 입력 시 버튼 활성화)
  function checkConditions() {
    const hasText = reviewText.value.trim().length > 0;
    const hasStar = currentRating > 0;
    const hasFeeling = hiddenInput.value !== "";

    if (hasText && hasStar && hasFeeling) {
      submitBtn.classList.add("active");
      submitBtn.disabled = false;
    } else {
      submitBtn.classList.remove("active");
      submitBtn.disabled = true;
    }
  }

  // 모달 닫기 버튼
  const closeBtn = document.querySelector(".close-btn");
  closeBtn.addEventListener("click", () => {
    modal.classList.add("hidden");
  });
});
