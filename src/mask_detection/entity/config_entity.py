from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    


#entity 
@dataclass
class model_training_config:
    root_dir: Path
    updated_model_path: Path
    trained_model_mod: Path
    img_size: int
    data_yaml: Path
    mode: str
    model: str
    epochs: int
    plots: bool
    task: str
    
    