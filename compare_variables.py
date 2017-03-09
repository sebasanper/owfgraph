def compare():
    data = open("michiel_variables.dat", "r")
    for line in data:
        if line[:-1] in open("owfgraph.graphml").read():
            print line[:-1]
    data.close()

compare()