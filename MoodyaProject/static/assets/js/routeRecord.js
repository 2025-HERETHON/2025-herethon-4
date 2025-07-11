document.addEventListener("DOMContentLoaded", () => {
  const textarea = document.getElementById("dayreview-text");
  const submitBtn = document.querySelector(".dayreview-btn");

  textarea.addEventListener("input", () => {
    const hasText = textarea.value.trim().length > 0;

    if (hasText) {
      submitBtn.style.backgroundColor = "#9334e9";
    } else {
      submitBtn.style.backgroundColor = "#d9b4fc";
    }
  });
});
