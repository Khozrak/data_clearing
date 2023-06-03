with open('table.txt', 'r', encoding='UTF-8') as table:
    list_tuple = []
    for line in table:
        new_list = [int(i) if i.isdigit()
                           else float(i)
                               if i.replace('.', '', 1).isdigit()
                               else i
                    for i in line.rstrip().split('\t')][1:]
        if len(new_list) == 1:
            list_tuple.append(f"('{new_list[0]}')")
        else:
            list_tuple.append(str(tuple(new_list)))
with open('input.txt', 'w', encoding='UTF-8') as inp:
    print(*list_tuple, sep=',\n', file=inp)
