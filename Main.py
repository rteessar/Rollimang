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

essanädal = {"Programmeerimine": "(Esimene loeng) Pythonis saab joonistada turtle teegiga. ",
             "Arvuti arhitektuur ja riistvara": "(Esimene loeng) Vähim aeg protsessori jaoks on üks takt. ",
             "Kõrgem matemaatika": "(Esimene loeng) Maatriksiks nimetatakse m reast ja n veerust koosnevat ristkülikukujulist arvude tabelit. ",
             "Arvuti arhitektuur ja riistvara2": "(Esimene loeng) IBM projekteeris esimese PC arvuti. ",
             "Matemaatiline maailmapilt": "(Esimene loeng) Matemaatika on kõikjal meie ümber. Kui me ei tunne matemaatika keelt, siis me suuda seda näha. ",
             "Sissejuhatus erialasse": "(Esimene loeng) Esmakursuslaste konverents "}

teine_nädal={"Programmeerimine": "(Teine loeng) Muutujaid, mille väärtust suurendatakse igal tsükli sammul ühe võrra, nimetatakse loenduriteks.",
             "Kõrgem matemaatika":"(Teine loeng) Suvalise n-järku ruutmaatriksi A korral kehtib AE = A, EA = A, kus E on n-järku ühikmaatriks.",
             "Matemaatiline maailmapilt":"(Teine loeng) Valem F on kehtestatav parajasti siis, kui tema eitus ¬F ei ole samaselt tõene.",
             "Arvuti arhitektuur ja riistvara":"(Teine loeng) Mälu, mille poole protsessor saab pöörduda oma siinide kaudu nimetatakse füüsiliseks mäluks",
             "Arvuti arhitektuur ja riistvara2":"(Teine loeng) Registrite suurus näitab ka mitme bitise protsessoriga on tegu",
             "Sissejuhatus erialasse":"(Teine loeng) Do it for the love of passion not for money!"}

kolmas_nädal={"Programmeerimine": "(Kolmas loeng) Meetodeid ei ole vaja kunagi import-ida.",
             "Kõrgem matemaatika":"(Kolmas loeng) Paarisfunktsioon on sümmeetriline y-telje suhtes. Paaritu funktsioon on sümmeetriline nullpunkti suhtes.",
             "Matemaatiline maailmapilt":"(Kolmas loeng) Tühjaks hulgaks ∅ nimetatakse hulka, mis ei sisalda ühtegi elementi.",
             "Arvuti arhitektuur ja riistvara":"(Kolmas loeng) Mälu ülesandeks on andmete ja programmide säilitamine.",
             "Arvuti arhitektuur ja riistvara2":"(Kolmas loeng) Moore'i seadus põhineb arvutiriistvara ajalool ning ütleb, et mikrokiibil olevate transistoride arv kahekordistub iga kahe aasta järel.",
             "Sissejuhatus erialasse":"(Kolmas loeng) Sinu eksamihinne on funktsioon ajast, mida sa panustad õpingutesse."}

neljas_nädal={"Programmeerimine": "(Neljas loeng) Python paneb lokaalsete muutujate nimekirja kokku funktsiooni koodis leiduvate omistuslausete põhjal.",
             "Kõrgem matemaatika":"(Neljas loeng) Piirväärtuse ühesus. Vaadeldavas protsessis saab funktsioonil olla ainult üks piirväärtus.",
             "Matemaatiline maailmapilt":"(Neljas loeng) Hulkade A ja B ühendiks nimetatakse hulka A ∪ B, A ∪ B = {x | x ∈ A ∨ x ∈ B}.",
             "Arvuti arhitektuur ja riistvara":"(Neljas loeng) Esimesena võeti pipeline kasutusele Intel 80486 protsessoris.",
             "Arvuti arhitektuur ja riistvara2":"(Neljas loeng) SLAT (Second Level Address Translation).",
             "Sissejuhatus erialasse":"(Neljas loeng) The first step: Don’t be anxious. Nature controls it all."}

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
    esimene_nädal_ise(teisipäev, kolmapäev, neljapäev, reede, tlp, klp, nlp, rlp, skill, essanädal)
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
