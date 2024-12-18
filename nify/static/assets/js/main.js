// Initialize AOS (Animate On Scroll)
AOS.init({
    duration: 1000,
    once: true
});

// Navbar scroll effect
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('navbar-scrolled');
    } else {
        navbar.classList.remove('navbar-scrolled');
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});


// about page Animation

// Stats Counter Animation
function animateStats() {
    const stats = document.querySelectorAll('.stat-number');
    stats.forEach(stat => {
        const target = parseInt(stat.getAttribute('data-count'));
        const duration = 2000; // 2 seconds
        const increment = target / (duration / 16); // 60fps
        let current = 0;

        const updateCount = () => {
            current += increment;
            stat.textContent = Math.round(current);
            
            if (current < target) {
                requestAnimationFrame(updateCount);
            } else {
                stat.textContent = target;
            }
        };

        updateCount();
    });
}

// Run stats animation when section is in view
const statsSection = document.querySelector('.stats-section');
if (statsSection) {
    const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            animateStats();
            observer.unobserve(statsSection);
        }
    });
    observer.observe(statsSection);
} 

// Contact Form Handling
document.getElementById('contactForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const subject = document.getElementById('subject').value;
    const message = document.getElementById('message').value;

    // Here you would typically send this data to your server
    console.log('Form submitted:', { name, email, subject, message });

    // Show success message (you can customize this)
    alert('Thank you for your message! We will get back to you soon.');
    
    // Reset form
    this.reset();
});

// Password Toggle
document.querySelectorAll('.toggle-password').forEach(icon => {
    icon.addEventListener('click', function() {
        const input = this.previousElementSibling;
        if (input.type === 'password') {
            input.type = 'text';
            this.classList.remove('fa-eye');
            this.classList.add('fa-eye-slash');
        } else {
            input.type = 'password';
            this.classList.remove('fa-eye-slash');
            this.classList.add('fa-eye');
        }
    });
});

// Form Handling
document.getElementById('loginForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    // Add your login logic here
    console.log('Login submitted');
});

document.getElementById('signupForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    // Add your signup logic here
    console.log('Signup submitted');
});

// Show More Projects Functionality
document.addEventListener('DOMContentLoaded', function() {
    const showMoreBtn = document.getElementById('showMoreBtn');
    const hiddenProjects = document.querySelectorAll('.hidden-project');
    let isExpanded = false;

    if (showMoreBtn) {
        showMoreBtn.addEventListener('click', function() {
            isExpanded = !isExpanded;
            
            hiddenProjects.forEach(project => {
                project.style.display = isExpanded ? 'block' : 'none';
            });

            // Update button text and icon
            this.querySelector('span').textContent = isExpanded ? 'Show Less' : 'Show More Projects';
            this.classList.toggle('active');

            // Animate scroll to new content if expanding
            if (isExpanded) {
                hiddenProjects[0].scrollIntoView({ behavior: 'smooth' });
            }
        });
    }
});

// Function to check login status
function checkLoginStatus() {
    // This is a mock function - replace with actual authentication check
    const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
    
    const guestView = document.querySelector('.guest-view');
    const userView = document.querySelector('.user-view');
    
    if (isLoggedIn) {
        guestView.style.display = 'none';
        userView.style.display = 'block';
    } else {
        guestView.style.display = 'block';
        userView.style.display = 'none';
    }
}

// Handle logout
function handleLogout() {
    // Clear authentication data
    localStorage.removeItem('isLoggedIn');
    
    // Redirect to home page
    window.location.href = 'index.html';
}

// Check login status when page loads
document.addEventListener('DOMContentLoaded', checkLoginStatus);

// Social Login Handling
function handleGitHubLogin() {
    // Implement GitHub OAuth login
    console.log('GitHub login clicked');
}

function handleGoogleLogin() {
    // Implement Google OAuth login
    console.log('Google login clicked');
}

// Add event listeners to social buttons
document.querySelectorAll('.github-btn').forEach(btn => {
    btn.addEventListener('click', handleGitHubLogin);
});

document.querySelectorAll('.google-btn').forEach(btn => {
    btn.addEventListener('click', handleGoogleLogin);
});



// for serch bar



