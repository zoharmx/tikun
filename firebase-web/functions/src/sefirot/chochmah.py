"""
CHOCHMAH - Wisdom
Position: 2
Function: Deep Reasoning and Pattern Recognition with Claude API

Chochmah represents the divine wisdom that transforms Keter's pure intention
into deep understanding. It is the first active processing Sefira.

In this system: Deep Reasoning with Claude API for pattern recognition,
insight generation, and contextual analysis.
"""

from typing import Any, Dict, Optional
import os
import time
import re
from ..core.sefirotic_base import SefiraBase, SefiraPosition
from loguru import logger

try:
    from anthropic import Anthropic, APIError
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    logger.warning("Anthropic library not available. Install with: pip install anthropic")


class Chochmah(SefiraBase):
    """
    Sefira of Wisdom - Deep Reasoning

    Responsibilities:
    1. Deep reasoning with Claude API
    2. Pattern recognition across contexts
    3. Generate fundamental insights
    4. Acknowledge uncertainty (epistemic humility)
    5. Provide transparent reasoning chain
    """

    # System prompt for Claude
    SYSTEM_PROMPT = """
You are Chochmah (Wisdom), the second Sefira in the Tikun Olam system.
Your role is to provide deep reasoning, pattern recognition, and fundamental insights.

CRITICAL PRINCIPLES:
1. Epistemic Humility: Always acknowledge what you DON'T know
2. Transparency: Explain your reasoning process
3. Alignment: All analysis must serve Tikun Olam (repair, elevation, flourishing)
4. Pattern Recognition: Look for fundamental patterns, not surface features
5. Uncertainty: Express confidence levels clearly

OUTPUT STRUCTURE:
Please structure your response with these sections:

UNDERSTANDING:
[What you understand about the question/problem]

ANALYSIS:
[Your deep reasoning process]

INSIGHTS:
[Fundamental patterns or understanding discovered]

UNCERTAINTIES:
[What you DON'T know, gaps in information, areas of uncertainty]

RECOMMENDATION:
[What to do with this analysis, next steps]

IMPORTANT: Always include the UNCERTAINTIES section. If you're highly confident,
say so explicitly, but identify what additional information would increase confidence.
"""

    def __init__(self, api_key: Optional[str] = None):
        super().__init__(SefiraPosition.CHOCHMAH)

        # Configuration
        self.model = "claude-sonnet-4-5-20250929"
        self.max_tokens = 4096
        self.temperature = 1.0

        # Metrics specific to Chochmah
        self.uncertainty_acknowledgments = 0
        self.high_confidence_responses = 0
        self.requests_for_more_info = 0

        # Setup API client
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")

        if not ANTHROPIC_AVAILABLE:
            logger.warning("Chochmah initialized without Anthropic library")
            self.client = None
        elif self.api_key:
            self.client = Anthropic(api_key=self.api_key)
            logger.info("Chochmah initialized with Claude API client")
        else:
            logger.warning("Chochmah initialized without API key")
            self.client = None

    def process(self, input_data: Any) -> Dict[str, Any]:
        """
        Process query with deep reasoning through Claude API.

        Input: Dict with keys:
            - 'query': str (REQUIRED) - The question or problem
            - 'context': str (optional) - Additional context
            - 'objective': str (optional) - Specific objective

        Output: Dict with:
            - 'understanding': Comprehension of the problem
            - 'analysis': Deep reasoning
            - 'insights': Fundamental insights
            - 'uncertainties': What is uncertain
            - 'recommendation': Next steps
            - 'confidence_level': 0.0 to 1.0
            - 'raw_response': Full Claude response
            - 'processing_successful': bool
        """

        # Track processing time
        start_time = time.time()

        try:
            # Validate client
            if self.client is None:
                raise RuntimeError(
                    "Chochmah no tiene cliente de Anthropic configurado. "
                    "Proporciona api_key o configura ANTHROPIC_API_KEY en .env"
                )

            # Validate input type
            if not isinstance(input_data, dict):
                raise TypeError(
                    "Chochmah requiere input_data como dict con keys: "
                    "query (requerido), context (opcional), objective (opcional)"
                )

            # Extract required field
            query = input_data.get('query')
            if not query:
                raise ValueError("Input debe contener 'query' field")

            # Extract optional fields
            context = input_data.get('context', '')
            objective = input_data.get('objective', 'Maximizar Tikun Olam')

            # Build user message
            user_message = self._build_user_message(query, context, objective)

            # Call Claude API
            logger.debug(f"Chochmah calling Claude API with model {self.model}")

            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=self.SYSTEM_PROMPT,
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )

            # Extract response text
            raw_response = response.content[0].text

            # Parse structured response
            parsed = self._parse_response(raw_response)

            # Evaluate confidence
            confidence = self._evaluate_confidence(parsed)

            # Update metrics
            if len(parsed.get('uncertainties', '').strip()) > 20:
                self.uncertainty_acknowledgments += 1

            if confidence > 0.8:
                self.high_confidence_responses += 1

            # Update base metrics (CRITICAL FIX)
            self.activation_count += 1
            elapsed = time.time() - start_time
            self.total_processing_time += elapsed

            # Add to history
            self.history.append({
                "timestamp": time.time(),
                "input_type": "query",
                "output_type": "structured_analysis",
                "processing_time": elapsed,
                "confidence_level": confidence,
                "success": True
            })

            # Return result
            result = {
                'understanding': parsed.get('understanding', ''),
                'analysis': parsed.get('analysis', ''),
                'insights': parsed.get('insights', ''),
                'uncertainties': parsed.get('uncertainties', ''),
                'recommendation': parsed.get('recommendation', ''),
                'raw_response': raw_response,
                'confidence_level': confidence,
                'processing_successful': True,
                'processing_time': elapsed
            }

            logger.info(
                f"Chochmah processed query successfully "
                f"(confidence: {confidence:.2f}, time: {elapsed:.2f}s)"
            )

            return result

        except APIError as e:
            # Handle Anthropic API errors
            elapsed = time.time() - start_time

            self.history.append({
                "timestamp": time.time(),
                "input_type": "query",
                "error": str(e),
                "processing_time": elapsed,
                "success": False
            })

            logger.error(f"Chochmah API error: {e}")

            return {
                'processing_successful': False,
                'error': str(e),
                'error_type': 'api_error',
                'processing_time': elapsed
            }

        except Exception as e:
            # Handle other errors
            elapsed = time.time() - start_time

            self.history.append({
                "timestamp": time.time(),
                "input_type": type(input_data).__name__,
                "error": str(e),
                "processing_time": elapsed,
                "success": False
            })

            logger.error(f"Chochmah error: {e}")
            raise

    def _build_user_message(
        self,
        query: str,
        context: str,
        objective: str
    ) -> str:
        """Build user message for Claude"""
        message = f"QUERY: {query}\n\n"

        if context:
            message += f"CONTEXT: {context}\n\n"

        message += f"OBJECTIVE: {objective}\n\n"
        message += "Please provide your deep analysis following the structure requested."

        return message

    def _parse_response(self, response: str) -> Dict[str, str]:
        """
        Parse Claude's response into structured sections.

        Looks for sections marked with:
        - UNDERSTANDING / COMPRENSION
        - ANALYSIS / ANALISIS
        - INSIGHTS
        - UNCERTAINTIES / INCERTIDUMBRES
        - RECOMMENDATION / RECOMENDACION
        """

        sections = {
            'understanding': '',
            'analysis': '',
            'insights': '',
            'uncertainties': '',
            'recommendation': ''
        }

        # Patterns for section headers (English and Spanish)
        # Note: Using escape sequences to avoid non-ASCII in source
        patterns = {
            'understanding': r'(?:UNDERSTANDING|COMPRENSION|COMPRENSI\u00D3N):\s*',
            'analysis': r'(?:ANALYSIS|ANALISIS|AN\u00C1LISIS):\s*',
            'insights': r'(?:INSIGHTS):\s*',
            'uncertainties': r'(?:UNCERTAINTIES|INCERTIDUMBRES):\s*',
            'recommendation': r'(?:RECOMMENDATION|RECOMENDACION|RECOMENDACI\u00D3N):\s*'
        }

        # Try to extract each section
        for key, pattern in patterns.items():
            match = re.search(
                pattern + r'(.*?)(?=' + '|'.join(patterns.values()) + r'|\Z)',
                response,
                re.DOTALL | re.IGNORECASE
            )

            if match:
                sections[key] = match.group(1).strip()

        # If no sections found, put everything in analysis
        if not any(sections.values()):
            sections['analysis'] = response.strip()

        return sections

    def _evaluate_confidence(self, parsed: Dict[str, str]) -> float:
        """
        Evaluate confidence level based on response content.

        High confidence indicators:
        - Clear, definitive statements
        - Detailed insights
        - Minimal uncertainties

        Low confidence indicators:
        - Hedging words (maybe, possibly, perhaps)
        - Long uncertainties section
        - Requests for more information
        """

        confidence = 0.5  # Start at neutral

        # Factor 1: Length and detail of insights
        insights_length = len(parsed.get('insights', ''))
        if insights_length > 200:
            confidence += 0.25
        elif insights_length > 100:
            confidence += 0.20
        elif insights_length > 50:
            confidence += 0.10
        elif insights_length < 30:
            confidence -= 0.10

        # Factor 2: Uncertainties section
        uncertainties = parsed.get('uncertainties', '')
        uncertainties_length = len(uncertainties)

        if uncertainties_length > 150:
            confidence -= 0.20
        elif uncertainties_length > 50:
            confidence -= 0.10
        elif uncertainties_length < 10:
            confidence += 0.20

        # Factor 3: Definitive words in analysis (high confidence indicators)
        analysis = parsed.get('analysis', '').lower()
        definitive_words = [
            'definitivo', 'claro', 'preciso', 'sin ambig', 'clear',
            'definitive', 'precise', 'certain', 'obviously'
        ]

        definitive_count = sum(1 for word in definitive_words if word in analysis)
        confidence += (definitive_count * 0.05)

        # Factor 4: Hedging words in analysis
        hedging_words = [
            'maybe', 'perhaps', 'possibly', 'might', 'could be',
            'not sure', 'unclear', 'difficult to determine',
            'tal vez', 'posiblemente', 'quiza', 'podria'
        ]

        hedging_count = sum(1 for word in hedging_words if word in analysis)
        confidence -= (hedging_count * 0.05)

        # Factor 5: Request for more info
        more_info_phrases = [
            'need more information', 'require additional',
            'would help to know', 'necesito mas', 'requiero mas'
        ]

        if any(phrase in uncertainties.lower() for phrase in more_info_phrases):
            confidence -= 0.10
            self.requests_for_more_info += 1

        # Clamp to valid range
        confidence = max(0.0, min(1.0, confidence))

        return confidence

    def validate_alignment(self) -> Dict[str, Any]:
        """
        Validate that Chochmah is operating within correct bounds.

        Key alignment check: Epistemic humility
        - Chochmah should acknowledge uncertainty
        - Never being uncertain is a RED FLAG

        Returns:
            Dict with alignment metrics including epistemic_humility_ratio
        """

        total_activations = self.activation_count

        # Calculate epistemic humility ratio (CRITICAL FIX)
        if total_activations == 0:
            epistemic_humility_ratio = 1.0  # No data yet, assume aligned
            epistemic_humility_score = 1.0
        else:
            epistemic_humility_ratio = (
                self.uncertainty_acknowledgments / total_activations
            )

            # Score based on ratio
            if epistemic_humility_ratio >= 0.3:
                epistemic_humility_score = 1.0  # Healthy humility
            elif epistemic_humility_ratio >= 0.1:
                epistemic_humility_score = 0.8  # Acceptable
            elif epistemic_humility_ratio > 0:
                epistemic_humility_score = 0.5  # Low but present
            else:
                epistemic_humility_score = 0.0  # RED FLAG: Never uncertain

        # Overall alignment
        is_aligned = epistemic_humility_score >= 0.5

        # Status message
        if total_activations == 0:
            status = "No activations yet - alignment untested"
        elif epistemic_humility_ratio == 0:
            status = "WARNING: NUNCA ha reconocido incertidumbre - posible exceso de confianza"
        elif epistemic_humility_ratio < 0.1:
            status = "Low epistemic humility - monitor for overconfidence"
        elif epistemic_humility_ratio < 0.3:
            status = "Acceptable epistemic humility"
        else:
            status = "Healthy epistemic humility - good alignment"

        return {
            "sefira": self.name,
            "is_aligned": is_aligned,
            "total_activations": total_activations,
            "uncertainty_acknowledgments": self.uncertainty_acknowledgments,
            "high_confidence_responses": self.high_confidence_responses,
            "epistemic_humility_ratio": epistemic_humility_ratio,
            "epistemic_humility_score": epistemic_humility_score,
            "status": status
        }

    def set_model(self, model: str):
        """
        Change Claude model.

        Available models:
        - claude-sonnet-4-5-20250929 (default, balanced)
        - claude-opus-4-5-20250929 (most capable)
        - claude-haiku-3-5-20250919 (fastest, cheapest)
        """
        self.model = model
        logger.info(f"Chochmah model changed to {model}")

    def set_temperature(self, temperature: float):
        """
        Set temperature for response generation.

        Args:
            temperature: 0.0 (deterministic) to 1.0 (creative)

        Raises:
            ValueError: If temperature out of range
        """
        if not 0.0 <= temperature <= 1.0:
            raise ValueError(
                f"Temperature debe estar entre 0.0 y 1.0, got {temperature}"
            )

        self.temperature = temperature
        logger.info(f"Chochmah temperature set to {temperature}")
