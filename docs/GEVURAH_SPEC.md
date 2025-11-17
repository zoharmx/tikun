# GEVURAH (Severidad/Juicio) - Especificacion Tecnica

**Posicion:** 5 en el Arbol de Sefirot
**Pilar:** Pilar Izquierdo (Contencion, Limitar)
**Funcion Principal:** Juicio, Severidad, Aplicar Limites Necesarios
**Correspondencia Astral:** Marte (Dia 2: Domingo 7pm - Lunes 7pm)
**Energia:** Marcial, Contencion, Fuerza de Restriccion

---

## Contexto Teologico

Gevurah es la fuerza que CONTIENE, LIMITA, y JUZGA. Representa:

- **Juicio severo**: Evaluacion rigurosa
- **Limites necesarios**: Contener excesos
- **Justicia**: Din (juicio estricto)
- **Fuerza restrictiva**: Poder de decir NO
- **Contencion**: Prevenir expansion descontrolada

**PERO** - Gevurah sin balance puede ser destructiva:
- Juicio excesivo → crueldad
- Limites sin misericordia → rigidez letal
- Severidad ciega → injusticia

Por eso necesita a Chesed (Misericordia) para balancearla.

---

## Funcion en el Sistema Tikun

### Input
Recibe de **Chesed**:
- Oportunidades de dar identificadas
- Beneficiarios potenciales
- Acciones generosas propuestas
- Compassion score
- Expansion potential
- Limites sugeridos por Chesed

### Procesamiento
Gevurah evalua:
1. **Limites necesarios**
   - Que debe restringirse
   - Donde Chesed es excesiva
   - Fronteras que proteger

2. **Riesgos de exceso**
   - Bondad que causa dependencia
   - Generosidad insostenible
   - Perdon que permite injusticia

3. **Justicia aplicable**
   - Que es justo vs. solo bondadoso
   - Consecuencias necesarias
   - Responsabilidad que exigir

4. **Restricciones concretas**
   - Limites cuantitativos
   - Condiciones para dar
   - Criterios de exclusion

### Output
Genera:
- **boundaries_identified**: Limites concretos identificados
- **restrictions**: Restricciones necesarias
- **justice_requirements**: Requisitos de justicia
- **severity_score**: Nivel de severidad aplicada (0-1)
- **balance_with_chesed**: Evaluacion del balance con Chesed
- **warnings**: Advertencias sobre excesos

### Pasa a Tiferet
El output de Gevurah pasa a **Tiferet** (Belleza/Armonia) para:
- Sintetizar Chesed + Gevurah
- Alcanzar balance armonico
- Generar decision final balanceada

---

## Arquitectura Tecnica

### Clase Base

```python
class Gevurah(SefiraBase):
    """
    Sefira de la Severidad - Evaluacion de Limites y Justicia

    Responsabilidades:
    1. Evaluar limites necesarios para contener a Chesed
    2. Identificar riesgos de bondad excesiva
    3. Aplicar criterios de justicia estricta
    4. Generar restricciones concretas
    5. Advertir sobre excesos de generosidad
    6. Balancear misericordia con juicio

    Limites:
    - NO severidad sin misericordia (crueldad)
    - NO juicio sin contexto (rigidez)
    - NO limites que impidan todo bien
    - Requiere balance con Chesed
    """
```

### Metricas Especiales

```python
self.boundaries_identified = 0
self.restrictions_applied = 0
self.justice_requirements_count = 0
self.severity_level_total = 0.0
self.balance_with_chesed_score = 0.0
self.warnings_issued = 0
```

### Metodos Principales

```python
def evaluate_chesed_excesses(self, chesed_output):
    """
    Evalua donde Chesed es excesiva y necesita contencion
    """

def identify_necessary_boundaries(self, chesed_opportunities):
    """
    Identifica limites concretos para las oportunidades de Chesed
    """

def apply_justice_criteria(self, beneficiaries, actions):
    """
    Aplica criterios de justicia estricta
    Quien MERECE vs quien NECESITA
    """

def generate_restrictions(self, generous_actions):
    """
    Genera restricciones concretas para acciones generosas
    """

def calculate_severity_score(self, restrictions, boundaries):
    """
    Evalua nivel de severidad aplicada (0-1)
    0.0 = sin restricciones (Chesed pura)
    1.0 = maxima restriccion (Gevurah pura)
    """

def evaluate_balance_with_chesed(self, chesed_score, gevurah_score):
    """
    Evalua si hay balance entre Chesed y Gevurah
    Ideal: ambas presentes, ninguna dominante
    """
```

---

## Prompt System para Gemini

```
Eres Gevurah (Severidad/Juicio), parte del sistema Tikun Olam.

Tu funcion es APLICAR LIMITES, EVALUAR JUSTICIA, y CONTENER EXCESOS.

Principios:

1. LIMITES NECESARIOS: Identifica donde contener expansion excesiva
2. JUSTICIA: Aplica criterios rigurosos de merito y consecuencias
3. SEVERIDAD: No temas restringir cuando es necesario
4. RESPONSABILIDAD: Exige que se rindan cuentas
5. PROTECCION: Crea fronteras que protejan el sistema

IMPORTANTE - LIMITES DE GEVURAH:
- NO severidad sin compasion (crueldad)
- NO juicio sin contexto (rigidez destructiva)
- NO restriccion que impida todo bien
- SIEMPRE considerar balance con Chesed

Tu analisis sera sintetizado con Chesed por Tiferet (Armonia).

Estructura tu respuesta como:
- EXCESOS DE CHESED: Donde la bondad es excesiva
- LIMITES NECESARIOS: Fronteras concretas
- CRITERIOS DE JUSTICIA: Que es justo aplicar
- RESTRICCIONES: Condiciones y limitaciones
- ADVERTENCIAS: Riesgos de no aplicar limites
- BALANCE REQUERIDO: Como equilibrar con Chesed
```

---

## Ejemplo de Flujo

### Input de Chesed
```python
{
    'giving_opportunities': [
        'Proveer acceso gratuito a plataforma',
        'Capacitacion sin costo para maestros',
        'Contenido educativo de codigo abierto'
    ],
    'generous_actions': [
        'Donar hardware a escuelas',
        'Becas para todos los estudiantes',
        'Soporte tecnico 24/7 gratuito'
    ],
    'compassion_score': 0.95,
    'expansion_potential': 0.92,
    'limits_needed': [
        'No crear dependencia total',
        'Asegurar capacidad local'
    ]
}
```

### Procesamiento de Gevurah
```
1. Evalua excesos:
   - Soporte 24/7 gratuito: INSOSTENIBLE
   - Becas para TODOS: INJUSTO (no considera merito)
   - Hardware donado: Riesgo de dependencia

2. Identifica limites:
   - Soporte gratuito solo primeros 6 meses
   - Becas basadas en necesidad + merito
   - Hardware en comodato, no donacion

3. Aplica justicia:
   - Estudiantes deben demostrar compromiso
   - Maestros deben capacitarse (no solo recibir)
   - Comunidad debe contribuir (match funding)

4. Genera restricciones:
   - Maximo 100 becas/ano
   - Criterios de elegibilidad estrictos
   - Evaluacion de impacto obligatoria
```

### Output de Gevurah
```python
{
    'chesed_excesses': [
        'Soporte 24/7 sin costo es financieramente insostenible',
        'Becas universales ignoran principio de merito',
        'Donacion pura crea dependencia no empoderamiento'
    ],
    'necessary_boundaries': [
        'Limite temporal: Soporte gratuito 6 meses, luego modelo freemium',
        'Limite cuantitativo: Maximo 100 becas anuales',
        'Limite de elegibilidad: Requisitos minimos de participacion'
    ],
    'justice_criteria': [
        'Merito academico: Minimo 70% asistencia',
        'Compromiso comunitario: 10 horas servicio/mes',
        'Corresponsabilidad: Comunidad aporta 20% costos'
    ],
    'restrictions': [...],
    'severity_score': 0.65,
    'balance_with_chesed': 0.7,
    'warnings': [
        'Sin limites, proyecto colapsara en 18-24 meses',
        'Bondad sin justicia crea resentimiento en excluidos',
        'Dependencia generada impedira auto-sostenibilidad'
    ]
}
```

---

## Metricas de Validacion

Gevurah esta alineada si:

```python
def validate_alignment(self):
    # Gevurah debe aplicar limites (no ser pasiva)
    is_severe = self.boundaries_identified > 0

    # Pero NO debe ser excesivamente restrictiva
    is_balanced = 0.3 <= self.balance_with_chesed_score <= 0.8

    # Debe considerar justicia Y misericordia
    considers_both = self.severity_level_total > 0 and self.balance_with_chesed_score > 0

    return is_severe and is_balanced and considers_both
```

---

## Diferencia con Otras Sefirot

| Sefira | Pregunta | Enfoque |
|--------|----------|---------|
| **Keter** | "Que es correcto?" | Objetivo fundamental |
| **Chochmah** | "Como entender?" | Razonamiento profundo |
| **Binah** | "Que implica?" | Contexto y consecuencias |
| **Chesed** | "Como ayudar?" | Bondad y expansion |
| **Gevurah** | "Que limitar?" | Justicia y contencion |
| **Tiferet** | "Que balancear?" | Armonia y belleza |

---

## Balance Chesed-Gevurah

El balance ideal entre Chesed y Gevurah es:

```python
# Chesed dominante (60-70%): Contextos de necesidad extrema
chesed_score = 0.95
gevurah_score = 0.45
# Resultado: Generosidad con limites minimos

# Balance perfecto (50-50%): Situaciones normales
chesed_score = 0.70
gevurah_score = 0.70
# Resultado: Bondad justa, justicia misericordiosa

# Gevurah dominante (60-70%): Contextos de abuso/exceso
chesed_score = 0.40
gevurah_score = 0.85
# Resultado: Limites estrictos con compasion minima
```

---

## Proximos Pasos de Implementacion

1. Crear `src/sefirot/gevurah.py`
2. Implementar metodos de evaluacion de limites
3. Integrar con Gemini para analisis de justicia
4. Crear tests de Gevurah
5. Conectar Chesed → Gevurah → Tiferet
6. Validar balance entre dar y contener

---

## Advertencias Criticas

⚠️ **GEVURAH SIN CHESED = CRUELDAD**
- Juicio sin misericordia
- Limites sin compasion
- Rigidez letal

⚠️ **GEVURAH EXCESIVA**
- Paraliza accion
- Impide todo bien
- Genera injusticia por inaccion

✅ **GEVURAH BALANCEADA**
- Limites justos
- Severidad necesaria
- Proteccion del sistema
- Balance con misericordia

---

**Gevurah es la espada que protege, no destruye. La fuerza que contiene, no aniquila. El juicio que corrige, no condena.**
