from py2neo import Graph, Node, Relationship
owfgraph = Graph("http://neo4j:kluyverwegwind@owfgraph.lr.tudelft.nl:7474/db/data/")
# fileread = open('michiel_variables.dat', 'r')
#
# def node_var(name1):
#    owfgraph.create(Node("Variable", name=name1))
#
# for line in fileread:
#     node_var(line[:-1])
#
# fileread.close()
#
# def node_mod(number):
#    owfgraph.create(Node("Model", name="m"+number))
#
# for n in range(171):
#    node_mod(str(n))

exe = owfgraph.run
#
model_number = 'm124'
# identifier = '811'

output = 'total time that lifting equipment is in the wind farm per year'

# if identifier:
#     exe("match (m:Model)<-[r:APPEARS_IN]-(v:Variable) where id(m)=" + identifier + " and not v.name='" + output + "' set r.output=false").dump()
#     exe("match (m:Model)<-[r:APPEARS_IN]-(v:Variable) where id(m)=" + identifier + " and v.name='" + output + "' set r.output=true").dump()
#     exe("match (m:Model), (n:Model) where m.name='MM' and id(m)=" + identifier + " create (n)-[r:PART_OF]->(m)").dump()
#     exe("match (m:Model) where id(m)=" + identifier + " set m:Internal").dump()
#     exe("match (m:Model)<-[r]-(v:Variable) where id(m)=" + identifier + " and v.name='" + output + "' set m.name=v.name").dump()

if model_number:
    exe("match (m:Model)<-[r:APPEARS_IN]-(v:Variable) where m.name='" + model_number + "' and not v.name='" + output + "' set r.output=false").dump()
    exe("match (m:Model)<-[r:APPEARS_IN]-(v:Variable) where m.name='" + model_number + "' and v.name='" + output + "' set r.output=true").dump()
    exe("match (m:Model), (n:Model) where m.name='MM' and n.name='" + model_number + "' create (n)-[r:PART_OF]->(m)").dump()
    exe("match (m:Model) where m.name='" + model_number + "' set m:Internal").dump()
    exe("match (m:Model)<-[r:APPEARS_IN]-(v:Variable) where m.name='" + model_number + "' and v.name='" + output + "' set m.name=v.name").dump()

# var_names = ['annual average wind speed', 'Weibull scale factor', 'Weibull shape factor']

# exe("create (v:Variable{author:'sebastian', name:'" + model_desc[0] + "'})")
# exe("match (m:Model{name:'" + model_number + "'}) set m.description='" + model_desc + "'")
#
# output = var_names[0]
# #
#
# # exe("match (m:Model{name:'" + model_number + "'}) return m").dump()
# # exe("match (m:Variable{name:'" + output + "'}) return m").dump()
#
# exe("match (v:Variable{name:'" + output + "'})-[r]->(m:Model{name:'" + model_number + "'}) set r.output=True return r").dump()
# exe("match (m:Model{name:'" + model_number + "'}) set m.name='" + output + "' return m").dump()

# MAINTENANCE ONLY
# exe("match (m:Model{name:'" + model_number + "'}), (n:Model{name:'MM'}) create (m)-[r:PART_OF]->(n)").dump()
# exe("match (m:Model{name:'" + model_number + "'}) set m:Internal").dump()
# for var in var_names:
#     exe("match (v:Variable{name:'" + var + "'}) set v:Internal").dump()
#
# print model_number
