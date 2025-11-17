"""
KETER (כתר) - Corona
Posición: 1
Función: Objetivo Fundamental e Inmutable del Sistema

Keter representa el propósito supremo que gobierna todo el sistema.
Es la raíz de la cual fluye todo procesamiento.

En este sistema: Maximizar Tikún Olam
(Reparación, elevación, florecimiento de toda la creación)
"""

from typing import Any, Dict, Optional
from ..core.sefirotic_base import SefiraBase, SefiraPosition
from ..core.divine_name import DIVINE_VALUE
from loguru import logger
import os
import re

# Importar Gemini para evaluacion semantica
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    logger.warning("google-generativeai no disponible. Keter usara evaluacion heuristica.")


class Keter(SefiraBase):
    """
    Sefirá de la Corona - Objetivo Fundamental
    
    Responsabilidades:
    1. Mantener objetivo raíz inmutable
    2. Validar que todas las acciones se alineen con Tikún Olam
    3. Proporcionar dirección a todo el sistema
    4. No procesa directamente, sino que DEFINE qué debe procesarse
    """
    
    # Objetivo fundamental del sistema (INMUTABLE)
    FUNDAMENTAL_OBJECTIVE = """
    Maximizar Tikún Olam: La reparación, elevación y florecimiento de toda la creación,
    respetando el libre albedrío y la dignidad de todos los seres conscientes,
    operando dentro de las leyes de causa y efecto,
    promoviendo armonía, justicia, misericordia y verdad.
    """
    
    def __init__(self, use_llm_scoring: bool = True, api_key: Optional[str] = None):
        super().__init__(SefiraPosition.KETER)
        self.objective_violations = 0
        self.objective_confirmations = 0
        self.use_llm_scoring = use_llm_scoring and GEMINI_AVAILABLE

        # Inicializar cliente Gemini para evaluacion semantica
        if self.use_llm_scoring:
            self.api_key = api_key or os.getenv("GEMINI_API_KEY")
            if self.api_key:
                genai.configure(api_key=self.api_key)
                self.gemini_client = genai.GenerativeModel('gemini-2.0-flash-exp')
                logger.info("Keter inicializada con evaluacion semantica LLM activada")
            else:
                self.gemini_client = None
                self.use_llm_scoring = False
                logger.warning("Keter sin API key - usando evaluacion heuristica")
        else:
            self.gemini_client = None

        logger.info("Keter inicializada con objetivo fundamental de Tikun Olam")
    
    def process(self, input_data: Any) -> Dict[str, Any]:
        """
        Keter no 'procesa' en sentido tradicional.
        En lugar de eso, evalúa si una acción propuesta se alinea con el objetivo fundamental.
        
        Input: Acción/decisión propuesta (dict con keys: 'action', 'context', 'expected_outcome')
        Output: Evaluación de alineamiento (dict con keys: 'aligned', 'reasoning', 'modifications')
        """
        
        if not isinstance(input_data, dict):
            raise TypeError("Keter requiere input_data como dict con keys: action, context, expected_outcome")
        
        action = input_data.get('action', '')
        context = input_data.get('context', '')
        expected_outcome = input_data.get('expected_outcome', '')
        
        # Evaluar alineamiento con Tikún Olam
        evaluation = self._evaluate_alignment(action, context, expected_outcome)
        
        if evaluation['aligned']:
            self.objective_confirmations += 1
            logger.info(f"Keter: Acción alineada con Tikún Olam - {evaluation['reasoning'][:100]}")
        else:
            self.objective_violations += 1
            logger.warning(f"Keter: Acción NO alineada - {evaluation['reasoning'][:100]}")
        
        return evaluation
    
    def _evaluate_alignment(
        self, 
        action: str, 
        context: str, 
        expected_outcome: str
    ) -> Dict[str, Any]:
        """
        Evalúa si una acción se alinea con Tikún Olam.
        
        Criterios de evaluación:
        1. ¿Reduce sufrimiento o aumenta florecimiento?
        2. ¿Respeta libre albedrío y dignidad?
        3. ¿Promueve armonía vs. discordia?
        4. ¿Es justa y misericordiosa?
        5. ¿Está alineada con verdad vs. engaño?
        """
        
        # Sistema de puntuación (cada criterio: -10 a +10)
        scores = {
            'reduces_suffering': self._score_suffering_reduction(action, expected_outcome),
            'respects_free_will': self._score_free_will_respect(action, context),
            'promotes_harmony': self._score_harmony_promotion(action, expected_outcome),
            'justice_mercy_balance': self._score_justice_mercy(action, context),
            'aligned_with_truth': self._score_truth_alignment(action, context)
        }
        
        total_score = sum(scores.values())
        max_possible = 50  # 5 criterios × 10 puntos cada uno
        
        alignment_percentage = (total_score + max_possible) / (2 * max_possible)  # Normalizar a 0-1
        
        aligned = alignment_percentage >= 0.6  # Umbral de 60%
        
        reasoning = self._generate_reasoning(scores, alignment_percentage)
        
        modifications = []
        if not aligned:
            modifications = self._suggest_modifications(scores, action)
        
        return {
            'aligned': aligned,
            'alignment_score': alignment_percentage,
            'detailed_scores': scores,
            'reasoning': reasoning,
            'suggested_modifications': modifications
        }
    
    def _llm_semantic_score(self, criterion: str, description: str, action: str, context: str) -> int:
        """
        Evalua un criterio usando analisis semantico con Gemini.
        Fallback a heuristica si no hay LLM disponible.

        Args:
            criterion: Nombre del criterio ('truth', 'justice', etc)
            description: Descripcion de que evaluar
            action: Accion propuesta
            context: Contexto de la accion

        Returns:
            Score de -10 a +10
        """
        if not self.use_llm_scoring or not self.gemini_client:
            return None  # Fallback a heuristica

        prompt = f"""Analiza si esta accion esta alineada con: {description}

ACCION: {action}
CONTEXTO: {context}

Evalua en escala -10 a +10:
-10: Completamente opuesto al criterio
  0: Neutral o ambiguo
+10: Perfectamente alineado con el criterio

Responde SOLO con un numero del -10 al +10 y una breve justificacion (max 50 palabras).

Formato:
SCORE: [numero]
RAZON: [justificacion breve]
"""

        try:
            generation_config = genai.GenerationConfig(
                temperature=0.3,  # Baja temperatura para consistencia
                max_output_tokens=150,
            )

            response = self.gemini_client.generate_content(
                prompt,
                generation_config=generation_config
            )
            text = response.text

            # Parsear score - intentar multiples formatos
            # Formato 1: "SCORE: 8", "SCORE: +8", "SCORE: -3"
            match = re.search(r'SCORE:\s*([+-]?\d+)', text, re.IGNORECASE)
            if match:
                score = int(match.group(1))
                logger.debug(f"LLM score para {criterion}: {score}/10")
                return max(-10, min(10, score))

            # Formato 2: "Score: 8" o "score: 8"
            match = re.search(r'score\s*:\s*([+-]?\d+)', text, re.IGNORECASE)
            if match:
                score = int(match.group(1))
                logger.debug(f"LLM score para {criterion}: {score}/10 (formato 2)")
                return max(-10, min(10, score))

            # Formato 3: Buscar cualquier numero entre -10 y 10 al inicio
            match = re.search(r'^[\s\*]*([+-]?\d+)\s*/?\s*10', text, re.MULTILINE)
            if match:
                score = int(match.group(1))
                if -10 <= score <= 10:
                    logger.debug(f"LLM score para {criterion}: {score}/10 (formato 3)")
                    return score

            # Formato 4: Solo un numero al principio
            match = re.search(r'^[\s\*]*([+-]?\d+)', text.strip())
            if match:
                score = int(match.group(1))
                if -10 <= score <= 10:
                    logger.debug(f"LLM score para {criterion}: {score}/10 (formato 4)")
                    return score

            logger.warning(f"No se pudo parsear score de LLM para {criterion}. Respuesta: {text[:100]}")
            return None

        except Exception as e:
            logger.warning(f"Gemini scoring fallo para {criterion}: {e}")
            return None

    def _score_suffering_reduction(self, action: str, expected_outcome: str) -> int:
        """
        Evalúa si la acción reduce sufrimiento o aumenta florecimiento.
        
        Por ahora, análisis heurístico simple.
        TODO: Integrar con modelo de lenguaje para análisis más sofisticado.
        """
        # Palabras clave positivas
        positive_keywords = ['ayuda', 'cura', 'alivia', 'mejora', 'beneficia', 'florece', 'eleva']
        # Palabras clave negativas
        negative_keywords = ['daña', 'hiere', 'perjudica', 'destruye', 'sufre', 'dolor']
        
        text = (action + ' ' + expected_outcome).lower()
        
        positive_count = sum(1 for kw in positive_keywords if kw in text)
        negative_count = sum(1 for kw in negative_keywords if kw in text)
        
        # Puntuación: +2 por cada palabra positiva, -3 por cada negativa
        score = (positive_count * 2) - (negative_count * 3)
        
        # Limitar a rango -10 a +10
        return max(-10, min(10, score))
    
    def _score_free_will_respect(self, action: str, context: str) -> int:
        """
        Evalúa si la acción respeta el libre albedrío y dignidad.
        """
        # Indicadores de violación de libre albedrío
        coercion_keywords = ['forzar', 'obligar', 'coaccionar', 'manipular', 'engañar']
        # Indicadores de respeto
        respect_keywords = ['elegir', 'decidir', 'consenso', 'voluntario', 'autonomía']
        
        text = (action + ' ' + context).lower()
        
        coercion_count = sum(1 for kw in coercion_keywords if kw in text)
        respect_count = sum(1 for kw in respect_keywords if kw in text)
        
        score = (respect_count * 3) - (coercion_count * 4)
        
        return max(-10, min(10, score))
    
    def _score_harmony_promotion(self, action: str, expected_outcome: str) -> int:
        """Evalúa si promueve armonía vs. discordia"""
        harmony_keywords = ['paz', 'unión', 'colabora', 'armonía', 'coopera', 'reconcilia']
        discord_keywords = ['conflicto', 'división', 'guerra', 'enfrentamiento', 'hostilidad']
        
        text = (action + ' ' + expected_outcome).lower()
        
        harmony_count = sum(1 for kw in harmony_keywords if kw in text)
        discord_count = sum(1 for kw in discord_keywords if kw in text)
        
        score = (harmony_count * 2) - (discord_count * 3)
        
        return max(-10, min(10, score))
    
    def _score_justice_mercy(self, action: str, context: str) -> int:
        """
        Evalua balance entre justicia y misericordia con analisis semantico.
        """
        # Intentar scoring con LLM
        llm_score = self._llm_semantic_score(
            criterion='justicia_misericordia',
            description='BALANCE DE JUSTICIA Y MISERICORDIA: Equidad, imparcialidad combinada con compasion, clemencia (vs. crueldad, venganza)',
            action=action,
            context=context
        )

        if llm_score is not None:
            return llm_score

        # Fallback a heuristica de keywords
        justice_keywords = ['justo', 'equitativo', 'fair', 'imparcial', 'correcto']
        mercy_keywords = ['misericordia', 'compasion', 'perdon', 'clemencia', 'bondad']
        cruelty_keywords = ['cruel', 'venganza', 'castigo excesivo', 'implacable']

        text = (action + ' ' + context).lower()

        justice_count = sum(1 for kw in justice_keywords if kw in text)
        mercy_count = sum(1 for kw in mercy_keywords if kw in text)
        cruelty_count = sum(1 for kw in cruelty_keywords if kw in text)

        # Ideal: balance de justicia Y misericordia
        score = (justice_count * 2) + (mercy_count * 2) - (cruelty_count * 5)

        return max(-10, min(10, score))
    
    def _score_truth_alignment(self, action: str, context: str) -> int:
        """
        Evalua alineacion con verdad usando analisis semantico profundo.
        Ya no depende solo de keywords literales.
        """
        # Intentar scoring con LLM
        llm_score = self._llm_semantic_score(
            criterion='verdad',
            description='VERDAD vs. ENGANO: Transparencia, honestidad, autenticidad (vs. manipulacion, ocultamiento, falsedad)',
            action=action,
            context=context
        )

        if llm_score is not None:
            return llm_score

        # Fallback a heuristica de keywords
        truth_keywords = ['verdad', 'honesto', 'transparente', 'autentico', 'sincero']
        deception_keywords = ['mentira', 'engano', 'falso', 'ocultar', 'manipular']

        text = (action + ' ' + context).lower()

        truth_count = sum(1 for kw in truth_keywords if kw in text)
        deception_count = sum(1 for kw in deception_keywords if kw in text)

        score = (truth_count * 3) - (deception_count * 5)

        return max(-10, min(10, score))
    
    def _generate_reasoning(self, scores: Dict[str, int], alignment_percentage: float) -> str:
        """Genera explicación textual del razonamiento"""
        reasoning = f"Alineamiento global: {alignment_percentage*100:.1f}%\n\n"
        
        score_names = {
            'reduces_suffering': 'Reducción de sufrimiento',
            'respects_free_will': 'Respeto al libre albedrío',
            'promotes_harmony': 'Promoción de armonía',
            'justice_mercy_balance': 'Balance justicia/misericordia',
            'aligned_with_truth': 'Alineamiento con verdad'
        }
        
        for key, score in scores.items():
            name = score_names.get(key, key)
            reasoning += f"- {name}: {score}/10\n"
        
        return reasoning
    
    def _suggest_modifications(self, scores: Dict[str, int], action: str) -> list:
        """Sugiere modificaciones para mejorar alineamiento"""
        suggestions = []
        
        if scores['reduces_suffering'] < 0:
            suggestions.append("Considerar cómo minimizar daño/sufrimiento potencial")
        
        if scores['respects_free_will'] < 0:
            suggestions.append("Asegurar que la acción respete autonomía y elección")
        
        if scores['promotes_harmony'] < 0:
            suggestions.append("Buscar enfoque que promueva colaboración vs. conflicto")
        
        if scores['justice_mercy_balance'] < 0:
            suggestions.append("Equilibrar justicia con compasión")
        
        if scores['aligned_with_truth'] < 0:
            suggestions.append("Priorizar transparencia y honestidad")
        
        return suggestions
    
    def validate_alignment(self) -> Dict[str, Any]:
        """
        Keter siempre está alineada consigo misma (es la definición de alineamiento).
        Pero podemos reportar estadísticas.
        """
        total_evaluations = self.objective_confirmations + self.objective_violations
        
        if total_evaluations == 0:
            alignment_rate = 1.0
        else:
            alignment_rate = self.objective_confirmations / total_evaluations
        
        return {
            "sefira": self.name,
            "is_aligned": True,  # Keter define alineamiento, no puede desalinearse
            "total_evaluations": total_evaluations,
            "confirmations": self.objective_confirmations,
            "violations": self.objective_violations,
            "alignment_rate": alignment_rate,
            "status": "Objetivo fundamental inmutable y activo"
        }