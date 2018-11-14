from funktsioonid import *

esmaspäev = ['Kõrgem matemaatika', 'Matemaatiline maailmapilt']
teisipäev = ['Programmeerimine', 'Arvuti arhitektuur ja riistvara', 'Kõrgem matemaatika']
kolmapäev = ['Matemaatiline maailmapilt', 'Sissejuhatus erialasse']
neljapäev = ['Programmeerimine', 'Sissejuhatus erialasse', 'Kõrgem matemaatika']
reede = ['Matemaatiline maailmapilt', 'Arvuti arhitektuur ja riistvara']

elp = ["loeng", "loeng"]
tlp = ["loeng", "loeng", "praktikum"]
klp = ["praktikum", "praktikum"]
nlp = ["praktikum", "loeng", "praktikum"]
rlp = ["praktikum", "loeng"]

essanädal = {"Programmeerimine":"Pythonis saab joonistada turtle teegiga", "Arvuti arhitektuur ja riistvara":"Kursuse saab läbida puhtalt Jurgasega"}




tutvustus = easygui.msgbox("""Tere tulemast Tartu ülikooli IT eriala simulatsiooni mängu. 
Mäng põhineb Oskari ja Risto kogemusel ja nägemusel ülikoolist. Mängus saad käia loengutes, teha märkmeid ja
kontrolltöid lahendada. On üritatud luua võimalikult reaalne simulatsioon ülikoolis käimisest.""", "Tutvustus", ok_button="Mängima!")

ise = easygui.ynbox("Kas soovid ise õppida?", "Enne mängu", ["Ise", "Arvuti"])

if not ise:
    skill = {"Programmeerimine": 0, "Matemaatiline maailmapilt": 0, "Sissejuhatus erialasse": 0,
             "Kõrgem matemaatika": 0, "Arvuti arhitektuur ja riistvara": 0}
    day0arvuti()
    day1arvuti(teisipäev, tlp, skill)
elif ise:
    skill = {"Programmeerimine": 0, "Matemaatiline maailmapilt": 0, "Sissejuhatus erialasse": 0,
             "Kõrgem matemaatika": 0, "Arvuti arhitektuur ja riistvara": 0}
    day0ise()
    day1ise(teisipäev, tlp, skill, essanädal)
    day1ise(kolmapäev, klp, skill, essanädal)
    day1ise(neljapäev, nlp, skill, essanädal)
    day1ise(reede,rlp,skill,essanädal)

# ISE ÕPPIDES:
# Saab valida sugu, vastavalt soole saad õppejõude võrgutada
# saab valida kuidas ülikooli astunud, erinevad võimalused annavad erinevaid boonuseid
# Saab teha loengutes märkmeid enda jaoks, loengus saab teha märkmeid enne kt saab vaadata märkmeid
# Ainetele registreerimine
# Saab valida mis kell ärgata tahab järgmisel päeval ja kui ei ärka õigel ajal siis magab loengu maha

# Arvuti õpib:
# Saab valida sugu, vastavalt soole saad õppejõude võrgutada
# saab valida kuidas ülikooli astunud, erinevad võimalused annavad erinevaid boonuseid
# Arvuti kalkuleerib kontrolltööst läbisaamise protsendi
# Saab valida mis kell ärgata tahab järgmisel päeval ja kui ei ärka õigel ajal siis magab loengu maha

# ÜLDINE:
# Esimene box on mängu kirjeldus, mis asi kus on.
