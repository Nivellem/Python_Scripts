import calendar

# pobierz dane od użytkownika
date_input = input("Podaj miesiąc i rok w formacie 'nazwa_miesiaca rok': ")

# rozdziel dane na nazwę miesiąca i rok
month_name, year = date_input.split()

# przetwórz nazwę miesiąca na numer miesiąca (1-12)
month_num = list(calendar.month_name).index(month_name.capitalize())

# wyświetl kalendarz dla podanego miesiąca i roku
print(calendar.month(int(year), month_num))
