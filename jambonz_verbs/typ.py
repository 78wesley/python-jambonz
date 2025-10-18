from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from enum import Enum


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
    startDelaySecs: int


@dataclass
class Record:
    action: str
    siprecServerURL: str
    recordingID: Optional[str] = None


@dataclass
class Vad:
    enable: bool
    mode: int
    voiceMs: int


@dataclass
class Recognizer:
    vendor: str
    transcriptionHook: str
    altLanguages: Optional[list] = None
    asrDtmfTerminationDigit: Optional[str] = None
    asrTimeout: Optional[int] = None
    azureServiceEndpoint: Optional[str] = None
    diarization: Optional[bool] = None
    diarizationMaxSpeakers: Optional[int] = None
    diarizationMinSpeakers: Optional[int] = None
    enhancedModel: Optional[bool] = None
    filterMethod: Optional[str] = None
    hints: Optional[list] = None
    hintsBoost: Optional[int] = None
    identifyChannels: Optional[bool] = None
    initialSpeechTimeoutMs: Optional[int] = None
    interactionType: Optional[type] = None
    interim: Optional[str] = None
    language: Optional[bool] = None
    languageModelName: Optional[str] = None
    minConfidence: Optional[str] = None
    model: Optional[int] = None
    naicsCode: Optional[str] = None
    outputFormat: Optional[int] = None
    profanityFilter: Optional[str] = None
    profanityOption: Optional[bool] = None
    punctuation: Optional[str] = None
    requestSnr: Optional[bool] = None
    separateRecognitionPerChannel: Optional[bool] = None
    singleUtterance: Optional[bool] = None
    vad: Optional[str] = None
    vocabularyFilterName: Optional[str] = None
    vocabularyName: Optional[str] = None


@dataclass
class Transcribe:
    enable: bool
    transcriptionHook: str
    recognizer: Optional[Recognizer] = None


@dataclass
class DtmfHook:
    url: str
    method: Optional[str] = "POST"


@dataclass
class ConfirmHook:
    url: str
    method: Optional[str] = "POST"


@dataclass
class Auth:
    username: Optional[str] = None
    password: Optional[str] = None


@dataclass
class TargetPhone:
    type: str = field(init=False, default="phone")
    number: str
    confirmHook: Optional[str] = None
    trunk: Optional[str] = None
    proxy: Optional[str] = None


@dataclass
class TargetSip:
    type: str = field(init=False, default="sip")
    sipUri: str
    confirmHook: Optional[str] = None
    auth: Optional[Auth] = None
    proxy: Optional[Auth] = None


@dataclass
class TargetUser:
    type: str = field(init=False, default="user")
    name: str
    confirmHook: Optional[str] = None
    proxy: Optional[str] = None


@dataclass
class TargetTeams:
    type: str = field(init=False, default="teams")
    number: str
    tenant: Optional[str] = None
    voicemail: Optional[bool] = None
    proxy: Optional[bool] = None


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
    timers: Optional[Timers] = None
    recognizer: Optional[Recognizer] = None


@dataclass
class Synthesizer:
    vendor: str
    voice: str
    gender: Optional[str] = None
    engine: Optional[str] = None
    label: Optional[str] = None
    language: Optional[str] = None
    options: Optional[Dict] = None


@dataclass
class WsAuth:
    username: str
    password: str


@dataclass
class BidirectionalAudio:
    enabled: Optional[bool] = True
    sampleRate: Optional[int] = None
    streaming: Optional[bool] = False


@dataclass
class Listen:
    actionHook: str
    url: str
    finishOnKey: Optional[str] = None
    maxLength: Optional[int] = None
    metadata: Optional[Dict] = None
    mixType: Optional[str] = "mono"
    passDtmf: Optional[bool] = False
    playBeep: Optional[bool] = False
    sampleRate: Optional[int] = 8000
    timeout: Optional[int] = None
    transcribe: Optional[Transcribe] = None
    wsAuth: Optional[WsAuth] = None
    bidirectionalAudio: Optional[BidirectionalAudio] = None


@dataclass
class TTS:
    language: str
    gender: Optional[str] = None
    vendor: Optional[str] = None
    voice: Optional[str] = None


@dataclass
class ActionHookDelayAction:
    actions: list[Dict]  # Dict needs to be fully Verb objects
    enabled: bool
    noResponseGiveUpTimeout: Optional[int] = None
    noResponseTimeout: Optional[int] = 0
    retries: Optional[int] = 1
