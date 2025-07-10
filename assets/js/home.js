document.addEventListener("DOMContentLoaded", function () {
  const newCourse = document.querySelector(".hello_bottom");
  const morebtn = document.querySelector(".more");

  newCourse.addEventListener("click", () => {
    window.location.href = "routeRecord.html";
  });

  morebtn.addEventListener("click", () => {
    window.location.href = "suggestCourse.html";
  });
});
