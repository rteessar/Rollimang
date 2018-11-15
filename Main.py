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

ktplaan = ['Programmeerimine', 'Arvuti arhitektuur ja riistvara', 'Kõrgem matemaatika']

esimene_nädal= {"Arvuti arhitektuur ja riistvara": "Vähim aeg protsessori jaoks on üks takt.",
             "Arvuti arhitektuur ja riistvara2": "IBM projekteeris esimese PC arvuti.",
             "Sissejuhatus erialasse": "Esmakursuslaste konverents",
                "Programmeerimine": "Pythonis saab joonistada kujundeid Turtle teegiga"}

teine_nädal={"Programmeerimine": "Muutujaid, mille väärtust suurendatakse igal tsükli sammul ühe võrra, nimetatakse loenduriteks.",
             "Kõrgem matemaatika":"Suvalise n-järku ruutmaatriksi A korral kehtib AE = A, EA = A, kus E on n-järku ühikmaatriks.",
             "Matemaatiline maailmapilt":"Valem F on kehtestatav parajasti siis, kui tema eitus ¬F ei ole samaselt tõene.",
             "Arvuti arhitektuur ja riistvara":"Mälu, mille poole protsessor saab pöörduda oma siinide kaudu nimetatakse füüsiliseks mäluks",
             "Arvuti arhitektuur ja riistvara2":"Registrite suurus näitab ka mitme bitise protsessoriga on tegu",
             "Sissejuhatus erialasse":"Do it for the love of passion not for money!"}

kolmas_nädal={"Programmeerimine": "Meetodeid ei ole vaja kunagi import-ida.",
             "Kõrgem matemaatika":"Paarisfunktsioon on sümmeetriline y-telje suhtes. Paaritu funktsioon on sümmeetriline nullpunkti suhtes.",
             "Matemaatiline maailmapilt":"Tühjaks hulgaks ∅ nimetatakse hulka, mis ei sisalda ühtegi elementi.",
             "Arvuti arhitektuur ja riistvara":"Mälu ülesandeks on andmete ja programmide säilitamine.",
             "Arvuti arhitektuur ja riistvara2":"Moore'i seadus põhineb arvutiriistvara ajalool ning ütleb, et mikrokiibil olevate transistoride arv kahekordistub iga kahe aasta järel.",
             "Sissejuhatus erialasse":"Sinu eksamihinne on funktsioon ajast, mida sa panustad õpingutesse."}

neljas_nädal={"Programmeerimine": "Python paneb lokaalsete muutujate nimekirja kokku funktsiooni koodis leiduvate omistuslausete põhjal.",
             "Kõrgem matemaatika":"Piirväärtuse ühesus. Vaadeldavas protsessis saab funktsioonil olla ainult üks piirväärtus.",
             "Matemaatiline maailmapilt":"Hulkade A ja B ühendiks nimetatakse hulka A ∪ B, A ∪ B = {x | x ∈ A ∨ x ∈ B}.",
             "Arvuti arhitektuur ja riistvara":"Esimesena võeti pipeline kasutusele Intel 80486 protsessoris.",
             "Arvuti arhitektuur ja riistvara2":"SLAT (Second Level Address Translation).",
             "Sissejuhatus erialasse":"The first step: Don’t be anxious. Nature controls it all."}

tutvustus = easygui.msgbox("""Tere tulemast Tartu ülikooli IT eriala simulatsiooni mängu. 
Mäng põhineb Oskari ja Risto kogemusel ja nägemusel ülikoolist. Mängus saad käia loengutes, teha märkmeid ja
kontrolltöid lahendada. On üritatud luua võimalikult reaalne simulatsioon ülikoolis käimisest.""", "Tutvustus",
                           ok_button="Mängima!")

ise = easygui.ynbox("Kas soovid ise õppida?", "Enne mängu", ["Ise", "Arvuti"])

if not ise:
    skill = {"Programmeerimine": 0, "Matemaatiline maailmapilt": 0, "Sissejuhatus erialasse": 0,
             "Kõrgem matemaatika": 0, "Arvuti arhitektuur ja riistvara": 0}
    esimene_nädal_arvuti(teisipäev, kolmapäev, neljapäev, reede, tlp, klp, nlp, rlp, skill)
    teine_nädal_arvuti(esmaspäev, teisipäev, kolmapäev, neljapäev, reede, elp, tlp, klp, nlp, rlp, skill)
    kolmas_nädal_arvuti(esmaspäev, teisipäev, kolmapäev, neljapäev, reede, elp, tlp, klp, nlp, rlp, skill)
    neljas_nädal_arvuti(esmaspäev, teisipäev, kolmapäev, neljapäev, reede, elp, tlp, klp, nlp, rlp, skill)
elif ise:
    skill = {"Programmeerimine": 0, "Matemaatiline maailmapilt": 0, "Sissejuhatus erialasse": 0,
             "Kõrgem matemaatika": 0, "Arvuti arhitektuur ja riistvara": 0}
    esimene_nädal_ise(teisipäev, kolmapäev, neljapäev, reede, tlp, klp, nlp, rlp, skill, esimene_nädal)
    teine_nädal_ise(esmaspäev, teisipäev, kolmapäev, neljapäev, reede, elp, tlp, klp, nlp, rlp, skill, teine_nädal)
    kolmas_nädal_ise(esmaspäev, teisipäev, kolmapäev, neljapäev, reede, elp, tlp, klp, nlp, rlp, skill, kolmas_nädal)
    neljas_nädal_ise(esmaspäev, teisipäev, kolmapäev, neljapäev, reede, elp, tlp, klp, nlp, rlp, skill, neljas_nädal)

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
