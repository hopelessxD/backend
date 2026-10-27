from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction:
    amount: float
    type: str
    timestamp: datetime = datetime.now()