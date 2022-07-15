from configs.constants import Const
from blocks.models.base import Model
import pandas as pd
from type import BaseConfig
from utils.random import random_string
from typing import Optional


class Transformation(Model):
    def __init__(self, id: Optional[str] = None, config: BaseConfig = None):
        super().__init__()
        self.config = BaseConfig(force_fit=False) if config is None else config

    def load_remote(self):
        pass

    def fit(self, dataset: pd.DataFrame, labels: Optional[pd.Series]) -> None:
        pass

    def predict(self, dataset: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError()

    def is_fitted(self) -> bool:
        return True
