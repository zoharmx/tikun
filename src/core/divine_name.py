"""
Sistema YHVH y Gematría
Implementa cálculos numéricos basados en letras hebreas y nombre divino.
"""

from typing import Dict, List
from enum import Enum


class HebrewLetter(Enum):
    """Letras hebreas con sus valores numéricos (Gematría)"""
    ALEF = 1
    BET = 2
    GIMEL = 3
    DALET = 4
    HEY = 5
    VAV = 6
    ZAYIN = 7
    CHET = 8
    TET = 9
    YUD = 10
    KAF = 20
    LAMED = 30
    MEM = 40
    NUN = 50
    SAMECH = 60
    AYIN = 70
    PEY = 80
    TZADIK = 90
    KUF = 100
    RESH = 200
    SHIN = 300
    TAV = 400


class DivineName:
    """
    Representa el Tetragrámaton (יהוה) y sus propiedades.
    Valor numérico: 26 (10 + 5 + 6 + 5)
    """
    
    YUD = 10    # י - Punto semilla, inicio
    HEY_1 = 5   # ה - Expansión, procesamiento
    VAV = 6     # ו - Conexión, función
    HEY_2 = 5   # ה - Manifestación, output
    
    TOTAL = YUD + HEY_1 + VAV + HEY_2  # 26
    
    @classmethod
    def calculate_gematria(cls, text: str) -> int:
        """
        Calcula el valor numérico (gematría) de un texto.
        Por ahora, simplificado. Puede expandirse con tabla completa.
        """
        # Implementación simplificada
        # TODO: Expandir con tabla completa de conversión
        return sum(ord(char) for char in text) % 1000
    
    @classmethod
    def is_harmonious_with_26(cls, value: int) -> bool:
        """
        Verifica si un valor está en armonía con el número 26.
        Armonía definida como: divisible por 26, o suma de dígitos = 26, etc.
        """
        if value == 0:
            return False
        
        # Divisible por 26
        if value % 26 == 0:
            return True
        
        # Suma de dígitos recursiva llega a 26
        digit_sum = sum(int(d) for d in str(value))
        if digit_sum == 26:
            return True
        
        # Múltiplo de 13 (mitad de 26, también significativo)
        if value % 13 == 0:
            return True
            
        return False
    
    @classmethod
    def apply_yhvh_cycle(cls, input_value: float) -> Dict[str, float]:
        """
        Aplica el ciclo YHVH como función recursiva:
        Yud (input) → Hey (expansión) → Vav (conexión) → Hey (output)
        
        El output se convierte en nuevo input del siguiente ciclo.
        """
        yud = input_value
        hey_1 = yud * 1.618  # Proporción áurea (phi) - expansión natural
        vav = (hey_1 + yud) / 2  # Conexión/promedio
        hey_2 = vav * 0.9  # Manifestación con ligera contracción (Tzimtzum)
        
        return {
            "yud": yud,
            "hey_1": hey_1,
            "vav": vav,
            "hey_2": hey_2,
            "next_cycle_input": hey_2  # Output se vuelve input
        }


# Constantes del sistema
DIVINE_VALUE = DivineName.TOTAL  # 26
PHI = 1.618033988749  # Proporción áurea (presente en naturaleza)
CYCLES_IN_MACHZOR = 19  # Ciclo Metónico
MACHZORIM_IN_EPOCH = 316  # Total de ciclos hasta año 6000
YEARS_IN_EPOCH = 6000  # Ciclo completo