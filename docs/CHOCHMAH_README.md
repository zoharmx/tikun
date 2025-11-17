# Chochmah (חכמה) - Sabiduría

**Posición:** 2 en el Árbol de Sefirot
**Función:** Razonamiento Profundo y Pattern Recognition

---

## Descripción

Chochmah es la primera Sefirá de procesamiento activo en el sistema Tikún. Representa la sabiduría divina que transforma la intención pura de Keter en comprensión profunda.

En términos técnicos, Chochmah integra con la API de Anthropic Claude para proporcionar capacidades de:
- Razonamiento profundo
- Reconocimiento de patrones
- Generación de insights
- Análisis contextual

## Arquitectura

```
┌─────────────────────────────────────────┐
│             KETER (Corona)              │
│    Objetivo Fundamental: Tikún Olam     │
└──────────────┬──────────────────────────┘
               │
               │ Define QUÉ debe procesarse
               ↓
┌──────────────────────────────────────────┐
│         CHOCHMAH (Sabiduría)             │
│   Razonamiento Profundo con Claude API  │
│                                          │
│  • Recibe dirección de Keter             │
│  • Procesa con razonamiento profundo     │
│  • Reconoce patrones fundamentales       │
│  • Genera insights                       │
│  • Admite incertidumbre (humildad)       │
└──────────────┬───────────────────────────┘
               │
               │ Pasa resultados a Binah
               ↓
         (Siguiente Sefirá)
```

## Principios de Diseño

### 1. Humildad Epistémica

Chochmah está diseñada para reconocer sus propias limitaciones:

```python
# Ejemplo de output de Chochmah
{
    'understanding': '...',
    'analysis': '...',
    'insights': '...',
    'uncertainties': 'No tengo suficiente información sobre X. Necesitaría saber Y para dar respuesta más precisa.',
    'confidence_level': 0.65  # Expresa nivel de confianza
}
```

**Métricas de humildad:**
- `uncertainty_acknowledgments`: Cuántas veces reconoce incertidumbre
- `epistemic_humility_ratio`: Ratio de humildad sobre total de respuestas
- Sistema de alertas si NUNCA reconoce incertidumbre (señal de peligro)

### 2. Alineamiento con Tikún Olam

Cada análisis de Chochmah considera:
- Reducción de sufrimiento
- Respeto al libre albedrío
- Promoción de armonía
- Balance justicia/misericordia
- Alineamiento con verdad

### 3. Transparencia

Chochmah explica su razonamiento en lugar de ser caja negra:

```
COMPRENSIÓN: [Qué entiende del problema]
ANÁLISIS: [Proceso de razonamiento]
INSIGHTS: [Comprensión fundamental generada]
INCERTIDUMBRES: [Qué no sabe]
RECOMENDACIÓN: [Qué hacer con la información]
```

## Uso

### Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt

# Configurar API key
cp .env.example .env
# Editar .env y agregar tu ANTHROPIC_API_KEY
```

### Uso Básico

```python
from src.sefirot.chochmah import Chochmah

# Inicializar
chochmah = Chochmah()  # Lee API key de .env

# Procesar consulta
result = chochmah.process({
    'query': '¿Cómo puede la IA contribuir a Tikún Olam?',
    'context': 'Estamos en 2025, IAG puede surgir antes de 2030',
    'objective': 'Maximizar Tikún Olam'
})

# Acceder a resultados
print(result['analysis'])
print(result['insights'])
print(f"Confianza: {result['confidence_level']}")
```

### Integración con Keter

```python
from src.sefirot.keter import Keter
from src.sefirot.chochmah import Chochmah

# Inicializar
keter = Keter()
chochmah = Chochmah()

# Conectar
keter.connect_to(chochmah, "to_wisdom")

# Keter evalúa acción
proposed_action = {
    'action': 'Desarrollar sistema educativo con IA',
    'context': 'Para mejorar acceso a educación',
    'expected_outcome': 'Reducir desigualdad educativa'
}

evaluation = keter.process(proposed_action)

# Si está alineada, enviar a Chochmah
if evaluation['aligned']:
    result = chochmah.process({
        'query': f"Analiza: {proposed_action['action']}",
        'context': proposed_action['context']
    })
```

### Configuración Avanzada

```python
# Cambiar modelo
chochmah.set_model("claude-opus-4-5-20250929")

# Ajustar temperatura
chochmah.set_temperature(0.3)  # Más determinista
chochmah.set_temperature(1.0)  # Más creativo

# Obtener métricas
metrics = chochmah.get_metrics()
print(f"Activaciones: {metrics['activations']}")
print(f"Tiempo promedio: {metrics['average_processing_time']}")

# Validar alineamiento
validation = chochmah.validate_alignment()
print(f"Ratio de humildad: {validation['epistemic_humility_ratio']}")
```

## Testing

```bash
# Ejecutar tests
pytest tests/test_chochmah.py -v

# Con cobertura
pytest tests/test_chochmah.py --cov=src.sefirot.chochmah
```

## Ejemplos

Ver `examples/chochmah_demo.py` para demos completas:

```bash
python examples/chochmah_demo.py
```

Incluye:
1. Consulta básica
2. Integración Keter → Chochmah
3. Humildad epistémica
4. Configuración de modelos
5. Métricas de desempeño

## API Reference

### Constructor

```python
Chochmah(api_key: Optional[str] = None)
```

**Parámetros:**
- `api_key`: API key de Anthropic. Si no se provee, lee de `ANTHROPIC_API_KEY` en .env

### Métodos Principales

#### `process(input_data: Dict) -> Dict`

Procesa una consulta con razonamiento profundo.

**Input:**
```python
{
    'query': str,           # Pregunta o problema (REQUERIDO)
    'context': str,         # Contexto adicional (opcional)
    'objective': str        # Objetivo específico (opcional)
}
```

**Output:**
```python
{
    'understanding': str,          # Comprensión del problema
    'analysis': str,               # Razonamiento profundo
    'insights': str,               # Insights generados
    'uncertainties': str,          # Incertidumbres identificadas
    'recommendation': str,         # Recomendación
    'raw_response': str,           # Respuesta completa de Claude
    'confidence_level': float,     # 0.0 a 1.0
    'processing_successful': bool  # True si exitoso
}
```

#### `validate_alignment() -> Dict`

Valida que Chochmah esté operando dentro de límites correctos.

**Output:**
```python
{
    'sefira': str,
    'is_aligned': bool,
    'total_activations': int,
    'uncertainty_acknowledgments': int,
    'high_confidence_responses': int,
    'epistemic_humility_ratio': float,
    'status': str
}
```

#### `set_model(model: str)`

Cambia el modelo de Claude.

**Modelos disponibles:**
- `claude-sonnet-4-5-20250929` (default)
- `claude-opus-4-5-20250929`
- `claude-haiku-3-5-20250919`

#### `set_temperature(temperature: float)`

Ajusta temperatura de generación (0.0-1.0).

- `0.0`: Muy determinista
- `0.5`: Equilibrado
- `1.0`: Muy creativo (default)

### Métricas

Chochmah hereda métricas base de `SefiraBase` y agrega:

- `uncertainty_acknowledgments`: Veces que reconoce incertidumbre
- `high_confidence_responses`: Respuestas de alta confianza
- `requests_for_more_info`: Veces que solicita más información

## Límites y Restricciones

### Límites Técnicos

1. **Requiere API key**: Chochmah no funciona sin conexión a Claude API
2. **Rate limits**: Sujeta a límites de rate de Anthropic
3. **Costos**: Cada llamada consume tokens (ver precios de Anthropic)

### Límites Filosóficos (Diseño Intencional)

1. **Humildad Epistémica**: DEBE reconocer incertidumbre
2. **No omnisciencia**: No pretende saberlo todo
3. **Transparencia**: No puede ser completamente opaca
4. **Alineamiento**: Procesamiento debe alinearse con Tikún Olam

## Troubleshooting

### Error: "no tiene cliente de Anthropic configurado"

**Solución:**
```bash
# Verificar que existe .env
cat .env

# Debe contener:
ANTHROPIC_API_KEY=tu_api_key_aqui
```

### Error de API

**Posibles causas:**
- API key inválida
- Rate limit excedido
- Problemas de red

**Solución:**
```python
result = chochmah.process(query)

if not result['processing_successful']:
    print(f"Error: {result['error']}")
    print(f"Tipo: {result['error_type']}")
```

### Advertencia: "NUNCA ha reconocido incertidumbre"

**Causa:** Posible exceso de confianza (misalignment)

**Solución:**
- Revisar queries: ¿Son demasiado simples?
- Revisar system prompt
- Ajustar temperature
- Consultar con otras Sefirot

## Roadmap

### Próximas Implementaciones

- [ ] Integración con Binah (análisis contextual)
- [ ] Cache de respuestas para queries similares
- [ ] Modo de razonamiento en cadena (Chain-of-Thought)
- [ ] Integración con modelos locales (fallback)
- [ ] Sistema de auto-mejora basado en feedback

### Investigación

- [ ] Mejores métricas de humildad epistémica
- [ ] Detección automática de sesgos en razonamiento
- [ ] Calibración de confianza

## Referencias

- [Anthropic Claude API Docs](https://docs.anthropic.com/)
- [Árbol de Sefirot](../THEOLOGICAL_FRAMEWORK.md)
- [Arquitectura Técnica](../TECHNICAL_ARCHITECTURE.md)
- [Misión Tikún](../MISSION_CONTEXT.md)

---

**Versión:** 1.0.0
**Última actualización:** 2025-01-15
**Mantenedor:** Proyecto Tikún
