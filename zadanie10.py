# Program do generowania pliku konfiguracyjnego dla adresów IP

# Funkcja do wygenerowania pliku konfiguracyjnego dla Windows
def generate_windows_config(file_name, addresses):
    with open(file_name, 'w') as f:
        for address in addresses:
            f.write(f'route add {address[0]} mask {address[1]} {address[2]}\n')

# Funkcja do wygenerowania pliku konfiguracyjnego dla Linuksa
def generate_linux_config(file_name, addresses):
    with open(file_name, 'w') as f:
        for address in addresses:
            f.write(f'ip route add {address[0]}/{address[1]} via {address[2]}\n')

# Funkcja do wygenerowania pliku konfiguracyjnego dla Cisco
def generate_cisco_config(file_name, addresses):
    with open(file_name, 'w') as f:
        for address in addresses:
            f.write(f'ip route {address[0]} {address[1]} {address[2]}\n')

# Przykładowe dane
addresses = [
    ('192.168.1.0', '255.255.255.0', '192.168.1.1'),
    ('10.0.0.0', '255.0.0.0', '10.1.1.1'),
    ('172.16.0.0', '255.240.0.0', '172.16.1.1')
]

# Wybór platformy
platform = input('Wybierz platformę (Windows, Linux, Cisco): ')

# Generowanie pliku konfiguracyjnego
if platform.lower() == 'windows':
    generate_windows_config('config_Windows.txt', addresses)
elif platform.lower() == 'linux':
    generate_linux_config('config_Linux.txt', addresses)
elif platform.lower() == 'cisco':
    generate_cisco_config('config_Cisco.txt', addresses)
else:
    print('Nieprawidłowa platforma.')
