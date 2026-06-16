#Из исходного текстового файла (experience.txt) выбрать стаж работы.
#Посчитать количество полученных элементов.

import re

def extract_experience_simple(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    pattern = r'\d+\s+(?:год|года|лет)\s*(?:\d+\s+(?:месяц|месяца|месяцев))?'

    return re.findall(pattern, text)

filename = 'experience.txt'
result = extract_experience_simple(filename)

for item in result:
    print(item)

print("Количество:", len(result))