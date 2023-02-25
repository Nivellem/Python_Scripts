def powtarzajace_znaki(zdanie):
    # utwórz słownik, w którym kluczami są znaki, a wartościami ich liczba wystąpień
    liczniki = {}
    for znak in zdanie:
        if znak in liczniki:
            liczniki[znak] += 1
        else:
            liczniki[znak] = 1

    # wybierz znaki, które występują więcej niż raz
    powtarzajace = [znak for znak in liczniki if liczniki[znak] > 1]

    # posortuj znaki malejąco według liczby ich wystąpień
    powtarzajace.sort(reverse=True, key=lambda znak: liczniki[znak])

    return powtarzajace
zdanie = "Ala ma kota, kot ma Ale"
print(powtarzajace_znaki(zdanie))  # ['a', ' ', 'm', 't', 'A', 'k', 'o']
