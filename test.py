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
app.add_verb(VerbAlert(message="Test alert message"))
app.add_verb(VerbAlert(message="Another alert!"))

# VerbAnswer
app.add_verb(VerbAnswer())

# VerbConference
app.add_verb(VerbConference(name="ConfA"))
app.add_verb(
    VerbConference(
        name="ConfB",
        beep=True,
        joinMuted=True,
        maxParticipants=10,
        statusEvents=["start", "end"],
    )
)

# VerbConfig
app.add_verb(VerbConfig())
app.add_verb(
    VerbConfig(
        notifyEvents=True,
        onHoldMusic="https://hold.com",
        recognizer=Recognizer(vendor="google", transcriptionHook="/hook"),
    )
)

# VerbDequeue
app.add_verb(VerbDequeue(name="Queue1"))
app.add_verb(VerbDequeue(name="Queue2", beep=True, timeout=30))

# VerbDial
app.add_verb(VerbDial(target=[TargetPhone(number="1234567890")]))
app.add_verb(
    VerbDial(
        target=[TargetSip(sipUri="sip:user@example.com")],
        timeout=10,
        answerOnBridge=True,
    )
)
app.add_verb(
    VerbDial(
        target=[TargetUser(name="alice"), TargetTeams(number="teamsid")],
        callerId="999",
        forwardPAI=False,
    )
)

# VerbDialogflow
app.add_verb(VerbDialogflow(credentials="creds", lang="en", project="proj"))
app.add_verb(
    VerbDialogflow(
        credentials="c2",
        lang="fr",
        project="p2",
        tts=TTS(language="nl"),
        welcomeEventParams={"foo": "bar"},
    )
)

# VerbDtmf
app.add_verb(VerbDtmf(dtmf="1234"))
app.add_verb(VerbDtmf(dtmf="*#", duration="1000"))

# Verbdub
app.add_verb(Verbdub(action="play", track="track1"))
app.add_verb(Verbdub(action="say", track="track2", gain="5", loop=True, say="Hello!"))

# VerbEnqueue
app.add_verb(VerbEnqueue(name="QueueA"))
app.add_verb(VerbEnqueue(name="QueueB", priority=1, waitHook="/wait"))

# VerbGather
app.add_verb(VerbGather(actionHook="/gather-result"))
app.add_verb(
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
app.add_verb(VerbHangup())
app.add_verb(VerbHangup(headers={"X-Reason": "test"}))

# VerbLeave
app.add_verb(VerbLeave())

# VerbListen
app.add_verb(VerbListen(actionHook="/hook", url="/url"))

# VerbPause
app.add_verb(VerbPause())
app.add_verb(VerbPause(length=5))

# VerbPlay
app.add_verb(VerbPlay(url="https://example.com/music.mp3"))
app.add_verb(
    VerbPlay(url="https://audio.com/track.wav", loop=3, earlyMedia=True, timeoutSecs=10)
)

# VerbRasa
app.add_verb(VerbRasa(url="https://rasa.example.com"))
app.add_verb(
    VerbRasa(url="https://rasa2.com", promt="Say something", tts=TTS(language="nl"))
)

# VerbRedirect
app.add_verb(VerbRedirect(actionHook="/redirect"))

# VerbSay
app.add_verb(VerbSay(text="Hello world"))
app.add_verb(
    VerbSay(
        text="Streamed",
        stream=True,
        loop=2,
        synthesizer=Synthesizer(vendor="abc", voice="female"),
    )
)

# VerbSipDecline
app.add_verb(VerbSipDecline(status=486))
app.add_verb(VerbSipDecline(status=603, reason="Busy", headers={"X-Reason": "busy"}))

# VerbSipRefer
app.add_verb(VerbSipRefer(referTo=12345))
app.add_verb(
    VerbSipRefer(referTo=67890, reason="test", eventHook="/event", referredBy="bob")
)

# VerbSipRequest
app.add_verb(VerbSipRequest(method="INVITE"))
app.add_verb(
    VerbSipRequest(method="BYE", actionHook="/bye", body="bye", headers={"X-Bye": "1"})
)

# VerbTag
app.add_verb(VerbTag(data={"key": "value"}))
app.add_verb(VerbTag(data={"foo": 123, "bar": [1, 2, 3]}))

# VerbTranscribe
app.add_verb(VerbTranscribe(transcriptionHook="/transcribe"))
app.add_verb(
    VerbTranscribe(
        transcriptionHook="/transcribe2",
        recognizer=Recognizer(
            vendor="google",
            transcriptionHook="/hook",
        ),
    )
)

print(app.to_json())
print(app.to_dict())
print(app.total_tasks())
