themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    themeToggle.setAttribute('aria-label', `Switch to ${newTheme === 'light' ? 'dark' : 'light'} mode`);
});



// otp veerification



const inputs = document.querySelectorAll('.otp-input');

// OTP Input Navigation
inputs.forEach((input, index) => {
    input.addEventListener('input', function () {
        this.value = this.value.replace(/[^0-9]/g, ''); // Only allow numbers
        if (this.value.length === 1) {
            if (index < inputs.length - 1) {
                inputs[index + 1].focus();
            }
        }
    });

    input.addEventListener('keydown', function (e) {
        if (e.key === 'Backspace' && !this.value) {
            if (index > 0) {
                inputs[index - 1].focus();
            }
        }
    });

    input.addEventListener('paste', function (e) {
        const pasteData = e.clipboardData.getData('text').slice(0, inputs.length);
        pasteData.split('').forEach((char, idx) => {
            if (inputs[idx]) inputs[idx].value = char;
        });
        const nextInputIndex = pasteData.length < inputs.length ? pasteData.length : inputs.length - 1;
        inputs[nextInputIndex].focus();
        e.preventDefault();
    });
});

// Timer Functionality
function startTimer(duration, display, resendButton) {
    let timer = duration;
    let minutes, seconds;
    let countdown = setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            clearInterval(countdown);
            resendButton.disabled = false;
            display.textContent = "00:00";
        }
    }, 1000);
}

window.onload = function () {
    const fiveMinutes = 60 * 5;
    const display = document.querySelector('#timer');
    const resendButton = document.querySelector('#resendButton');
    startTimer(fiveMinutes, display, resendButton);

    // Handle Resend Button Click
    resendButton.addEventListener('click', function () {
        this.disabled = true;
        inputs.forEach(input => input.value = ''); // Clear inputs
        inputs[0].focus(); // Focus on the first input
        startTimer(fiveMinutes, display, this); // Restart timer
    });
};




// admin upload 



document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', function() {
        document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));
        this.classList.add('active');
    });
});

// Handle file uploads
document.querySelectorAll('.upload-area').forEach(area => {
    area.addEventListener('click', function() {
        this.querySelector('input[type="file"]').click();
    });

    area.addEventListener('dragover', function(e) {
        e.preventDefault();
        this.style.borderColor = '#4a90e2';
    });

    area.addEventListener('dragleave', function(e) {
        e.preventDefault();
        this.style.borderColor = '#ddd';
    });

    area.addEventListener('drop', function(e) {
        e.preventDefault();
        this.style.borderColor = '#ddd';
        const files = e.dataTransfer.files;
        console.log('Files dropped:', files);
        // Handle file upload logic here
    });
});