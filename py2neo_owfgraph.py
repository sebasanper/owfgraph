__author__ = 'Sebastian Sanchez Perez-Moreno. Email: s.sanchezperezmoreno@tudelft.nl'
from py2neo_functions import add_node, add_relationship, add_property, del_relationship, del_node
from py2neo import Graph
owfgraph = Graph("http://neo4j:neo4j@localhost:7474/db/data/")
exe = owfgraph.cypher.execute

query = "match (m:Model)<-[]-(v) where m.name={name} return v.name as Variable"

# print exe(query, name='m31')
