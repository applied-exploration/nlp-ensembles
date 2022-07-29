from typing import List, Optional, Union

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator

from type import DataType

from .base import Transformation


class SKLearnTransformation(Transformation):

    model: BaseEstimator
    inputTypes = [DataType.NpArray, DataType.Series, DataType.List]
    outputType = DataType.NpArray

    def __init__(self, sklearn_transformation: BaseEstimator):
        super().__init__()
        self.model = sklearn_transformation
        self.id += "-" + sklearn_transformation.__class__.__name__

    def fit(
        self,
        dataset: Union[List, np.ndarray],
        labels: Optional[Union[List, np.ndarray]],
    ) -> None:
        self.model.fit(dataset)

    def predict(self, dataset: Union[List, np.ndarray]) -> np.ndarray:
        return self.model.transform(dataset)

    def is_fitted(self) -> bool:
        if self.model is None:
            return False
        # source: https://stackoverflow.com/a/63839394
        attrs = [
            v for v in vars(self.model) if v.endswith("_") and not v.startswith("__")
        ]
        return len(attrs) != 0
