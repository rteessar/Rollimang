import easygui

märkmed = {"Infotund": "", "Kõrgem matemaatika": "", "Arvuti arhitektuur ja riistvara": "","Arvuti arhitektuur ja riistvara2": "",
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


def info_tund():
    osalemine = easygui.ynbox("Kas tahad infotunnis osaleda?", "Esimene päev", ["Jah", "Ei"])
    if osalemine:
        kirjutamine = easygui.ynbox("Kas soovid märkmeid teha?", "Märkmed", ["Jah", "Ei"])
        if kirjutamine:
            easygui.msgbox("Tegid infotunnis märkmeid.")
            märkmed["Infotund"] += " Ainetele ja eksamitele registreerimine ÕIS'is"
        else:
            easygui.msgbox("Sa ei teinud infotunnis märkmeid.")
    else:
        easygui.msgbox('Jätsid infotunnis käimata!', 'Väga halb!')


def esimese_nädala_päevad(tunniplaan, lp, skillid):
    i = 0
    while i in range(len(lp)):
        if lp[i] == "loeng":
            osalemine = easygui.ynbox("Kas tahad aine " + tunniplaan[i].lower() + " loengus osaleda?", "Järgmine päev",
                                      ["Jah", "Ei"])
            if osalemine:
                kirjutamine = easygui.ynbox("Kas soovid märkmeid teha?", "Märkmed", ["Jah", "Ei"])
                if kirjutamine:
                    if tunniplaan[i] == "Programmeerimine":
                        easygui.msgbox("Tegid aines " + tunniplaan[i].lower() + " märkmeid.")
                        märkmed["Programmeerimine"] += "Arenduskeskkonna Thonny paigaldamine"
                    if tunniplaan[i] == "Kõrgem matemaatika":
                        easygui.msgbox("Tegid aines " + tunniplaan[i].lower() + " märkmeid.")
                        märkmed["Kõrgem matemaatika"] += "Maatriksiks nimetatakse m reast ja n veerust koosnevat ristkülikukujulist arvude tabelit."
                    if tunniplaan[i] == "Matemaatiline maailmapilt":
                        easygui.msgbox("Tegid aines " + tunniplaan[i].lower() + " märkmeid.")
                        märkmed["Matemaatiline maailmapilt"] += "Matemaatika on kõikjal meie ümber. Kui me ei tunne matemaatika keelt, siis me suuda seda näha."
                    if tunniplaan[i] == "Sissejuhatus erialasse":
                        easygui.msgbox("Tegid aines " + tunniplaan[i].lower() + " märkmeid.")
                        märkmed["Sissejuhatus erialasse"] += "Esmakursuslaste konverents"
                    if tunniplaan[i] == "Arvuti arhitektuur ja riistvara":
                       if märkmed["Arvuti arhitektuur ja riistvara"] == "":
                         easygui.msgbox("Tegid aines " + tunniplaan[i].lower() + " märkmeid.")
                         märkmed["Arvuti arhitektuur ja riistvara"] += "(Esimene loeng) IBM projekteeris esimese PC arvuti"
                       else:
                            märkmed["Arvuti arhitektuur ja riistvara2"] += " (Teine loeng) Vähim aeg protsessori jaoks on üks takt"
                else:
                    easygui.msgbox("Sa ei teinud selles aines märkmeid.")
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
                if skillid[tunniplaan[i]] < 100:
                    skillid[tunniplaan[i]] += 5
                    i += 1
            else:
                easygui.msgbox("Jätsid praktikumis käimata!", "Väga halb!")
                i += 1
    # easygui.msgbox(str(märkmed["Programmeerimine"]))
    return skillid


def esimene_nädal(teisipäev, kolmapäev, neljapäev, reede, tlp, klp, nlp, rlp, skill):
    info_tund()
    esimese_nädala_päevad(teisipäev, tlp, skill)
    esimese_nädala_päevad(kolmapäev, klp, skill)
    esimese_nädala_päevad(neljapäev, nlp, skill)
    esimese_nädala_päevad(reede, rlp, skill)
    print(märkmed)
