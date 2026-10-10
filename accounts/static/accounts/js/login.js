document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("loginForm");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    // ✅ Backend এ ডেটা পাঠাতে চাইলে fetch() ব্যবহার করো
    alert("✅ Login successful! Welcome back.");

    // Redirect to home page (index)
    window.location.href = "/";
  });
});
