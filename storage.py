# storage.py
import json
import os
from typing import List, Any

DATA_DIR = "data"

def _path(nome_arquivo: str) -> str:
    os.makedirs(DATA_DIR, exist_ok=True)
    return os.path.join(DATA_DIR, nome_arquivo)

def load_list(nome_arquivo: str) -> List[Any]:
    path = _path(nome_arquivo)
    try:
        with open(path, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return dados if isinstance(dados, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_list(nome_arquivo: str, dados: List[Any]) -> None:
    path = _path(nome_arquivo)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
