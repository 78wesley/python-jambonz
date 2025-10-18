from jambonz_verbs import *

app = Application()


# app.add_verb(VerbSay(""))
# app.add_verb(VerbGather(input="speech", actionHook="/gather-result"))
# app.add_verb(VerbPlay("https://example.com/music.mp3"))
# app.add_verb(VerbHangup())

# app.add_verb(VerbAlert(""))
# app.add_verb(VerbAlert("abc"))

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

app.add_verb(VerbConfig())

print(app.to_json())
print(app.to_dict())
print(app.total_tasks())
