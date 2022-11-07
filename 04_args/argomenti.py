from typing import Any

nome, congome = ("Pippo","Semper")

primo, *rest = ['Pippo','Sergej','Larry','Steve']


print(primo)
print(rest)


specs = {"type": "dynamic", "optional": "static typing", "found": "everywhere"}
lang = {"name": "Python", **specs}
print(lang)

#------------------------------argomenti variabili -----------------------------

def amici_sconosciuti(*args: str) -> str:
    if 'mario' in args:
        print("ci sono")
        for alieni in args:
            print(alieni)

amici_sconosciuti("pippo","cesare","arturo","flavio","mario")


#------------------------------keywords variabili -------------------------------------


def prodotto_sconosciuto(**kwargs: Any) -> None:
    for k, v in kwargs.items():
        print(f'{k}: {v}')

prodotto_sconosciuto(nome="pizza", prezzo=4.99, topping="mozzarella", extra_cheese=True)


prodotto_sconosciuto()


#------------------------------insieme  -------------------------------------

def fattura(prodotto: str, *args, **kwargs) -> None:
    print(prodotto)
    print(args)
    print(kwargs)

fattura("Sneakers", "black", "white", brand="Adidas", categoria="Tennis", price=89.99, in_stock=False)