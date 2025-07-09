document.addEventListener("DOMContentLoaded", function () {
  const logoutBtn = document.querySelector(".logout");

  logoutBtn.addEventListener("click", () => {
    window.location.href = "index.html";
  });
});
