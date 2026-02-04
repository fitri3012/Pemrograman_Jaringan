// JavaScript for interactivity

// Mobile Navigation Toggle
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
const navLinks = document.querySelectorAll('.nav-link');

navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    
    // Toggle icon (optional, can swap bars with times)
    const icon = navToggle.querySelector('i');
    if (navMenu.classList.contains('active')) {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-times');
    } else {
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
    }
});

// Close menu when clicking a link
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        const icon = navToggle.querySelector('i');
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
    });
});

// Scroll Reveal Effect (Simple Intersection Observer)
const sections = document.querySelectorAll('.section');

const revealSection = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    }); // removed unobserve to keep revealing if scrolling back and forth? or maybe once.
    // Let's keep it simple for now, CSS opacity transition is needed.
};

const sectionObserver = new IntersectionObserver(revealSection, {
    root: null,
    threshold: 0.15,
});

sections.forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'all 0.6s ease-out';
    
    // Add class for styling when visible
    sectionObserver.observe(section);
});

// Modify observer callback to use a class
const revealSectionWithClass = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
};

// Re-init with correct callback logic
const finalObserver = new IntersectionObserver(revealSectionWithClass, {
    root: null,
    threshold: 0.15,
});

sections.forEach(section => {
    finalObserver.observe(section);
});

// Navbar background change on scroll
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(5, 5, 8, 0.95)';
        navbar.style.boxShadow = '0 5px 20px rgba(0,0,0,0.5)';
    } else {
        navbar.style.background = 'rgba(10, 10, 18, 0.9)';
        navbar.style.boxShadow = 'none';
    }
});
