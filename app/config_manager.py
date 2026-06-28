import json
from dataclasses import asdict
from pathlib import Path

from app.config import DownloadConfig

CONFIG_PATH = Path("settings.json")


def save_config(config: DownloadConfig):
    data = asdict(config)

    with open(CONFIG_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_config() -> DownloadConfig:
    if not CONFIG_PATH.exists():
        default_config = DownloadConfig()
        save_config(default_config)
        return default_config

    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    return DownloadConfig(**data)