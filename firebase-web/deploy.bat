@echo off
echo ================================================================================
echo Tikun Olam - Firebase Deployment Script
echo ================================================================================
echo.

echo [1/4] Checking Firebase CLI installation...
call firebase --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Firebase CLI not found. Please install it with: npm install -g firebase-tools
    exit /b 1
)
echo OK: Firebase CLI found
echo.

echo [2/4] Checking Firebase login...
call firebase login:list >nul 2>&1
if %errorlevel% neq 0 (
    echo Please login to Firebase...
    call firebase login
)
echo OK: Logged in to Firebase
echo.

echo [3/4] Installing Python dependencies for Cloud Functions...
cd functions
if exist requirements.txt (
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo WARNING: Error installing Python dependencies
    ) else (
        echo OK: Dependencies installed
    )
) else (
    echo WARNING: requirements.txt not found
)
cd ..
echo.

echo [4/4] Deploying to Firebase...
echo.
echo Choose deployment option:
echo   1. Deploy all (Hosting + Functions)
echo   2. Deploy Hosting only
echo   3. Deploy Functions only
echo   4. Cancel
echo.
set /p choice="Enter choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Deploying all...
    call firebase deploy
) else if "%choice%"=="2" (
    echo.
    echo Deploying Hosting only...
    call firebase deploy --only hosting
) else if "%choice%"=="3" (
    echo.
    echo Deploying Functions only...
    call firebase deploy --only functions
) else (
    echo Deployment cancelled
    exit /b 0
)

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Deployment failed
    exit /b 1
)

echo.
echo ================================================================================
echo Deployment completed successfully!
echo ================================================================================
echo.
echo Your app is now live at: https://proyecto-tikun.web.app
echo.
echo To open the app:
echo   firebase open hosting:site
echo.
pause
