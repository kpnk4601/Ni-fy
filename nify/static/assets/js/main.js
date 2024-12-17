themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    themeToggle.setAttribute('aria-label', `Switch to ${newTheme === 'light' ? 'dark' : 'light'} mode`);
});


const sparksContainer = document.getElementById('sparks');
        
function createSpark() {
    const spark = document.createElement('div');
    spark.className = 'spark';
    
    // Random direction
    const angle = Math.random() * Math.PI * 2;
    const distance = 20 + Math.random() * 30;
    const tx = Math.cos(angle) * distance;
    const ty = Math.sin(angle) * distance;
    
    spark.style.setProperty('--tx', `${tx}px`);
    spark.style.setProperty('--ty', `${ty}px`);
    
    sparksContainer.appendChild(spark);
    
    // Remove spark after animation
    setTimeout(() => {
        spark.remove();
    }, 1000);
}

// Create sparks periodically
setInterval(createSpark, 100);