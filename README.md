# Python_Scripts

## Zadanie 1

Program drukujący kalendarz dla zadanego miesiąca i roku. Użytkownik wprowadza informację w formacie "nazwa_miesiaca rok". Program wykorzystuje bibliotekę calendar i umożliwia wyświetlenie kalendarza dla podanego miesiąca i roku.

## Zadanie 2

Funkcja powtarzajace_znaki przyjmuje jako argument zdanie i zwraca listę znaków, które powtarzają się w zdaniu, posortowanych od najczęściej do najrzadziej występującego. Funkcja tworzy słownik z liczbą wystąpień każdego znaku w zdaniu, a następnie wybiera tylko te znaki, które powtarzają się i sortuje je według liczby ich wystąpień.

## Zadanie 3

Funkcja znajdz_numer_telefonu przyjmuje jako argument tekst i zwraca pierwszy znaleziony poprawny numer telefonu (cyfry oddzielone spacjami bądź znakiem -, numer może być poprzedzony znakiem +). Funkcja wykorzystuje wyrażenia regularne do wyszukania w tekście pasujących do wzorca numerów telefonów.

## Zadanie 4

Funkcja decimal_to_roman przyjmuje jako argument liczbę dziesiętną i zwraca odpowiadającą jej liczbę rzymską. Funkcja sprawdza, czy podany argument jest liczbą całkowitą i czy jest ona z odpowiedniego przedziału (1-49999). Następnie używa pętli for i list wartości rzymskich i dziesiętnych, aby przekształcić liczbę dziesiętną na liczbę rzymską

## Zadanie 5

Funkcja znajdz_najwieksze przyjmuje jako argument listę liczb i zwraca największą liczbę z listy. Funkcja tworzy pomocniczą zmienną, która na początku jest ustawiona na wartość pierwszego elementu listy, a następnie używa pętli for, aby przejść przez każdy element listy i porównać go z aktualną największą liczbą. Jeśli znaleziono liczbę, która jest większa od aktualnie ustawionej największej liczby, największa liczba jest zastąpiona tą nową liczbą. Po zakończeniu pętli największa liczba jest zwracana jako wynik działania funkcji.

## Zadanie 6

Funkcja remove_comments przyjmuje jako argument ścieżkę do pliku programu w języku C++ i usuwa wszystkie komentarze z pliku, nie pozostawiając pustych linii. Funkcja otwiera plik i czyta jego zawartość, a następnie używa pętli for, aby przejść przez każdą linię i usunąć komentarze. Funkcja używa zmiennych in_comment i out, aby śledzić, czy jest aktualnie w komentarzu i zachować tylko niekomentowane linie. Funkcja zwraca tekst bez komentarzy jako ciąg znaków, który jest następnie zapisywany w nowym pliku.

## Zadanie 7

Funkcja zliczająca najczęściej występujące słowa w plikach tekstowych. Funkcja przyjmuje nazwy plików tekstowych jako argumenty wiersza poleceń lub może je pobrać od użytkownika. Funkcja tworzy słownik, który zlicza wystąpienia każdego słowa w pliku, a następnie sortuje słownik i wypisuje 10 najczęściej występujących słów wraz z liczbą ich wystąpień.

## Zadanie 8

Program, który umożliwia wyszukiwanie plików, które zawierają podane słowo. Użytkownik wprowadza ścieżkę do katalogu, w którym program ma wyszukać pliki, oraz słowo, które ma wyszukać w treści tych plików. Funkcja find_files_with_word wykorzystuje funkcję os.walk() do rekursywnego przeglądania katalogu i jego podkatalogów. Funkcja otwiera każdy plik i sprawdza, czy zawiera podane słowo. W przypadku niepoprawnego odczytu pliku (np. plik jest binarny), program wyświetla odpowiedni komunikat.

## Zadanie 9

Funkcja get_unique_filenames przyjmuje jako argument ścieżkę do katalogu i zwraca listę unikalnych nazw plików znajdujących się w tym katalogu i jego podkatalogach. Kod używa funkcji os.walk do przeszukiwania katalogu i zbierania nazw plików. Następnie tworzy set z nazwami plików i zwraca jego listę.

## Zadanie 10

Program ten pozwala na wygenerowanie pliku konfiguracyjnego dla różnych platform (Windows, Linux, Cisco) na podstawie listy adresów IP.

Dane wejściowe to lista adresów w postaci: adres / maska / bramka. Program umożliwia wybór platformy, dla której ma być wygenerowany plik konfiguracyjny.

Funkcje generate_windows_config, generate_linux_config i generate_cisco_config odpowiadają za wygenerowanie pliku konfiguracyjnego dla odpowiedniej platformy. Każda z funkcji otrzymuje jako argumenty nazwę pliku i listę adresów, a następnie zapisuje w pliku odpowiednie polecenia w składni dla danej platformy.

Aby użyć programu, należy wybrać platformę, a następnie uruchomić program. Zostanie on wygenerowany plik konfiguracyjny zawierający polecenia w składni dla wybranej platformy

## Zadanie 11

Program ten jest implementacją analizatora HTML, który wydobywa tekst z pliku HTML. Kod używa modułu html.parser w celu wydobycia tekstu z pliku HTML, ignorując wszystkie znaczniki.

Program składa się z jednej klasy MyHTMLParser, która dziedziczy po klasie HTMLParser z modułu html.parser. Klasa ta posiada jeden atrybut text, który jest pustym stringiem i będzie używany do zachowania wydobytego tekstu. Funkcja handle_data jest nadpisywana w celu dodania wydobytego tekstu do atrybutu text.

Następnie, plik HTML jest otwierany i przetwarzany przez obiekt analizatora HTML. Wydobyty tekst jest wyświetlany na końcu programu.


