from verbs import *

app = Application()

# Alert
app.add(Alert(message="Test alert message"))
app.add(Alert(message="Another alert!", id="123"))


# Answer
app.add(Answer())

# Conference
app.add(Conference(name="ConfA"))
app.add(
    Conference(
        name="ConfB",
        beep=True,
        joinMuted=True,
        maxParticipants=10,
        statusEvents=["start", "end"],
    )
)

# Config
app.add(Config())
app.add(
    Config(
        notifyEvents=True,
        onHoldMusic="https://hold.com",
        recognizer=Recognizer(vendor="aws"),
    )
)

# Dequeue
app.add(Dequeue(name="Queue1"))
app.add(Dequeue(name="Queue2", beep=True, timeout=30))

# Dial
app.add(Dial(target=[Target(type="number", number="1234567890")]))
app.add(
    Dial(
        target=[Target(type="sipUri", sipUri="sip:user@example.com")],
        timeout=10,
        answerOnBridge=True,
    )
)
app.add(
    Dial(
        target=[Target(type="teams", number="1234567890")],
        callerId="999",
        forwardPAI=False,
    )
)
app.add(
    Dial(
        target=[Target(type="user", name="alice")],
        timeout=20,
    )
)


# Dialogflow
app.add(Dialogflow(credentials="creds", lang="en", project="proj"))
app.add(
    Dialogflow(
        credentials="c2",
        lang="fr",
        project="p2",
        tts=Synthesizer(vendor="aws", voice="jean"),
        welcomeEventParams={"foo": "bar"},
    )
)

# Dtmf
app.add(Dtmf(dtmf="1234"))
app.add(Dtmf(dtmf="*#", duration="1000"))

# Dub
app.add(Dub(action="play", track="track1"))
app.add(Dub(action="say", track="track2", gain="5", loop=True, say="Hello!"))

# Enqueue
app.add(Enqueue(name="QueueA"))
app.add(Enqueue(name="QueueB", priority=1, waitHook="/wait"))

# Gather
app.add(Gather(actionHook="/gather-result"))
app.add(
    Gather(
        actionHook="/gather2",
        input=["speech"],
        minDigits=2,
        maxDigits=5,
        fillerNoise=Fillernoise(enable=True, startDelaySecs=1, url="/abc"),
        play={"url": "https://audio"},
    )
)

# Hangup
app.add(Hangup())
app.add(Hangup(headers={"X-Reason": "test"}))

# Leave
app.add(Leave())

# Listen
app.add(Listen(actionHook="/hook", url="/url"))
app.add(Listen(actionHook="/hook", url="/url", metadata={"ABC": "DEF"}))

# Pause
app.add(Pause(length=5))

# Play
app.add(Play(url="https://example.com/music.mp3"))
app.add(
    Play(url="https://audio.com/track.wav", loop=3, earlyMedia=True, timeoutSecs=10)
)

# Rasa
app.add(Rasa(url="https://rasa.example.com"))
app.add(
    Rasa(
        url="https://rasa2.com",
        prompt="Say something",
        tts=Synthesizer(vendor="aws", language="nl"),
    )
)

# Redirect
app.add(Redirect(actionHook="/redirect"))

# Say
app.add(Say(text="Hello world"))
app.add(
    Say(
        text="Streamed",
        stream=True,
        loop=2,
        synthesizer=Synthesizer(vendor="abc", voice="female"),
    )
)

# SipDecline
app.add(SipDecline(status=486))
app.add(SipDecline(status=603, reason="Busy", headers={"X-Reason": "busy"}))

# SipRefer
app.add(SipRefer(referTo=12345))
app.add(SipRefer(referTo=67890, eventHook="/event", referredBy="bob"))

# SipRequest
app.add(SipRequest(method="INVITE"))
app.add(SipRequest(method="BYE", actionHook="/bye", body="bye", headers={"X-Bye": "1"}))

# VerbTag
app.add(Tag(data={"key": "value"}))
app.add(Tag(data={"foo": 123, "bar": [1, 2, 3]}))

# Transcribe
app.add(Transcribe(transcriptionHook="/transcribe"))
app.add(
    Transcribe(
        transcriptionHook="/transcribe2",
        recognizer=Recognizer(vendor="google"),
    )
)

# Custom Verbs
app.add(Verb(verb="customverb"))
app.add(Verb(verb="customverb", foo="bar", count=3))

# print(app.to_json(indent=4))
# print(app.to_dict())
print(app.to_readable())
# print("Total tasks:", app.total())
