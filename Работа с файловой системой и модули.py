#Задание 1
my_dict = {}
with open ('purchase_log.txt', 'r', encoding='utf-8') as f:
    f.seek(47)
    for line in f:
        my_dict[line.strip(',":{}').split()[1].strip('{}:",')] = line.strip(',":{}').split()[3].strip(':"{}')
#Задание 2
with open ('visit_log.csv', 'r', encoding='utf-8') as f:
     with open ('funnel.csv', 'w', encoding='utf-8') as f1:
        f.seek(47)
        for line in f:
            id_user = line.strip().split(',')[0]
            if id_user in my_dict.keys():
                f1.write(line.strip() + ',' + my_dict[id_user] + '\n')