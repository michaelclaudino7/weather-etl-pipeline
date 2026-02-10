import requests
import logging
from datetime import datetime
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class WeatherExtractor:
    def __init__(self, base_url: str, latitude: float, longitude: float, params: list):
        self.base_url = base_url
        self.latitude = latitude
        self.longitude = longitude
        self.params = params
        
    def extract(self) -> Optional[Dict[str, Any]]:
        try:
            logger.info(f"Iniciando extração de dados para coordenadas: {self.latitude}, {self.longitude}")
            
            query_params = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "current": ",".join(self.params)
            }
            
            response = requests.get(self.base_url, params=query_params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            data['extraction_timestamp'] = datetime.now().isoformat()
            data['extraction_success'] = True
            
            logger.info("Extração concluída com sucesso")
            return data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro na requisição da API: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Erro inesperado na extração: {str(e)}")
            return None