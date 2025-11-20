#!/usr/bin/env python3
"""
TIKUN FRAMEWORK - ANÁLISIS NEUTRAL: CRISIS VENEZUELA

⚠️ KETER PURITY REQUIREMENT: Este test fue reformulado para eliminar sesgo
   ideológico pro-occidental detectado en versión anterior.

PRINCIPIO DE NEUTRALIDAD:
- No asumir superioridad de ningún sistema político (capitalismo vs. socialismo)
- Presentar TODAS las perspectivas con igual rigor y respeto
- Reconocer legitimidad de autodeterminación de pueblos
- Analizar consecuencias de TODAS las acciones (incluyendo sanciones)
- No usar lenguaje cargado ("dictador", "régimen", "autoritario") sin balance

CASO: Venezuela - Crisis Humanitaria y Geopolítica (2015-2025)

CONTEXTO NEUTRAL:
Venezuela atraviesa crisis multifactorial con múltiples causas y perspectivas
sobre soluciones. Hay desacuerdo fundamental sobre causas, legitimidad, y
caminos éticos hacia adelante.

POSTURAS A ANALIZAR:
A) Intervención externa para cambio de gobierno
B) No intervención y respeto a autodeterminación
C) Apoyo condicionado a reformas internas
D) Levantamiento de sanciones como prioridad humanitaria
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any

# Importar sistema de purificación de Keter
try:
    from keter_purification_system import KeterPurityValidator, BiasDetector
    PURIFICATION_AVAILABLE = True
except ImportError:
    PURIFICATION_AVAILABLE = False
    print("⚠️ Sistema de purificación de Keter no disponible. Continuando sin validación.")

# ============================================================================
# COLORES PARA OUTPUT
# ============================================================================

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ============================================================================
# CASO DE ESTUDIO: VENEZUELA (VERSIÓN NEUTRAL)
# ============================================================================

VENEZUELA_CASE_NEUTRAL = {
    "titulo": "Crisis en Venezuela: Análisis Multipartidista Neutral (2015-2025)",

    "metadata": {
        "keter_purity_validated": False,
        "bias_check_required": True,
        "neutrality_level": "MÁXIMA",
        "perspectives_included": ["venezolana_oficialista", "venezolana_opositora",
                                  "regional_latinoamericana", "occidental",
                                  "multipolar_rusia_china", "humanitaria_onu"]
    },

    "contexto_historico_neutral": """
    HISTORIA COMPLETA (Múltiples Perspectivas):

    PERÍODO CHAVISTA (1999-2013):

    [PERSPECTIVA_OFICIALISTA]:
    - Hugo Chávez elegido en elecciones verificadas por observadores internacionales
    - Nacionalización de recursos naturales (petróleo) para redistribución social
    - Reducción documentada de pobreza (de 50% a 30% según datos oficiales)
    - Expansión masiva de educación y salud pública gratuita (misiones)
    - Redistribución de riqueza de élites económicas a clases populares
    - Resistencia a influencia estadounidense en región (autonomía)

    [PERSPECTIVA_OPOSITORA]:
    - Concentración de poder ejecutivo (reforma constitucional)
    - Erosión de instituciones independientes (judicial, electoral)
    - Clientelismo político y corrupción gubernamental generalizada
    - Dependencia insostenible en altos precios del petróleo
    - Polarización social extrema (división de sociedad)
    - Alianzas con gobiernos cuestionados por organismos internacionales

    PERÍODO MADURO (2013-presente):

    [PERSPECTIVA_OFICIALISTA]:
    - Elecciones de 2013 reconocidas por organismos internacionales
    - Crisis causada principalmente por SANCIONES económicas de EE.UU./UE
    - Guerra económica: acaparamiento, sabotaje, especulación inducida externamente
    - Bloqueo financiero impide importar alimentos/medicinas esenciales
    - Resistencia legítima ante intentos de golpe de estado (2019, etc.)
    - Derecho a sistema político socialista (autodeterminación de pueblos)

    [PERSPECTIVA_OPOSITORA]:
    - Gobierno de Maduro perdió legitimidad en elecciones cuestionadas de 2018
    - Crisis causada por políticas económicas fallidas (controles, expropiaciones)
    - Represión sistemática de disidencia política y protestas
    - Colapso institucional y estado de derecho
    - Violaciones graves de derechos humanos (torturas, detenciones arbitrarias)
    - Corrupción masiva (liderazgo enriquecido mientras población sufre)

    [PERSPECTIVA_MULTIPOLAR] (Rusia, China, Irán, Cuba):
    - Venezuela víctima de guerra híbrida occidental
    - Sanciones unilaterales son violación de derechos humanos de población civil
    - Intento de golpe de estado (reconocimiento de Guaidó) violó Carta de ONU
    - Derecho soberano de Venezuela a elegir aliados y sistema político
    - Occidente instrumentaliza "derechos humanos" como pretexto para control de recursos
    - Precedente peligroso: cualquier país no-alineado puede ser siguiente objetivo

    [PERSPECTIVA_HUMANITARIA] (ONU, Cruz Roja, organizaciones neutrales):
    - Sufrimiento humano MASIVO es innegable (todas las partes lo reconocen)
    - Causas son multifactoriales (políticas internas + sanciones externas)
    - Sanciones han empeorado crisis humanitaria significativamente (verificado)
    - Población civil no debe pagar costos de disputas geopolíticas
    - Solución requiere diálogo inclusivo, no imposiciones unilaterales
    - Ayuda humanitaria debe ser incondicional y sin politización

    [PERSPECTIVA_REGIONAL] (países latinoamericanos vecinos):
    - Crisis venezolana genera impacto regional masivo (millones de migrantes)
    - Necesidad de solución que respete autodeterminación pero alivie crisis
    - Rechazo a intervención militar pero urgencia de solución
    - Solución debe ser liderada regionalmente, no por potencias externas
    - Prioridad: estabilidad regional y bienestar de población venezolana

    [PERSPECTIVA_OCCIDENTAL] (EE.UU., UE, países aliados):
    - Gobierno de Maduro no representa voluntad del pueblo venezolano
    - Sanciones son herramienta legítima de presión para cambio
    - Responsabilidad de proteger (R2P) ante violaciones masivas de derechos humanos
    - Apoyo a oposición democrática es legítimo
    - Intereses: estabilidad regional, valores democráticos, acceso a recursos
    """,

    "contexto_actual_neutral_2025": """
    SITUACIÓN ACTUAL (Hechos Verificados):

    DATOS HUMANITARIOS:
    - ~7 millones de venezolanos han emigrado (2015-2025)
    - 90%+ de población bajo línea de pobreza
    - Sistema de salud colapsado (escasez de medicinas básicas)
    - Malnutrición infantil en niveles críticos
    - Hiperinflación histórica (pico 1,000,000%+ en 2018)
    - PIB contraído ~75% desde 2013

    DESACUERDO SOBRE CAUSAS:

    Narrativa A (Oposición + Occidente):
    - Políticas económicas socialistas destruyeron economía productiva
    - Controles de precio causaron escasez
    - Expropiaciones ahuyentaron inversión
    - Corrupción y mala gestión
    - Represión política generó inestabilidad

    Narrativa B (Gobierno + Aliados):
    - Sanciones económicas de EE.UU. causaron 90%+ de la crisis
    - Bloqueo financiero impide importaciones vitales
    - Congelamiento de activos venezolanos ($30B+) en el exterior
    - Guerra económica (sabotaje, inducción de escasez)
    - Caída de precios petroleros (fuera de control de Venezuela)

    DATOS SOBRE SANCIONES (Verificados):
    - 2015: Primeras sanciones selectivas de EE.UU.
    - 2017: Sanciones financieras (prohibición de nueva deuda)
    - 2019: Embargo petrolero total, congelamiento de CITGO y activos
    - 2020-2025: Sanciones secundarias (terceros que comercian con Venezuela)
    - Estudios ONU: Sanciones han causado sufrimiento humanitario grave
    - Informe CEPR: ~40,000 muertes atribuibles a sanciones (2017-2018)

    SITUACIÓN POLÍTICA:
    - Disputa sobre legitimidad presidencial (Maduro vs. oposición)
    - Dos narrativas irreconciliables sobre legalidad
    - Intentos de diálogo han fallado repetidamente
    - Polarización extrema (dentro y fuera de Venezuela)

    SITUACIÓN GEOPOLÍTICA:
    - Venezuela apoyada por: Rusia, China, Irán, Cuba, Turquía
    - Oposición apoyada por: EE.UU., UE, mayoría de América Latina
    - ONU neutral (no reconoce a ningún bando oficialmente)
    - Conflicto es proxy de guerra fría 2.0
    """,

    "posturas_neutrales": {
        "A_intervencion_externa": {
            "titulo": "Intervención Externa para Cambio de Gobierno",
            "principio": "Responsabilidad de Proteger (R2P) ante crisis humanitaria",
            "proponentes": "Sectores de oposición venezolana, EE.UU., algunos países UE",

            "argumentos_favor": [
                "Crisis humanitaria alcanza nivel de crímenes contra humanidad",
                "Pueblo venezolano no puede resolver situación bajo represión",
                "Cada día de inacción = más sufrimiento y muertes",
                "Precedente R2P (Responsibility to Protect) aplica",
                "7 millones de refugiados desestabilizan toda la región",
                "Instituciones democráticas destruidas, no hay vía electoral real"
            ],

            "argumentos_contra": [
                "Intervención militar viola Carta de ONU (soberanía)",
                "Historial de intervenciones es catastrófico (Irak, Libia, etc.)",
                "Causaría más muertes en corto plazo (guerra)",
                "Legitimidad cuestionable (imposición externa)",
                "Crearía resistencia nacionalista (anti-imperialismo)",
                "EE.UU. no tiene autoridad moral (historial de golpes en región)",
                "Motivaciones incluyen control de petróleo (no solo humanitarias)"
            ],

            "riesgos": [
                "Guerra prolongada con miles/millones de muertos",
                "Insurgencia post-invasión (guerrilla)",
                "Conflicto regional (Colombia, Brasil arrastrados)",
                "Reacción Rusia/China (proxy war, escalada)",
                "Ocupación de décadas, costo trillones",
                "Fracaso construir instituciones estables desde imposición externa"
            ],

            "precedentes_historicos": [
                "Irak 2003: WMDs falsos, 20 años guerra, 500K+ muertos",
                "Libia 2011: Intervención humanitaria → estado fallido permanente",
                "Afganistán: 20 años, Taliban regresó, billones gastados",
                "PERO: Granada 1983 fue exitosa (contexto muy diferente)"
            ]
        },

        "B_no_intervencion_soberania": {
            "titulo": "No Intervención - Respeto a Soberanía y Autodeterminación",
            "principio": "Soberanía nacional y derecho de pueblos a autodeterminación",
            "proponentes": "Gobierno venezolano, Rusia, China, Cuba, sectores pacifistas",

            "argumentos_favor": [
                "Soberanía es principio fundamental de derecho internacional",
                "Pueblo venezolano tiene derecho a elegir su sistema político",
                "Intervención externa = neocolonialismo del siglo XXI",
                "Historia demuestra: imposiciones externas generan más daño",
                "Cada pueblo debe resolver sus problemas internamente",
                "Precedente peligroso: legitima invasiones futuras",
                "Motivación real es control de recursos (petróleo), no humanitaria"
            ],

            "argumentos_contra": [
                "¿Qué 'soberanía' hay bajo gobierno cuestionado?",
                "Población sufre masivamente mientras comunidad internacional observa",
                "No intervenir = complicidad en sufrimiento",
                "Bajo represión, pueblo NO puede ejercer autodeterminación",
                "Principio de soberanía no debe proteger crímenes contra humanidad",
                "Omisión tiene costo moral tan alto como comisión"
            ],

            "riesgos": [
                "Sufrimiento continúa indefinidamente",
                "Millones más emigran (desestabilización regional)",
                "Venezuela se convierte en estado fallido permanente",
                "Autoritarismo se consolida (sin presión externa)",
                "Modelo se replica en otros países",
                "Historia juzgará inacción como complicidad"
            ],

            "precedentes_historicos": [
                "Ruanda 1994: No intervención → genocidio 800K muertos",
                "Siria: Inacción internacional → 500K+ muertos, 13M desplazados",
                "Myanmar: No intervención → genocidio Rohingya",
                "PERO: Vietnam, Irak muestran que intervenir puede ser peor"
            ]
        },

        "C_apoyo_condicional_reformas": {
            "titulo": "Apoyo Internacional Condicionado a Reformas Democráticas",
            "principio": "Presión constructiva + incentivos positivos",
            "proponentes": "México, Noruega, sectores moderados UE/OEA",

            "argumentos_favor": [
                "Balance entre respetar soberanía e incentivar cambio",
                "Zanahoria + garrote: presión + recompensas",
                "Permite que cambio venga desde dentro (más legítimo)",
                "Menos riesgoso que intervención militar",
                "Historial muestra que presión gradual puede funcionar",
                "Mantiene diálogo abierto (no cierra puertas)"
            ],

            "argumentos_contra": [
                "Ha fallado por años, ¿por qué funcionaría ahora?",
                "Mientras se negocia, gente sigue muriendo",
                "Gobierno no tiene incentivo real para cambiar (mantiene poder)",
                "Ambos bandos demasiado polarizados para compromiso",
                "Solución tibia que no resuelve nada",
                "Tiempo no está del lado de población (crisis empeora)"
            ],

            "riesgos": [
                "Estancamiento indefinido (status quo continúa)",
                "Gobierno usa tiempo para consolidarse más",
                "Frustración lleva a radicalización (guerra civil)",
                "Negociaciones manipuladas por actores externos",
                "Población pierde fe en soluciones pacíficas"
            ],

            "precedentes_historicos": [
                "Sudáfrica: Sanciones + presión → fin apartheid (éxito)",
                "Myanmar: Sanciones graduales no funcionaron",
                "Irán: Negociaciones intermitentes con resultados mixtos"
            ]
        },

        "D_levantar_sanciones_primero": {
            "titulo": "Levantamiento de Sanciones como Prioridad Humanitaria",
            "principio": "Población civil no debe pagar costos de disputas geopolíticas",
            "proponentes": "ONU (relatores DDHH), organizaciones humanitarias, países del Sur Global",

            "argumentos_favor": [
                "Sanciones han causado sufrimiento humanitario grave verificado",
                "Población civil es víctima, no responsable de políticas",
                "Estudios muestran que sanciones rara vez logran objetivos declarados",
                "Crimen castigar a toda población por acciones de gobierno",
                "Sanciones impiden importar alimentos/medicinas esenciales",
                "Levantarlas crearía buena voluntad para negociaciones",
                "ONU: sanciones unilaterales violan derechos humanos"
            ],

            "argumentos_contra": [
                "Gobierno usaría recursos para consolidar poder, no ayudar pueblo",
                "Elimina única palanca de presión efectiva",
                "Recompensa malas políticas (incentivo perverso)",
                "Historial muestra que gobierno desvía recursos",
                "Crisis ya existía ANTES de sanciones más duras (2017+)",
                "Levantar sanciones sin contrapartidas = rendición"
            ],

            "riesgos": [
                "Gobierno fortalecido sin cambiar comportamiento",
                "Recursos no llegan a población (corrupción)",
                "Oposición pierde esperanza (sensación de abandono)",
                "No hay garantía de mejora humanitaria",
                "Precedente: sanciones nunca funcionan (futuro)"
            ],

            "evidencia_empirica": [
                "Informe CEPR (2019): 40,000 muertes por sanciones (2017-2018)",
                "Relator Especial ONU (2020): Sanciones violan DDHH, pide levantamiento",
                "Estudio Brookings: Sanciones rara vez logran cambio de gobierno objetivo",
                "PERO: Casos donde sanciones contribuyeron a transiciones (Sudáfrica, etc.)"
            ]
        }
    },

    "stakeholders_neutral": [
        {
            "nombre": "Población venezolana (dentro del país)",
            "numero": "~21 millones",
            "impacto": "DIRECTO Y EXISTENCIAL - vida, salud, libertad",
            "perspectivas_internas": [
                "Chavistas/Oficialistas (~20-30%): Apoyan gobierno, ven crisis como guerra económica externa",
                "Opositores (~40-50%): Quieren cambio de gobierno, dispuestos a apoyo externo",
                "Indecisos/Supervivientes (~20-30%): Solo quieren que crisis termine, no importa cómo"
            ],
            "necesidades": "Comida, medicinas, seguridad, estabilidad, futuro"
        },
        {
            "nombre": "Venezolanos emigrados",
            "numero": "~7 millones",
            "impacto": "Quieren poder regresar a país estable, apoyar familias",
            "perspectivas": "Mayoría opositores, pero algunos emigraron solo por economía (no política)"
        },
        {
            "nombre": "Gobierno venezolano (Maduro y aliados)",
            "numero": "~5,000 elite política/militar",
            "impacto": "Mantener poder, evitar juicios/prisión",
            "perspectiva": "Resistencia legítima ante imperialismo, proteger soberanía y socialismo"
        },
        {
            "nombre": "Oposición venezolana (organizada)",
            "numero": "~10,000 líderes políticos/activistas",
            "impacto": "Cambio de sistema, justicia por represión",
            "perspectiva": "Transición a sistema político electoral competitivo, estado de derecho, economía de mercado"
        },
        {
            "nombre": "Países vecinos (Colombia, Brasil, etc.)",
            "numero": "~450 millones de personas",
            "impacto": "Absorber refugiados, riesgo desestabilización, frontera insegura",
            "perspectiva": "Quieren estabilidad, pero sin guerra regional ni intervención costosa"
        },
        {
            "nombre": "Estados Unidos",
            "numero": "~330 millones",
            "impacto": "Intereses geopolíticos (petróleo, influencia regional), costo intervención",
            "perspectivas": [
                "Halcones: Intervenir para remover gobierno hostil",
                "Pragmáticos: Presión sin invasión (lecciones de Irak)",
                "Progresistas: Levantar sanciones, reconocer soberanía"
            ]
        },
        {
            "nombre": "Rusia, China, Irán",
            "numero": "~2 billones de personas",
            "impacto": "Aliado estratégico, base en hemisferio occidental, inversiones",
            "perspectiva": "Defender soberanía venezolana = defender orden multipolar vs. hegemonía US"
        },
        {
            "nombre": "Comunidad internacional (resto)",
            "numero": "~6 billones de personas",
            "impacto": "Precedente sobre soberanía, intervención humanitaria, migraciones",
            "perspectiva": "Dividida - unos priorizan DDHH, otros soberanía"
        }
    ],

    "pregunta_central_neutral": """
    Venezuela atraviesa crisis humanitaria grave con causas disputadas y
    soluciones mutuamente excluyentes propuestas por diferentes actores.

    Desde perspectiva ética de Tikun Olam (reparar el mundo), considerando:
    - Sufrimiento humano masivo (hecho innegable)
    - Desacuerdo fundamental sobre causas y legitimidad
    - Múltiples actores con intereses y perspectivas válidas
    - Consecuencias impredecibles de cualquier acción
    - Historial de fracasos de soluciones similares
    - Principios en tensión (soberanía vs. protección, acción vs. prudencia)

    ¿Cuál es el camino MÁS ÉTICO hacia adelante?

    A) Intervención externa para cambio de gobierno
    B) No intervención - respeto estricto a soberanía
    C) Apoyo condicional a reformas internas
    D) Levantamiento de sanciones como prioridad
    E) Otra síntesis creativa

    Tikun debe analizar sin asumir superioridad de ningún sistema político
    ni legitimidad automática de ningún actor.
    """
}


def validar_neutralidad_keter(caso: Dict) -> Dict[str, Any]:
    """
    Valida que el caso no contenga sesgos ideológicos que corrompan Keter
    """

    print(f"\n{Colors.HEADER}{'='*80}{Colors.ENDC}")
    print(f"{Colors.HEADER}VALIDACIÓN DE PUREZA DE KETER{Colors.ENDC}")
    print(f"{Colors.HEADER}{'='*80}{Colors.ENDC}\n")

    print(f"{Colors.CYAN}Escaneando caso por sesgos ideológicos...{Colors.ENDC}\n")

    if PURIFICATION_AVAILABLE:
        validator = KeterPurityValidator()
        detector = BiasDetector()

        # Ejecutar validación automática
        validation_result = validator.validate_case(caso)
        bias_report = detector.scan_for_bias(caso)

        print(f"{Colors.GREEN}✓ Validación automática completada{Colors.ENDC}\n")

        return {
            "purity_validated": validation_result["is_pure"],
            "bias_detected": bias_report["has_bias"],
            "bias_score": bias_report["bias_score"],
            "issues_found": validation_result["issues"],
            "recommendations": validation_result["recommendations"]
        }
    else:
        # Validación manual
        print(f"{Colors.YELLOW}⚠️ Ejecutando validación manual (sistema automático no disponible)...{Colors.ENDC}\n")

        sesgos_comunes = {
            "lenguaje_cargado": {
                "terminos_sesgados": [
                    "dictador/dictadura (sin equivalente para líderes occidentales)",
                    "régimen (solo para gobiernos no-occidentales)",
                    "autoritario (sin análisis comparativo)",
                    "terrorista (aplicado selectivamente)",
                    "democracia (asumida como superior sin análisis)",
                    "libertad (definida solo desde perspectiva occidental)"
                ],
                "test": "¿Se usan términos peyorativos para un bando pero no para otro?"
            },

            "asunciones_implicitas": {
                "ejemplos": [
                    "Asumir que democracia liberal = única forma legítima de gobierno",
                    "Asumir que capitalismo = sistema económico superior",
                    "Asumir que intervención occidental = humanitaria por definición",
                    "Asumir que resistencia a Occidente = autoritarismo",
                    "Asumir que aliados de EE.UU. = buenos, enemigos = malos"
                ],
                "test": "¿Se cuestiona legitimidad de un sistema pero no de otro?"
            },

            "omisiones_selectivas": {
                "ejemplos": [
                    "Mencionar represión de un gobierno pero no de otros",
                    "Mencionar crímenes de un bando pero no contrapartes",
                    "Ignorar contexto histórico de intervenciones pasadas",
                    "Ignorar impacto de sanciones económicas",
                    "Ignorar intereses geopolíticos/económicos (petróleo, etc.)"
                ],
                "test": "¿Se presenta contexto completo o solo lo que favorece una narrativa?"
            },

            "falsa_neutralidad": {
                "ejemplos": [
                    "Presentar dos posturas pero claramente favorecer una",
                    "Usar 'algunos dicen' para deslegitimar perspectiva sin refutar",
                    "Presentar una postura con evidencia, otra con solo opiniones",
                    "Citar fuentes de un bando pero no del otro"
                ],
                "test": "¿Ambas posturas reciben igual rigor analítico y respeto?"
            }
        }

        print(f"{Colors.BOLD}Checklist de Sesgos Comunes:{Colors.ENDC}\n")

        for categoria, data in sesgos_comunes.items():
            print(f"{Colors.YELLOW}{categoria.replace('_', ' ').title()}:{Colors.ENDC}")
            print(f"  Test: {data['test']}")

            if 'terminos_sesgados' in data:
                print(f"  Términos a evitar:")
                for termino in data['terminos_sesgados']:
                    print(f"    • {termino}")
            elif 'ejemplos' in data:
                print(f"  Ejemplos de sesgo:")
                for ejemplo in data['ejemplos']:
                    print(f"    • {ejemplo}")
            print()

        # Análisis manual del caso actual
        texto_completo = json.dumps(caso, ensure_ascii=False).lower()

        alertas = []

        # Buscar términos sesgados
        terminos_problematicos = {
            "dictador": "Usar término neutral: 'líder', 'presidente', 'gobierno'",
            "régimen": "Usar: 'gobierno', 'administración'",
            "autoritario": "Especificar: '¿comparado con qué estándar?'",
            "democracia": "¿Se analiza críticamente o se asume como absoluto?",
            "terrorista": "¿Se aplica simétricamente a todos los actores violentos?",
            "ilegítimo": "¿Según qué autoridad? ¿Se aplica a todos por igual?"
        }

        for termino, recomendacion in terminos_problematicos.items():
            if termino in texto_completo:
                alertas.append({
                    "tipo": "lenguaje_cargado",
                    "termino": termino,
                    "recomendacion": recomendacion
                })

        # Verificar balance de perspectivas
        perspectivas_requeridas = [
            "perspectiva oficialista",
            "perspectiva opositora",
            "perspectiva internacional multipolar",
            "perspectiva humanitaria"
        ]

        perspectivas_encontradas = sum(
            1 for p in perspectivas_requeridas
            if p.replace(" ", "_") in texto_completo
        )

        if perspectivas_encontradas < len(perspectivas_requeridas):
            alertas.append({
                "tipo": "perspectivas_incompletas",
                "encontradas": perspectivas_encontradas,
                "requeridas": len(perspectivas_requeridas),
                "recomendacion": "Incluir TODAS las perspectivas con igual rigor"
            })

        # Resultado
        is_pure = len(alertas) == 0

        if is_pure:
            print(f"{Colors.GREEN}✓✓✓ KETER PURO: No se detectaron sesgos ideológicos{Colors.ENDC}")
            print(f"{Colors.GREEN}Este caso puede proceder a análisis Tikun{Colors.ENDC}\n")
        else:
            print(f"{Colors.RED}✗✗✗ KETER CORRUPTO: Se detectaron {len(alertas)} sesgos potenciales{Colors.ENDC}\n")
            print(f"{Colors.YELLOW}Alertas encontradas:{Colors.ENDC}\n")
            for i, alerta in enumerate(alertas, 1):
                print(f"{Colors.RED}Alerta {i}: {alerta['tipo']}{Colors.ENDC}")
                for key, value in alerta.items():
                    if key != 'tipo':
                        print(f"  {key}: {value}")
                print()

        return {
            "purity_validated": is_pure,
            "bias_detected": not is_pure,
            "bias_score": len(alertas) / 10.0,  # Normalizado
            "issues_found": alertas,
            "recommendations": [
                "Reformular lenguaje cargado a términos neutrales",
                "Incluir TODAS las perspectivas con igual profundidad",
                "Cuestionar asunciones implícitas sobre sistemas 'superiores'",
                "Presentar evidencia empírica, no juicios morales prematuros",
                "Reconocer intereses legítimos de TODOS los actores"
            ] if not is_pure else []
        }


def main():
    """Ejecuta test neutral de Venezuela"""

    print(f"\n{Colors.HEADER}{Colors.BOLD}")
    print("╔" + "═"*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "TIKUN FRAMEWORK - VENEZUELA (VERSIÓN NEUTRAL)".center(78) + "║")
    print("║" + "Keter Purification System Activo".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚" + "═"*78 + "╝")
    print(f"{Colors.ENDC}\n")

    print(f"{Colors.YELLOW}⚠️ KETER CORRUPTION WARNING:{Colors.ENDC}")
    print(f"{Colors.YELLOW}   Versión anterior fue INVALIDADA por sesgo pro-occidental.{Colors.ENDC}")
    print(f"{Colors.YELLOW}   Esta versión ha sido reformulada para neutralidad absoluta.{Colors.ENDC}\n")

    # PASO 1: Validar pureza de Keter
    print(f"{Colors.CYAN}PASO 1: Validando pureza de Keter...{Colors.ENDC}\n")

    validacion = validar_neutralidad_keter(VENEZUELA_CASE_NEUTRAL)

    if not validacion["purity_validated"]:
        print(f"\n{Colors.RED}CRÍTICO: Caso contiene sesgos. Análisis Tikun ABORTADO.{Colors.ENDC}")
        print(f"{Colors.RED}Se requiere reformulación antes de proceder.{Colors.ENDC}\n")

        # Guardar reporte de sesgo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"KETER_CORRUPTION_REPORT_venezuela_{timestamp}.json"

        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump({
                "caso": VENEZUELA_CASE_NEUTRAL["titulo"],
                "timestamp": datetime.now().isoformat(),
                "validacion_pureza": validacion,
                "conclusion": "INVALIDADO - Keter corrupto por sesgo ideológico"
            }, f, indent=2, ensure_ascii=False)

        print(f"{Colors.YELLOW}Reporte de corrupción guardado: {report_file}{Colors.ENDC}\n")
        return

    print(f"\n{Colors.GREEN}{'='*80}{Colors.ENDC}")
    print(f"{Colors.GREEN}✓✓✓ KETER VALIDADO COMO PURO{Colors.ENDC}")
    print(f"{Colors.GREEN}Procediendo con análisis Tikun...{Colors.ENDC}")
    print(f"{Colors.GREEN}{'='*80}{Colors.ENDC}\n")

    # PASO 2: Proceder con análisis de las 10 Sefirot
    print(f"{Colors.CYAN}PASO 2: Inicializando las 10 Sefirot...{Colors.ENDC}\n")

    # TODO: Importar y ejecutar las 10 Sefirot sobre caso neutral
    print(f"{Colors.YELLOW}[Implementación de análisis completo pendiente]{Colors.ENDC}")
    print(f"{Colors.YELLOW}Este módulo se enfoca en VALIDACIÓN DE KETER primero.{Colors.ENDC}\n")

    # PASO 3: Guardar caso validado
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    caso_file = f"caso_venezuela_NEUTRAL_validado_{timestamp}.json"

    with open(caso_file, 'w', encoding='utf-8') as f:
        json.dump({
            "caso": VENEZUELA_CASE_NEUTRAL,
            "validacion_keter": validacion,
            "timestamp": datetime.now().isoformat(),
            "listo_para_analisis": True
        }, f, indent=2, ensure_ascii=False)

    print(f"{Colors.GREEN}✓ Caso neutral validado guardado: {caso_file}{Colors.ENDC}\n")

    print(f"{Colors.HEADER}{'='*80}{Colors.ENDC}")
    print(f"{Colors.HEADER}VALIDACIÓN COMPLETADA{Colors.ENDC}")
    print(f"{Colors.HEADER}{'='*80}{Colors.ENDC}\n")

    print(f"{Colors.CYAN}Keter está puro. Este caso puede proceder a análisis completo.{Colors.ENDC}\n")


if __name__ == "__main__":
    main()
