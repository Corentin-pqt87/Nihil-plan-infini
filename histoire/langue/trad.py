import json
from colorama import init, Fore, Back, Style
init(autoreset=True)

with open('./langue/sedonien.json', 'r') as fichier:
    global sedonien
    sedonien = json.load(fichier)
with open('./langue/sumarique.json', 'r') as fichier:
    global sumarique
    sumarique = json.load(fichier)

def save():
    with open(f'./langue/sedonien.json', "w", encoding="utf-8") as f:
        json.dump(sedonien, f, indent=4, ensure_ascii=False)
    with open(f'./langue/sumarique.json', "w", encoding="utf-8") as f:
        json.dump(sumarique, f, indent=4, ensure_ascii=False)

def read_terminal(t:str):
    """
    lit une entré de terminale
    """
    l = t.split(' ')
    return {
        'function':l[0],
        'argument':l[1:]

    }

def man(t:str):
    if t in stop_:
        print(Fore.WHITE + Back.BLACK + "faire un retour arriere ou quiter l'application si a la racine")
        print(Fore.WHITE + Back.BLACK + stop_)
        print(Fore.WHITE + Back.BLACK + ">>> ..")
    if t in ajout_:
        print(Fore.WHITE + Back.BLACK + "Ajoute un mot dans le dictionnaire de la langue selectionner")
        print(Fore.WHITE + Back.BLACK + ajout_)
        print(Fore.WHITE + Back.BLACK + ">>> test")
        print(Fore.WHITE + Back.BLACK + ">>> tset")
    if t in recherche_:
        print(Fore.WHITE + Back.BLACK + "Recheche un mot dans le dictionnaire de la langue selectionner")
        print(Fore.WHITE + Back.BLACK + recherche_)
        print(Fore.WHITE + Back.BLACK + ">>> test")
        print(Fore.WHITE + Back.BLACK + "tset")

global stop_
stop_ = ['stop','break','..']
global ajout_
ajout_ = ['ajout','nouveau','ajouter','+','=','modification','modifier','/set']
global recherche_
recherche_ = ['recherche','rechercher','trouver','==','?','/get']
global aide_
aide_ = ['help','aide','??','/help']
run = True
langue = str()
option_action = str()

print("START")
while run:
    print("1 : sedonien\n2 : sumarique")
    print("langue :")
    enter = input(">>> ")

    if enter.lower() in stop_:
        run = False
        print("fin du programe")
    else:
        # langue----------------------------------------------
        if enter == 'sedonien' or enter == '1':
            langue = 'sedonien'
            print(f'\033[91m{langue}/\033[0m$ langue choisis : sedonien')

        elif enter == 'sumarique' or enter == '2':
            langue = 'sumarique'
            print(f'\033[91m{langue}/\033[0m$ langue choisis : sumarique')
        
        # action----------------------------------------------
        run_option = True
        while run_option:
            print(f'\033[91m{langue}/\033[0m$ action :')
            action = input('>>> ')

            if action.lower() in stop_:
                run_option = False
                print(f'\033[91m{langue}/\033[0m\033[32maction/\033[0m$ retour au choix de langue')
            elif action.lower() in aide_:
                print("Pour ajouter :")
                print(ajout_) 
                print('Pour rechercher :')
                print(recherche_)
                print("Pour faire quiter :")
                print(stop_)
            else:
                if action.lower() in ajout_:
                    option_action = 'ajout'
                    print(f"\033[91m{langue}/\033[0m\033[32maction/\033[0m$ ajout de nouveau mots ou modification")

                    run_ajout = True
                    while run_ajout:
                        print(f'\033[91m{langue}/\033[0m\033[32maction/\033[0m\033[94majout/\033[0m$ Mot en français :')
                        mot_fr = input('>>> ')
                        if mot_fr in stop_:
                            run_ajout = False
                        elif mot_fr in aide_:
                            print("Entré un mot en français puis sa traduction.")
                            print("Pour faire quiter :")
                            print(stop_)
                        else:
                            print(f'\033[91m{langue}/\033[0m\033[32maction/\033[0m\033[94majout/\033[0m$ Mot en',langue)
                            n_mot = input('>>> ')
                            # en fonction de la langue
                            if langue == 'sedonien': sedonien[mot_fr] = n_mot
                            elif langue == 'sumarique' : sumarique[mot_fr] = n_mot
                            print(f'\033[91m{langue}/\033[0m\033[32maction/\033[0m\033[94majout/\033[0m$ nouveau mot ajouter',mot_fr,'->',n_mot)
                            save()
                        print('-'*40)
                elif action.lower() in recherche_:
                    option_action = 'recherche'
                    print(f"\033[91m{langue}/\033[0m\033[32maction/\033[0m$ recherche de mot")

                    run_recherche = True
                    while run_recherche:

                        print(f"\033[91m{langue}/\033[0m\033[32maction/\033[0m\033[94mrecherche/\033[0m$ mot en français :")
                        mot_fr = input('>>> ')
                        if mot_fr in stop_:
                            run_recherche = False
                        else:
                            print(
                                f"|\tfrançais\t|\ttraduction\t|\n|\t:---\t\t|\t:---\t\t|"                                
                            )
                            if langue == "sedonien":
                                if mot_fr in sedonien.keys():
                                    print(f"|\t{mot_fr}\t\t|\t{sedonien[mot_fr]}\t\t|")
                            if langue == "sumarique":
                                if mot_fr in sumarique.keys():
                                    print(f"|\t{mot_fr}\t\t|\t{sumarique[mot_fr]}\t\t|")
                        print('-'*40)
            print('-'*40)
    print('-'*40)