# TODO Напишите функцию find_common_participants

def find_common_participants (string1, string2, a=","):
    Res = []
    string1 = string1.replace ("|", a)
    string2 = string2.replace ("|", a)
    string1 = string1.split (a)
    string2 = string2.split (a)
    for i in range (0, len(string1)):
        for j in range (0, len(string2)):
            if string1[i] == string2[j]:
                Res.append(string1[i])
    Res =sorted(Res)
    return Res

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result1 = find_common_participants (participants_first_group, participants_second_group)
print (result1)
# TODO Провеьте работу функции с разделителем отличным от запятой
result2 = find_common_participants (participants_first_group, participants_second_group, "/")
print (result2)