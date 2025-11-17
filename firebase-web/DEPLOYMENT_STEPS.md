# 🚀 Pasos Simples para Deployment

## ✅ Paso 1: Verificar Prerequisitos

Ya tienes instalado:
- ✅ Node.js v20.19.5
- ✅ npm v10.8.2
- ✅ Python 3.13
- ✅ Firebase CLI

## ✅ Paso 2: Login a Firebase

Abre tu terminal y ejecuta:

```bash
firebase login
```

Esto abrirá tu navegador. Sigue estos pasos:
1. Selecciona tu cuenta de Google
2. Click en "Permitir"
3. Verás "Success! Logged in as tu@email.com"

## ✅ Paso 3: Configurar tu API Key de Gemini

Necesitas tu API key de Google Gemini:

### Obtener la API Key:
1. Ve a: https://makersuite.google.com/app/apikey
2. Click en "Create API Key"
3. Copia la key (se ve así: `AIza...`)

### Configurarla en Firebase:

```bash
cd firebase-web
firebase functions:config:set gemini.api_key="PEGA_TU_KEY_AQUI"
```

Reemplaza `PEGA_TU_KEY_AQUI` con tu key real.

## ✅ Paso 4: Desplegar (3 Opciones)

### Opción A: Despliegue Completo (Recomendado)

```bash
cd firebase-web
firebase deploy
```

Esto despliega:
- ✅ Hosting (Frontend)
- ✅ Cloud Functions (Backend)

Tiempo estimado: 3-5 minutos

### Opción B: Solo Frontend (Demo Rápido)

```bash
cd firebase-web
firebase deploy --only hosting
```

Esto despliega solo la interfaz con datos mock.

Tiempo estimado: 1 minuto

### Opción C: Usar el Script Automatizado (Windows)

```cmd
cd firebase-web
deploy.bat
```

Sigue el menú interactivo.

## ✅ Paso 5: Habilitar Autenticación

1. Ve a: https://console.firebase.google.com/
2. Selecciona tu proyecto "proyecto-tikun"
3. Click en "Authentication" en el menú lateral
4. Click en "Get started"
5. Habilita estos métodos:
   - **Email/Password**: Click en "Email/Password" → Habilitar → Guardar
   - **Google**: Click en "Google" → Habilitar → Guardar

## ✅ Paso 6: Verificar Deployment

Una vez completado, verás:

```
✔ Deploy complete!

Project Console: https://console.firebase.google.com/project/proyecto-tikun/overview
Hosting URL: https://proyecto-tikun.web.app
```

Abre la Hosting URL en tu navegador: `https://proyecto-tikun.web.app`

## ✅ Paso 7: Probar la Aplicación

1. Ve a https://proyecto-tikun.web.app
2. Verás la pantalla de login
3. Crea una cuenta con tu email o Google
4. ¡Prueba el sistema con una acción!

## 🔧 Troubleshooting Rápido

### Error: "Firebase CLI not found"

```bash
npm install -g firebase-tools
```

### Error: "Not logged in"

```bash
firebase login --reauth
```

### Error: "Permission denied"

Verifica que estés usando la cuenta correcta:

```bash
firebase login:list
```

Si no es la correcta:

```bash
firebase logout
firebase login
```

### Error: "Functions deployment failed"

El plan Blaze (pago por uso) es requerido para Cloud Functions.

1. Ve a Firebase Console
2. Configuración → Planes y facturacion
3. Actualiza a Blaze (tiene capa gratuita)

O despliega solo el frontend:

```bash
firebase deploy --only hosting
```

### Error: "API key not set"

```bash
firebase functions:config:set gemini.api_key="TU_KEY"
```

## 📊 Verificar que Todo Funciona

### 1. Hosting ✅

Abre: https://proyecto-tikun.web.app

Deberías ver la pantalla de login.

### 2. Authentication ✅

Intenta crear una cuenta.

Si funciona → ✅ Auth configurado

### 3. Functions ✅ (Solo si desplegaste functions)

En la app, intenta procesar una acción.

Si ves resultados reales → ✅ Functions funcionando
Si ves solo datos mock → ⚠️ Functions no desplegadas (normal si usaste --only hosting)

## 🎉 ¡Éxito!

Si llegaste aquí, tu app está desplegada.

### URLs Importantes:

- **App**: https://proyecto-tikun.web.app
- **Console**: https://console.firebase.google.com/project/proyecto-tikun
- **Analytics**: https://console.firebase.google.com/project/proyecto-tikun/analytics

### Próximos Pasos:

1. Lee GUIA_DE_USUARIO.md para aprender a usar el sistema
2. Prueba con diferentes acciones
3. Comparte la URL con otros usuarios

## 📝 Comandos Útiles

```bash
# Ver logs de Functions
firebase functions:log

# Ver config actual
firebase functions:config:get

# Re-desplegar después de cambios
firebase deploy

# Solo hosting
firebase deploy --only hosting

# Solo functions
firebase deploy --only functions

# Abrir la app
firebase open hosting:site

# Abrir consola
firebase open console
```

## 🆘 ¿Necesitas Ayuda?

1. Revisa DEPLOYMENT_GUIDE.md para más detalles
2. Revisa los logs: `firebase functions:log`
3. Verifica Firebase Console: https://console.firebase.google.com/
4. Asegúrate de que tu API key de Gemini funcione

---

¡Buena suerte con el deployment! 🚀
