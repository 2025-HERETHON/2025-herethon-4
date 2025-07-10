document.addEventListener("DOMContentLoaded", function () {
  const newCourse = document.querySelector(".hello_bottom");
  const morebtn = document.querySelector(".more");

  newCourse.addEventListener("click", () => {
    window.location.href = "routeRecord.html";
  });

  morebtn.addEventListener("click", () => {
    window.location.href = "suggestCourse.html";
  });

  // 추천 장소 정보
  const suggestItems = document.querySelectorAll(".suggest_item");

  const newSuggestions = [
    {
      emoji: "🌳",
      name: "연남동 연트럴파크",
      tag: "자연힐링",
    },
    {
      emoji: "☕",
      name: "테일러 커피 연남점",
      tag: "카페 투어",
    },
  ];

  suggestItems.forEach((item, index) => {
    const emojiEl = item.querySelector(".emoji");
    const nameEl = item.querySelector(".course_name");
    const tagEl = item.querySelector(".purple_tag");

    if (emojiEl && nameEl && tagEl && newSuggestions[index]) {
      emojiEl.textContent = newSuggestions[index].emoji;
      nameEl.textContent = newSuggestions[index].name;
      tagEl.textContent = newSuggestions[index].tag;
    }
  });
});
