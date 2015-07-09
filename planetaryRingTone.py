from music import *

################################################################################################
#This program generates a ringtone-like piece of music that takes the orbital speeds of planets#
#in ft/sec and maps them onto musical elements to create the piece.                            #
################################################################################################
score = Score("Planet Rock!", 300)
values = [47.89, 35.03, 29.79, 24.13, 17.882, 13.06, 9.64, 6.81, 5.43, 4.74]
startTime = 0.0

minValue = min(values)
maxValue = max(values)
whole_tone = [0, 2, 4, 6, 8, 10]

#map those values onto pitches in the major scale between C1 and C5
#add pitches to phrases using eigth notes as values
pitches = []
dur     = []

for i in values:
   pitch = mapScale(i, minValue, maxValue, C4, C6, PENTATONIC_SCALE)
   pitches.append(pitch)
   dur.append(EN)

phrase1 = Phrase(0.0)
phrase2 = Phrase(0.0)
phrase3 = Phrase(0.0)

phrase1.addNoteList(pitches, dur)
Mod.repeat(phrase1, 4)
Mod.shuffle(phrase1)

phrase2 = phrase1.copy()
Mod.elongate(phrase2, 2.0)
Mod.repeat(phrase2, 2)
Mod.shuffle(phrase2)

phrase3 = phrase1.copy()
Mod.elongate(phrase3, 5.0)
Mod.shuffle(phrase3)


guitar1 = Part(XYLOPHONE, 0)
guitar2 = Part(BELLS, 1)
bass =    Part(MARIMBA, 2)
Mod.repeat(guitar1, 1)

guitar1.addPhrase(phrase1)
guitar2.addPhrase(phrase2)
bass.addPhrase(phrase3)




score.addPart(guitar1)
score.addPart(guitar2)
score.addPart(bass)



Mod.repeat(score, 4)

#Uncomment below to write the output to a midi file called "Planetary ring tone.mid"
#Write.midi(score, "Planetary ring tone.mid")
Play.midi(score)

