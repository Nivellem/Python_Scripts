def decimal_to_roman(num):
    if not isinstance(num, int):
        raise TypeError("Argument musi być liczbą całkowitą")
    if num < 1 or num > 49999:
        raise ValueError("Argument musi być z przedziału [1, 49999]")

    # Utwórz listy reprezentujące wartości rzymskie i odpowiadające im wartości dziesiętne
    roman_numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    decimal_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    # Przekształć liczbę dziesiętną na liczbę rzymską
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // decimal_values[i]):
            roman_num += roman_numerals[i]
            num -= decimal_values[i]
        i += 1

    return roman_num


# Pobierz od użytkownika liczbę dziesiętną
num_str = input("Podaj liczbę dziesiętną: ")

# Spróbuj przekształcić wprowadzoną wartość na liczbę całkowitą
try:
    num = int(num_str)
except ValueError:
    print("Podana wartość nie jest liczbą całkowitą")
    exit()

# Wywołaj funkcję i wyświetl wynik
result = decimal_to_roman(num)
print(f"Liczba rzymska: {result}")
