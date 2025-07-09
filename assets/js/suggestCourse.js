document.addEventListener("DOMContentLoaded", function () {
  // 1. 뒤로가기 버튼
  const backIcon = document.querySelector(".back-icon");
  backIcon.addEventListener("click", function () {
    window.location.href = "../index.html";
  });

  // 2. 모달 열기
  const recordBtns = document.querySelectorAll(".record-btn");
  const modal = document.querySelector(".modal");
  const modalTitle = document.querySelector(".modal-title");
  let currentCard = null;

  recordBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      currentCard = e.target.closest(".place-card");
      const title = currentCard.querySelector(".place-title h3").textContent;
      modalTitle.textContent = title;
      modal.style.display = "flex";
      modal.classList.remove("hidden");
    });
  });

  // 3. 진행 상황
  const progressCount = document.querySelector(".progress-count");
  const progressBar = document.querySelector(".progress-bar");
  const totalCards = document.querySelectorAll(".place-card").length;
  let completed = 0;

  // 4. 모달 내부 요소
  const submitBtn = document.querySelector(".submit-btn");
  const reviewText = document.querySelector("#review-text");
  const stars = document.querySelectorAll(".star");
  const dropdown = document.querySelector(".dropdown");
  const selected = document.querySelector(".dropdown-selected");
  const options = document.querySelector(".dropdown-options");
  const hiddenInput = document.querySelector("#feeling");

  let currentRating = 0;

  // 5. 별점 클릭 시
  stars.forEach((star, index) => {
    star.addEventListener("click", () => {
      currentRating = index + 1;
      updateStars(currentRating);
      checkConditions();
    });
  });

  function updateStars(rating) {
    stars.forEach((star, i) => {
      star.src =
        i < rating ? "../img/star-full.svg" : "../img/star-outline2.svg";
    });
  }

  // 6. 여정 후기 입력 시 조건 확인
  reviewText.addEventListener("input", checkConditions);

  // 7. 감정 선택 드롭다운 열고 닫기
  dropdown.addEventListener("click", () => {
    options.classList.toggle("show");
    options.classList.toggle("hidden");
  });

  // 8. 감정 선택 → 텍스트 교체 + 닫기 + 조건 확인
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

  // 9. 조건 충족 여부
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

  // 10. 제출 버튼 클릭 시
  submitBtn.addEventListener("click", () => {
    if (submitBtn.disabled || !currentCard) return;

    completed++;
    progressCount.textContent = `${completed}/${totalCards} 완료`;
    progressBar.style.width = `${(completed / totalCards) * 100}%`;

    // 현재 카드의 기록 버튼 상태 변경
    const recordButton = currentCard.querySelector(".record-btn");
    recordButton.classList.add("completed");
    recordButton.textContent = "기록 완료됨";

    modal.classList.add("hidden");
    modal.style.display = "none";

    // 초기화
    submitBtn.classList.remove("active");
    submitBtn.disabled = true;
    reviewText.value = "";
    currentRating = 0;
    updateStars(0);
    selected.textContent = "다녀온 후에 어떤 기분이셨나요?";
    hiddenInput.value = "";
  });

  // 11. 모달 닫기 버튼
  const closeBtn = document.querySelector(".close-btn");
  closeBtn.addEventListener("click", () => {
    modal.classList.add("hidden");
    modal.style.display = "none";
  });
});
