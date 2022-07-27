from dataclasses import dataclass
from enum import Enum
from sklearn.base import ClassifierMixin
from typing import Callable, List, Tuple

from transformers import TrainingArguments


Label = int
Probabilities = List[float]

PredsWithProbs = Tuple[Label, Probabilities]


class DataType(Enum):
    Any = "Any"
    NpArray = "ndarray"
    List = "List"
    PredictionsWithProbs = "PredictionsWithProbs"
    Series = "Series"
    Tensor = "Tensor"


EvaluatorId = str
Evaluator = Tuple[EvaluatorId, Callable]
Evaluators = List[Evaluator]


""" Model Configs """


@dataclass
class BaseConfig:
    force_fit: bool
    save: bool
    save_remote: bool


@dataclass
class HuggingfaceConfig(BaseConfig):
    pretrained_model: str
    user_name: str
    repo_name: str
    num_classes: int
    val_size: float
    training_args: TrainingArguments


@dataclass
class SKLearnConfig(BaseConfig):
    classifier: ClassifierMixin
    one_vs_rest: bool


""" Preprocessing Configs """


@dataclass
class PreprocessConfig:
    train_size: int
    val_size: int
    test_size: int
    input_col: str
    label_col: str


@dataclass
class PytorchConfig(BaseConfig):
    hidden_size: int
    output_size: int
    val_size: float
