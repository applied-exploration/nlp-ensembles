from typing import List
from model.average_ensemble import AverageEnsembleModel
from model.huggingface import HuggingfaceModel

from model.sklearn import SKLearnModel
from data.dataloader import load_data
from config import (
    global_preprocess_config,
    huggingface_config,
    sklearn_config,
    GlobalPreprocessConfig,
)
from model.base import BaseModel
from model.average_ensemble import AverageEnsembleModel
from training.train import train_model


def run_pipeline(preprocess_config: GlobalPreprocessConfig, model: BaseModel):
    train_dataset, val_dataset, test_dataset = load_data(
        "data/original", preprocess_config
    )

    train_model(model, train_dataset, val_dataset)
    model.predict(test_dataset)


if __name__ == "__main__":
    run_pipeline(
        global_preprocess_config,
        AverageEnsembleModel(
            [
                SKLearnModel(config=sklearn_config),
                SKLearnModel(config=sklearn_config),
                # HuggingfaceModel(config=huggingface_config),
            ]
        ),
    )
