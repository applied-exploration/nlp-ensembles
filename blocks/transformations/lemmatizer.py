from .base import Transformation
from configs.constants import Const
import pandas as pd
from utils.spacy import get_spacy
from typing import List, Any
import spacy
from type import DataType


class Lemmatizer(Transformation):

    inputTypes = DataType.List
    outputType = DataType.List

    def __init__(self, remove_stopwords: bool) -> None:
        super().__init__()
        self.remove_stopwords = remove_stopwords

    def load(self, pipeline_id: str, execution_order: int) -> int:
        self.nlp = get_spacy()
        return super().load(pipeline_id, execution_order)

    def predict(self, dataset: List) -> List[str]:
        return [preprocess(item, self.remove_stopwords) for item in dataset]


def preprocess(tokens: List[Any], remove_stopwords: bool) -> str:
    return " ".join(
        [
            token.lemma_
            for token in tokens
            if (not token.is_stop if remove_stopwords else True)
            and not token.is_punct
            and token.lemma_ != " "
        ]
    )
