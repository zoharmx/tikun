# Guia de Despliegue - Tikun Olam Firebase App

Esta guia te ayudara a desplegar la aplicacion Tikun Olam en Firebase paso a paso.

## Prerequisitos

1. **Node.js y npm** instalados
2. **Python 3.11** instalado
3. **Cuenta de Google** para Firebase
4. **API Key de Google Gemini** (para las Cloud Functions)

## Paso 1: Instalar Firebase CLI

Abre una terminal y ejecuta:

```bash
npm install -g firebase-tools
```

Verifica la instalacion:

```bash
firebase --version
```

## Paso 2: Login a Firebase

```bash
firebase login
```

Esto abrira tu navegador para autenticarte con Google.

## Paso 3: Copiar archivos del proyecto

Asegurate de que tienes la siguiente estructura:

```
firebase-web/
├── public/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── functions/
│   ├── main.py
│   └── requirements.txt
├── firebase.json
├── .firebaserc
└── README.md
```

## Paso 4: Copiar el codigo de las Sefirot

Las Cloud Functions necesitan acceso al codigo Python de las Sefirot. Copia la carpeta `src/` del proyecto principal:

```bash
# Desde la raiz del proyecto
cp -r src firebase-web/functions/
```

O en Windows:

```cmd
xcopy /E /I src firebase-web\functions\src
```

## Paso 5: Configurar Variables de Entorno

Necesitas configurar tu API Key de Gemini:

```bash
cd firebase-web
firebase functions:config:set gemini.api_key="TU_API_KEY_DE_GEMINI"
```

Para obtener tu API key de Gemini:
1. Ve a https://makersuite.google.com/app/apikey
2. Crea o copia tu API key
3. Usa el comando de arriba con tu key

## Paso 6: Instalar dependencias de Python

```bash
cd functions
pip install -r requirements.txt
cd ..
```

## Paso 7: Probar localmente (Opcional)

Antes de desplegar, puedes probar localmente:

```bash
firebase emulators:start
```

Abre http://localhost:5000 en tu navegador.

Para detener los emuladores, presiona `Ctrl+C`.

## Paso 8: Desplegar a Firebase

### Opcion 1: Usar el script de deployment (Windows)

```cmd
deploy.bat
```

Sigue las instrucciones en pantalla.

### Opcion 2: Deployment manual

```bash
# Desplegar todo
firebase deploy

# O solo hosting
firebase deploy --only hosting

# O solo functions
firebase deploy --only functions
```

## Paso 9: Abrir la aplicacion

Una vez desplegada, tu app estara en:

```
https://proyecto-tikun.web.app
```

O abrela directamente con:

```bash
firebase open hosting:site
```

## Paso 10: Verificar Authentication

1. Ve a la [Consola de Firebase](https://console.firebase.google.com/)
2. Selecciona tu proyecto "proyecto-tikun"
3. Ve a **Authentication** > **Sign-in method**
4. Habilita:
   - **Email/Password**
   - **Google**

## Troubleshooting

### Error: "Firebase CLI not found"

Reinstala Firebase CLI:

```bash
npm install -g firebase-tools
```

### Error: "Python dependencies failed"

Asegurate de tener Python 3.11 instalado:

```bash
python --version
```

Instala las dependencias manualmente:

```bash
cd functions
pip install firebase-functions firebase-admin google-generativeai loguru python-dotenv
```

### Error: "Module not found" en Cloud Functions

Asegurate de haber copiado la carpeta `src/` a `functions/`:

```bash
# Verifica que existe
ls firebase-web/functions/src/sefirot/
```

### Error de autenticacion

Verifica que Email/Password y Google esten habilitados en Firebase Console:

1. https://console.firebase.google.com/
2. Authentication > Sign-in method
3. Habilita los metodos necesarios

### Error: "Functions deployment failed"

Verifica que tienes el plan Blaze (pago por uso) activado en Firebase. Las Cloud Functions requieren este plan, aunque tiene una capa gratuita generosa.

1. Ve a Firebase Console
2. Configuracion del proyecto
3. Planes y facturacion
4. Actualiza a Blaze si es necesario

## Comandos Utiles

```bash
# Ver logs de Functions
firebase functions:log

# Ver configuracion actual
firebase functions:config:get

# Eliminar deployment
firebase hosting:disable

# Ver proyectos
firebase projects:list

# Ver estado del proyecto
firebase projects:describe proyecto-tikun
```

## Proximos Pasos

Una vez desplegada la aplicacion:

1. **Crea una cuenta** en la app usando email o Google
2. **Prueba el sistema** ingresando una accion
3. **Observa el proceso** a traves de las 10 Sefirot
4. **Revisa los resultados** del analisis completo

## Soporte

Si encuentras problemas:

1. Revisa los logs: `firebase functions:log`
2. Verifica la consola de Firebase
3. Asegurate de que todas las dependencias esten instaladas
4. Verifica que la API key de Gemini sea valida

## Notas Importantes

- **Costos**: Firebase tiene una capa gratuita generosa, pero las Cloud Functions en plan Blaze se cobran por uso. Las primeras 2 millones de invocaciones son gratis.
- **Limites**: Gemini API tiene limites de rate. Para uso en produccion, considera implementar caching y rate limiting.
- **Seguridad**: Las credenciales de Firebase ya estan configuradas en el codigo del frontend. NO compartas tu API key de Gemini publicamente.

## Actualizaciones

Para actualizar la app despues de cambios:

```bash
# Si cambiaste el frontend (HTML/CSS/JS)
firebase deploy --only hosting

# Si cambiaste las Cloud Functions
firebase deploy --only functions

# Para actualizar todo
firebase deploy
```

¡Felicidades! Tu sistema Tikun Olam ahora esta en la nube. 🌳
