@echo off
echo ================================================================================
echo TIKUN OLAM - Deployment Final
echo ================================================================================
echo.
echo Los archivos de la aplicacion han sido copiados correctamente.
echo Ahora vamos a re-desplegar el hosting con la aplicacion completa.
echo.
echo Presiona cualquier tecla para continuar...
pause >nul

echo.
echo [1/3] Agregando archivos al repositorio Git...
git add public/
git commit -m "Add complete web app to public directory"
echo.

echo [2/3] Subiendo a GitHub...
git push
echo.

echo [3/3] Desplegando a Firebase Hosting...
firebase deploy --only hosting
echo.

echo ================================================================================
echo DEPLOYMENT COMPLETO!
echo ================================================================================
echo.
echo Tu aplicacion esta ahora en:
echo https://proyecto-tikun.web.app
echo.
echo Proximos pasos:
echo 1. Abre https://proyecto-tikun.web.app en tu navegador
echo 2. Ve a Firebase Console: https://console.firebase.google.com/project/proyecto-tikun
echo 3. En Authentication, habilita Email/Password y Google Sign-In
echo 4. Crea una cuenta y prueba el sistema
echo.
echo Para habilitar el backend (Cloud Functions):
echo - Lee el archivo: INSTRUCCIONES_FINALES.md
echo.
pause
