import pandas as pd
import logging
from typing import Dict, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class WeatherTransformer:
    def __init__(self):
        """Inicializa o transformador de dados."""
        self.weather_codes = {
            0: "Céu limpo",
            1: "Principalmente limpo",
            2: "Parcialmente nublado",
            3: "Nublado",
            45: "Neblina",
            48: "Neblina com geada",
            51: "Garoa leve",
            53: "Garoa moderada",
            55: "Garoa densa",
            61: "Chuva leve",
            63: "Chuva moderada",
            65: "Chuva forte",
            71: "Neve leve",
            73: "Neve moderada",
            75: "Neve forte",
            95: "Tempestade"
        }
    
    def transform(self, raw_data: Dict[str, Any]) -> Optional[pd.DataFrame]:
        try:
            logger.info("Iniciando transformação dos dados")
            
            if not raw_data or 'current' not in raw_data:
                logger.error("Dados brutos inválidos ou vazios")
                return None
            
            current = raw_data['current']
            
            transformed_data = {
                'timestamp': datetime.now().isoformat(),
                'latitude': raw_data.get('latitude'),
                'longitude': raw_data.get('longitude'),
                'temperature_celsius': current.get('temperature_2m'),
                'precipitation_mm': current.get('precipitation'),
                'weather_code': current.get('weather_code'),
                'weather_description': self.weather_codes.get(current.get('weather_code'), "Desconhecido"),
                'wind_speed_kmh': current.get('wind_speed_10m'),
                'relative_humidity': current.get('relative_humidity_2m'),
                'extraction_timestamp': raw_data.get('extraction_timestamp')
            }
            
            df = pd.DataFrame([transformed_data])
            
            logger.info(f"Transformação concluída. Registros processados: {len(df)}")
            return df
            
        except Exception as e:
            logger.error(f"Erro na transformação dos dados: {str(e)}")
            return None