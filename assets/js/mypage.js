document.addEventListener("DOMContentLoaded", function () {
  const logoutBtn = document.querySelector(".logout");

  logoutBtn.addEventListener("click", () => {
    window.location.href = "../index.html";
  });

  // URL 파라미터에서 감정 가져와 표시
  const params = new URLSearchParams(window.location.search);
  const emotion = params.get("emotion");
  const activity = params.get("activity");
  const region = params.get("region");

  if (emotion) {
    const emotionTag = document.querySelector(".setting_first .yellow_tag");
    if (emotionTag) {
      emotionTag.textContent = emotion;
    }
  }

  // 혼자 외출 레벨 반영
  if (activity) {
    // 두 번째 yellow_tag가 외출 레벨을 가리킴
    const activityTag = document.querySelector(".setting_second .yellow_tag");
    if (activityTag) {
      activityTag.textContent = activity;
    }
  }

  // 선호 지역 반영
  if (region) {
    const regionTag = document.querySelector(".setting_third .yellow_tag");
    if (regionTag) {
      regionTag.textContent = region;
    }
  }
});
