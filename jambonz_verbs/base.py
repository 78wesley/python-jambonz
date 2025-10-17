from dataclasses import dataclass, asdict, field
from typing import Any, Dict, List, Optional, Union
from .typ import (
    BargeIn,
    FillerNoise,
    Record,
    Transcribe,
    DtmfHook,
    ConfirmHook,
    Target,
    Amd,
)
import json


@dataclass
class Verb:
    """Jambonz Verb base class."""

    verb: str = field(init=False)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class Application:
    """Container for a sequence of Verbs with JSON serialization."""

    def __init__(self, verbs: Optional[List[Verb]] = None):
        self.verbs: List[Verb] = verbs or []

    def add_verb(self, verb: Verb) -> None:
        if not isinstance(verb, Verb):
            raise TypeError("verb must be a Verb instance")
        self.verbs.append(verb)

    def to_dict(self) -> List[Dict[str, Any]]:
        return [v.to_dict() for v in self.verbs]

    def to_json(self, **kwargs: Any) -> str:
        """Serialize verbs to JSON. Accepts all kwargs that json.dumps supports."""
        return json.dumps(self.to_dict(), **kwargs)


@dataclass
class VerbAlert(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/alert)."""

    verb: str = field(init=False, default="alert")
    message: str


@dataclass
class VerbAnswer(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/answer)."""

    verb: str = field(init=False, default="answer")


@dataclass
class VerbConference(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/conference)."""

    verb: str = field(init=False, default="conference")
    # Required
    name: str
    # Optional
    actionHook: Optional[str] = None
    beep: bool = False
    endConferenceOnExit: bool = False
    enterHook: Optional[str] = None
    joinMuted: bool = False
    maxParticipants: Optional[int] = None
    memberTag: Optional[str] = None
    speakOnlyTo: Optional[str] = None
    startConferenceOnEnter: bool = True
    statusHook: Optional[str] = None
    statusEvents: List[str] = field(default_factory=list)
    waitHook: Optional[str] = None


@dataclass
class VerbConfig(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/config)."""

    verb: str = field(init=False, default="config")
    # Optional top-level fields
    amd: Optional[bool] = None
    actionHookDelayAction: Optional[Dict[str, Any]] = None
    bargeIn: Optional[BargeIn] = None
    boostAudioSignal: Optional[Union[str, int]] = None
    fillerNoise: Optional[FillerNoise] = None
    listen: Optional[Dict[str, Any]] = None
    notifyEvents: Optional[bool] = None
    onHoldMusic: Optional[str] = None
    recognizer: Optional[Dict[str, Any]] = None
    reset: Optional[Union[str, List[str]]] = None
    record: Optional[Record] = None
    transcribe: Optional[Transcribe] = None
    sipRequestWithinDialogHook: Optional[Union[str, Dict[str, Any]]] = None
    synthesizer: Optional[Dict[str, Any]] = None


@dataclass
class VerbDequeue(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/dequeue)."""

    verb: str = field(init=False, default="dequeue")

    # Required
    name: str

    # Optional
    callSid: Optional[str] = None
    actionHook: Optional[str] = None
    beep: bool = False
    timeout: Optional[int] = None


@dataclass
class VerbDial:
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/dial)."""

    verb: str = "dial"
    actionHook: Optional[str] = None
    amd: Optional[Amd] = None
    anchorMedia: Optional[bool] = False
    answerOnBridge: Optional[bool] = False
    boostAudioSignal: Optional[Union[str, int]] = None
    callerId: Optional[str] = None
    confirmHook: Optional[ConfirmHook] = None
    dialMusic: Optional[str] = None
    dtmfCapture: Optional[List[str]] = None
    dtmfHook: Optional[DtmfHook] = None
    dub: Optional[Dict] = None
    exitMediaPath: Optional[bool] = False
    forwardPAI: Optional[bool] = True
    headers: Optional[Dict[str, str]] = None
    listen: Optional[Dict] = None
    referHook: Optional[str] = None
    timeLimit: Optional[int] = None
    timeout: Optional[int] = 60
    transcribe: Optional[Dict] = None
    target: List[Target] = field(default_factory=list)
