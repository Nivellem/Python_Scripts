import os

def find_files_with_word(root_path, search_word):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r') as f:
                        file_contents = f.read()
                        if search_word in file_contents:
                            print(f"Found '{search_word}' in file: {file_path}")
                except UnicodeDecodeError:
                    print(f"Cannot read file: {file_path} - it may be a binary file.")

# przykładowe użycie
root_path = input("Podaj ścieżkę do katalogu, w którym chcesz szukać plików: ")
search_word = input("Podaj słowo, które chcesz wyszukać w plikach: ")

find_files_with_word(root_path, search_word)
