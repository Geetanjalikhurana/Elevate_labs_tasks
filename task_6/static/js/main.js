document.addEventListener('DOMContentLoaded', () => {
    // 1. Navbar Mobile Toggle
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });
    }

    // 2. Client-side Realtime Form Validation for Contact Form
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        const nameInput = document.getElementById('name');
        const emailInput = document.getElementById('email');
        const subjectInput = document.getElementById('subject');
        const messageInput = document.getElementById('message');

        const validateEmail = (email) => {
            const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(String(email).toLowerCase());
        };

        const showError = (input, errorEl, message) => {
            input.classList.add('is-invalid');
            errorEl.textContent = message;
        };

        const clearError = (input, errorEl) => {
            input.classList.remove('is-invalid');
            errorEl.textContent = '';
        };

        contactForm.addEventListener('submit', (e) => {
            let isValid = true;

            // Name validation
            if (!nameInput.value.trim()) {
                showError(nameInput, document.getElementById('nameError'), 'Name is required.');
                isValid = false;
            } else {
                clearError(nameInput, document.getElementById('nameError'));
            }

            // Email validation
            if (!emailInput.value.trim()) {
                showError(emailInput, document.getElementById('emailError'), 'Email is required.');
                isValid = false;
            } else if (!validateEmail(emailInput.value.trim())) {
                showError(emailInput, document.getElementById('emailError'), 'Please enter a valid email address.');
                isValid = false;
            } else {
                clearError(emailInput, document.getElementById('emailError'));
            }

            // Subject validation
            if (!subjectInput.value.trim()) {
                showError(subjectInput, document.getElementById('subjectError'), 'Subject is required.');
                isValid = false;
            } else {
                clearError(subjectInput, document.getElementById('subjectError'));
            }

            // Message validation
            if (!messageInput.value.trim()) {
                showError(messageInput, document.getElementById('messageError'), 'Message is required.');
                isValid = false;
            } else if (messageInput.value.trim().length < 10) {
                showError(messageInput, document.getElementById('messageError'), 'Message must be at least 10 characters.');
                isValid = false;
            } else {
                clearError(messageInput, document.getElementById('messageError'));
            }

            if (!isValid) {
                e.preventDefault();
            }
        });
    }

    // 3. Auto-dismiss Flash Alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach((alert) => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transition = 'opacity 0.5s ease';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
});
