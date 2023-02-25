def licz_dni():
    data1 = input("Podaj pierwszą datę w formacie dd.mm.rrrr: ")
    data2 = input("Podaj drugą datę w formacie dd.mm.rrrr: ")
    dzien1, miesiac1, rok1 = map(int, data1.split('.'))
    dzien2, miesiac2, rok2 = map(int, data2.split('.'))
    dni_w_miesiacach = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dni = 0
    # licz dni między datami, uwzględniając tylko rok przestępny
    for rok in range(rok1, rok2):
        if rok % 4 == 0:
            dni += 366
        else:
            dni += 365
    # dodaj dni w miesiącach między datami
    if rok1 == rok2:
        for miesiac in range(miesiac1-1, miesiac2-1):
            dni += dni_w_miesiacach[miesiac]
        dni += dzien2 - dzien1
    else:
        for miesiac in range(miesiac1-1, 12):
            dni += dni_w_miesiacach[miesiac] - dzien1
        for miesiac in range(0, miesiac2-1):
            dni += dni_w_miesiacach[miesiac]
        dni += dzien2
    print(f"Liczba dni między datami {data1} i {data2}: {dni}")
