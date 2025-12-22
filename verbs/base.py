from dataclasses import dataclass, asdict, field
from typing import Any, Dict, List, Optional, Union
from .types import *

import json


class Application:
    """Container for a sequence of Verbs."""

    def __init__(self, verbs: Optional[List[Verb]] = None):
        self.verbs: List[Verb] = verbs or []

    def add(self, verb: Verb) -> None:
        if not isinstance(verb, Verb):
            raise TypeError("verb must be a Verb instance")
        self.verbs.append(verb)

    def to_dict(self) -> List[Dict[str, Any]]:
        return [v.to_dict() for v in self.verbs]

    def to_json(self, **kwargs: Any) -> str:
        return json.dumps(self.to_dict(), **kwargs)

    def total(self) -> int:
        return len(self.verbs)
