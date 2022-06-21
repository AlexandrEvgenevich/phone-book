import csv
import re

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts_list = str(contacts_list)
contacts_list2 = str(contacts_list).replace(',', ' ').replace("'", ' ')

names = re.compile(r"([А-ЯЁ]{1}[а-яё]+)\s*([А-ЯЁ]{1}[а-яё]+)\s*([А-ЯЁ]{1}[а-яё]+)")
tel_num = re.compile(r"(\+)?([7|8])\s*\D*(\d{3})\s*\D*(\d{3})\D*(\d{2})\D*(\d{2})\s*\(?(([а-яё]{3}\.)\w*\D*(\d{4}))?")

f_all_names = re.findall(names, contacts_list2)
f_all_tel = re.findall(tel_num, contacts_list)

new_names = []

for a in f_all_names:
    b = []
    for c in a:
        b.append(c)
    new_names.append(b)

nn_dups = []

for a in new_names:
    if a not in nn_dups:
        nn_dups.append(a)

new_num = []

for a in f_all_tel:
    b = []
    for c in a:
        b.append(c)
    if b not in new_num:
        new_num.append(b)

one_dub_pattern = re.compile(r"([7|8])\s*\D*(\d{3})\s*\D*(\d{3})\D*(\d{2})\D*(\d{2})\D*(\d{4})?")
one_dub = re.findall(one_dub_pattern, str(new_num))

num_list = []

for a in one_dub:
    b = (f"+{a[0]}({a[1]}){a[2]}-{a[3]}-{a[4]} доб.{a[5]}", "")
    num_list.append(b)

full_list_dikt = {}

bbb = 0

for a in nn_dups:
    full_list_dikt[a[0], a[1], a[2]] = num_list[bbb]
    bbb += 1

full_list = []

for a, b in full_list_dikt.items():
    full_list.append([a, b])

full_list2 = []

for a in full_list:
    full_list2.append(list((a[0][0], a[0][1], a[0][2], a[1][0], a[1][1])))

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(full_list2)

