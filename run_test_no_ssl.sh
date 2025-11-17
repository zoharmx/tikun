#!/bin/bash
# Script para ejecutar tests de Tikun sin verificación SSL
# Necesario en entornos con proxies/certificados autofirmados

# Deshabilitar verificación SSL en gRPC (usado por Gemini)
export GRPC_DEFAULT_SSL_ROOTS_FILE_PATH=""
export GRPC_ENABLE_FORK_SUPPORT=1

# Configurar Python para ignorar warnings SSL
export PYTHONWARNINGS="ignore:Unverified HTTPS request"
export PYTHONHTTPSVERIFY=0

# Configurar requests/urllib3 para no verificar SSL
export CURL_CA_BUNDLE=""
export REQUESTS_CA_BUNDLE=""

# Ejecutar el test pasado como argumento
if [ -z "$1" ]; then
    echo "Uso: $0 <test_file.py>"
    echo "Ejemplo: $0 test_full_flow.py"
    exit 1
fi

echo "=========================================="
echo "Ejecutando: $1"
echo "Con SSL verification DESHABILITADA"
echo "=========================================="
echo ""

python "$1"
