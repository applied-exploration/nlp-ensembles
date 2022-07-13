import nltk
from nltk.corpus import wordnet as wn
from model.base import BaseModel
from typing import List, Any
import pandas as pd
import spacy
from type import BaseConfig
from configs.constants import Const
from collections import Counter
from urlextract import URLExtract


class StatisticAugmenter(BaseModel):
    def __init__(self, num_synonyms: int):
        self.config = BaseConfig(force_fit=False)

    def preload(self):
        nltk.download("wordnet")
        nltk.download("omw-1.4")
        self.nlp = spacy.load("en_core_web_lg")

    def fit(self, train_dataset: pd.DataFrame):
        pass

    def predict(self, test_dataset: pd.DataFrame) -> pd.DataFrame:
        test_dataset[Const.input_col] = test_dataset[Const.input_col].apply(
            lambda x: get_statistic([token.word for token in self.nlp(x)])
        )
        return test_dataset

    def is_fitted(self) -> bool:
        return True


def get_num_words(words: list[str]) -> int:
    return len(words)


def get_word_freq(words: list[str]) -> dict:
    return dict(Counter(words))


def get_outliers(word_freq: dict) -> dict:
    outliers = {}
    ratio = 0.1

    for word, freq in word_freq.items():
        if freq >= (len(word_freq.keys()) * ratio):
            outliers[word] = freq

    return outliers


def get_num_of_urls(string: str) -> int:
    extractor = URLExtract()
    urls = extractor.find_urls(string)
    return len(urls)


def get_non_alphanumeric(string: str) -> int:
    return len([char for char in string if not char.isalnum()])


def get_statistic(words: list[str]) -> str:
    words_fused = " ".join(words)
    num_words = get_num_words(words)
    word_freq = get_word_freq(words)
    outliers = get_outliers(word_freq)
    num_urls = get_num_of_urls(words_fused)
    num_non_alphanumeric = get_non_alphanumeric(words_fused)

    return " ".join([num_words, word_freq, outliers, num_urls, num_non_alphanumeric])
