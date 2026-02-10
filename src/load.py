import pandas as pd
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class WeatherLoader:
    def __init__(self, raw_path: str = "data/raw", processed_path: str = "data/processed"):
        self.raw_path = Path(raw_path)
        self.processed_path = Path(processed_path)
        
        self.raw_path.mkdir(parents=True, exist_ok=True)
        self.processed_path.mkdir(parents=True, exist_ok=True)
    
    def save_raw_data(self, data: Dict[str, Any], format: str = "json") -> bool:
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"weather_raw_{timestamp}.{format}"
            filepath = self.raw_path / filename
            
            logger.info(f"Salvando dados brutos em: {filepath}")
            
            if format == "json":
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            else:
                logger.error(f"Formato não suportado: {format}")
                return False
            
            logger.info("Dados brutos salvos com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao salvar dados brutos: {str(e)}")
            return False
    
    def save_processed_data(self, df: pd.DataFrame, format: str = "csv") -> bool:
        try:
            if df is None or df.empty:
                logger.warning("DataFrame vazio, nada para salvar")
                return False
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"weather_processed_{timestamp}.{format}"
            filepath = self.processed_path / filename
            
            logger.info(f"Salvando dados processados em: {filepath}")
            
            if format == "csv":
                df.to_csv(filepath, index=False, encoding='utf-8')
            elif format == "json":
                df.to_json(filepath, orient='records', indent=2, force_ascii=False)
            else:
                logger.error(f"Formato não suportado: {format}")
                return False
            
            logger.info(f"Dados processados salvos com sucesso. Total de registros: {len(df)}")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao salvar dados processados: {str(e)}")
            return False
    
    def append_to_historical(self, df: pd.DataFrame, filename: str = "weather_historical.csv") -> bool:
        try:
            filepath = self.processed_path / filename
            
            logger.info(f"Adicionando dados ao histórico: {filepath}")
            
            # Verifica se o arquivo já existe
            if filepath.exists():
                # Lê dados existentes e concatena
                existing_df = pd.read_csv(filepath)
                combined_df = pd.concat([existing_df, df], ignore_index=True)
                combined_df.to_csv(filepath, index=False, encoding='utf-8')
                logger.info(f"Dados adicionados ao histórico. Total de registros: {len(combined_df)}")
            else:
                # Cria novo arquivo
                df.to_csv(filepath, index=False, encoding='utf-8')
                logger.info(f"Arquivo histórico criado com {len(df)} registros")
            
            return True
            
        except Exception as e:
            logger.error(f"Erro ao adicionar ao histórico: {str(e)}")
            return False