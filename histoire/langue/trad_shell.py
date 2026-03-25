import json
from colorama import init, Fore, Style
import os
import re

init(autoreset=True)

#FILE_PATH = './test/test_langue.json'

# ------------------ DATA ------------------

def load(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save():
    if not current_file:
        return
    if current_file:
        with open(current_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

def require_file():
    if current_file is None:
        error("aucun fichier sélectionné (cd fichier.json)")
        return False
    return True

# ------------------ UTILS ------------------

def read_terminal(t: str):
    parts = t.strip().split()
    if not parts:
        return None
    return {
        'function': parts[0],
        'argument': parts[1:]
    }

def resolve(expr, visited=None):
    if visited is None:
        visited = set()

    # éviter les boucles infinies
    if expr in visited:
        return "?"
    visited.add(expr)

    # trouver {langue[mot]}
    pattern = r"\{(\w+)\[(\w+)\]\}"

    while re.search(pattern, expr):
        match = re.search(pattern, expr)
        langue, mot = match.groups()

        if langue in data and mot in data[langue]:
            value = resolve(data[langue][mot], visited)
        else:
            value = "?"

        expr = expr[:match.start()] + value + expr[match.end():]

    # gérer concat avec "+"
    parts = expr.split("+")
    return "".join(parts)

def error(msg):
    print(Style.BRIGHT + Fore.RED + msg)

def success(msg):
    print( Fore.GREEN + msg)

def info(msg):
    print(Fore.CYAN + msg)

def warning(msg):
    print(Style.BRIGHT + Fore.YELLOW + msg)

def system(msg):
    print(Fore.MAGENTA + msg)

def output(msg):
    print(Fore.WHITE + msg)


# ------------------ COMMANDES ------------------

def add(langue, *args):
    """
    add {langue} {mot}
    """
    if not require_file():
        return
    if len(args) % 2 != 0:
        return error("arguments invalides (mot_fr mot_lg ...)")

    data.setdefault(langue, {})

    for fr, lg in zip(args[::2], args[1::2]):
        data[langue][fr] = lg

    save()
    success("mots ajoutés")



def echo(langue, mot=None):
    """
    echo {langue} {mot}
    """
    if not require_file():
        return
    if langue not in data:
        return error(f"langue '{langue}' inexistante")

    if mot:
        val = data[langue].get(mot)
        if val:
            print(resolve(val))
        else:
            error(f"mot '{mot}' introuvable")
    else:
        for fr, lg in data[langue].items():
            print(Fore.GREEN + fr + Fore.WHITE + " : " + Fore.CYAN + resolve(lg))


def delete(langue, mot):
    """
    delete {langue} {mot}
    """
    if not require_file():
        return
    if langue not in data:
        return error("langue inexistante")

    if mot not in data[langue]:
        return error("mot inexistant")

    del data[langue][mot]
    save()
    success("mot supprimé")


def lang():
    """
    lang
    """
    if not require_file():
        return
    if not data:
        return warning("aucune langue")
    info("langues disponibles :")
    for l in data:
        print(Fore.CYAN + " - " + l)


def help_cmd():
    """
    help
    """
    system("Commandes disponibles :\n")

    info("Ajouter un mot")
    print(Fore.GREEN + "add" + Fore.WHITE + " langue mot_fr mot_lg [...]\n")
    info("Pour faire le lien entre un mot d'une langue : {langue[mot]}")

    info("afficher la valeur d'une clé (pas de mot alors : tout les mots)")
    print(Fore.GREEN + "echo" + Fore.WHITE + " langue [mot]\n")

    info("Supprimer un mot")
    print(Fore.GREEN + "del" + Fore.WHITE + " langue mot\n")

    info("Lister les langue")
    print(Fore.GREEN + "lang\n")

    info("Ce dépplacer entre les fichiers")
    print(Fore.GREEN + "cd fichier.json | cd ..\n")

    info("Afficher les aides")
    print(Fore.GREEN + "help\n")

    info("Liste de mots aléatoire")
    print(Fore.GREEN + "rd" + Fore.WHITE + " langue nombre_de_mot\n")

    info("Traduire un mot ou une phrase")
    print(Fore.GREEN + "trad" + Fore.WHITE + " langue [mots]\n")

    info("Lister un dossier ou un fichier")
    print(Fore.GREEN + "ls")


def cd(path=None):
    """
    cd {lacate.json}
    """
    global current_file, data

    if path is None:
        warning("usage: cd fichier.json | cd ..")
        return

    # retour arrière
    if path == "..":
        current_file = None
        data = {}
        system("retour au menu principal")
        return

    # si le fichier n'existe pas → on le crée
    if not os.path.exists(path):
        warning(f"fichier '{path}' inexistant → création...")
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({}, f, indent=4)

    # hargement
    current_file = path
    data = load(path)
    success(f"fichier chargé: {path}")

def rd(langue, nb=None):
    from random import choice

    if not require_file():
        return

    if langue not in data:
        return error(f"langue '{langue}' inexistante")

    words = list(data[langue].items())

    if not words:
        return warning("aucun mot dans cette langue")

    # 1 seul mot
    if nb is None or nb == 1:
        fr, lg = choice(words)
        success(fr)
        success(Fore.CYAN + lg)

    # plusieurs mots
    else:
        results = [choice(words) for _ in range(int(nb))]

        for fr, lg in results:
            output(Fore.GREEN + fr + Fore.WHITE + " : " + Fore.CYAN + lg)

def trad(langue, *phrase):
    """
    trad {langue} mot mot mot ...
    """

    if not require_file():
        return

    if langue not in data:
        return error(f"langue '{langue}' inexistante")

    # reconstruire la phrase
    words = list(phrase)

    traduction = []

    for mot in words:
        # si le mot existe → on traduit
        if mot in data[langue]:
            traduction.append(data[langue][mot])
        else:
            traduction.append(resolve(data[langue][mot]))

    # afficher la traduction
    output(" ".join(traduction))

def ls():
    """
    ls
    """

    # dans dossier
    if current_file is None:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        try:
            files = os.listdir(BASE_DIR)

            if not files:
                return warning("dossier vide")

            info("contenu du dossier :")
            for f in files:
                path = os.path.join(BASE_DIR, f)

                if os.path.isdir(path):
                    print(Fore.CYAN + "[DIR]  " + f)
                else:
                    print(Fore.WHITE + "[FILE] " + f)

        except Exception as e:
            error(str(e))

    # dans JSON
    else:
        if not data:
            return warning("fichier vide")

        info("structure du fichier :")

        for langue, mots in data.items():
            print(Fore.CYAN + langue)

            if isinstance(mots, dict):
                for fr, lg in mots.items():
                    print("  " + Fore.GREEN + fr + Fore.WHITE + " : " + Fore.YELLOW + lg)
            else:
                print("  " + Fore.RED + "format invalide")

# ------------------ ROUTEUR ------------------

COMMANDS = {
    'add': add,
    '+': add,
    'echo': echo,
    'print': echo,
    '->':echo,
    'del': delete,
    '-': delete,
    'lang': lang,
    'language': lang,
    'help': help_cmd,
    '?': help_cmd,
    'cd':cd,
    'rd':rd,
    'random':rd,
    'trad':trad,
    'traduction':trad,
    't':trad,
    'echo-s':trad,
    'ls':ls
}


def interpret(cmd, args):
    func = COMMANDS.get(cmd)

    if not func:
        return error(f"commande inconnue: {cmd}")

    try:
        func(*args)
    except TypeError as e:
        error(f"erreur: {e}")

# ------------------ VAR -------------------
current_file = None
data = {}

# ------------------ LOOP ------------------

while True:
    prefix = (os.path.basename(current_file) if current_file else "root")
    user_input = input(f"{prefix} >>> ")
    parsed = read_terminal(user_input)
    if not parsed:
        continue
    else:
        interpret(parsed['function'], parsed['argument'])