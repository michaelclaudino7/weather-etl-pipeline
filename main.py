import yaml
import logging
from pathlib import Path
from datetime import datetime

from src.extract import WeatherExtractor
from src.transform import WeatherTransformer
from src.load import WeatherLoader


def setup_logging(log_level: str = "INFO", log_format: str = None):
    if log_format is None:
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / f"etl_{datetime.now().strftime('%Y%m%d')}.log"
    
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format=log_format,
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )


def load_config(config_path: str = "config/config.yaml") -> dict:
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        return config
    except Exception as e:
        logging.error(f"Erro ao carregar configuração: {str(e)}")
        raise


def run_pipeline():
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("=" * 50)
        logger.info("Iniciando Weather ETL Pipeline")
        logger.info("=" * 50)
        
        logger.info("Carregando configurações...")
        config = load_config()
        
        logger.info("Fase 1: EXTRACT")
        extractor = WeatherExtractor(
            base_url=config['api']['base_url'],
            latitude=config['api']['latitude'],
            longitude=config['api']['longitude'],
            params=config['api']['params']
        )
        
        raw_data = extractor.extract()
        
        if not raw_data:
            logger.error("Falha na extração de dados. Abortando pipeline.")
            return False
        
        logger.info("Fase 2: TRANSFORM")
        transformer = WeatherTransformer()
        processed_data = transformer.transform(raw_data)
        
        if processed_data is None or processed_data.empty:
            logger.error("Falha na transformação de dados. Abortando pipeline.")
            return False
        
        logger.info("Fase 3: LOAD")
        loader = WeatherLoader()
        
        raw_saved = loader.save_raw_data(
            raw_data, 
            format=config['output']['raw_format']
        )
        
        processed_saved = loader.save_processed_data(
            processed_data,
            format=config['output']['processed_format']
        )
        
        historical_saved = loader.append_to_historical(processed_data)
        
        if raw_saved and processed_saved and historical_saved:
            logger.info("=" * 50)
            logger.info("Pipeline concluído com SUCESSO!")
            logger.info(f"Registros processados: {len(processed_data)}")
            logger.info("=" * 50)
            return True
        else:
            logger.warning("Pipeline concluído com avisos. Verifique os logs.")
            return False
            
    except Exception as e:
        logger.error(f"Erro crítico no pipeline: {str(e)}", exc_info=True)
        return False


if __name__ == "__main__":
    config = load_config()
    setup_logging(
        log_level=config['logging']['level'],
        log_format=config['logging']['format']
    )
    
    success = run_pipeline()
    
    exit(0 if success else 1)