// signup.js
function togglePassword() {
  const passwordField = document.getElementById("password");
  if (passwordField.type === "password") {
    passwordField.type = "text";
  } else {
    passwordField.type = "password";
  }
}

function continueWithEmail() {
    // এখানে তুমি চাইলে অন্য URL redirect করতে পারো
    window.location.href = "{% url 'signup' %}"; // অথবা তোমার desired page
}
