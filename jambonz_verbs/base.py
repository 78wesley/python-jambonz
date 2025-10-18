from dataclasses import dataclass, asdict, field
from typing import Any, Dict, List, Optional, Union
from .typ import (
    BargeIn,
    FillerNoise,
    Record,
    Transcribe,
    DtmfHook,
    ConfirmHook,
    Amd,
    TargetPhone,
    TargetSip,
    TargetUser,
    TargetTeams,
    Recognizer,
    Synthesizer,
    Listen,
    TTS,
    ActionHookDelayAction,
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

    def total_tasks(self) -> int:
        return len(self.verbs)


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
    listen: Optional[Listen] = None
    notifyEvents: Optional[bool] = None
    onHoldMusic: Optional[str] = None
    recognizer: Optional[Recognizer] = None
    reset: Optional[Union[str, List[str]]] = None
    record: Optional[Record] = None
    transcribe: Optional[Transcribe] = None
    sipRequestWithinDialogHook: Optional[Union[str, Dict[str, Any]]] = None
    synthesizer: Optional[Synthesizer] = None


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
class VerbDial(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/dial)."""

    verb: str = field(init=False, default="dial")
    # Required
    target: List[TargetPhone | TargetSip | TargetUser | TargetTeams] = field(
        default_factory=list
    )

    # Optional
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


@dataclass
class VerbDialogflow(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/Dialogflow)."""

    verb: str = field(init=False, default="Dialogflow")
    # Required
    credentials: str
    lang: str
    project: str

    # Optional
    actionHook: Optional[str] = None
    bargein: Optional[bool] = None
    eventHook: Optional[str] = None
    noInputEvent: Optional[str] = None
    noInputTimeout: Optional[float] = None
    passDtmfAsTextInput: Optional[bool] = None
    thinkingMusic: Optional[str] = None
    tts: Optional[TTS] = None
    welcomeEvent: Optional[str] = None
    welcomeEventParams: Optional[Dict] = field(default_factory=dict)


@dataclass
class VerbDtmf(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/dtmf)."""

    verb: str = field(init=False, default="dtmf")
    # Required
    dtmf: str

    # Optional
    duration: Optional[str] = 500


@dataclass
class Verbdub(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/dub)."""

    verb: str = field(init=False, default="dub")
    # Required
    action: str
    track: str

    # Optional
    gain: Optional[str] = None
    loop: Optional[bool] = None
    play: Optional[str] = None
    say: Optional[str] = None


@dataclass
class VerbEnqueue(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/enqueue)."""

    verb: str = field(init=False, default="enqueue")
    # Required
    name: str

    # Optional
    actionHook: Optional[str] = None
    priority: Optional[int] = 999
    waitHook: Optional[str] = None


@dataclass
class VerbGather(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/gather)."""

    verb: str = field(init=False, default="gather")
    # Required
    actionHook: str

    # Optional
    actionHookDelayAction: Optional[ActionHookDelayAction] = None
    bargein: Optional[bool] = None
    dtmfBargein: Optional[bool] = None
    fillerNoise: Optional[FillerNoise] = None
    finishOnKey: Optional[str] = None
    input: Optional[List[str]] = field(default_factory=lambda: ["digits"])
    interDigitTimeout: Optional[int] = None
    listenDuringPrompt: Optional[bool] = True
    maxDigits: Optional[int] = None
    minBargeinWordCount: Optional[int] = 1
    minDigits: Optional[int] = 1
    numDigits: Optional[int] = None
    partialResultHook: Optional[str] = None
    play: Optional[Dict[str, Any]] = None
    recognizer: Optional[Dict[str, Any]] = None
    say: Optional[Dict[str, Any]] = None


@dataclass
class VerbHangup(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/hangup)."""

    verb: str = field(init=False, default="hangup")
    headers: Optional[Dict] = None


@dataclass
class VerbLeave(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/leave)."""

    verb: str = field(init=False, default="leave")


@dataclass
class VerbListen(Verb, Listen):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/listen)."""

    verb: str = field(init=False, default="listen")


@dataclass
class VerbPause(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/pause)."""

    verb: str = field(init=False, default="pause")
    length: Optional[int] = None


@dataclass
class VerbPlay(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/play)."""

    verb: str = field(init=False, default="play")

    # Required
    url: str

    # Optional
    actionHook: Optional[str] = None
    earlyMedia: Optional[bool] = False
    loop: Optional[int] = 1
    seekOffset: Optional[int] = None
    timeoutSecs: Optional[int] = None


@dataclass
class VerbRasa(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/rasa)."""

    verb: str = field(init=False, default="rasa")

    # Required
    url: str

    # Optional
    actionHook: Optional[str] = None
    eventhook: Optional[str] = None
    promt: Optional[str] = None
    recognizer: Optional[Recognizer] = None
    tts: Optional[TTS] = None


@dataclass
class VerbRedirect(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/redirect)."""

    verb: str = field(init=False, default="redirect")
    actionHook: str


@dataclass
class VerbSay(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/say)."""

    verb: str = field(init=False, default="say")

    # Optional
    earlyMedia: Optional[bool] = None
    loop: Optional[int] = False
    stream: Optional[bool] = None
    synthesizer: Optional[Synthesizer] = None
    text: Optional[str] = None


@dataclass
class VerbSipDecline(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/sipdecline)."""

    verb: str = field(init=False, default="sip:decline")

    # Required
    status: int

    # Optional
    headers: Optional[Dict] = None
    reason: Optional[str] = None


@dataclass
class VerbSipRefer(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/siprefer)."""

    verb: str = field(init=False, default="sip:refer")
    # Required
    referTo: int
    # Optional
    reason: Optional[str] = None
    eventHook: Optional[str] = None
    headers: Optional[Dict] = None
    referredBy: Optional[str] = None


@dataclass
class VerbSipRequest(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/siprequest)."""

    verb: str = field(init=False, default="sip:request")

    # Required
    method: str

    # Optional
    actionHook: Optional[str] = None
    body: Optional[str] = None
    headers: Optional[Dict] = None


@dataclass
class VerbTag(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/tag)."""

    verb: str = field(init=False, default="tag")
    data: Dict


@dataclass
class VerbTranscribe(Verb):
    """Read the docs [here](https://docs.jambonz.org/verbs/verbs/transcribe)."""

    verb: str = field(init=False, default="transcribe")
    transcriptionHook: str
    recognizer: Optional[Recognizer] = None
