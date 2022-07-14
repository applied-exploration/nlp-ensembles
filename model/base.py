from type import BaseConfig
from abc import ABC
import pandas as pd
from typing import Optional
from runner.store import Store


class Block(ABC):
    id: str


class Model(Block):

    config: BaseConfig

    def __init__(self, id: str, config: BaseConfig):
        raise NotImplementedError()

    def preload(self):
        pass

    def fit(self, dataset: pd.DataFrame, labels: Optional[pd.Series]) -> None:
        raise NotImplementedError()

    def predict(self, dataset: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError()

    def is_fitted(self) -> bool:
        raise NotImplementedError()


class DataSource(Block):

    id: str

    def __init__(self, id: str):
        self.id = id

    def deplate(self, store: Store) -> pd.DataFrame:
        return store.get_data(self.id)

    def preload(self):
        pass
