import keyboard
import time
# Apre il file in modalità lettura ('r' sta per 'read')
result = []

# Apre il file in modalità lettura ('r' sta per 'read')
time.sleep(5)
with open('a.txt', 'r') as file:
    # Legge il contenuto del file
    contenuto = file.read()
    for chart in contenuto:
        if chart=='>':
            keyboard.press('d')
            time.sleep(1/4)
            keyboard.release('d')
        elif chart=='>':
            keyboard.press('a')
            time.sleep(1/4)
            keyboard.release('a')
        elif chart=='^':
            keyboard.press('w')
            time.sleep(1/4)
            keyboard.release('w')
        elif chart=='v':
            keyboard.press('s')
            time.sleep(1/4)
            keyboard.release('s')
    print(contenuto)
