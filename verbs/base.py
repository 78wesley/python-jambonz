import json
from typing import Any, Dict, List, Optional
from .types import *

__all__ = [
    "Application",
    "Verb",
    "Alert",
    "Answer",
    "SipDecline",
    "SipRequest",
    "SipRefer",
    "Awsoptions",
    "Googleoptions",
    "Deepgramoptions",
    "Formatting",
    "Nuanceoptions",
    "Vad",
    "Azureoptions",
    "Assemblyaioptions",
    "Customoptions",
    "Turndetection",
    "Prompttemplates",
    "Openaioptions",
    "Cobaltoptions",
    "Houndifyoptions",
    "Nvidiaoptions",
    "SmAudioeventsconfig",
    "SmSpeakerdiarizationconfig",
    "SmPuctuationoverrides",
    "SmTranscriptfilteringconfig",
    "SmAudiofilteringconfig",
    "SmTranscriptionconfig",
    "SmTranslationconfig",
    "Speechmaticsoptions",
    "Ibmoptions",
    "Verbiooptions",
    "Elevenlabsoptions",
    "Sonioxstorage",
    "Sonioxoptions",
    "Recognizer",
    "Synthesizer",
    "Ttsstream",
    "Auth",
    "Bidirectionalaudio",
    "Listenoptions",
    "Bargein",
    "Fillernoise",
    "Transcribeoptions",
    "Actionhookdelayaction",
    "Recordoptions",
    "Amdtimers",
    "Amd",
    "Config",
    "Dub",
    "Dequeue",
    "Enqueue",
    "Leave",
    "Hangup",
    "Play",
    "Say",
    "Gather",
    "Record",
    "Conference",
    "Transcribe",
    "Listen",
    "Dial",
    "Queryinput",
    "Dialogflow",
    "Dtmf",
    "Lexintent",
    "Lex",
    "Stream",
    "Llm",
    "Mcpserver",
    "Message",
    "Pause",
    "Rasa",
    "Redirect",
    "Dialfrom",
    "Target",
    "RestDial",
    "Tag",
    "Resourcereference",
    "Resource",
    "Turndetectionpipeline",
    "Pipeline",
]


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

    def to_readable(self) -> str:
        lines = []
        for i, verb in enumerate(self.to_dict(), start=1):
            lines.append(
                f"{i}. {verb.get('verb', '')}: { {k: v for k, v in verb.items() if k != 'verb'} }"
            )
        return "\n".join(lines)

    def total(self) -> int:
        return len(self.verbs)
