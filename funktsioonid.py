import easygui

märkmed = {"Infotund": "", "Kõrgem matemaatika": "", "Arvuti arhitektuur ja riistvara": "",
           "Matemaatiline maailmapilt": "", "Sissejuhatus erialasse": "", "Programmeerimine": ""}


def day0arvuti():
    osalemine = easygui.ynbox("Kas tahad infotunnis osaleda?", "Esimene päev", ["Jah", "Ei"], image="pildid/vanemuine46.png")
    if osalemine:
        easygui.msgbox("Käisid infotunnis, tubli!", "Infotund")
    else:
        easygui.msgbox('Jätsid infotunnis käimata!', 'Väga halb!')


def day1arvuti(tunniplaan, lp, skillid):
    i = 0
    while i in range(len(lp)):
        if lp[i] == "loeng":
            pilt = "pildid/" + tunniplaan[i] + "-loeng" + ".png"
            osalemine = easygui.ynbox("Kas tahad aine " + tunniplaan[i].lower() + " loengus osaleda?", "Esimene päev", ["Jah", "Ei"])
            if osalemine:
                easygui.msgbox("",tunniplaan[i], image=pilt)
                if skillid[tunniplaan[i]] < 100:
                    skillid[tunniplaan[i]] += 1
                    i += 1
            else:
                easygui.msgbox('Jätsid loengus käimata!', 'Väga halb!')
                i += 1
        else:

            osalemine = easygui.ynbox("Kas tahad aine " + tunniplaan[i].lower() + " praktikumis osaleda?",
                                      "Järgmine päev", ["Jah", "Ei"])
            if osalemine:
                easygui.msgbox("Käisid praktikumis, tubli!", "Kiitused")
                if skillid[tunniplaan[i]] < 100:
                    skillid[tunniplaan[i]] += 5
                    i += 1
            else:
                easygui.msgbox("Jätsid praktikumis käimata!", "Väga halb!")
                i += 1
    return skillid


def day0ise():
    osalemine = easygui.ynbox("Kas tahad infotunnis osaleda?", "Infotund", ["Jah", "Ei"], image="pildid/vanemuine46.png")
    if osalemine:
        kirjutamine = easygui.ynbox("Kas soovid märkmeid teha?", "Märkmed", ["Jah", "Ei"])
        if kirjutamine:
            easygui.msgbox("Tegid infotunnis märkmeid.")
            märkmed["Infotund"] += " Ainetele ja eksamitele registreerimine ÕIS'is"
        else:
            easygui.msgbox("Sa ei teinud infotunnis märkmeid.")
    else:
        easygui.msgbox('Jätsid infotunnis käimata!', 'Väga halb!')


def day1ise(tunniplaan, lp, skillid, märkmenädal):
    i = 0
    while i in range(len(lp)):
        if lp[i] == "loeng":
            pilt = "pildid/" + tunniplaan[i] + "-loeng" + ".png"
            osalemine = easygui.ynbox("Kas tahad aine " + tunniplaan[i].lower() + " loengus osaleda?", "Loeng",
                                      ["Jah", "Ei"])
            if osalemine:
                kirjutamine = easygui.ynbox("Kas soovid märkmeid teha?", "Märkmed", ["Jah", "Ei"], image=pilt)
                if kirjutamine:
                    märkmed[tunniplaan[i]] += märkmenädal[tunniplaan[i]]
                i += 1
            else:
                easygui.msgbox('Jätsid loengus käimata!', 'Väga halb!')
                i += 1
        else:

            osalemine = easygui.ynbox("Kas tahad aine " + tunniplaan[i].lower() + " praktikumis osaleda?", "",
                                      ["Jah", "Ei"])
            if osalemine:
                kirjutamine = easygui.ynbox("Kas soovid teha märkmeid?", "Märkmed", ["Jah", "Ei"])
                if kirjutamine:
                    if skillid[tunniplaan[i]] < 100:
                        skillid[tunniplaan[i]] += 5
                    i += 1
                else:
                    easygui.msgbox("Jätsid praktikumis käimata! ", "Väga halb!")
                    i += 1
    return skillid, märkmed


def daykontrolltöö(tunniplaan, lp, skillid, märkmenädal):
    i = 0
    punktid = 0
    easygui.msgbox("Sul on täna aines kõrgem matemaatika kontrolltöö")
    while i in range(len(lp)):
        if lp[i] == "loeng":
            osalemine = easygui.ynbox("Kas tahad aine " + tunniplaan[i].lower() + " loengus osaleda?", "loeng",
                                      ["Jah", "Ei"])
            if osalemine:
                kirjutamine = easygui.ynbox("Kas soovid märkmeid teha?")
                if kirjutamine:
                    märkmed[tunniplaan[i]] += märkmenädal[tunniplaan[i]]
                i += 1
            else:
                easygui.msgbox('Jätsid loengus käimata!', 'Väga halb!')
                i += 1
        else:
            if tunniplaan[i] == "Kõrgem matemaatika":
                osalemine = easygui.ynbox("Kas tahad aine " + tunniplaan[i].lower() + " praktikumis osaleda?",
                                          "KONTROLLTÖÖ", ["Jah", "Ei"])
                if osalemine:
                    kirjutamine = easygui.ynbox("Kas soovid märkmeid näha enne kontrolltöö alustamist?")
                    if kirjutamine:
                        easygui.textbox("Märkmed","Märkmed",märkmed[tunniplaan[i]])
                        kt1 = easygui.choicebox("Mis on ühikmaatriksi tähis?", "Esimene küsimus",
                                                ["A", "B", "C", "D", "E"])
                        if kt1 == "E":
                            punktid += 25
                        kt2 = easygui.choicebox("Mis telje suhtes on paarisfunktsioon sümmeetriline?", "Teine küsimus",
                                                ["x", "y", "z"])
                        if kt2 == "y":
                            punktid += 25
                        kt3 = easygui.choicebox("Mille suhtes on paaritufunktsioon sümmeetriline?", "Kolmas küsimus",
                                                ["x-telje", "nullpunkti", "z-telje"])
                        if kt3 == "nullpunkti":
                            punktid += 25
                        kt4 = easygui.choicebox("Mitu piirväärtust saab funktsioonil olla?", "Neljas küsimus",
                                                ["1", "2", "3"])
                        if kt4 == "1":
                            punktid += 25
                        if punktid >= 50:
                            easygui.msgbox("Tubli, said kontrolltööst edukalt läbi!")
                        else:
                            easygui.msgbox("Kukkusid kontrolltööst läbi!")
                        i += 1
                    else:
                        easygui.msgbox("Sa ei teinud kontrolltööd kaasa.")
                        i += 1
                else:
                    easygui.msgbox("Jätsid kontrolltööl käimata! Pead registreeruma järeltööle! ", "Väga halb!")
                    i += 1
    return skillid, märkmed


def esimene_nädal_ise(teisipäev, kolmapäev, neljapäev, reede, tlp, klp, nlp, rlp, skill, essanädal):
    day0ise()
    day1ise(teisipäev, tlp, skill, essanädal)
    day1ise(kolmapäev, klp, skill, essanädal)
    day1ise(neljapäev, nlp, skill, essanädal)
    day1ise(reede, rlp, skill, essanädal)




def esimene_nädal_arvuti(teisipäev, kolmapäev, neljapäev, reede, tlp, klp, nlp, rlp, skill):
    day0arvuti()
    day1arvuti(teisipäev, tlp, skill)
    day1arvuti(kolmapäev, klp, skill)
    day1arvuti(neljapäev, nlp, skill)
    day1arvuti(reede, rlp, skill)


def teine_nädal_ise(esmaspäev, teisipäev, kolmapäev, neljapäev, reede, elp, tlp, klp, nlp, rlp, skill, teine_nädal):
    day1ise(esmaspäev, elp, skill, teine_nädal)
    day1ise(teisipäev, tlp, skill, teine_nädal)
    day1ise(kolmapäev, klp, skill, teine_nädal)
    day1ise(neljapäev, nlp, skill, teine_nädal)
    day1ise(reede, rlp, skill, teine_nädal)


def teine_nädal_arvuti(esmaspäev, teisipäev, kolmapäev, neljapäev, reede, elp, tlp, klp, nlp, rlp, skill):
    day1arvuti(esmaspäev, elp, skill)
    day1arvuti(teisipäev, tlp, skill)
    day1arvuti(kolmapäev, klp, skill)
    day1arvuti(neljapäev, nlp, skill)
    day1arvuti(reede, rlp, skill)


def kolmas_nädal_ise(esmaspäev, teisipäev, kolmapäev, neljapäev, reede, elp, tlp, klp, nlp, rlp, skill, kolmas_nädal):
    day1ise(esmaspäev, elp, skill, kolmas_nädal)
    day1ise(teisipäev, tlp, skill, kolmas_nädal)
    day1ise(kolmapäev, klp, skill, kolmas_nädal)
    day1ise(neljapäev, nlp, skill, kolmas_nädal)
    day1ise(reede, rlp, skill, kolmas_nädal)


def kolmas_nädal_arvuti(esmaspäev, teisipäev, kolmapäev, neljapäev, reede, elp, tlp, klp, nlp, rlp, skill):
    day1arvuti(esmaspäev, elp, skill)
    day1arvuti(teisipäev, tlp, skill)
    day1arvuti(kolmapäev, klp, skill)
    day1arvuti(neljapäev, nlp, skill)
    day1arvuti(reede, rlp, skill)


def neljas_nädal_ise(esmaspäev, teisipäev, kolmapäev, neljapäev, reede, elp, tlp, klp, nlp, rlp, skill, neljas_nädal):
    day1ise(esmaspäev, elp, skill, neljas_nädal)
    daykontrolltöö(teisipäev, tlp, skill, neljas_nädal)
    day1ise(kolmapäev, klp, skill, neljas_nädal)
    day1ise(neljapäev, nlp, skill, neljas_nädal)
    day1ise(reede, rlp, skill, neljas_nädal)


def neljas_nädal_arvuti(esmaspäev, teisipäev, kolmapäev, neljapäev, reede, elp, tlp, klp, nlp, rlp, skill):
    day1arvuti(esmaspäev, elp, skill)
    day1arvuti(teisipäev, tlp, skill)
    day1arvuti(kolmapäev, klp, skill)
    day1arvuti(neljapäev, nlp, skill)
    day1arvuti(reede, rlp, skill)
