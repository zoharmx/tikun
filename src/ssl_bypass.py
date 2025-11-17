"""
Módulo para configurar bypass de SSL en entornos con proxies/certificados autofirmados
ADVERTENCIA: Solo usar en desarrollo/testing, no en producción
"""

import os
import ssl
import warnings

def configure_ssl_bypass():
    """
    Configura el entorno para deshabilitar verificación SSL
    Necesario en entornos con proxies que usan certificados autofirmados
    """

    # Configurar variables de entorno para gRPC (usado por Gemini)
    os.environ['GRPC_DEFAULT_SSL_ROOTS_FILE_PATH'] = ''
    os.environ['GRPC_ENABLE_FORK_SUPPORT'] = '1'

    # Deshabilitar warnings SSL
    warnings.filterwarnings('ignore', message='Unverified HTTPS request')

    # Configurar SSL context global para no verificar
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
    except AttributeError:
        pass

    # Variables de entorno adicionales
    os.environ['PYTHONWARNINGS'] = 'ignore:Unverified HTTPS request'
    os.environ['CURL_CA_BUNDLE'] = ''
    os.environ['REQUESTS_CA_BUNDLE'] = ''

    print("⚠️  SSL Verification DESHABILITADA - Solo para desarrollo/testing")
    print()

# Auto-configurar cuando se importa el módulo
configure_ssl_bypass()
