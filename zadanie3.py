import re

def znajdz_numer_telefonu(tekst):
    # wzorzec regularny dla numerów telefonów
    wzorzec = r'\+?\d{0,3}[-\s]?\d{2,3}[-\s]?\d{3}[-\s]?\d{3}'

    # wyszukaj pasujące do wzorca fragmenty tekstu
    numery = re.findall(wzorzec, tekst)

    # zwróć pierwszy znaleziony numer
    if numery:
        return numery[0]
    else:
        return None
tekst = "Moim numerem telefonu jest +48 123-456-789. Skontaktuj się ze mną."
numer = znajdz_numer_telefonu(tekst)
print(numer)  # +48 123-456-789
