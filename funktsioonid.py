import easygui

märkmed = {"Infotund": "", "Kõrgem matemaatika": "", "Arvuti arhitektuur ja riistvara": "",
           "Matemaatiline maailmapilt": "", "Sissejuhatus erialasse": "", "Programmeerimine": ""}


def day0arvuti():
    osalemine = easygui.ynbox("Kas tahad infotunnis osaleda?", "Esimene päev", ["Jah", "Ei"])
    if osalemine:
        easygui.msgbox("Käisid infotunnis, tubli!", "kiitused")
    else:
        easygui.msgbox('Jätsid infotunnis käimata!', 'Väga halb!')


def day1arvuti(tunniplaan, lp, skillid):
    i = 0
    while i in range(len(lp)):
        if lp[i] == "loeng":
            osalemine = easygui.ynbox("Kas tahad aine " + tunniplaan[i].lower() + " loengus osaleda?", "Järgmine päev",
                                      ["Jah", "Ei"], )
            if osalemine:
                easygui.msgbox("Käisid loengus, tubli!", "kiitused")
                if skillid[tunniplaan[i]] < 100:
                    skillid[tunniplaan[i]] += 1
                    i += 1
            else:
                easygui.msgbox('Jätsid loengus käimata!', 'Väga halb!')
                i += 1
        else:
            osalemine = easygui.ynbox("Kas tahad aine " + tunniplaan[i].lower() + " praktikumis osaleda?",
                                      "Järgmine päev")
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
    osalemine = easygui.ynbox("Kas tahad infotunnis osaleda?", "Esimene päev", ["Jah", "Ei"])
    if osalemine:
        kirjutamine = easygui.ynbox("Kas soovid märkmeid teha?")
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
            osalemine = easygui.ynbox("Kas tahad aine " + tunniplaan[i].lower() + " loengus osaleda?", "Järgmine päev",
                                      ["Jah", "Ei"])
            if osalemine:
                kirjutamine = easygui.ynbox("Kas soovid märkmeid teha?")
                if kirjutamine:
                    easygui.msgbox("Tegid aines " + tunniplaan[i].lower() + " märkmeid.")
                    märkmed[tunniplaan[i]] += märkmenädal[tunniplaan[i]]
                    i += 1
                else:
                    easygui.msgbox("Sa ei teinud selles aines märkmeid.")
            else:
                easygui.msgbox('Jätsid loengus käimata!', 'Väga halb!')
                i += 1
        else:
            osalemine = easygui.ynbox("Kas tahad aine " + tunniplaan[i].lower() + " praktikumis osaleda?",
                                      "Järgmine päev")
            if osalemine:
                kirjutamine = easygui.ynbox("Kas soovid märkmeid teha?")
                if kirjutamine:
                    easygui.msgbox("Tegid aines " + tunniplaan[i].lower() + " märkmeid.")
                    skillid[tunniplaan[i]] += 5
                    i += 1
                else:
                    easygui.msgbox("Sa ei teinud selles aines märkmeid.")
            else:
                easygui.msgbox("Jätsid praktikumis käimata! ", "Väga halb!")
                i += 1
    easygui.textbox("Siin näed selle päeva jooksul erinevates loengutes tehtud märkmeid","Tehtud märkmed",str(märkmed))
    return skillid, märkmed
