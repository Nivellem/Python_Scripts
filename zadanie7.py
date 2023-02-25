import sys
import collections

# Inicjalizacja słownika licznika dla słów
word_counts = collections.defaultdict(int)

# Sprawdzenie, czy podano nazwę pliku .txt jako argument wiersza poleceń
if len(sys.argv) > 1 and sys.argv[1].endswith('.txt'):
    filenames = sys.argv[1:]
else:
    filenames = []
    
# Wczytanie nazwy pliku .txt, jeśli nie podano jej jako argument wiersza poleceń
if not filenames:
    while True:
        filename = input("Podaj nazwę pliku .txt lub 'q' aby zakończyć: ")
        if filename.lower() == 'q':
            sys.exit()
        elif filename.endswith('.txt'):
            filenames.append(filename)
            break
        else:
            print("Niepoprawna nazwa pliku. Plik musi mieć rozszerzenie .txt")

# Przeglądanie plików tekstowych i zliczanie wystąpień słów
for file_name in filenames:
    with open(file_name, 'r') as f:
        for line in f:
            # Podzielenie linii na słowa i zaktualizowanie licznika
            for word in line.strip().split():
                word_counts[word] += 1

# Wypisanie 10 najczęściej występujących słów
for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f'{word}: {count}')
