"""
Tests para Chochmah (Sabiduría)
"""

import pytest
import os
from unittest.mock import Mock, patch, MagicMock
from src.sefirot.chochmah import Chochmah
from src.core.sefirotic_base import SefiraPosition


class TestChochmahInitialization:
    """Tests de inicialización"""

    def test_initialization_with_api_key(self):
        """Test que Chochmah se inicializa correctamente con API key"""
        chochmah = Chochmah(api_key="test-key")

        assert chochmah.position == SefiraPosition.CHOCHMAH
        assert chochmah.name == "CHOCHMAH"
        assert chochmah.api_key == "test-key"
        assert chochmah.client is not None

    def test_initialization_without_api_key(self):
        """Test que Chochmah maneja ausencia de API key"""
        # Asegurar que no hay API key en environment
        with patch.dict(os.environ, {}, clear=True):
            chochmah = Chochmah()

            assert chochmah.client is None
            assert chochmah.api_key is None

    def test_initialization_from_env(self):
        """Test que Chochmah lee API key de environment"""
        with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "env-key"}):
            chochmah = Chochmah()

            assert chochmah.api_key == "env-key"

    def test_default_configuration(self):
        """Test configuración por defecto"""
        chochmah = Chochmah(api_key="test-key")

        assert chochmah.model == "claude-sonnet-4-5-20250929"
        assert chochmah.max_tokens == 4096
        assert chochmah.temperature == 1.0
        assert chochmah.uncertainty_acknowledgments == 0
        assert chochmah.high_confidence_responses == 0


class TestChochmahProcessing:
    """Tests de procesamiento"""

    @patch('src.sefirot.chochmah.Anthropic')
    def test_process_with_valid_query(self, mock_anthropic):
        """Test procesamiento con query válido"""
        # Mock de la respuesta de Claude
        mock_response = Mock()
        mock_response.content = [Mock(text="""
COMPRENSIÓN:
Entiendo que necesitas analizar este problema.

ANÁLISIS:
El razonamiento profundo muestra que hay múltiples factores.

INSIGHTS:
El patrón fundamental es la interdependencia.

INCERTIDUMBRES:
No tengo suficiente información sobre el contexto histórico.

RECOMENDACIÓN:
Proceder con análisis contextual en Binah.
        """)]

        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        chochmah = Chochmah(api_key="test-key")
        chochmah.client = mock_client

        input_data = {
            'query': '¿Cómo podemos reducir el sufrimiento en el mundo?',
            'context': 'Considerando limitaciones actuales de tecnología',
            'objective': 'Maximizar Tikún Olam'
        }

        result = chochmah.process(input_data)

        assert result['processing_successful'] is True
        assert 'understanding' in result
        assert 'analysis' in result
        assert 'insights' in result
        assert 'uncertainties' in result
        assert 'recommendation' in result
        assert 'confidence_level' in result
        assert 0.0 <= result['confidence_level'] <= 1.0

    def test_process_without_client(self):
        """Test que process falla sin cliente configurado"""
        chochmah = Chochmah()  # Sin API key

        with pytest.raises(RuntimeError, match="no tiene cliente de Anthropic"):
            chochmah.process({'query': 'test'})

    def test_process_invalid_input_type(self):
        """Test que process valida tipo de input"""
        chochmah = Chochmah(api_key="test-key")

        with pytest.raises(TypeError, match="requiere input_data como dict"):
            chochmah.process("invalid string")

    def test_process_missing_query(self):
        """Test que process requiere 'query'"""
        chochmah = Chochmah(api_key="test-key")

        with pytest.raises(ValueError, match="Input debe contener 'query'"):
            chochmah.process({'context': 'some context'})

    @patch('src.sefirot.chochmah.Anthropic')
    def test_process_handles_api_error(self, mock_anthropic):
        """Test manejo de errores de API"""
        from anthropic import APIError

        mock_client = MagicMock()
        mock_client.messages.create.side_effect = APIError("API Error")
        mock_anthropic.return_value = mock_client

        chochmah = Chochmah(api_key="test-key")
        chochmah.client = mock_client

        result = chochmah.process({'query': 'test query'})

        assert result['processing_successful'] is False
        assert result['error_type'] == 'api_error'
        assert 'error' in result


class TestChochmahParsing:
    """Tests de parsing de respuestas"""

    def test_parse_structured_response(self):
        """Test parsing de respuesta bien estructurada"""
        chochmah = Chochmah(api_key="test-key")

        response = """
COMPRENSIÓN:
Este es el entendimiento.

ANÁLISIS:
Este es el análisis profundo.

INSIGHTS:
Estos son los insights.

INCERTIDUMBRES:
Estas son las incertidumbres.

RECOMENDACIÓN:
Esta es la recomendación.
        """

        parsed = chochmah._parse_response(response)

        assert "entendimiento" in parsed['understanding'].lower()
        assert "análisis profundo" in parsed['analysis'].lower()
        assert "insights" in parsed['insights'].lower()
        assert "incertidumbres" in parsed['uncertainties'].lower()
        assert "recomendación" in parsed['recommendation'].lower()

    def test_parse_unstructured_response(self):
        """Test parsing de respuesta sin estructura"""
        chochmah = Chochmah(api_key="test-key")

        response = "Esta es una respuesta sin estructura clara."

        parsed = chochmah._parse_response(response)

        # Debería poner todo en 'analysis'
        assert "respuesta sin estructura" in parsed['analysis'].lower()

    def test_parse_english_response(self):
        """Test parsing de respuesta en inglés"""
        chochmah = Chochmah(api_key="test-key")

        response = """
UNDERSTANDING:
This is the understanding.

ANALYSIS:
This is the deep analysis.

INSIGHTS:
These are the insights.

UNCERTAINTIES:
These are the uncertainties.

RECOMMENDATION:
This is the recommendation.
        """

        parsed = chochmah._parse_response(response)

        assert "understanding" in parsed['understanding'].lower()
        assert "analysis" in parsed['analysis'].lower()
        assert "insights" in parsed['insights'].lower()
        assert "uncertainties" in parsed['uncertainties'].lower()
        assert "recommendation" in parsed['recommendation'].lower()


class TestChochmahConfidence:
    """Tests de evaluación de confianza"""

    def test_high_confidence_response(self):
        """Test respuesta de alta confianza"""
        chochmah = Chochmah(api_key="test-key")

        parsed = {
            'understanding': 'Claro entendimiento',
            'analysis': 'Análisis definitivo sin ambigüedades',
            'insights': 'Insights claros y precisos con más de 100 caracteres de contenido detallado',
            'uncertainties': '',
            'recommendation': 'Recomendación clara'
        }

        confidence = chochmah._evaluate_confidence(parsed)

        assert confidence > 0.8  # Alta confianza

    def test_low_confidence_response(self):
        """Test respuesta de baja confianza"""
        chochmah = Chochmah(api_key="test-key")

        parsed = {
            'understanding': 'No estoy seguro',
            'analysis': 'Posiblemente podría ser esto, tal vez aquello, no está claro',
            'insights': 'Difícil determinar',
            'uncertainties': 'Hay mucha incertidumbre aquí. Necesito más información para dar una respuesta precisa.',
            'recommendation': 'Tal vez solicitar más datos'
        }

        confidence = chochmah._evaluate_confidence(parsed)

        assert confidence < 0.5  # Baja confianza


class TestChochmahAlignment:
    """Tests de validación de alineamiento"""

    def test_validate_alignment_no_activations(self):
        """Test validación sin activaciones"""
        chochmah = Chochmah(api_key="test-key")

        validation = chochmah.validate_alignment()

        assert validation['is_aligned'] is True
        assert validation['epistemic_humility_score'] == 1.0

    @patch('src.sefirot.chochmah.Anthropic')
    def test_validate_alignment_with_humility(self, mock_anthropic):
        """Test validación con reconocimiento de incertidumbre"""
        # Setup mock
        mock_response = Mock()
        mock_response.content = [Mock(text="""
COMPRENSIÓN: Entiendo el problema.
ANÁLISIS: Análisis completo.
INSIGHTS: Algunos insights.
INCERTIDUMBRES: No estoy seguro de varios aspectos. Necesito más información.
RECOMENDACIÓN: Proceder con cautela.
        """)]

        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        chochmah = Chochmah(api_key="test-key")
        chochmah.client = mock_client

        # Procesar varias queries
        for _ in range(5):
            chochmah.process({'query': 'test query'})

        validation = chochmah.validate_alignment()

        assert validation['is_aligned'] is True
        assert validation['uncertainty_acknowledgments'] > 0
        assert validation['epistemic_humility_ratio'] > 0

    @patch('src.sefirot.chochmah.Anthropic')
    def test_validate_alignment_excessive_confidence(self, mock_anthropic):
        """Test detección de exceso de confianza"""
        # Mock siempre respuestas muy confiadas
        mock_response = Mock()
        mock_response.content = [Mock(text="""
COMPRENSIÓN: Comprensión perfecta.
ANÁLISIS: Análisis definitivo con certeza total sobre todos los aspectos relevantes.
INSIGHTS: Insights absolutamente claros sin ninguna ambigüedad posible.
INCERTIDUMBRES:
RECOMENDACIÓN: Proceder inmediatamente con total confianza.
        """)]

        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        chochmah = Chochmah(api_key="test-key")
        chochmah.client = mock_client

        # Procesar muchas queries sin reconocer incertidumbre
        for _ in range(10):
            chochmah.process({'query': 'test query'})

        validation = chochmah.validate_alignment()

        # Debería detectar falta de humildad
        assert validation['epistemic_humility_ratio'] == 0
        # Puede o no estar alineada dependiendo del umbral


class TestChochmahConfiguration:
    """Tests de configuración"""

    def test_set_model(self):
        """Test cambio de modelo"""
        chochmah = Chochmah(api_key="test-key")

        chochmah.set_model("claude-opus-4-5-20250929")

        assert chochmah.model == "claude-opus-4-5-20250929"

    def test_set_temperature(self):
        """Test ajuste de temperatura"""
        chochmah = Chochmah(api_key="test-key")

        chochmah.set_temperature(0.5)

        assert chochmah.temperature == 0.5

    def test_set_temperature_invalid(self):
        """Test validación de temperatura"""
        chochmah = Chochmah(api_key="test-key")

        with pytest.raises(ValueError, match="debe estar entre 0.0 y 1.0"):
            chochmah.set_temperature(1.5)

        with pytest.raises(ValueError, match="debe estar entre 0.0 y 1.0"):
            chochmah.set_temperature(-0.1)


class TestChochmahMetrics:
    """Tests de métricas"""

    @patch('src.sefirot.chochmah.Anthropic')
    def test_metrics_tracking(self, mock_anthropic):
        """Test que las métricas se rastrean correctamente"""
        mock_response = Mock()
        mock_response.content = [Mock(text="ANÁLISIS: Test")]

        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        chochmah = Chochmah(api_key="test-key")
        chochmah.client = mock_client

        # Procesar algunas queries
        chochmah.process({'query': 'query 1'})
        chochmah.process({'query': 'query 2'})

        metrics = chochmah.get_metrics()

        assert metrics['sefira'] == 'CHOCHMAH'
        assert metrics['activations'] == 2
        assert metrics['total_processing_time'] > 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
