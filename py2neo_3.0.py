from py2neo import Node, Relationship, Graph, authenticate
from py2neo_v3_functions import DESCRIBES, change_label, change_property, change_relationship, create_node, \
    create_property, create_relationship, delete_node, delete_relationship, make_node, neighbours, find, RELATES_TO, add_label, exe

# authenticate("owfgraph.lr.tudelft.nl:7474", "neo4j", "kluyverweg")
# owfgraph = Graph("http://neo4j:kluyverwegwind@owfgraph.lr.tudelft.nl:7474/db/data/")
# localgraph = Graph("http://neo4j:neo4j@localhost:7474/db/data/")
# owfgraph = Graph("http://owfgraph.lr.tudelft.nl:7474/db/data/")

procedure = 'procedure'
attribute = 'attribute'
variable = 'variable'
object_ = 'object'
model = 'model'
describes = 'DESCRIBES'
partof = 'PART_OF'
inputto = 'INPUT_TO'
outputof = 'OUTPUT_OF'
appearsin = 'APPEARS_IN'
variantof = 'VARIANT_OF'
instructs = 'INSTRUCTS'
description = 'description'
unit = 'unit'
value = 'value'
domain = 'domain'
name = 'name'
reference = 'reference'


# sxcvyytr = {'label': attribute,
#
#              'name': 'structure of the support structure',
#
#              'author': 'sebastian',
#
#              'description': '',
#
#              'unit': '',
#
#              'domain': '',
#
#              'value': '',
#
#              'expression': '',
#
#              'reference': '',
#
#              'note': ''}
#
# fasd2 = {'label': variable,
#
#              'name': 'turbulence at every turbine',
#
#              'author': ' ',
#
#              'description': '',
#
#              'unit': '',
#
#              'domain': '',
#
#              'value': '',
#
#              'expression': '',
#
#              'reference': '',
#
#              'note': ''}

if __name__ == '__main__':

    number = []
    names = []
    desc = []

    with open('cost_breakdown/cost_NREL.csv', 'r') as original:
        for line in original:
            col = line.split('\t')
            number.append(int(col[0]))
            if col[1][-1] == " ":
                names.append(col[1][:-1])
            else:
                names.append(col[1])
            desc.append(col[2][:-1])
    counter = [names.count(i) for i in names]

    # print(names)

    for i in range(len(number), 0, - 1):
        num1 = number[i - 1]
        name1 = names[i - 1]

        for j in range(i, 0, - 1):
            if number[j - 1] == number[i - 1] - 1:
                num2 = number[j - 1]
                name2 = names[j - 1]
                if counter[i - 1] > 1:
                    names[i-1] += ' - ' + name2
                    name1 += ' - ' + name2
                break

    for i in range(len(names)):
        names[i] += ' cost'

    # print(names[285])

    # for i in range(len(names)):
    #     print(i)
    #     node = {'label': variable,
    #
    #              'name': names[i],
    #
    #              'author': 'sebastian',
    #
    #              'description': desc[i],
    #
    #              'unit': '¤',
    #
    #              'domain': 'real',
    #
    #              'value': '',
    #
    #              'expression': '',
    #
    #              'reference': 'NREL cost breakdown',
    #
    #              'note': ''}
        # create_node(node)
        # add_label(variable, names[i], 'Nrelcostbreakdown')

    # for i in range(len(number), 0, - 1):
    #     num1 = number[i - 1]
    #     name1 = names[i - 1]
    #
    #     for j in range(i, 0, - 1):
    #         if number[j - 1] == number[i - 1] - 1:
    #             num2 = number[j - 1]
    #             name2 = names[j - 1]
    #             a = [num1, name1]
    #             b = [num2, name2]
    #             pair = [a, b]
    #             print(name1, '//////////', name2)
    #             # exe("match (n:Variable:Nrelcostbreakdown{name:'" + name1 + "'}), (m:Variable:Nrelcostbreakdown{name:'" + name2 + "'}) create (n)-[r:PART_OF]->(m)").dump()
    #             break

    # find('area of incidence of partial wake or multiple wake overlap')

    # change_label('MBZ13', 'thrust coefficient', 'Mbz13')
    # add_label(variable, 'annual energy production', 'Mbz13')
    # change_relationship(variable, 'set of wind turbines', inputto, describes, attribute, 'OWF structure')

    # create_node(fyy2)
    # create_node(assembly)
    # create_node(rna_cost)

    # del_relationship('variable', 'distance to coast', 'describes', 'object', 'site')

    # delete_node(variable, 'electricity production')

    # change_property(model, 'drag coefficient', name, 'drag coefficient of the support structure')

    # change_property(variable, 'inertia coefficient', name, 'inertia coefficient of the support structure')

    # create_relationship(attribute, 'monopile state', describes, object_, 'monopile')
    # create_relationship(variable, 'turbulence at every turbine', inputto, model, 'fatigue')

    # delete_relationship('variable', 'costs of operation and maintenance excluding management costs', 'describes', 'attribute', 'OWF cost')

    # create_property(variable, 'storm fraction for reference access method', domain, 'real')
    #
    # create_property(variable, 'storm fraction', description, 'N')

    # create_property(variable, 'annual loss in electrical infrastructure', description, 'Annual energy losses in the whole electrical connection system.')

    # delete_node('object', 'foundation')

    # neighbours('attribute', 'availability of owf')