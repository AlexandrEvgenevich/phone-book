import csv
import re

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts_list = str(contacts_list).replace("[", "").replace("]", "").replace("'", "")\
    .replace(",", "").replace("–", "").replace("-", "").replace("(", "").replace(")", "")

print(contacts_list)

pattern = re.compile("([А-ЯЁ]{1}[а-яё]+)(\s?)([А-ЯЁ]{1}[а-яё]+)(\s?)([А-ЯЁ]{1}[а-яё]+)(\s+)(\D+)(\+)?([7|8])(\s*)(\d{3})(\s*)(\d{3})(\s*)(\d{2})(\s*)(\d{2})(\s+)?([а-яё]{3}\.)?(\s+)?(\d{4})?")

# cl = re.findall(pattern, contacts_list)
cl = re.sub(pattern, r"\1 \3 \5 +\9(\11)\13-\15-\17 \19\21", contacts_list)

print(cl)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(cl)