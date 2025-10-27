import os
import requests
import colorama

colorama.init()

logo = '''

▄▄▄█████▓ ▄▄▄       ██▀███   ▒█████     
▓  ██▒ ▓▒▒████▄    ▓██ ▒ ██▒▒██▒  ██▒   
▒ ▓██░ ▒░▒██  ▀█▄  ▓██ ░▄█ ▒▒██░  ██▒   
░ ▓██▓ ░ ░██▄▄▄▄██ ▒██▀▀█▄  ▒██   ██░   
  ▒██▒ ░  ▓█   ▓██▒░██▓ ▒██▒░ ████▓▒░   
  ▒ ░░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░▒░▒░    
    ░      ▒   ▒▒ ░  ░▒ ░ ▒░  ░ ▒ ▒░    
  ░        ░   ▒     ░░   ░ ░ ░ ░ ▒     
               ░  ░   ░         ░ ░     
                                       
'''

def new_func(data):
    
    print(f"country: {data.get('country', 'N/A')}")

while True:
    os.system('cls')
    print(logo)
    os.system('title Orbit IP - by Taro')
    x = input('Press Enter to Start!')

    if x == '':
        os.system('cls')
        IP = input('ENTER TARGET IP: ').strip()
        if not IP:
            print("IP manquante.")
            input('Press Enter To Continue...')
            continue

        try:
            r = requests.get(f'http://ip-api.com/json/{IP}', timeout=10)
            r.raise_for_status()
            data = r.json()
        except requests.RequestException as e:
            print('Erreur réseau / requête:', e)
            input('Press Enter To Continue...')
            continue
        except ValueError:
            print('Réponse invalide (pas du JSON).')
            input('Press Enter To Continue...')
            continue

        print('RESULTS\n')
        new_func(data)
        print(f"Region: {data.get('regionName', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Zip: {data.get('zip', 'N/A')}")
        print(f"ISP: {data.get('isp', 'N/A')}")
        print(f"IP: {data.get('query', 'N/A')}")
        input('Press Enter To Proceed...')
