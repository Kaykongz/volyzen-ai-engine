from abc import ABC, abstractmethod
from typing import List, Dict, Any

class ExchangeAdapter(ABC):
    """
    Abstract Base Class for all exchange adapters.
    It defines the common interface for interacting with different exchanges.
    """

    def __init__(self, api_key: str, api_secret: str, sandbox: bool = True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.sandbox = sandbox
        self.client = self._create_client()

    @abstractmethod
    def _create_client(self) -> Any:
        """Create and return the exchange-specific client."""
        pass

    @abstractmethod
    async def get_markets(self) -> List[Dict[str, Any]]:
        """Fetch all available markets."""
        pass

    @abstractmethod
    async def get_ohlcv(self, symbol: str, timeframe: str, since: int = None, limit: int = None) -> List[list]:
        """Fetch OHLCV data for a given symbol."""
        pass
    
    @abstractmethod
    async def create_order(self, symbol: str, type: str, side: str, amount: float, price: float = None, params: dict = {}):
        """Create a new order."""
        pass

    @abstractmethod
    async def get_balances(self) -> Dict[str, Any]:
        """Fetch account balances."""
        pass
