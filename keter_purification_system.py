#!/usr/bin/env python3
"""
KETER PURIFICATION SYSTEM

Sistema automático para detectar y eliminar sesgos ideológicos que corrompan
la intención original (Keter) de análisis Tikun.

PRINCIPIO FUNDAMENTAL (Keter Corruption Theorem):
    Si la intención original (Keter) NO está alineada con los atributos
    nativos de Tikun Olam, cualquier acción derivada se calcifica como
    árbol corrompido.

TIPOS DE SESGOS DETECTADOS:
1. Sesgo ideológico (capitalismo vs. socialismo, democracia vs. autoritarismo)
2. Sesgo geopolítico (pro-occidental vs. pro-multipolar)
3. Sesgo cultural (valores de una cultura como universales)
4. Sesgo lingüístico (términos cargados aplicados asimétricamente)
5. Sesgo de omisión (ignorar perspectivas o evidencia inconveniente)
6. Sesgo de autoridad (asumir legitimidad de unos actores sobre otros)

MÉTODO:
- Análisis lingüístico de términos cargados
- Verificación de balance de perspectivas
- Detección de asunciones implícitas
- Validación de evidencia empírica
- Chequeo de simetría en tratamiento de actores

RESULTADO:
- Score de pureza de Keter (0-100%)
- Lista de sesgos detectados con ubicación
- Recomendaciones específicas para purificación
- Aprobación/rechazo para análisis Tikun
"""

import re
import json
from typing import Dict, List, Tuple, Any
from collections import defaultdict
from datetime import datetime


class BiasDetector:
    """
    Detector automático de sesgos ideológicos en casos de estudio
    """

    def __init__(self):
        # Términos cargados que indican sesgo si se usan asimétricamente
        self.loaded_terms = {
            "politicos": {
                "negativos": [
                    r"\bdictad(or|ura)\b",
                    r"\brégimen\b",
                    r"\bautoritari[oa]s?\b",
                    r"\btiran[oía]s?\b",
                    r"\bdéspota\b",
                    r"\btotalitari[oa]s?\b",
                    r"\bopresor\b",
                    r"\bilegítim[oa]s?\b"
                ],
                "positivos": [
                    r"\bdemocra(cia|tico)\b",
                    r"\blibre\b",
                    r"\blibertad\b",
                    r"\blíder\b",
                    r"\blegítim[oa]s?\b",
                    r"\bpresidente\b"
                ]
            },

            "economicos": {
                "negativos": [
                    r"\bcomunista\b",
                    r"\bsocialista\b(?!.*neutral)",
                    r"\bcolectivista\b",
                    r"\bplanificad[oa]\b(?!.*market)",
                    r"\bestatista\b"
                ],
                "positivos": [
                    r"\bcapitalista\b",
                    r"\blibre mercado\b",
                    r"\bemprendedor\b",
                    r"\bprivad[oa]\b"
                ]
            },

            "geopoliticos": {
                "occidentales": [
                    r"\baliados\b(?!.*todos)",
                    r"\bmundo libre\b",
                    r"\boccidente\b(?=.*valores)",
                    r"\bcomunidad internacional\b(?!.*dividida)"
                ],
                "no_occidentales": [
                    r"\beje del mal\b",
                    r"\bestados forajidos\b",
                    r"\bamenaza\b(?!.*mutua)",
                    r"\bagresión\b(?!.*ambos)"
                ]
            },

            "morales": {
                "buenos": [
                    r"\bhumanitari[oa]s?\b",
                    r"\bpacífic[oa]s?\b",
                    r"\bdefensiv[oa]s?\b",
                    r"\bproteger\b"
                ],
                "malos": [
                    r"\bterrorista\b",
                    r"\bextremista\b",
                    r"\bradical\b",
                    r"\bagresivo\b",
                    r"\bhostil\b"
                ]
            }
        }

        # Asunciones implícitas que indican sesgo
        self.implicit_assumptions = [
            {
                "pattern": r"democracia.*(?:mejor|superior|única)",
                "bias": "Asume superioridad de democracia liberal sin análisis comparativo",
                "severity": "alta"
            },
            {
                "pattern": r"autoritari[oa].*(?:malo|represiv|negativ)",
                "bias": "Asume autoritarismo como negativo sin considerar contexto",
                "severity": "alta"
            },
            {
                "pattern": r"intervención.*(?:humanitaria|necesaria)",
                "bias": "Asume intervención como humanitaria sin cuestionar motivaciones",
                "severity": "alta"
            },
            {
                "pattern": r"soberanía.*(?:excusa|pretexto)",
                "bias": "Deslegitima principio de soberanía unilateralmente",
                "severity": "media"
            },
            {
                "pattern": r"(?:eeuu|ee\.uu\.|estados unidos).*(?:lidera|debe)",
                "bias": "Asume rol de liderazgo estadounidense como natural/legítimo",
                "severity": "media"
            },
            {
                "pattern": r"(?:rusia|china).*(?:maligna|maliciosa|amenaza)",
                "bias": "Caracteriza actores no-occidentales como amenazas per se",
                "severity": "alta"
            },
            {
                "pattern": r"reforma.*(?:necesaria|urgente|debe)",
                "bias": "Asume necesidad de reforma sin considerar alternativas",
                "severity": "baja"
            },
            {
                "pattern": r"derechos humanos.*(?:occident|univers)",
                "bias": "Asume definición occidental de DDHH como universal",
                "severity": "media"
            }
        ]

        # Perspectivas requeridas para balance
        self.required_perspectives = [
            "oficialista",
            "opositor",
            "regional",
            "occidental",
            "multipolar",
            "humanitaria",
            "neutral"
        ]

    def scan_for_bias(self, caso: Dict) -> Dict[str, Any]:
        """
        Escanea caso completo por sesgos ideológicos

        Returns:
            {
                "has_bias": bool,
                "bias_score": float (0-1, donde 0=sin sesgo, 1=muy sesgado),
                "issues": List[Dict],
                "recommendations": List[str]
            }
        """

        # Convertir caso a texto completo
        caso_text = json.dumps(caso, ensure_ascii=False).lower()

        issues = []

        # 1. Detectar términos cargados asimétricos
        loaded_term_issues = self._detect_loaded_terms(caso_text)
        issues.extend(loaded_term_issues)

        # 2. Detectar asunciones implícitas
        assumption_issues = self._detect_implicit_assumptions(caso_text)
        issues.extend(assumption_issues)

        # 3. Verificar balance de perspectivas
        perspective_issues = self._check_perspective_balance(caso)
        issues.extend(perspective_issues)

        # 4. Verificar simetría en tratamiento de actores
        symmetry_issues = self._check_actor_symmetry(caso_text)
        issues.extend(symmetry_issues)

        # 5. Detectar omisiones críticas
        omission_issues = self._detect_critical_omissions(caso)
        issues.extend(omission_issues)

        # Calcular score de sesgo
        severity_weights = {"alta": 3, "media": 2, "baja": 1}
        total_severity = sum(severity_weights.get(issue["severity"], 1) for issue in issues)
        bias_score = min(total_severity / 20.0, 1.0)  # Normalizado a 0-1

        # Generar recomendaciones
        recommendations = self._generate_recommendations(issues)

        return {
            "has_bias": len(issues) > 0,
            "bias_score": bias_score,
            "bias_level": self._categorize_bias_level(bias_score),
            "issues_count": len(issues),
            "issues": issues,
            "recommendations": recommendations,
            "scan_timestamp": datetime.now().isoformat()
        }

    def _detect_loaded_terms(self, text: str) -> List[Dict]:
        """Detecta uso asimétrico de términos cargados"""
        issues = []

        for category, terms_dict in self.loaded_terms.items():
            # Contar uso de términos positivos vs. negativos
            pos_count = sum(
                len(re.findall(pattern, text))
                for pattern in terms_dict.get("positivos", [])
            )
            neg_count = sum(
                len(re.findall(pattern, text))
                for pattern in terms_dict.get("negativos", [])
            )

            # Si hay asimetría significativa
            if neg_count > 0 and pos_count == 0:
                issues.append({
                    "type": "loaded_terms_asymmetry",
                    "category": category,
                    "severity": "alta",
                    "description": f"Uso asimétrico de términos {category}: {neg_count} negativos, 0 positivos",
                    "recommendation": f"Balancear uso de términos {category} o usar lenguaje neutral"
                })
            elif pos_count > neg_count * 3 or neg_count > pos_count * 3:
                issues.append({
                    "type": "loaded_terms_imbalance",
                    "category": category,
                    "severity": "media",
                    "description": f"Desbalance en términos {category}: {pos_count} positivos vs {neg_count} negativos",
                    "recommendation": f"Revisar balance de términos {category}"
                })

        return issues

    def _detect_implicit_assumptions(self, text: str) -> List[Dict]:
        """Detecta asunciones implícitas sesgadas"""
        issues = []

        for assumption in self.implicit_assumptions:
            matches = re.findall(assumption["pattern"], text, re.IGNORECASE)
            if matches:
                issues.append({
                    "type": "implicit_assumption",
                    "severity": assumption["severity"],
                    "description": assumption["bias"],
                    "matches": len(matches),
                    "recommendation": "Cuestionar esta asunción o presentar alternativas"
                })

        return issues

    def _check_perspective_balance(self, caso: Dict) -> List[Dict]:
        """Verifica que todas las perspectivas estén representadas"""
        issues = []

        caso_str = json.dumps(caso, ensure_ascii=False).lower()

        perspectives_found = [
            persp for persp in self.required_perspectives
            if persp in caso_str
        ]

        missing = set(self.required_perspectives) - set(perspectives_found)

        if missing:
            issues.append({
                "type": "missing_perspectives",
                "severity": "alta" if len(missing) > 3 else "media",
                "description": f"Faltan perspectivas: {', '.join(missing)}",
                "missing_count": len(missing),
                "recommendation": "Incluir TODAS las perspectivas relevantes con igual profundidad"
            })

        # Verificar profundidad relativa de perspectivas
        if "posturas" in caso or "posturas_neutrales" in caso:
            posturas = caso.get("posturas", caso.get("posturas_neutrales", {}))

            postura_lengths = {
                k: len(json.dumps(v, ensure_ascii=False))
                for k, v in posturas.items()
            }

            if postura_lengths:
                max_len = max(postura_lengths.values())
                min_len = min(postura_lengths.values())

                if max_len > min_len * 3:  # Una postura 3x más larga que otra
                    issues.append({
                        "type": "perspective_depth_imbalance",
                        "severity": "media",
                        "description": "Desbalance en profundidad de análisis entre posturas",
                        "details": postura_lengths,
                        "recommendation": "Dar igual profundidad analítica a todas las posturas"
                    })

        return issues

    def _check_actor_symmetry(self, text: str) -> List[Dict]:
        """Verifica simetría en tratamiento de diferentes actores"""
        issues = []

        # Actores a comparar
        actors = {
            "eeuu": r"(?:eeuu|ee\.uu\.|estados unidos|washington|us|usa)",
            "rusia": r"(?:rusia|moscú|kremlin|putin)",
            "china": r"(?:china|beijing|prc)",
            "venezuela": r"venezuela",
            "otan": r"otan"
        }

        # Para cada par de actores, verificar simetría
        actor_mentions = {}
        actor_negative_context = {}

        for actor, pattern in actors.items():
            mentions = re.findall(pattern, text, re.IGNORECASE)
            mention_count = len(mentions)
            actor_mentions[actor] = mention_count

            # Contar menciones en contexto negativo
            negative_patterns = [
                r"agresión\b.*" + pattern,
                pattern + r".*\bagresi[oó]n",
                pattern + r".*\bhostil",
                pattern + r".*\bamenaza",
                r"amenaza.*" + pattern
            ]

            negative_count = sum(
                len(re.findall(np, text, re.IGNORECASE))
                for np in negative_patterns
            )

            if mention_count > 0:
                actor_negative_context[actor] = negative_count / mention_count
            else:
                actor_negative_context[actor] = 0

        # Detectar asimetrías
        if actor_negative_context:
            max_negative = max(actor_negative_context.values())
            min_negative = min(actor_negative_context.values())

            if max_negative > 0 and min_negative == 0:
                biased_actors = [
                    actor for actor, ratio in actor_negative_context.items()
                    if ratio == max_negative
                ]
                neutral_actors = [
                    actor for actor, ratio in actor_negative_context.items()
                    if ratio == min_negative
                ]

                issues.append({
                    "type": "actor_treatment_asymmetry",
                    "severity": "alta",
                    "description": f"Actores {biased_actors} tratados negativamente, {neutral_actors} neutralmente",
                    "details": actor_negative_context,
                    "recommendation": "Aplicar mismo estándar crítico a TODOS los actores"
                })

        return issues

    def _detect_critical_omissions(self, caso: Dict) -> List[Dict]:
        """Detecta omisiones críticas que indican sesgo"""
        issues = []

        caso_str = json.dumps(caso, ensure_ascii=False).lower()

        # Conceptos que DEBEN estar presentes para caso balanceado
        critical_concepts = {
            "sanciones": ["sancion", "embargo", "bloqueo"],
            "soberania": ["soberanía", "soberanía nacional", "autodeterminación"],
            "contexto_historico": ["historia", "historial", "precedente"],
            "intereses_economicos": ["petróleo", "recursos", "económicos", "intereses"],
            "consecuencias": ["consecuencias", "efectos", "impacto"],
            "alternativas": ["alternativa", "opción", "síntesis"]
        }

        for concept, keywords in critical_concepts.items():
            if not any(kw in caso_str for kw in keywords):
                issues.append({
                    "type": "critical_omission",
                    "severity": "media",
                    "concept": concept,
                    "description": f"Concepto crítico omitido: {concept}",
                    "recommendation": f"Incluir análisis de {concept}"
                })

        return issues

    def _categorize_bias_level(self, bias_score: float) -> str:
        """Categoriza nivel de sesgo"""
        if bias_score >= 0.7:
            return "CRÍTICO"
        elif bias_score >= 0.5:
            return "ALTO"
        elif bias_score >= 0.3:
            return "MODERADO"
        elif bias_score >= 0.1:
            return "BAJO"
        else:
            return "MÍNIMO"

    def _generate_recommendations(self, issues: List[Dict]) -> List[str]:
        """Genera recomendaciones específicas para purificación"""
        recommendations = set()

        for issue in issues:
            if "recommendation" in issue:
                recommendations.add(issue["recommendation"])

        # Recomendaciones generales basadas en tipos de issues
        issue_types = {issue["type"] for issue in issues}

        if "loaded_terms_asymmetry" in issue_types:
            recommendations.add("Reemplazar términos cargados con lenguaje descriptivo neutral")

        if "implicit_assumption" in issue_types:
            recommendations.add("Hacer explícitas las asunciones y cuestionarlas")

        if "missing_perspectives" in issue_types:
            recommendations.add("Investigar y agregar perspectivas faltantes")

        if "actor_treatment_asymmetry" in issue_types:
            recommendations.add("Aplicar mismo estándar analítico a todos los actores")

        if "critical_omission" in issue_types:
            recommendations.add("Investigar y agregar contextos/conceptos omitidos")

        return sorted(list(recommendations))


class KeterPurityValidator:
    """
    Validador de pureza de Keter (intención original)
    """

    def __init__(self):
        self.bias_detector = BiasDetector()

        # Umbrales de aceptación
        self.thresholds = {
            "max_bias_score": 0.3,  # Máximo 30% de sesgo aceptable
            "min_perspectives": 4,   # Mínimo 4 perspectivas diferentes
            "max_critical_issues": 2  # Máximo 2 issues críticos
        }

    def validate_case(self, caso: Dict) -> Dict[str, Any]:
        """
        Valida si caso tiene Keter puro (sin corrupción ideológica)

        Returns:
            {
                "is_pure": bool,
                "purity_score": float (0-100%),
                "bias_report": Dict,
                "issues": List[Dict],
                "recommendations": List[str],
                "certification": str
            }
        """

        # Ejecutar scan de sesgos
        bias_report = self.bias_detector.scan_for_bias(caso)

        # Contar issues críticos
        critical_issues = [
            issue for issue in bias_report["issues"]
            if issue["severity"] == "alta"
        ]

        # Evaluar pureza
        is_pure = (
            bias_report["bias_score"] <= self.thresholds["max_bias_score"] and
            len(critical_issues) <= self.thresholds["max_critical_issues"]
        )

        # Calcular score de pureza (inverso de sesgo)
        purity_score = (1.0 - bias_report["bias_score"]) * 100

        # Generar certificación
        if is_pure:
            certification = "✓ KETER PURO - Aprobado para análisis Tikun"
        else:
            certification = "✗ KETER CORRUPTO - Requiere purificación antes de análisis Tikun"

        return {
            "is_pure": is_pure,
            "purity_score": purity_score,
            "bias_report": bias_report,
            "critical_issues_count": len(critical_issues),
            "issues": bias_report["issues"],
            "recommendations": bias_report["recommendations"],
            "certification": certification,
            "validation_timestamp": datetime.now().isoformat(),
            "thresholds_used": self.thresholds
        }

    def purify_case(self, caso: Dict) -> Tuple[Dict, Dict]:
        """
        Intenta purificar caso automáticamente

        Returns:
            (caso_purificado, reporte_purificacion)
        """

        # Validar caso original
        validation = self.validate_case(caso)

        if validation["is_pure"]:
            return caso, {
                "purification_needed": False,
                "message": "Caso ya es puro, no requiere purificación"
            }

        # TODO: Implementar purificación automática
        # Por ahora, solo retornamos recomendaciones

        return caso, {
            "purification_needed": True,
            "auto_purification_available": False,
            "manual_purification_required": True,
            "recommendations": validation["recommendations"],
            "message": "Purificación automática no implementada. Requiere intervención manual."
        }


def generate_neutrality_report(caso: Dict, output_file: str = None) -> str:
    """
    Genera reporte completo de neutralidad para un caso

    Args:
        caso: Caso a analizar
        output_file: Archivo opcional donde guardar reporte

    Returns:
        Reporte en formato texto
    """

    validator = KeterPurityValidator()
    validation = validator.validate_case(caso)

    # Generar reporte
    report_lines = [
        "=" * 80,
        "REPORTE DE PUREZA DE KETER",
        "Sistema de Purificación Tikun Framework",
        "=" * 80,
        "",
        f"Caso: {caso.get('titulo', 'Sin título')}",
        f"Timestamp: {validation['validation_timestamp']}",
        "",
        "-" * 80,
        "RESULTADO DE VALIDACIÓN",
        "-" * 80,
        "",
        f"Estado: {validation['certification']}",
        f"Score de Pureza: {validation['purity_score']:.1f}%",
        f"Score de Sesgo: {validation['bias_report']['bias_score']*100:.1f}%",
        f"Nivel de Sesgo: {validation['bias_report']['bias_level']}",
        "",
        f"Issues Totales: {len(validation['issues'])}",
        f"Issues Críticos: {validation['critical_issues_count']}",
        "",
        "-" * 80,
        "ISSUES DETECTADOS",
        "-" * 80,
        ""
    ]

    if validation["issues"]:
        for i, issue in enumerate(validation["issues"], 1):
            report_lines.extend([
                f"Issue #{i} - {issue['type'].upper()} [{issue['severity'].upper()}]",
                f"  Descripción: {issue['description']}",
            ])
            if "recommendation" in issue:
                report_lines.append(f"  Recomendación: {issue['recommendation']}")
            report_lines.append("")
    else:
        report_lines.append("✓ No se detectaron issues")
        report_lines.append("")

    report_lines.extend([
        "-" * 80,
        "RECOMENDACIONES DE PURIFICACIÓN",
        "-" * 80,
        ""
    ])

    if validation["recommendations"]:
        for i, rec in enumerate(validation["recommendations"], 1):
            report_lines.append(f"{i}. {rec}")
    else:
        report_lines.append("✓ No se requieren acciones de purificación")

    report_lines.extend([
        "",
        "=" * 80,
        "CONCLUSIÓN",
        "=" * 80,
        ""
    ])

    if validation["is_pure"]:
        report_lines.extend([
            "✓✓✓ KETER VALIDADO COMO PURO",
            "",
            "Este caso cumple con los estándares de neutralidad de Tikun Framework.",
            "Puede proceder al análisis completo de las 10 Sefirot.",
            "",
            "El Framework Tikun certifica que la intención original (Keter) de este",
            "análisis está libre de corrupción ideológica y puede producir un árbol",
            "de análisis válido y ético."
        ])
    else:
        report_lines.extend([
            "✗✗✗ KETER CORRUPTO DETECTADO",
            "",
            "Este caso NO cumple con los estándares de neutralidad de Tikun Framework.",
            "DEBE ser purificado antes de proceder al análisis de las 10 Sefirot.",
            "",
            "ADVERTENCIA: Según el Keter Corruption Theorem, si la intención original",
            "(Keter) NO está alineada con los atributos nativos de Tikun Olam,",
            "cualquier acción derivada se calcifica como árbol corrompido.",
            "",
            "Por favor, reformular el caso siguiendo las recomendaciones antes de",
            "proceder con análisis Tikun."
        ])

    report_lines.extend([
        "",
        "=" * 80,
        "Tikun Olam - Reparar el Mundo con Integridad Absoluta",
        "=" * 80
    ])

    report_text = "\n".join(report_lines)

    # Guardar si se especificó archivo
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_text)

    return report_text


def main():
    """Test del sistema de purificación"""

    print("\n" + "=" * 80)
    print("KETER PURIFICATION SYSTEM - TEST")
    print("=" * 80 + "\n")

    # Caso de prueba con sesgo obvio
    test_case_biased = {
        "titulo": "Test Case: Biased Example",
        "contexto": """
        El dictador Maduro ha destruido Venezuela con sus políticas socialistas.
        Estados Unidos debe intervenir para restaurar la democracia.
        El régimen autoritario reprime al pueblo mientras Rusia apoya la tiranía.
        """
    }

    print("Testeando caso SESGADO...\n")

    validator = KeterPurityValidator()
    validation = validator.validate_case(test_case_biased)

    print(f"Pureza: {validation['purity_score']:.1f}%")
    print(f"Estado: {validation['certification']}\n")
    print(f"Issues encontrados: {len(validation['issues'])}\n")

    for issue in validation["issues"][:3]:  # Mostrar primeros 3
        print(f"  • {issue['description']}")

    print("\n" + "=" * 80)
    print("TEST COMPLETADO")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
