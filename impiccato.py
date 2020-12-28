import json
import random
diz = json.load(open("original.json"))
parole = list(diz.keys())
ind = random.randint(0, 40000)
x = parole[ind]
x = x.lower()


def controllalet(let, par, trat):
    lis = list(par)
    listrat = list(trat)
    cont = 0
    for el in lis:
        if let == el:
            listrat[cont] = let
        cont += 1
    return "".join(listrat)


def gioca(par):
    vite = 10
    y = ""
    for el in x:
        if(el.isalpha()):
            y += "-"
        else:
            y += el
    print(y)
    while "-" in y:
        if vite == 0:
                print("  _____    ")
                print(" |    ☺  ")
                print(" |   /|\     ")
                print(" |   / \     ")
                print(" |___________    ")
                print("Hai perso! La parola era:", par)
                break
        let = input("Inserisci una nuova lettera: ")
        if len(let) > 1 or len(let) == 0:
            let = input("Inserisci solo una lettera alla volta: ")
        r = controllalet(let, par, y)
        print(r)
        if r == y:
            vite -= 1
            print("Nessuna corrispondenza!")
        y = r
        if y == par:
            print("Hai vinto!")
            break
        print("Vite rimaste:", vite)
        if vite == 1:
            print("  _____    ")
            print(" |    ☺  ")
            print(" |   /|\     ")
            print(" |       ")
            print(" |___________    ")
        if vite == 2:
                print("  _____    ")
                print(" |    ☺  ")
                print(" |        ")
                print(" |        ")
                print(" |___________    ")
        if vite == 3:
            print("  _____    ")
            print(" |      ")
            print(" |        ")
            print(" |       ")
            print(" |___________    ")
        if vite == 4:
            print("     ")
            print(" |      ")
            print(" |        ")
            print(" |       ")
            print(" |___________    ")
        if vite == 5:
            print("     ")
            print("       ")
            print("        ")
            print(" |       ")
            print(" |___________    ")
        if vite == 6:
            print("     ")
            print("       ")
            print("         ")
            print("        ")
            print(" |___________    ")
        if vite == 7:
            print("     ")
            print("       ")
            print("         ")
            print("        ")
            print(" ___________    ")
        if vite == 8:
            print("     ")
            print("       ")
            print("         ")
            print("       ")
            print(" ______    ")
        if vite == 9:
            print("     ")
            print("       ")
            print("         ")
            print("        ")
            print(" __    ")
gioca(x)
