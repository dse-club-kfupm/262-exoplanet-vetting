"""Submission entry point for 262-planet-hunters.

The committee calls predict(df) once on the hidden test set. df has the test
columns described in the README. Return 1 (confirmed planet) or 0 (false positive) per row,
in the same order as the rows of df.

predict.py may load a model saved in models/ or train one from data/train.csv
when it runs. Use only pandas, NumPy and scikit-learn.
"""

from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]
TRAIN_PATH = REPO_ROOT / "data" / "train.csv"


def predict(df: pd.DataFrame) -> list:
    # Baseline: always predict the most common class in the training data.
    # Replace this with your model.
    train = pd.read_csv(TRAIN_PATH)
    most_common = int(train["is_planet"].mode().iloc[0])
    return [most_common] * len(df)
