
password = 'mishubishi'

if __name__ == '__main__':
    number = []
    names = []
    desc = []

    with open('cost_NREL.csv', 'r') as original:
        for line in original:
            col = line.split('\t')
            number.append(int(col[0]))
            if col[1][-1] == " ":
                names.append(col[1][:-1])
            else:
                names.append(col[1])
            desc.append(col[2][:-1])
    counter = [names.count(i) for i in names]
    print(counter)

    # print(names)

    # for i in range(len(names)):
    #     print("create (n:Variable:Nrelcostbreakdown{name:'"+names[i]+"', domain:'real', unit:'¤', author:'sebastian', desc:'"+desc[i]+"'});")

    for i in range(len(number), 0, - 1):
        num1 = number[i-1]
        name1 = names[i-1]

        for j in range(i, 0, - 1):
            if number[j-1] == number[i-1] - 1:
                num2 = number[j-1]
                name2 = names[j-1]
                if counter[i-1] > 1:
                    print(counter[i-1])
                    name1 += ' - ' + name2
                a = [num1, name1]
                b = [num2, name2]
                pair = [a, b]
                print(pair)
                break

    # for x in range(len(names)):
    #     if counter[x] > 1:
    #         print(counter[x], names[x])
