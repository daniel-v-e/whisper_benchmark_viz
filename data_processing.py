"""Data processing functions for the benchmarking project."""
import math
from dataclasses import dataclass
from typing import List

import numpy as np


@dataclass
class PricePerformanceArgs:
    """Dataclass for the price/performance arguments."""
    performance_weight: float = 1


def convert_time_to_seconds(time: str) -> float:
    """Convert a time string in the format [h]:mm:ss.000 to seconds."""
    minutes, seconds, milliseconds = map(
        float, time.split(":")[-2:] + time.split(".")[-1:]
    )
    return minutes * 60 + seconds + milliseconds / 1000


def convert_seconds_to_minutes(seconds: float) -> float:
    """Convert seconds to minutes."""
    return seconds / 60


def calculate_averages(data: List[List[List[str]]]) -> List[List[float]]:
    """Calculate the averages for the provided data."""
    data_seconds = [
        [[convert_time_to_seconds(time) for time in run] for run in comp]
        for comp in data
    ]

    averages_seconds = np.mean(data_seconds, axis=2)

    averages_time = [[avg for avg in comp] for comp in averages_seconds]

    return averages_time
