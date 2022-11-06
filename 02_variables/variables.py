#--------------------------------------------
# About Variables Declaration
#--------------------------------------------


cliente: str = "Ciro"
pizza_base: str = "Leggera"
pizza_size: int = 12
condimenti: str = "Prosciutto"
extra_cheese: bool = True
price: float = 7.99


#--------------------------------------------
# 1 - Stampiamo le variabili
#--------------------------------------------

print(f"Sto ricevendo ordine da: {cliente}")
print(f"Pizza : {pizza_base}, dimensione: {pizza_size} cm, Condimento: {condimenti}")
print(f"prezzo della pizza: {price} Euro")



#--------------------------------------------
# 2 - Stampiamo variabili con formattazione
#--------------------------------------------

dettaglio_ordine: str = f""" 
Sto ricevendo ordine da: {cliente}
Pizza : {pizza_base}, dimensione: {pizza_size} cm, Condimento: {condimenti}
prezzo della pizza: {price} Euro
"""

print(dettaglio_ordine)


