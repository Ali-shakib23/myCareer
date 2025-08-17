document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const fullNameInput = document.getElementById("full_name");
    const emailInput = document.getElementById("email");
    const cvInput = document.getElementById("cv_link");
    const coverLetterInput = document.getElementById("cover_letter");

    
    function createErrorElement(input) {
        const error = document.createElement("div");
        error.style.color = "red";
        error.style.fontSize = "0.9em";
        error.style.margin = "5px";
        input.parentNode.appendChild(error);
        return error;
    }

    const fullNameError = createErrorElement(fullNameInput);
    const emailError = createErrorElement(emailInput);
    const cvError = createErrorElement(cvInput);
    const coverLetterError = createErrorElement(coverLetterInput);

    form.addEventListener("submit", function(e) {
        let valid = true;

        // Raw and trimmed values
        const rawName = fullNameInput.value;
        const nameValue = rawName.trim();
        const rawEmail = emailInput.value;
        const emailValue = rawEmail.trim();
        const rawCv = cvInput.value;
        const cvValue = rawCv.trim();
        const rawCover = coverLetterInput.value;
        const coverValue = rawCover.trim();

        // Full name validation
        const nameWords = nameValue.split(/\s+/).filter(word => word.length > 0);
        if (/^\s/.test(rawName)) {
            fullNameError.textContent = "Full name cannot start with a space.";
            fullNameInput.style.borderColor = "red";
            valid = false;
        } else if (nameWords.length === 0) {
            fullNameError.textContent = "Full name cannot be empty.";
            fullNameInput.style.borderColor = "red";
            valid = false;
        } else if (!/^[A-Za-z\s]+$/.test(nameValue)) {
            fullNameError.textContent = "Full name must contain only letters and spaces.";
            fullNameInput.style.borderColor = "red";
            valid = false;
        } else if (nameWords.length !== 4) {
            fullNameError.textContent = "Full name must contain exactly four words.";
            fullNameInput.style.borderColor = "red";
            valid = false;
        } else {
            fullNameError.textContent = "";
            fullNameInput.style.borderColor = "";
        }

        // Email validation
        const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (/^\s/.test(rawEmail)) {
            emailError.textContent = "Email cannot start with a space.";
            emailInput.style.borderColor = "red";
            valid = false;
        } else if (emailValue === "") {
            emailError.textContent = "Email cannot be empty.";
            emailInput.style.borderColor = "red";
            valid = false;
        } else if (!emailPattern.test(emailValue)) {
            emailError.textContent = "Please enter a valid email address.";
            emailInput.style.borderColor = "red";
            valid = false;
        } else {
            emailError.textContent = "";
            emailInput.style.borderColor = "";
        }

        // CV link validation
        if (/^\s/.test(rawCv)) {
            cvError.textContent = "CV link cannot start with a space.";
            cvInput.style.borderColor = "red";
            valid = false;
        } else if (cvValue === "") {
            cvError.textContent = "CV link cannot be empty.";
            cvInput.style.borderColor = "red";
            valid = false;
        } else {
            cvError.textContent = "";
            cvInput.style.borderColor = "";
        }

        
        const coverWords = coverValue.split(/\s+/).filter(word => word.length > 0);
        const minWords = 20;
        const maxWords = 300;
        if (/^\s/.test(rawCover)) {
            coverLetterError.textContent = "Cover letter cannot start with a space.";
            coverLetterInput.style.borderColor = "red";
            valid = false;
        } else if (coverWords.length === 0) {
            coverLetterError.textContent = "Cover letter cannot be empty.";
            coverLetterInput.style.borderColor = "red";
            valid = false;
        } else if (coverWords.length < minWords) {
            coverLetterError.textContent = `Cover letter must have at least ${minWords} words.`;
            coverLetterInput.style.borderColor = "red";
            valid = false;
        } else if (coverWords.length > maxWords) {
            coverLetterError.textContent = `Cover letter cannot exceed ${maxWords} words.`;
            coverLetterInput.style.borderColor = "red";
            valid = false;
        } else {
            coverLetterError.textContent = "";
            coverLetterInput.style.borderColor = "";
        }

        if (!valid) e.preventDefault();
    });
});
