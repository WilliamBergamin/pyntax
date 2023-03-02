import logging
from .grammar_suggestion import grammar_suggestion

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

__all__ = ["grammar_suggestion"]
