import verbs as verb

app = verb.Application()

# VerbAlert
app.add(verb.Alert(message="Test alert message"))
app.add(verb.Alert(message="Another alert!"))


# VerbAnswer
app.add(verb.Answer())

# VerbConference
app.add(verb.Conference(name="ConfA"))
app.add(verb.Conference(
        name="ConfB",
        beep=True,
        joinMuted=True,
        maxParticipants=10,
        statusEvents=["start", "end"],
    )
)

# VerbConfig
app.add(verb.Config())
app.add(verb.Config(
        notifyEvents=True,
        onHoldMusic="https://hold.com",
        recognizer=verb.Recognizer(vendor="aws"),
    )
)

# VerbDequeue
app.add(verb.Dequeue(name="Queue1"))
app.add(verb.Dequeue(name="Queue2", beep=True, timeout=30))

# VerbDial
app.add(verb.Dial(target=[verb.Target(number="1234567890")]))
app.add(verb.Dial(
        target=[verb.Target(sipUri="sip:user@example.com")],
        timeout=10,
        answerOnBridge=True,
    )
)
app.add(verb.Dial(
        target=[verb.Target(name="alice"), verb.Target(number="teamsid")],
        callerId="999",
        forwardPAI=False,
    )
)

# VerbDialogflow
app.add(verb.Dialogflow(credentials="creds", lang="en", project="proj"))
app.add(verb.Dialogflow(
        credentials="c2",
        lang="fr",
        project="p2",
        tts=verb.Synthesizer(vendor="aws", voice="jean"),
        welcomeEventParams={"foo": "bar"},
    )
)

# VerbDtmf
app.add(verb.Dtmf(dtmf="1234"))
app.add(verb.Dtmf(dtmf="*#", duration="1000"))

# VerbDub
app.add(verb.Dub(action="play", track="track1"))
app.add(verb.Dub(action="say", track="track2", gain="5", loop=True, say="Hello!"))

# VerbEnqueue
app.add(verb.Enqueue(name="QueueA"))
app.add(verb.Enqueue(name="QueueB", priority=1, waitHook="/wait"))

# VerbGather
app.add(verb.Gather(actionHook="/gather-result"))
app.add(verb.Gather(
        actionHook="/gather2",
        input=["speech"],
        minDigits=2,
        maxDigits=5,
        fillerNoise=verb.Fillernoise(enable=True, startDelaySecs=1, url="/abc"),
        play={"url": "https://audio"},
    )
)

# VerbHangup
app.add(verb.Hangup())
app.add(verb.Hangup(headers={"X-Reason": "test"}))

# VerbLeave
app.add(verb.Leave())

# VerbListen
app.add(verb.Listen(actionHook="/hook", url="/url"))
app.add(verb.Listen(actionHook="/hook", url="/url", metadata={"ABC": "DEF"}))

# VerbLLM
app.add(verb.Llm(model="abc", vendor="123"))

# VerbPause
app.add(verb.Pause())
app.add(verb.Pause(length=5))

# VerbPlay
app.add(verb.Play(url="https://example.com/music.mp3"))
app.add(verb.Play(url="https://audio.com/track.wav", loop=3, earlyMedia=True, timeoutSecs=10)
)

# VerbRasa
app.add(verb.Rasa(url="https://rasa.example.com"))
app.add(verb.Rasa(url="https://rasa2.com", promt="Say something", tts=verb.Synthesizer(vendor="aws", language="nl"))
)

# VerbRedirect
app.add(verb.Redirect(actionHook="/redirect"))

# VerbSay
app.add(verb.Say(text="Hello world"))
app.add(verb.Say(
        text="Streamed",
        stream=True,
        loop=2,
        synthesizer=verb.Synthesizer(vendor="abc", voice="female"),
    )
)

# VerbSipDecline
app.add(verb.SipDecline(status=486))
app.add(verb.SipDecline(status=603, reason="Busy", headers={"X-Reason": "busy"}))

# VerbSipRefer
app.add(verb.SipRefer(referTo=12345))
app.add(verb.SipRefer(referTo=67890, reason="test", eventHook="/event", referredBy="bob")
)

# VerbSipRequest
app.add(verb.SipRequest(method="INVITE"))
app.add(verb.SipRequest(method="BYE", actionHook="/bye", body="bye", headers={"X-Bye": "1"})
)

# VerbTag
app.add(verb.Tag(data={"key": "value"}))
app.add(verb.Tag(data={"foo": 123, "bar": [1, 2, 3]}))

# VerbTranscribe
app.add(verb.Transcribe(transcriptionHook="/transcribe"))
app.add(verb.Transcribe(
        transcriptionHook="/transcribe2",
        recognizer=verb.Recognizer(
            vendor="google",
            transcriptionHook="/hook",
        ),
    )
)

# Custom Verbs
app.add(verb.Verb(verb="customverb"))
app.add(verb.Verb(verb="customverb", abc="def"))

app.add(verb.Say())


print(app.to_json(indent=4))
print(app.to_dict())
print(app.total())
