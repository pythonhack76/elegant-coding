
#--------------------------------------------
# 3 - Funzioni Python migliorata
#--------------------------------------------


def welcome(nome: str) -> str:
    return f"welcome {nome}"


def main() -> None:
    amici: list[str] = ["Pippo","Pluto","Paperino","Topolino"]
    for amico in amici:
        if "Pippo" in welcome(amico):
            print(f'{amico} è simaptico')
        else:
            print(welcome(amico))

#stampiamo la funzione 

main() 
