// --- YOUR VALIDATION HELPER FUNCTIONS ---

function est_alpha(ch) {
    if (!ch || ch.length <= 3) return false;
    let test = true;
    let i = 0;
    while (test && i < ch.length) {
        let c = ch[i].toUpperCase();
        if (("A" <= c && c <= "Z") || c === " ") {
            i++;
        } else {
            test = false;
        }
    }
    return test;
}

function isFieldValid(fieldId) {
    switch (fieldId) {
        case "nom": {
            let np = document.getElementById("nom").value;
            return np.length > 3 && est_alpha(np);
        }
        case "freres_soeurs": {
            let nSibVal = document.getElementById("freres_soeurs").value;
            let nSib = parseInt(nSibVal);
            return nSibVal !== "" && !isNaN(nSib) && 0 <= nSib && nSib <= 10;
        }
        case "date_naissance": {
            let dNVal = document.getElementById("date_naissance").value;
            if (dNVal === "") return false;
            let dN = new Date(dNVal);
            let dA = new Date();
            return dN <= dA;
        }
        case "adresse": {
            let adr = document.getElementById("adresse").value;
            return adr.length >= 10;
        }
        case "tel": {
            let tel = document.getElementById("tel").value;
            return tel.length === 8 && !isNaN(tel);
        }
        case "section": {
            let sec = document.getElementById("section").selectedIndex;
            return sec > 0;
        }
        case "loisir": {
            let loi = document.getElementById("loisir").value;
            return loi.trim().length > 0;
        }
        case "adresseSite": {
            let site = document.getElementById("adresseSite").value;
            return site.trim().length > 0;
        }
        default:
            return false;
    }
}

// Global variable to store the ID of the field with an error
let currentErrorFieldId = null;

// Function to trigger the Error Modal and remember which field failed
function showErrorModal(message, fieldId) {
    const errorModal = document.getElementById("errorModal");
    const errorMessageText = document.getElementById("errorMessageText");
    errorMessageText.textContent = message;
    currentErrorFieldId = fieldId;
    errorModal.classList.add("active");
}

// Highlight the invalid field and place focus on it
function highlightAndFocusField(fieldId) {
    if (!fieldId) return;

    let targetElement = document.getElementById(fieldId);

    // If it's a radio group, highlight the container
    if (fieldId === "genre") {
        targetElement = document.querySelector(".radio-group");
    }

    if (targetElement) {
        // Clear previous error highlights first
        document.querySelectorAll(".input-error").forEach(el => el.classList.remove("input-error"));

        // Add red error highlight class
        targetElement.classList.add("input-error");

        // Focus & scroll smoothly into view
        if (targetElement.focus) {
            targetElement.focus();
        }
        targetElement.scrollIntoView({ behavior: "smooth", block: "center" });

        // Remove red error highlight when user interacts with the input
        const removeError = () => {
            targetElement.classList.remove("input-error");
            targetElement.removeEventListener("input", removeError);
            targetElement.removeEventListener("change", removeError);
        };
        targetElement.addEventListener("input", removeError);
        targetElement.addEventListener("change", removeError);
    }
}

function verif2() {
    if (!isFieldValid("nom")) {
        showErrorModal("Erreur: Nom et Prénom invalides (minimum 4 lettres) !", "nom");
        return false;
    }
    if (!isFieldValid("freres_soeurs")) {
        showErrorModal("Erreur: Nombre de frères et sœurs doit être entre 0 et 10 !", "freres_soeurs");
        return false;
    }
    if (!isFieldValid("date_naissance")) {
        showErrorModal("Erreur: Date de naissance invalide !", "date_naissance");
        return false;
    }

    let gen = document.getElementsByName("genre");
    if (!(gen[0].checked || gen[1].checked)) {
        showErrorModal("Erreur: Veuillez choisir votre Genre !", "genre");
        return false;
    }

    if (!isFieldValid("adresse")) {
        showErrorModal("Erreur: Adresse trop courte (minimum 10 caractères) !", "adresse");
        return false;
    }
    if (!isFieldValid("tel")) {
        showErrorModal("Erreur: N° Tel doit comporter exactement 8 chiffres !", "tel");
        return false;
    }
    if (!isFieldValid("section")) {
        showErrorModal("Erreur: Veuillez choisir une Section !", "section");
        return false;
    }
    if (!isFieldValid("loisir")) {
        showErrorModal("Erreur: Veuillez préciser vos Loisirs !", "loisir");
        return false;
    }
    if (!isFieldValid("adresseSite")) {
        showErrorModal("Erreur: Veuillez saisir l'Adresse de votre site web !", "adresseSite");
        return false;
    }

    let rob = document.getElementById("robot").checked;
    if (!rob) {
        showErrorModal("Erreur: Veuillez cocher 'Je ne suis pas un robot' !", "robot");
        return false;
    }

    return true;
}

// --- 3D INTERACTIVE & DYNAMIC PROGRESS LOGIC ---

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("inscriptionForm");
    const progressBar = document.getElementById("progress-bar");
    const completionText = document.getElementById("completion-text");
    const rangeInput = document.getElementById("niveau");
    const rangeBadge = document.getElementById("range-val-badge");
    const successModal = document.getElementById("successModal");
    const closeModal = document.getElementById("closeModal");
    const errorModal = document.getElementById("errorModal");
    const closeErrorModal = document.getElementById("closeErrorModal");

    // 1. Three.js 3D Background Mesh
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

    // 2. Condition-Based Progress Bar Calculation
    const validatedFieldIds = [
        "nom",
        "freres_soeurs",
        "date_naissance",
        "adresse",
        "tel",
        "section",
        "loisir",
        "adresseSite"
    ];

    function updateProgress() {
        let validCount = 0;

        validatedFieldIds.forEach(id => {
            if (isFieldValid(id)) {
                validCount++;
            }
        });

        const gen = document.getElementsByName("genre");
        if (gen[0].checked || gen[1].checked) {
            validCount++;
        }

        if (document.getElementById("robot").checked) {
            validCount++;
        }

        let totalConditions = validatedFieldIds.length + 2;
        let percentage = Math.round((validCount / totalConditions) * 100);

        progressBar.style.width = percentage + "%";
        completionText.textContent = percentage + "% complété";
    }

    form.addEventListener("input", updateProgress);
    form.addEventListener("change", updateProgress);

    // 3. Range Badge Update
    rangeInput.addEventListener("input", (e) => {
        rangeBadge.textContent = e.target.value + "%";
    });

    // 4. Form Submission
    form.addEventListener("submit", (e) => {
        e.preventDefault();

        if (verif2()) {
            successModal.classList.add("active");

            if (typeof confetti === "function") {
                confetti({
                    particleCount: 150,
                    spread: 80,
                    origin: { y: 0.6 },
                    colors: ['#6366f1', '#a855f7', '#06b6d4', '#10b981']
                });
            }
        }
    });

    // Close Modal and Apply Red Highlight & Focus to Invalid Field
    closeErrorModal.addEventListener("click", () => {
        errorModal.classList.remove("active");
        if (currentErrorFieldId) {
            highlightAndFocusField(currentErrorFieldId);
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

    errorModal.addEventListener("click", (e) => {
        if (e.target === errorModal) {
            errorModal.classList.remove("active");
            if (currentErrorFieldId) {
                highlightAndFocusField(currentErrorFieldId);
            }
        }
    });
});