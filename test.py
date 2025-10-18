from jambonz_verbs import *
from jambonz_verbs.typ import (
    TargetPhone,
    TargetSip,
    TargetUser,
    TargetTeams,
    Recognizer,
    Synthesizer,
    TTS,
    FillerNoise,
)

app = Application()

# VerbAlert
app.add(VerbAlert(message="Test alert message"))
app.add(VerbAlert(message="Another alert!"))


# VerbAnswer
app.add(VerbAnswer())

# VerbConference
app.add(VerbConference(name="ConfA"))
app.add(
    VerbConference(
        name="ConfB",
        beep=True,
        joinMuted=True,
        maxParticipants=10,
        statusEvents=["start", "end"],
    )
)

# VerbConfig
app.add(VerbConfig())
app.add(
    VerbConfig(
        notifyEvents=True,
        onHoldMusic="https://hold.com",
        recognizer=Recognizer(vendor="google", transcriptionHook="/hook"),
    )
)

# VerbDequeue
app.add(VerbDequeue(name="Queue1"))
app.add(VerbDequeue(name="Queue2", beep=True, timeout=30))

# VerbDial
app.add(VerbDial(target=[TargetPhone(number="1234567890")]))
app.add(
    VerbDial(
        target=[TargetSip(sipUri="sip:user@example.com")],
        timeout=10,
        answerOnBridge=True,
    )
)
app.add(
    VerbDial(
        target=[TargetUser(name="alice"), TargetTeams(number="teamsid")],
        callerId="999",
        forwardPAI=False,
    )
)

# VerbDialogflow
app.add(VerbDialogflow(credentials="creds", lang="en", project="proj"))
app.add(
    VerbDialogflow(
        credentials="c2",
        lang="fr",
        project="p2",
        tts=TTS(language="nl"),
        welcomeEventParams={"foo": "bar"},
    )
)

# VerbDtmf
app.add(VerbDtmf(dtmf="1234"))
app.add(VerbDtmf(dtmf="*#", duration="1000"))

# Verbdub
app.add(Verbdub(action="play", track="track1"))
app.add(Verbdub(action="say", track="track2", gain="5", loop=True, say="Hello!"))

# VerbEnqueue
app.add(VerbEnqueue(name="QueueA"))
app.add(VerbEnqueue(name="QueueB", priority=1, waitHook="/wait"))

# VerbGather
app.add(VerbGather(actionHook="/gather-result"))
app.add(
    VerbGather(
        actionHook="/gather2",
        input=["speech"],
        minDigits=2,
        maxDigits=5,
        fillerNoise=FillerNoise(enable=True, startDelaySecs=1, url="/abc"),
        play={"url": "https://audio"},
    )
)

# VerbHangup
app.add(VerbHangup())
app.add(VerbHangup(headers={"X-Reason": "test"}))

# VerbLeave
app.add(VerbLeave())

# VerbListen
app.add(VerbListen(actionHook="/hook", url="/url"))
app.add(VerbListen(actionHook="/hook", url="/url", metadata={"ABC": "DEF"}))

# VerbLLM
app.add(VerbLLM(model="abc", vendor="123"))

# VerbPause
app.add(VerbPause())
app.add(VerbPause(length=5))

# VerbPlay
app.add(VerbPlay(url="https://example.com/music.mp3"))
app.add(
    VerbPlay(url="https://audio.com/track.wav", loop=3, earlyMedia=True, timeoutSecs=10)
)

# VerbRasa
app.add(VerbRasa(url="https://rasa.example.com"))
app.add(
    VerbRasa(url="https://rasa2.com", promt="Say something", tts=TTS(language="nl"))
)

# VerbRedirect
app.add(VerbRedirect(actionHook="/redirect"))

# VerbSay
app.add(VerbSay(text="Hello world"))
app.add(
    VerbSay(
        text="Streamed",
        stream=True,
        loop=2,
        synthesizer=Synthesizer(vendor="abc", voice="female"),
    )
)

# VerbSipDecline
app.add(VerbSipDecline(status=486))
app.add(VerbSipDecline(status=603, reason="Busy", headers={"X-Reason": "busy"}))

# VerbSipRefer
app.add(VerbSipRefer(referTo=12345))
app.add(
    VerbSipRefer(referTo=67890, reason="test", eventHook="/event", referredBy="bob")
)

# VerbSipRequest
app.add(VerbSipRequest(method="INVITE"))
app.add(
    VerbSipRequest(method="BYE", actionHook="/bye", body="bye", headers={"X-Bye": "1"})
)

# VerbTag
app.add(VerbTag(data={"key": "value"}))
app.add(VerbTag(data={"foo": 123, "bar": [1, 2, 3]}))

# VerbTranscribe
app.add(VerbTranscribe(transcriptionHook="/transcribe"))
app.add(
    VerbTranscribe(
        transcriptionHook="/transcribe2",
        recognizer=Recognizer(
            vendor="google",
            transcriptionHook="/hook",
        ),
    )
)

# Custom Verbs
app.add(Verb(verb="customverb"))
app.add(Verb(verb="customverb", abc="def"))

app.add(VerbSay())


print(app.to_json(indent=4))
print(app.to_dict())
print(app.total())
