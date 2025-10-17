from jambonz_verbs import *

app = Application()


# say = Say("")
# gather = Gather(input="speech", actionHook="/gather-result")
# play = Play("https://example.com/music.mp3")
# hangup = Hangup()

# app.add_verb(say)
# app.add_verb(gather)
# app.add_verb(play)
# app.add_verb(hangup)

# app.add_verb(Alert(""))
# app.add_verb(Alert("abc"))

# app.add_verb(
#     Conference(
#         name="",
#         actionHook="",
#         beep=False,
#         enterHook="",
#         joinMuted=True,
#         maxParticipants=0,
#         memberTag="",
#         speakOnlyTo="",
#         endConferenceOnExit=False,
#         startConferenceOnEnter=True,
#         statusHook="",
#         statusEvents=[],
#         waitHook="",
#     )

# )

# app.add_verb(VerbConfig())

print(app.to_json())
print(app.to_dict())
