document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("inscriptionForm");
    const progressBar = document.getElementById("progress-bar");
    const completionText = document.getElementById("completion-text");
    const rangeInput = document.getElementById("niveau");
    const rangeBadge = document.getElementById("range-val-badge");
    const successModal = document.getElementById("successModal");
    const closeModal = document.getElementById("closeModal");

    // 1. Three.js 3D Interactive Background Animation (Floating 3D Wireframe Torus)
    const canvas = document.getElementById("bg-canvas");
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const geometry = new THREE.TorusGeometry(10, 3, 16, 100);
    const material = new THREE.MeshStandardMaterial({
        color: 0x6366f1,
        wireframe: true,
        roughness: 0.2,
        metalness: 0.8
    });
    const torusMesh = new THREE.Mesh(geometry, material);
    scene.add(torusMesh);

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
    scene.add(ambientLight);

    const pointLight = new THREE.PointLight(0xa855f7, 2, 50);
    pointLight.position.set(15, 15, 15);
    scene.add(pointLight);

    camera.position.z = 25;

    let mouseX = 0;
    let mouseY = 0;
    window.addEventListener("mousemove", (e) => {
        mouseX = (e.clientX / window.innerWidth - 0.5) * 0.5;
        mouseY = (e.clientY / window.innerHeight - 0.5) * 0.5;
    });

    function animate() {
        requestAnimationFrame(animate);
        torusMesh.rotation.x += 0.003 + mouseY * 0.1;
        torusMesh.rotation.y += 0.005 + mouseX * 0.1;
        torusMesh.rotation.z += 0.002;
        renderer.render(scene, camera);
    }
    animate();

    window.addEventListener("resize", () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });

    // 2. Live Progress Bar Calculation
    const fields = form.querySelectorAll("input:not([type='radio']):not([type='checkbox']), select, textarea");
    
    function updateProgress() {
        let filledCount = 0;
        fields.forEach(field => {
            if (field.value.trim() !== "") {
                filledCount++;
            }
        });

        const radioChecked = form.querySelector("input[name='genre']:checked");
        const checkboxChecked = document.getElementById("robot").checked;
        
        let totalItems = fields.length + 2;
        let currentScore = filledCount + (radioChecked ? 1 : 0) + (checkboxChecked ? 1 : 0);

        let percentage = Math.round((currentScore / totalItems) * 100);
        if (percentage > 100) percentage = 100;

        progressBar.style.width = percentage + "%";
        completionText.textContent = percentage + "% complété";
    }

    form.addEventListener("input", updateProgress);
    form.addEventListener("change", updateProgress);

    // 3. Live Range Slider Badge Updater
    rangeInput.addEventListener("input", (e) => {
        rangeBadge.textContent = e.target.value + "%";
    });

    // 4. Smooth Form Submission & Confetti Celebration
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        successModal.classList.add("active");

        if (typeof confetti === "function") {
            confetti({
                particleCount: 150,
                spread: 80,
                origin: { y: 0.6 },
                colors: ['#6366f1', '#a855f7', '#06b6d4', '#10b981']
            });
        }
    });

    closeModal.addEventListener("click", () => {
        successModal.classList.remove("active");
        form.reset();
        updateProgress();
        rangeBadge.textContent = "50%";
    });

    successModal.addEventListener("click", (e) => {
        if (e.target === successModal) {
            successModal.classList.remove("active");
        }
    });
});