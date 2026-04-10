import pytest
from main import Verkaufte_Menge, Ausgabe

# Testet die Berechnung: Einnahmen / Preis = Menge
def test_berechnung_logik():
    # Beispiel: Preis 2€, Einnahmen 20€ -> Menge 10
    m1, m2, m3 = Verkaufte_Menge(2, 2, 2, 20, 40, 60)
    assert m1 == 100
    assert m2 == 100
    assert m3 == 100

# Testet die Textausgabe für den Gewinner
def test_ausgabe_sieger(capsys):
    # Wir geben Bar 1 die höchste Menge (100)
    Ausgabe(100, 10, 10)
    captured = capsys.readouterr()
    assert "Bar 1 hat am meisten verkauft!" in captured.out

# Testet das Verhalten bei Preis 0 (Division durch Null)
def test_division_durch_null():
    with pytest.raises(ZeroDivisionError):
        Verkaufte_Menge(0, 2, 2, 10, 10, 10)