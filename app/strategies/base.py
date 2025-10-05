from abc import ABC, abstractmethod
import pandas as pd
from typing import Dict, Any

class Strategy(ABC):
    """
    Abstract Base Class for all trading strategies.
    """
    def __init__(self, parameters: Dict[str, Any]):
        self.parameters = parameters
        self.validate_parameters()

    @abstractmethod
    def validate_parameters(self):
        """Validate the strategy-specific parameters."""
        pass

    @abstractmethod
    def generate_signals(self, market_data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate trading signals based on market data.

        Args:
            market_data (pd.DataFrame): DataFrame with OHLCV data. 
                                        Must contain 'Open', 'High', 'Low', 'Close', 'Volume'.

        Returns:
            pd.DataFrame: A DataFrame with a 'signal' column.
                          1 for Long, -1 for Short, 0 for No Signal.
        """
        pass
