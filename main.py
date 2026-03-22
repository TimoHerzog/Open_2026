
def Eingabe():
    price_bar1 = float(input("Preis Bar 1: "))
    revenue_bar1 = float(input("Einnahmen Bar 1: "))
    price_bar2 = float(input("Preis Bar 2: "))
    revenue_bar2 = float(input("Einnahmen Bar 2: "))   
    price_bar3 = float(input("Preis Bar 3: "))
    revenue_bar3 = float(input("Einnahmen Bar 3: "))
    return price_bar1, price_bar2, price_bar3, revenue_bar1, revenue_bar2, revenue_bar3

def Verkaufte_Menge(price_bar1, price_bar2, price_bar3, revenue_bar1, revenue_bar2, revenue_bar3):
    amount_bar1 = revenue_bar1/price_bar1
    amount_bar2 = revenue_bar2/price_bar2
    amount_bar3 = revenue_bar3/price_bar3
    return amount_bar1, amount_bar2, amount_bar3


def Ausgabe(amount_bar1, amount_bar2, amount_bar3):
    if amount_bar1 >= amount_bar2 and amount_bar1 >= amount_bar3:
        print("Bar 1 hat am meisten verkauft!")
    if amount_bar2 >= amount_bar1 and amount_bar2 >= amount_bar3:
        print("Bar 2 hat am meisten verkauft!")
    if amount_bar3 >= amount_bar2 and amount_bar3 >= amount_bar1:
        print("Bar 3 hat am meisten verkauft!")

price_bar1, revenue_bar1, price_bar2, revenue_bar2, price_bar3, revenue_bar3 = Eingabe()
amount_bar1, amount_bar2, amount_bar3 = Verkaufte_Menge(price_bar1, revenue_bar1, price_bar2, revenue_bar2, price_bar3, revenue_bar3)
Ausgabe(amount_bar1, amount_bar2, amount_bar3)
