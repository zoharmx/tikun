# Test de Flujo Simplificado - Keter -> Chochmah -> Binah

## Descripcion

Este test demuestra el funcionamiento completo del flujo de las 3 Sefirot superiores trabajando juntas:

1. **KETER** - Evalua si una accion propuesta esta alineada con Tikun Olam
2. **CHOCHMAH** - Genera razonamiento profundo e insights usando Gemini API
3. **BINAH** - Realiza analisis contextual multidimensional usando Gemini API

## Requisitos

1. Python 3.8+
2. API Key de Google Gemini configurada en archivo `.env`:
   ```
   GEMINI_API_KEY=tu_api_key_aqui
   ```
3. Dependencias instaladas:
   ```bash
   pip install -r requirements.txt
   ```

## Como Ejecutar

```bash
python test_flow_simple.py
```

## Que hace el test

### Paso 1: Inicializacion
- Inicializa las 3 Sefirot (Keter, Chochmah, Binah)
- Verifica que las API keys esten configuradas

### Paso 2: Definicion de Accion
- Define una accion de ejemplo: "Implementar IA para educacion en comunidades rurales"
- Incluye contexto y resultado esperado

### Paso 3: Evaluacion de Keter
- Keter evalua si la accion se alinea con Tikun Olam
- Criterios:
  - Reduccion de sufrimiento
  - Respeto al libre albedrio
  - Promocion de armonia
  - Balance justicia/misericordia
  - Alineamiento con verdad
- Si la accion NO esta alineada (score < 60%), el flujo se detiene

### Paso 4: Razonamiento de Chochmah
- Chochmah usa Gemini API para generar:
  - Comprension del problema
  - Analisis profundo
  - Insights clave
  - Incertidumbres reconocidas
  - Recomendaciones
- Genera un nivel de confianza basado en humildad epistemica

### Paso 5: Analisis de Binah
- Binah recibe los insights de Chochmah
- Realiza analisis contextual multidimensional:
  - Contexto historico
  - Stakeholders afectados
  - Efectos de primer, segundo y tercer orden
  - Riesgos sistemicos
  - Consideraciones eticas
  - Sintesis contextual
- Considera 6 dimensiones: temporal, social, economica, cultural, ambiental, politica

### Paso 6: Metricas Finales
- Muestra estadisticas de cada Sefira
- Valida alineamiento del sistema completo

## Resultado Esperado

Si todo funciona correctamente, veras:

```
======================================================================

  *** TEST EXITOSO ***

  El flujo Keter -> Chochmah -> Binah funciona correctamente.
  Las 3 Sefirot trabajan juntas de forma coordinada.
  El sistema esta alineado con Tikun Olam.

======================================================================

>> TEST COMPLETADO EXITOSAMENTE
```

## Metricas Importantes

### Keter
- **Tasa de alineamiento**: % de acciones aprobadas
- **Score de alineamiento**: Puntuacion de 0-100%

### Chochmah
- **Nivel de confianza**: 0-100% basado en reconocimiento de incertidumbre
- **Ratio de humildad epistemica**: % de respuestas que reconocen incertidumbre
- Chochmah esta alineada si ratio >= 20%

### Binah
- **Perspectivas consideradas**: Numero de dimensiones analizadas (ideal: 6)
- **Score de profundidad contextual**: 0-100% basado en analisis de 2do/3er orden
- Binah esta alineada si:
  - Score profundidad >= 60%
  - Perspectivas promedio >= 3

## Notas

- El test usa solo caracteres ASCII (compatible con Windows)
- La API de Gemini puede tardar 10-30 segundos por Sefira
- Si falla, verifica:
  1. GEMINI_API_KEY configurada correctamente
  2. Conexion a internet funcionando
  3. Creditos de API disponibles en Google AI Studio

## Ejemplo de Salida

El test muestra:
- Evaluacion de Keter con scores detallados
- Insights de Chochmah truncados a 400-500 caracteres por seccion
- Analisis de Binah truncado a 350-500 caracteres por seccion
- Metricas finales de las 3 Sefirot
- Estado del sistema (OPERATIVO / REQUIERE ATENCION)

## Modificar la Accion de Prueba

Para probar con tu propia accion, edita el archivo `test_flow_simple.py` en la seccion:

```python
action_data = {
    'action': 'Tu accion aqui...',
    'context': 'Contexto de la accion...',
    'expected_outcome': 'Resultado esperado...'
}
```

**Importante**: Para que Keter apruebe la accion, debe incluir palabras clave positivas como:
- Reduccion de sufrimiento: ayuda, mejora, beneficia, eleva
- Libre albedrio: decision, autonomia, elegir, consenso, voluntario
- Armonia: colaboracion, paz, coopera
- Justicia/Misericordia: justo, equitativo, compasion, misericordia
- Verdad: transparencia, honesto, autentico
