# Tikun Olam - Firebase Web Application

Sistema de IA etica basado en el Arbol de la Vida (Kabbalah) desplegado en Firebase.

## Arquitectura

- **Frontend**: HTML + CSS + Vanilla JavaScript
- **Authentication**: Firebase Authentication (Email + Google)
- **Backend**: Firebase Cloud Functions (Python 3.11)
- **Hosting**: Firebase Hosting
- **Analytics**: Firebase Analytics

## Estructura del Proyecto

```
firebase-web/
├── public/              # Frontend files
│   ├── index.html      # Main HTML
│   ├── styles.css      # Styles
│   └── app.js          # Frontend JavaScript
├── functions/          # Cloud Functions
│   ├── main.py        # Python Cloud Functions
│   └── requirements.txt
├── firebase.json      # Firebase configuration
└── README.md
```

## Instalacion y Despliegue

### 1. Instalar Firebase CLI

```bash
npm install -g firebase-tools
```

### 2. Login a Firebase

```bash
firebase login
```

### 3. Inicializar Firebase en el proyecto

```bash
cd firebase-web
firebase init
```

Selecciona:
- **Hosting**: Firebase Hosting
- **Functions**: Cloud Functions (Python)
- **Public directory**: public
- **Single-page app**: Yes

### 4. Configurar Variables de Entorno

Crea un archivo `.env` en la raiz del proyecto con:

```
GEMINI_API_KEY=tu_api_key_de_gemini
```

Luego configura las variables en Firebase:

```bash
firebase functions:config:set gemini.api_key="tu_api_key_de_gemini"
```

### 5. Desplegar a Firebase

```bash
# Desplegar todo (Hosting + Functions)
firebase deploy

# Solo Hosting
firebase deploy --only hosting

# Solo Functions
firebase deploy --only functions
```

### 6. Abrir la aplicacion

```bash
firebase open hosting:site
```

## Desarrollo Local

### Ejecutar localmente

```bash
# Instalar dependencias de Functions
cd functions
pip install -r requirements.txt

# Volver a la raiz y ejecutar emuladores
cd ..
firebase emulators:start
```

La aplicacion estara disponible en `http://localhost:5000`

## Funcionalidades

### Autenticacion
- Login con correo electronico y contrasena
- Login con cuenta de Google
- Registro de nuevos usuarios
- Cierre de sesion

### Procesamiento de Acciones
1. El usuario ingresa una accion a evaluar
2. La accion pasa por las 10 Sefirot en secuencia:
   - **Keter**: Voluntad divina y alineamiento
   - **Chochmah**: Sabiduria y razonamiento
   - **Binah**: Entendimiento contextual
   - **Chesed**: Misericordia (Jupiter)
   - **Gevurah**: Severidad (Marte)
   - **Tiferet**: Belleza y armonia (Sol)
   - **Netzach**: Victoria y persistencia (Venus)
   - **Hod**: Esplendor y estructura (Mercurio)
   - **Yesod**: Fundamento y conexion (Luna)
   - **Malchut**: Reino y manifestacion (Saturno)
3. Se muestran los resultados del analisis completo

## Cloud Functions API

### `process_action`

Procesa una accion a traves de todas las Sefirot.

```javascript
const processAction = httpsCallable(functions, 'process_action');
const result = await processAction({
  action: 'Implementar sistema de IA educativa',
  context: 'Comunidades rurales',
  expected_outcome: 'Mejorar acceso a educacion'
});
```

### `process_sefira`

Procesa una Sefira individual.

```javascript
const processSefira = httpsCallable(functions, 'process_sefira');
const result = await processSefira({
  sefira: 'keter',
  input_data: { action: '...', context: '...' }
});
```

### `validate_sefira_alignment`

Valida el alineamiento de una Sefira.

```javascript
const validateAlignment = httpsCallable(functions, 'validate_sefira_alignment');
const result = await validateAlignment({ sefira: 'keter' });
```

## Configuracion de Firebase

El proyecto usa la siguiente configuracion de Firebase:

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyCyO1p53Os8z-znEsJroB589bJuLgAfWdE",
  authDomain: "proyecto-tikun.firebaseapp.com",
  projectId: "proyecto-tikun",
  storageBucket: "proyecto-tikun.firebasestorage.app",
  messagingSenderId: "924692229038",
  appId: "1:924692229038:web:a66c4e4b498f52735cf63f",
  measurementId: "G-PPZEG3S0FV"
};
```

## Seguridad

- Autenticacion requerida para acceder a la aplicacion
- Cloud Functions protegidas con Firebase Auth
- Reglas de seguridad de Firestore (si se implementa base de datos)

## Proximos Pasos

1. **Base de Datos**: Agregar Firestore para almacenar historial de acciones procesadas
2. **Dashboard**: Crear panel de estadisticas y metricas
3. **API REST**: Exponer API publica para integraciones
4. **Modo Offline**: Implementar service workers para funcionalidad offline
5. **Tests**: Agregar tests unitarios y de integracion

## Soporte

Para problemas o preguntas, contacta al equipo de desarrollo.

## Licencia

Copyright 2025 - Proyecto Tikun Olam
