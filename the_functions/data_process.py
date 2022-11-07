
#--------------------------------------------
# 3 - Funzioni Python 
#--------------------------------------------


def welcome(nome: str) -> None:
    print(f"welcome {nome}")


def main() -> None:
    amici: list[str] = ["Pippo","Pluto","Paperino","Topolino"]
    for amico in amici:
        welcome(amico)

#stampiamo la funzione 

main() 
