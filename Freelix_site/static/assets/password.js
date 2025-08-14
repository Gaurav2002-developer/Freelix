document.addEventListener("DOMContentLoaded", function () {
  const toggleButtons = document.querySelectorAll(".toggle-password");

  toggleButtons.forEach((btn) => {
    btn.addEventListener("click", function () {
      const targetId = this.getAttribute("data-target");
      const input = document.getElementById(targetId);

      if (input.type === "password") {
        input.type = "text";
        this.textContent = "👁"; // eye open
      } else {
        input.type = "password";
        this.textContent = "🚫"; // eye close (or any close eye emoji)
      }
    });
  });

  // Password match validation
  const form = document.querySelector(".login-form");
  form.addEventListener("submit", function (e) {
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;

    if (password !== confirmPassword) {
      e.preventDefault();
      alert("Passwords do not match!");
    }
  });
});
