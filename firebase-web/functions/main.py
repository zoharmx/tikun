# Firebase Cloud Functions for Tikun Olam System
import os
import sys
from firebase_functions import https_fn
from firebase_admin import initialize_app

# Add parent directory to path to import sefirot modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.sefirot.keter import Keter
from src.sefirot.chochmah_gemini import ChochmahGemini
from src.sefirot.binah import Binah
from src.sefirot.chesed import Chesed
from src.sefirot.gevurah import Gevurah
from src.sefirot.tiferet import Tiferet
from src.sefirot.netzach import Netzach
from src.sefirot.hod import Hod
from src.sefirot.yesod import Yesod
from src.sefirot.malchut import Malchut

# Initialize Firebase Admin
initialize_app()


@https_fn.on_call()
def process_action(req: https_fn.CallableRequest) -> dict:
    """
    Process an action through all 10 Sefirot

    Args:
        req: Request with data containing:
            - action: str - The action to evaluate
            - context: str - Context for the action
            - expected_outcome: str - Expected outcome

    Returns:
        dict: Results from all 10 Sefirot
    """
    # Get input data
    data = req.data
    action = data.get('action')
    context = data.get('context', '')
    expected_outcome = data.get('expected_outcome', '')

    if not action:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
            message='Action is required'
        )

    try:
        # Initialize all Sefirot
        keter = Keter(use_llm_scoring=True)
        chochmah = ChochmahGemini()
        binah = Binah()
        chesed = Chesed()
        gevurah = Gevurah()
        tiferet = Tiferet()
        netzach = Netzach()
        hod = Hod()
        yesod = Yesod()
        malchut = Malchut()

        results = {}

        # 1. KETER - Divine Will & Alignment
        action_input = {
            'action': action,
            'context': context,
            'expected_outcome': expected_outcome
        }
        results['keter'] = keter.process(action_input)

        # 2. CHOCHMAH - Wisdom & Understanding
        results['chochmah'] = chochmah.process({
            'query': action,
            'context': context
        })

        # 3. BINAH - Contextual Analysis
        results['binah'] = binah.process({
            'understanding': results['chochmah']['understanding'],
            'analysis': results['chochmah']['analysis'],
            'action': action
        })

        # 4. CHESED - Loving-Kindness
        results['chesed'] = chesed.process({
            'stakeholders': results['binah']['stakeholders'],
            'first_order_effects': results['binah']['first_order_effects'],
            'second_order_effects': results['binah']['second_order_effects'],
            'systemic_risks': results['binah']['systemic_risks'],
            'ethical_considerations': results['binah']['ethical_considerations'],
            'action': action
        })

        # 5. GEVURAH - Severity & Boundaries
        results['gevurah'] = gevurah.process({
            'giving_opportunities': results['chesed']['giving_opportunities'],
            'beneficiaries': results['chesed']['beneficiaries'],
            'generous_actions': results['chesed']['generous_actions'],
            'compassion_score': results['chesed']['compassion_score'],
            'expansion_potential': results['chesed']['expansion_potential'],
            'limits_needed': results['chesed']['limits_needed'],
            'action': action
        })

        # 6. TIFERET - Beauty & Harmony
        results['tiferet'] = tiferet.process({
            'chesed_output': results['chesed'],
            'gevurah_output': results['gevurah'],
            'action': action
        })

        # 7. NETZACH - Victory & Persistence
        results['netzach'] = netzach.process({
            'balanced_decision': results['tiferet']['balanced_decision'],
            'implementation_path': results['tiferet']['implementation_path'],
            'harmony_score': results['tiferet']['harmony_score'],
            'beauty_score': results['tiferet']['beauty_score'],
            'action': action
        })

        # 8. HOD - Splendor & Structure
        results['hod'] = hod.process({
            'persistence_strategy': results['netzach']['persistence_strategy'],
            'obstacles_identified': results['netzach']['obstacles_identified'],
            'victory_conditions': results['netzach']['victory_conditions'],
            'endurance_plan': results['netzach']['endurance_plan'],
            'momentum_mechanisms': results['netzach']['momentum_mechanisms'],
            'sustainability_score': results['netzach']['sustainability_score'],
            'action': action
        })

        # 9. YESOD - Foundation & Connection
        results['yesod'] = yesod.process({
            'structured_plan': results['hod']['structured_plan'],
            'communication_strategy': results['hod']['communication_strategy'],
            'metrics_framework': results['hod']['metrics_framework'],
            'documentation': results['hod']['documentation'],
            'stakeholder_messages': results['hod']['stakeholder_messages'],
            'precision_score': results['hod']['precision_score'],
            'clarity_score': results['hod']['clarity_score'],
            'action': action
        })

        # 10. MALCHUT - Kingdom & Manifestation
        results['malchut'] = malchut.process({
            'foundation_assessment': results['yesod']['foundation_assessment'],
            'reality_connection': results['yesod']['reality_connection'],
            'first_concrete_steps': results['yesod']['first_concrete_steps'],
            'resource_requirements': results['yesod']['resource_requirements'],
            'stakeholder_alignment': results['yesod']['stakeholder_alignment'],
            'manifestation_readiness': results['yesod']['manifestation_readiness'],
            'ready_to_manifest': results['yesod']['ready_to_manifest'],
            'action': action
        })

        # Return all results
        return {
            'success': True,
            'results': results,
            'summary': {
                'keter_alignment': results['keter']['alignment_score'],
                'chochmah_confidence': results['chochmah']['confidence_level'],
                'tiferet_harmony': results['tiferet']['harmony_score'],
                'yesod_readiness': results['yesod']['manifestation_readiness'],
                'malchut_completion': results['malchut']['completion_percentage'],
                'ready_to_manifest': results['malchut']['manifestation_complete']
            }
        }

    except Exception as e:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INTERNAL,
            message=f'Error processing action: {str(e)}'
        )


@https_fn.on_call()
def process_sefira(req: https_fn.CallableRequest) -> dict:
    """
    Process a single Sefira

    Args:
        req: Request with data containing:
            - sefira: str - Name of the Sefira to process
            - input_data: dict - Input data for the Sefira

    Returns:
        dict: Result from the Sefira
    """
    data = req.data
    sefira_name = data.get('sefira')
    input_data = data.get('input_data', {})

    if not sefira_name:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
            message='Sefira name is required'
        )

    try:
        # Map sefira names to classes
        sefirot_map = {
            'keter': Keter(use_llm_scoring=True),
            'chochmah': ChochmahGemini(),
            'binah': Binah(),
            'chesed': Chesed(),
            'gevurah': Gevurah(),
            'tiferet': Tiferet(),
            'netzach': Netzach(),
            'hod': Hod(),
            'yesod': Yesod(),
            'malchut': Malchut()
        }

        sefira = sefirot_map.get(sefira_name.lower())
        if not sefira:
            raise https_fn.HttpsError(
                code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
                message=f'Unknown Sefira: {sefira_name}'
            )

        result = sefira.process(input_data)

        return {
            'success': True,
            'sefira': sefira_name,
            'result': result
        }

    except Exception as e:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INTERNAL,
            message=f'Error processing Sefira {sefira_name}: {str(e)}'
        )


@https_fn.on_call()
def validate_sefira_alignment(req: https_fn.CallableRequest) -> dict:
    """
    Validate alignment of a Sefira

    Args:
        req: Request with data containing:
            - sefira: str - Name of the Sefira to validate

    Returns:
        dict: Validation results
    """
    data = req.data
    sefira_name = data.get('sefira')

    if not sefira_name:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
            message='Sefira name is required'
        )

    try:
        sefirot_map = {
            'keter': Keter(use_llm_scoring=True),
            'chochmah': ChochmahGemini(),
            'binah': Binah(),
            'chesed': Chesed(),
            'gevurah': Gevurah(),
            'tiferet': Tiferet(),
            'netzach': Netzach(),
            'hod': Hod(),
            'yesod': Yesod(),
            'malchut': Malchut()
        }

        sefira = sefirot_map.get(sefira_name.lower())
        if not sefira:
            raise https_fn.HttpsError(
                code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
                message=f'Unknown Sefira: {sefira_name}'
            )

        validation = sefira.validate_alignment()

        return {
            'success': True,
            'sefira': sefira_name,
            'validation': validation
        }

    except Exception as e:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INTERNAL,
            message=f'Error validating Sefira {sefira_name}: {str(e)}'
        )
