from funktsioonid import *

esmaspäev = ['Kõrgem matemaatika', 'Matemaatiline maailmapilt']
teisipäev = ['Programmeerimine', 'Arvuti arhitektuur ja riistvara', 'Kõrgem matemaatika']
kolmapäev = ['Matemaatiline maailmapilt', 'Sissejuhatus erialasse']
neljapäev = ['Programmeerimine', 'Sissejuhatus erialasse', 'Kõrgem matemaatika']
reede = ['Matemaatiline maailmapilt', 'Arvuti arhitektuur ja riistvara']

elp = ["loeng","loeng"]
tlp = ["loeng","loeng","praktikum"]
klp = ["praktikum","praktikum"]
nlp = ["praktikum", "loeng", "praktikum"]
rlp = ["praktikum","loeng"]

ise = easygui.ynbox("Kas soovid ise õppida?","Jah""Ei","Enne mängu")


if ise == false:
    skill = {"Programmeerimine":0,"Matemaatiline maailmapilt":0,"Sissejuhatus erialasse":0, "Kõrgem matemaatika":0,"Arvuti arhitektuur ja riistvara":0}
    day0()
    day1(teisipäev,tlp, skill)
    day1(kolmapäev,klp, skill)
    day1(neljapäev,nlp, skill)
    day1(reede,rlp, skill)
    
#ISE ÕPPIDES:
# Saab valida sugu, vastavalt soole saad õppejõude võrgutada
# saab valida kuidas ülikooli astunud, erinevad võimalused annavad erinevaid boonuseid
# Saab teha loengutes märkmeid enda jaoks, loengus saab teha märkmeid enne kt saab vaadata märkmeid
# Ainetele registreerimine
# Saab valida mis kell ärgata tahab järgmisel päeval ja kui ei ärka õigel ajal siis magab loengu maha
#Arvuti õpib:
# Saab valida sugu, vastavalt soole saad õppejõude võrgutada
# saab valida kuidas ülikooli astunud, erinevad võimalused annavad erinevaid boonuseid
# Arvuti kalkuleerib kontrolltööst läbisaamise protsendi
# Saab valida mis kell ärgata tahab järgmisel päeval ja kui ei ärka õigel ajal siis magab loengu maha