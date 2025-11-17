"""
Clase base para todas las Sefirot.
Define la interfaz común y comportamientos compartidos.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from enum import Enum
from loguru import logger
import time


class SefiraPosition(Enum):
    """Posición de cada Sefirá en el Árbol"""
    KETER = 1      # Corona
    CHOCHMAH = 2   # Sabiduría
    BINAH = 3      # Entendimiento
    CHESED = 4     # Misericordia
    GEVURAH = 5    # Juicio/Severidad
    TIFERET = 6    # Belleza/Armonía
    NETZACH = 7    # Victoria/Eternidad
    HOD = 8        # Esplendor/Gloria
    YESOD = 9      # Fundamento
    MALCHUT = 10   # Reino/Manifestación


class SefiraBase(ABC):
    """
    Clase base abstracta para todas las Sefirot.
    
    Cada Sefirá es un módulo con:
    - Función específica en el sistema
    - Límites y restricciones
    - Canales de comunicación con otras Sefirot
    - Métricas de desempeño y alineamiento
    """
    
    def __init__(self, position: SefiraPosition):
        self.position = position
        self.name = position.name
        self.activation_count = 0
        self.total_processing_time = 0.0
        self.connected_sefirot: Dict[str, 'SefiraBase'] = {}
        self.history: List[Dict[str, Any]] = []
        
        logger.info(f"Sefirá {self.name} inicializada en posición {position.value}")
    
    @abstractmethod
    def process(self, input_data: Any) -> Any:
        """
        Función principal de procesamiento de cada Sefirá.
        Debe ser implementada por cada Sefirá específica.
        """
        pass
    
    @abstractmethod
    def validate_alignment(self) -> Dict[str, Any]:
        """
        Valida que la Sefirá esté operando dentro de sus límites correctos.
        Retorna métricas de alineamiento.
        """
        pass
    
    def connect_to(self, other_sefira: 'SefiraBase', channel_name: str):
        """Establece canal de comunicación con otra Sefirá"""
        self.connected_sefirot[channel_name] = other_sefira
        logger.debug(f"{self.name} conectada a {other_sefira.name} vía canal '{channel_name}'")
    
    def send_to(self, channel_name: str, data: Any) -> Any:
        """Envía datos a otra Sefirá a través de canal establecido"""
        if channel_name not in self.connected_sefirot:
            raise ValueError(f"Canal '{channel_name}' no existe en {self.name}")
        
        target_sefira = self.connected_sefirot[channel_name]
        logger.debug(f"{self.name} → {target_sefira.name}: {type(data).__name__}")
        
        return target_sefira.process(data)
    
    def execute_with_tracking(self, input_data: Any) -> Any:
        """
        Ejecuta process() con tracking de métricas.
        Usado internamente para mantener estadísticas.
        """
        start_time = time.time()
        
        try:
            result = self.process(input_data)
            self.activation_count += 1
            elapsed = time.time() - start_time
            self.total_processing_time += elapsed
            
            # Guardar en historial
            self.history.append({
                "timestamp": time.time(),
                "input_type": type(input_data).__name__,
                "output_type": type(result).__name__,
                "processing_time": elapsed,
                "success": True
            })
            
            return result
            
        except Exception as e:
            elapsed = time.time() - start_time
            self.history.append({
                "timestamp": time.time(),
                "input_type": type(input_data).__name__,
                "error": str(e),
                "processing_time": elapsed,
                "success": False
            })
            logger.error(f"Error en {self.name}: {e}")
            raise
    
    def get_metrics(self) -> Dict[str, Any]:
        """Retorna métricas de desempeño de la Sefirá"""
        avg_time = (
            self.total_processing_time / self.activation_count 
            if self.activation_count > 0 
            else 0
        )
        
        successful_activations = sum(
            1 for h in self.history if h.get("success", False)
        )
        
        success_rate = (
            successful_activations / len(self.history) 
            if self.history 
            else 0
        )
        
        return {
            "sefira": self.name,
            "position": self.position.value,
            "activations": self.activation_count,
            "total_processing_time": self.total_processing_time,
            "average_processing_time": avg_time,
            "success_rate": success_rate,
            "connected_channels": list(self.connected_sefirot.keys())
        }
    
    def __repr__(self) -> str:
        return f"<Sefirá {self.name} (Posición {self.position.value})>"