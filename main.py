
def Eingabe(): #Eingeben von Preisen und Umsatz pro Bar
    print("Bitte geben Sie nur ganze Preise und Einnahmen ein (keine Centbeträge). Preise dürfen nicht 0 sein.")
    price_bar1 = float(input("Preis Bar 1 in €: "))
    revenue_bar1 = float(input("Einnahmen Bar 1 in €: "))
    price_bar2 = float(input("Preis Bar 2 in €: "))
    revenue_bar2 = float(input("Einnahmen Bar 2 in €: "))   
    price_bar3 = float(input("Preis Bar 3 in €: "))
    revenue_bar3 = float(input("Einnahmen Bar 3 in €: "))
    return price_bar1, price_bar2, price_bar3, revenue_bar1, revenue_bar2, revenue_bar3

def Verkaufte_Menge(price_bar1, price_bar2, price_bar3, revenue_bar1, revenue_bar2, revenue_bar3): #Ermittlung wie viel welche Bar verkauft hat
    amount_bar1 = revenue_bar1/price_bar1
    amount_bar2 = revenue_bar2/price_bar2
    amount_bar3 = revenue_bar3/price_bar3   
    return amount_bar1, amount_bar2, amount_bar3


def Ausgabe(amount_bar1, amount_bar2, amount_bar3): 
    if amount_bar1 > amount_bar2 and amount_bar1 > amount_bar3:
        print("Bar 1 hat am meisten verkauft!")
    elif amount_bar2 > amount_bar1 and amount_bar2 > amount_bar3:
        print("Bar 2 hat am meisten verkauft!")
    elif amount_bar3 > amount_bar2 and amount_bar3 > amount_bar1:
        print("Bar 3 hat am meisten verkauft!")
    elif amount_bar1 == amount_bar2 and amount_bar1 > amount_bar3:
        print("Bar 1 und Bar 2 haben am meisten verkauft!")
    elif amount_bar1 == amount_bar3 and amount_bar1 > amount_bar2:
        print("Bar 1 und Bar 3 haben am meisten verkauft!")
    elif amount_bar2 == amount_bar3 and amount_bar2 > amount_bar1:
        print("Bar 2 und Bar 3 haben am meisten verkauft!")
    else:
        print("Alle Bars haben gleich viel verkauft!")
    
price_bar1, revenue_bar1, price_bar2, revenue_bar2, price_bar3, revenue_bar3 = Eingabe()
amount_bar1, amount_bar2, amount_bar3 = Verkaufte_Menge(price_bar1, revenue_bar1, price_bar2, revenue_bar2, price_bar3, revenue_bar3)
Ausgabe(amount_bar1, amount_bar2, amount_bar3)
