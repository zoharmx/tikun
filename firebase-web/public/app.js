// Import Firebase SDKs
import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js';
import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword, signInWithPopup, GoogleAuthProvider, onAuthStateChanged, signOut } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js';
import { getAnalytics } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js';
import { getFunctions, httpsCallable } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-functions.js';

// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCyO1p53Os8z-znEsJroB589bJuLgAfWdE",
  authDomain: "proyecto-tikun.firebaseapp.com",
  projectId: "proyecto-tikun",
  storageBucket: "proyecto-tikun.firebasestorage.app",
  messagingSenderId: "924692229038",
  appId: "1:924692229038:web:a66c4e4b498f52735cf63f",
  measurementId: "G-PPZEG3S0FV"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const analytics = getAnalytics(app);
const functions = getFunctions(app);

// DOM Elements
const loadingScreen = document.getElementById('loading-screen');
const authScreen = document.getElementById('auth-screen');
const mainApp = document.getElementById('main-app');
const authError = document.getElementById('auth-error');
const emailAuthForm = document.getElementById('email-auth-form');
const googleSigninBtn = document.getElementById('google-signin-btn');
const signupLink = document.getElementById('signup-link');
const signoutBtn = document.getElementById('signout-btn');
const userAvatar = document.getElementById('user-avatar');
const userName = document.getElementById('user-name');
const actionForm = document.getElementById('action-form');
const processingSection = document.getElementById('processing-section');
const resultsSection = document.getElementById('results-section');
const resultsContent = document.getElementById('results-content');

// State
let isSignupMode = false;
let currentUser = null;

// Initialize app
setTimeout(() => {
    loadingScreen.classList.add('hidden');
}, 2000);

// Auth state observer
onAuthStateChanged(auth, (user) => {
    if (user) {
        currentUser = user;
        showMainApp(user);
    } else {
        currentUser = null;
        showAuthScreen();
    }
});

// Email auth
emailAuthForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    hideError();

    try {
        if (isSignupMode) {
            await createUserWithEmailAndPassword(auth, email, password);
        } else {
            await signInWithEmailAndPassword(auth, email, password);
        }
    } catch (error) {
        showError(getErrorMessage(error.code));
    }
});

// Google Sign-in
googleSigninBtn.addEventListener('click', async () => {
    const provider = new GoogleAuthProvider();

    try {
        await signInWithPopup(auth, provider);
    } catch (error) {
        showError(getErrorMessage(error.code));
    }
});

// Sign up toggle
signupLink.addEventListener('click', (e) => {
    e.preventDefault();
    isSignupMode = !isSignupMode;

    const authTitle = document.querySelector('.auth-title');
    const submitBtn = emailAuthForm.querySelector('button[type="submit"]');

    if (isSignupMode) {
        authTitle.textContent = 'Crear Cuenta';
        submitBtn.textContent = 'Registrarse';
        signupLink.textContent = 'Ya tengo cuenta';
    } else {
        authTitle.textContent = 'Bienvenido';
        submitBtn.textContent = 'Iniciar Sesion';
        signupLink.textContent = 'Registrate';
    }
});

// Sign out
signoutBtn.addEventListener('click', async () => {
    try {
        await signOut(auth);
    } catch (error) {
        console.error('Error signing out:', error);
    }
});

// Action form submission
actionForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const action = document.getElementById('action-input').value;
    const context = document.getElementById('context-input').value;
    const outcome = document.getElementById('outcome-input').value;

    await processAction({ action, context, expected_outcome: outcome });
});

// Show/hide screens
function showAuthScreen() {
    loadingScreen.classList.add('hidden');
    authScreen.classList.remove('hidden');
    mainApp.classList.add('hidden');
}

function showMainApp(user) {
    loadingScreen.classList.add('hidden');
    authScreen.classList.add('hidden');
    mainApp.classList.remove('hidden');

    // Update user info
    userName.textContent = user.displayName || user.email;
    userAvatar.src = user.photoURL || `https://ui-avatars.com/api/?name=${encodeURIComponent(user.email)}&background=6366f1&color=fff`;
}

// Error handling
function showError(message) {
    authError.textContent = message;
    authError.classList.remove('hidden');
}

function hideError() {
    authError.classList.add('hidden');
}

function getErrorMessage(code) {
    const messages = {
        'auth/invalid-email': 'Correo electronico invalido',
        'auth/user-disabled': 'Esta cuenta ha sido deshabilitada',
        'auth/user-not-found': 'No existe una cuenta con este correo',
        'auth/wrong-password': 'Contrasena incorrecta',
        'auth/email-already-in-use': 'Ya existe una cuenta con este correo',
        'auth/weak-password': 'La contrasena debe tener al menos 6 caracteres',
        'auth/popup-closed-by-user': 'Inicio de sesion cancelado'
    };

    return messages[code] || 'Ocurrio un error. Por favor intenta de nuevo.';
}

// Process action through Sefirot
async function processAction(inputData) {
    // Show processing section
    processingSection.classList.remove('hidden');
    resultsSection.classList.add('hidden');

    // Scroll to processing section
    processingSection.scrollIntoView({ behavior: 'smooth' });

    const sefirot = [
        'keter', 'chochmah', 'binah', 'chesed', 'gevurah',
        'tiferet', 'netzach', 'hod', 'yesod', 'malchut'
    ];

    try {
        // Simulate processing through each Sefira
        // In production, this would call Firebase Cloud Functions
        const results = {};

        for (let i = 0; i < sefirot.length; i++) {
            const sefira = sefirot[i];
            const stepElement = document.querySelector(`[data-sefira="${sefira}"]`);

            // Mark as active
            stepElement.classList.add('active');
            stepElement.querySelector('.step-status').textContent = '⏳';

            // Simulate processing
            await new Promise(resolve => setTimeout(resolve, 1500));

            // Mock result for demo
            results[sefira] = await processSefirot(sefira, inputData, results);

            // Mark as completed
            stepElement.classList.remove('active');
            stepElement.classList.add('completed');
            stepElement.querySelector('.step-status').textContent = '✓';
        }

        // Show results
        displayResults(results);

    } catch (error) {
        console.error('Error processing action:', error);
        alert('Error al procesar la accion. Por favor intenta de nuevo.');
    }
}

// Mock Sefirot processing (in production, this calls Cloud Functions)
async function processSefirot(sefira, inputData, previousResults) {
    // This is a mock function for the demo
    // In production, this would call Firebase Cloud Functions that run the Python backend

    const mockResults = {
        keter: {
            alignment_score: 0.67,
            is_aligned: true,
            message: 'Accion alineada con Tikun Olam'
        },
        chochmah: {
            confidence_level: 0.75,
            understanding: 'Sistema educativo con IA para comunidades rurales',
            insights: ['Personalizacion del aprendizaje', 'Acceso a recursos', 'Capacitacion docente']
        },
        binah: {
            perspectives_count: 5,
            stakeholders: ['Estudiantes', 'Maestros', 'Comunidad', 'Gobierno'],
            risks: ['Brecha digital', 'Dependencia tecnologica']
        },
        chesed: {
            compassion_score: 1.0,
            giving_opportunities: 6,
            beneficiaries: ['Ninos rurales', 'Familias', 'Comunidad educativa']
        },
        gevurah: {
            severity_score: 1.0,
            boundaries: 7,
            warnings: ['Limitar tiempo de pantalla', 'Validar contenido']
        },
        tiferet: {
            harmony_score: 1.0,
            beauty_score: 1.0,
            conflicts_resolved: 4
        },
        netzach: {
            sustainability_score: 1.0,
            victory_probability: 1.0,
            obstacles: 7
        },
        hod: {
            precision_score: 0.4,
            clarity_score: 0.5,
            phases: 4
        },
        yesod: {
            manifestation_readiness: 0.825,
            ready_to_manifest: true,
            concrete_steps: 7
        },
        malchut: {
            completion_percentage: 0.75,
            actions_executed: 10,
            world_updated: true,
            responsibilities_assigned: 6
        }
    };

    return mockResults[sefira] || {};
}

// Display results
function displayResults(results) {
    resultsContent.innerHTML = '';

    // Overall summary
    const summaryCard = document.createElement('div');
    summaryCard.className = 'result-card';
    summaryCard.innerHTML = `
        <h3>Resumen del Analisis</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <p style="color: var(--color-text-secondary); font-size: 0.875rem;">Alineamiento Keter</p>
                <p style="font-size: 1.5rem; font-weight: 700;">${(results.keter.alignment_score * 100).toFixed(0)}%</p>
            </div>
            <div>
                <p style="color: var(--color-text-secondary); font-size: 0.875rem;">Confianza Chochmah</p>
                <p style="font-size: 1.5rem; font-weight: 700;">${(results.chochmah.confidence_level * 100).toFixed(0)}%</p>
            </div>
            <div>
                <p style="color: var(--color-text-secondary); font-size: 0.875rem;">Armonia Tiferet</p>
                <p style="font-size: 1.5rem; font-weight: 700;">${(results.tiferet.harmony_score * 100).toFixed(0)}%</p>
            </div>
            <div>
                <p style="color: var(--color-text-secondary); font-size: 0.875rem;">Readiness Yesod</p>
                <p style="font-size: 1.5rem; font-weight: 700;">${(results.yesod.manifestation_readiness * 100).toFixed(0)}%</p>
            </div>
        </div>
    `;
    resultsContent.appendChild(summaryCard);

    // Malchut - Final manifestation
    const malchutCard = document.createElement('div');
    malchutCard.className = 'result-card';
    malchutCard.innerHTML = `
        <h3>
            Malchut - Manifestacion
            <span class="result-badge ${results.malchut.completion_percentage > 0.7 ? 'high' : 'medium'}">
                ${(results.malchut.completion_percentage * 100).toFixed(0)}% Completado
            </span>
        </h3>
        <p style="margin-bottom: 1rem; color: var(--color-text-secondary);">
            ${results.malchut.world_updated ? 'Reino Manifestado - Tikun Olam en accion' : 'En proceso de manifestacion'}
        </p>
        <div style="display: grid; gap: 0.5rem;">
            <p><strong>Acciones Ejecutadas:</strong> ${results.malchut.actions_executed}</p>
            <p><strong>Responsabilidades Asignadas:</strong> ${results.malchut.responsibilities_assigned}</p>
            <p><strong>Mundo Actualizado:</strong> ${results.malchut.world_updated ? 'Si' : 'No'}</p>
        </div>
    `;
    resultsContent.appendChild(malchutCard);

    // Key insights
    const insightsCard = document.createElement('div');
    insightsCard.className = 'result-card';
    insightsCard.innerHTML = `
        <h3>Insights Clave</h3>
        <ul style="list-style: none; padding: 0; display: grid; gap: 0.75rem; margin-top: 1rem;">
            ${results.chochmah.insights.map(insight => `
                <li style="padding-left: 1.5rem; position: relative;">
                    <span style="position: absolute; left: 0; color: var(--color-primary);">•</span>
                    ${insight}
                </li>
            `).join('')}
        </ul>
    `;
    resultsContent.appendChild(insightsCard);

    // Stakeholders
    const stakeholdersCard = document.createElement('div');
    stakeholdersCard.className = 'result-card';
    stakeholdersCard.innerHTML = `
        <h3>Stakeholders Identificados (${results.binah.stakeholders.length})</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem;">
            ${results.binah.stakeholders.map(stakeholder => `
                <span style="background: var(--color-surface-light); padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.875rem;">
                    ${stakeholder}
                </span>
            `).join('')}
        </div>
    `;
    resultsContent.appendChild(stakeholdersCard);

    // Show results section
    resultsSection.classList.remove('hidden');
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}
