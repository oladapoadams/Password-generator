function generatePassword() {
    fetch("/generate-password")
    .then(response => response.json())
    .then(data => {
        document.getElementById("password").value = data.password;
    })
    .catch(error => console.error("Error:", error));
}

function copyPassword() {
    let passwordField = document.getElementById("password");
    passwordField.select();
    document.execCommand("copy");
    alert("Password copied to clipboard! ✅");
}
