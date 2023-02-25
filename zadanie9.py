import os

def get_unique_filenames(directory):
    # Utwórz pustą listę do przechowywania nazw plików
    filenames = []
    
    # Przejdź przez każdy plik i folder w danym katalogu
    for root, dirs, files in os.walk(directory):
        # Dodaj każdą nazwę pliku do listy
        for file in files:
            filenames.append(file)
    
    # Zwróć listę unikalnych nazw plików
    return list(set(filenames))

# Przykład użycia
directory = "C:/Users/Public/Test"
unique_filenames = get_unique_filenames(directory)
print(unique_filenames)
