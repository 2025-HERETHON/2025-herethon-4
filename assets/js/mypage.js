document.addEventListener("DOMContentLoaded", function () {
  // 로그아웃
  const logoutBtn = document.querySelector(".logout");

  logoutBtn.addEventListener("click", () => {
    window.location.href = "../index.html";
  });

  // 내 설정 값 변경
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

  // ✅ 저장된 장소 더미 데이터 (DB 대체용)
  const savedPlacesFromDB = [
    {
      name: "연남동 연트럴파크",
      visitedDate: "7/7",
    },
    {
      name: "북촌 한옥마을",
      visitedDate: "7/5",
    },
  ];

  const noPlaceEl = document.querySelector(".no_place");
  const yesPlacesEl = document.querySelector(".yes_places");

  if (savedPlacesFromDB.length > 0) {
    // 숨김 처리
    noPlaceEl.style.display = "none";
    yesPlacesEl.style.display = "block";

    // 기존 내용 초기화
    yesPlacesEl.innerHTML = "";

    // 장소 목록 렌더링
    savedPlacesFromDB.forEach((place) => {
      const div = document.createElement("div");
      div.className = "place_info";
      div.innerHTML = `
        <div class="place_name">${place.name}</div>
        <div class="visited"><span>${place.visitedDate}</span> 방문 코스</div>
      `;
      yesPlacesEl.appendChild(div);
    });
  } else {
    // 저장된 장소 없을 경우
    noPlaceEl.style.display = "block";
    yesPlacesEl.style.display = "none";
  }
});
