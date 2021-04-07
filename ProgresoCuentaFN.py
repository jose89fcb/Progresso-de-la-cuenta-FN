import requests
import json

import time
import os
start = time.time()
from colorama import Back, Fore, init
init()





CuentaFortnite = input("Escribe el nombre de la cuenta: ")
response = requests.get(f'https://jose89fcb.webcindario.com/json/NivelDeCuentaFN.php?usuario={CuentaFortnite}')


NVlCuenta = response.json()['Nivel']
ProgressoFn = response.json()['Progreso']


print('\n')
print(Fore.RED +  '----------- -----------------')
print(Fore.GREEN + "Nivel de la cuenta: " +  NVlCuenta)
print('\n')
print(Fore.RED +  '----------- -----------------')
print(Fore.YELLOW + "Progresso al siguiente nivel: " +  ProgressoFn)

print('\n')
print('\n')
print('\n')
print('\n')
print('\n')






# sleeping for 1 sec to get 10 sec runtime
time.sleep(0)

os.system("pause")
