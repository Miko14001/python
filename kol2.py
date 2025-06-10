f = open("tata/test", "r")
file_list = []
for line in f:
    one_line = line.strip("\n")
    file_list.append(one_line)
f.close()

list_of_titles = []
dict_of_titles = {}
for i in range(len(file_list)):
    if file_list[i] != "" and file_list[i][0] == "=" and file_list[i][1] == " ":
        list_of_titles.append(file_list[i][2:-2])
        dict_of_titles[file_list[i][2:-2]] = {"from":i}
            


previous = False
for key, value in dict_of_titles.items():
    if previous == False:
        previous = key
        continue

    dict_of_titles[previous]['to'] = value['from']
    previous = key

dict_of_titles[key]['to'] = len(file_list)

sorted_list_of_titles = sorted(list_of_titles, key=lambda s: (not s[0].islower(), s))

for title in sorted_list_of_titles:
    for i in range(dict_of_titles[title]["from"], dict_of_titles[title]["to"]):
            print(file_list[i])

