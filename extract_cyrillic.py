import os
import re

files = [
    "/Users/alenpak/Desktop/контент для сайта 3.0/2021, Конференция к  20 летию ННЦТО.doc",
    "/Users/alenpak/Desktop/контент для сайта 3.0/2022, Конференция в Туркестане.doc",
    "/Users/alenpak/Desktop/контент для сайта 3.0/2023, Конференция.doc",
    "/Users/alenpak/Desktop/контент для сайта 3.0/Раздел О НАС  - Кодекс этики и поведения членов КАТО.doc",
    "/Users/alenpak/Desktop/контент для сайта 3.0/Раздел О НАС - Филиалы КАТО в регионах.xls"
]

def extract_strings(filename, min_len=4):
    with open(filename, 'rb') as f:
        content = f.read()
    
    # Simple regex for strings (printable chars)
    # We specifically want Cyrillic
    cyrillic_pattern = re.compile(rb'[\x20-\x7E\xC0-\xFF]{' + str(min_len).encode() + rb',}')
    
    found = []
    for match in cyrillic_pattern.finditer(content):
        try:
            # CP1251 is common for legacy Russian docs
            decoded = match.group().decode('cp1251')
            if any(c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' for c in decoded):
                found.append(decoded)
        except:
            pass
            
    return found

for f in files:
    print(f"--- {os.path.basename(f)} ---")
    lines = extract_strings(f, 20)
    # Print first few relevant lines
    for l in lines[:10]:
        print(l)
    print("\n")
