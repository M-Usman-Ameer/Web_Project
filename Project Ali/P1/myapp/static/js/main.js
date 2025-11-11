/* =========================
   PROCEDURE SLIDER
========================= */
const steps = document.querySelectorAll('.step-box');
const prevBtn = document.getElementById('prev-procedure');
const nextBtn = document.getElementById('next-procedure');
let currentStep = 0;

function showStep(index) {
    steps.forEach((step) => step.classList.remove('active'));
    steps[index].classList.add('active');
}

// Initial display
showStep(currentStep);

// Next button
nextBtn.addEventListener('click', () => {
    currentStep = (currentStep + 1) % steps.length; // loop to 1 after 7
    showStep(currentStep);
});

// Prev button
prevBtn.addEventListener('click', () => {
    currentStep = (currentStep - 1 + steps.length) % steps.length; // loop to 7 from 1
    showStep(currentStep);
});

// Auto-slide every 6 seconds
setInterval(() => {
    currentStep = (currentStep + 1) % steps.length;
    showStep(currentStep);
}, 6000);

/* =========================
   TESTIMONIALS SLIDER
========================= */
const testimonials = document.querySelectorAll('.testimonial');
const prevTestimonialBtn = document.getElementById('prev');
const nextTestimonialBtn = document.getElementById('next');

let currentTestimonial = 0;
let autoSlideInterval = 5000; // 5 seconds

function showTestimonial(index) {
    testimonials.forEach((t) => t.classList.remove('active'));
    testimonials[index].classList.add('active');
}

// Initial display
showTestimonial(currentTestimonial);

// Buttons navigation
prevTestimonialBtn.addEventListener('click', () => {
    currentTestimonial = (currentTestimonial - 1 + testimonials.length) % testimonials.length;
    showTestimonial(currentTestimonial);
    resetAutoSlide();
});

nextTestimonialBtn.addEventListener('click', () => {
    currentTestimonial = (currentTestimonial + 1) % testimonials.length;
    showTestimonial(currentTestimonial);
    resetAutoSlide();
});

// Automatic slide
let slideTimer = setInterval(() => {
    currentTestimonial = (currentTestimonial + 1) % testimonials.length;
    showTestimonial(currentTestimonial);
}, autoSlideInterval);

// Reset auto slide when user clicks
function resetAutoSlide() {
    clearInterval(slideTimer);
    slideTimer = setInterval(() => {
        currentTestimonial = (currentTestimonial + 1) % testimonials.length;
        showTestimonial(currentTestimonial);
    }, autoSlideInterval);
}

/* =========================
   TOUCH SUPPORT FOR MOBILE
========================= */
let startX = 0;
let endX = 0;
const slider = document.querySelector('.testimonial-slider');

slider.addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX;
});

slider.addEventListener('touchend', (e) => {
    endX = e.changedTouches[0].clientX;
    if (startX - endX > 50) { // swipe left
        currentTestimonial = (currentTestimonial + 1) % testimonials.length;
        showTestimonial(currentTestimonial);
        resetAutoSlide();
    } else if (endX - startX > 50) { // swipe right
        currentTestimonial = (currentTestimonial - 1 + testimonials.length) % testimonials.length;
        showTestimonial(currentTestimonial);
        resetAutoSlide();
    }
});
