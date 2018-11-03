import easygui


def day0():
    osalemine = easygui.ynbox("Kas tahad infotunnis osaleda?", "Esimene päev", ["Jah", "Ei"],
                              image="vanemuine46.png")
    if osalemine:
        easygui.msgbox("Käisid infotunnis, tubli!", "kiitused")
    else:
        easygui.msgbox('Jätsid loengus käimata!', 'Väga halb!')


def day1(tunniplaan, skillid):
    for tund in tunniplaan:
        osalemine = easygui.ynbox("Kas tahad aine " + tund.lower() + " loengus  osaleda?", "Teine päev", ["Jah", "Ei"],
                                  image="vanemuine46.png")
        skillid[tund] = 0
        if osalemine:
            easygui.msgbox("Käisid loengus, tubli!", "kiitused")
            if skillid[tund] < 100:
                skillid[tund] += 1
        else:
            easygui.msgbox('Jätsid loengus käimata!', 'Väga halb!')
    return skillid
