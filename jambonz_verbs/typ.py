from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class BargeIn:
    enable: Optional[bool] = None
    sticky: Optional[bool] = None
    actionHook: Optional[str] = None
    input: List[str] = field(default_factory=list)
    finishOnKey: Optional[str] = None
    numDigits: Optional[int] = None
    minDigits: Optional[int] = 1
    maxDigits: Optional[int] = None
    interDigitTimeout: Optional[int] = None


@dataclass
class FillerNoise:
    enable: bool
    url: str
    startDelaySecs: Optional[int] = None


@dataclass
class Record:
    action: str
    siprecServerURL: str
    recordingID: Optional[str] = None


@dataclass
class Transcribe:
    enable: bool
    transcriptionHook: str
    recognizer: Optional[Dict[str, Any]] = None  # TODO Recognizer


@dataclass
class DtmfHook:
    url: str
    method: Optional[str] = "POST"


@dataclass
class ConfirmHook:
    url: str
    method: Optional[str] = "POST"


@dataclass
class Target:
    type: str
    number: Optional[str] = None
    sipUri: Optional[str] = None
    name: Optional[str] = None
    tenant: Optional[str] = None
    voicemail: Optional[bool] = None
    trunk: Optional[str] = None
    auth: Optional[Dict[str, str]] = None
    proxy: Optional[str] = None


@dataclass
class Timers:
    decisionTimeoutMs: Optional[int] = 15000
    greetingCompletionTimeoutMs: Optional[int] = 2000
    noSpeechTimeoutMs: Optional[int] = 5000
    toneTimeoutMs: Optional[int] = 20000


@dataclass
class Amd:
    actionHook: str
    thresholdWordCount: Optional[int] = 9
    digitCount: Optional[int] = 0
    timers: Optional[Dict[str, int]] = None
