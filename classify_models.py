__author__ = 'Sebastian Sanchez Perez-Moreno. Email: s.sanchezperezmoreno@tudelft.nl'
from py2neo import Graph, Node, Relationship
owfgraph=Graph("http://neo4j:neo4j@localhost:7474/db/data/")
exe = owfgraph.cypher.execute

