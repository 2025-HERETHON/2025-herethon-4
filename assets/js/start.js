document.addEventListener("DOMContentLoaded", function () {
  const startBtn = document.querySelector(".start-btn");
  const loginBtn = document.querySelector(".login-btn");

  startBtn.addEventListener("click", function () {
    window.location.href = "./pages/signUp.html";
  });

  loginBtn.addEventListener("click", function (e) {
    e.preventDefault();
    window.location.href = "./pages/login.html";
  });
});
