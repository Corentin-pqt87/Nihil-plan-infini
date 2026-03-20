import json

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


stop_ = ['stop','break','..']
ajout_ = ['ajout','nouveau','ajouter','+','=','modification','modifier']
recherche_ = ['recherche','rechercher','trouver','==','?']
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
            print(f'{langue}/$ langue choisis : sedonien')

        elif enter == 'sumarique' or enter == '2':
            langue = 'sumarique'
            print(f'{langue}/$ langue choisis : sumarique')
        
        # action----------------------------------------------
        run_option = True
        while run_option:
            print(f'{langue}/$ action :')
            action = input('>>> ')

            if action.lower() in stop_:
                run_option = False
                print(f'{langue}/action/$ retour au choix de langue')
            else:
                if action.lower() in ajout_:
                    option_action = 'ajout'
                    print(f"{langue}/action/$ ajout de nouveau mots ou modification")

                    run_ajout = True
                    while run_ajout:
                        print(f'{langue}/action/ajout/$ Mot en français :')
                        mot_fr = input('>>> ')
                        if mot_fr in stop_:
                            run_ajout = False
                        else:
                            print(f'{langue}/action/ajout/$ Mot en',langue)
                            n_mot = input('>>> ')
                            # en fonction de la langue
                            if langue == 'sedonien': sedonien[mot_fr] = n_mot
                            elif langue == 'sumarique' : sumarique[mot_fr] = n_mot
                            print(f'{langue}/action/ajout/$ nouveau mot ajouter',mot_fr,'->',n_mot)
                            save()
                        print('-'*40)
                elif action.lower() in recherche_:
                    option_action = 'recherche'
                    print(f"{langue}/action/$ recherche de mot")

                    run_recherche = True
                    while run_recherche:

                        print(f"{langue}/action/recherche/$ mot en français :")
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