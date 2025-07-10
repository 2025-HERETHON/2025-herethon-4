document.addEventListener("DOMContentLoaded", function () {
  const logoutBtn = document.querySelector(".logout");

  logoutBtn.addEventListener("click", () => {
    window.location.href = "../index.html";
  });

  const emotion = localStorage.getItem("emotion");
  const activity = localStorage.getItem("activity");
  const region = localStorage.getItem("region");

  if (emotion) {
    const tag = document.querySelector(".setting_first .yellow_tag");
    if (tag) tag.textContent = emotion;
  }

  if (activity) {
    const tag = document.querySelector(".setting_second .yellow_tag");
    if (tag) tag.textContent = activity;
  }

  if (region) {
    const tag = document.querySelector(".setting_third .yellow_tag");
    if (tag) tag.textContent = region;
  }
});
