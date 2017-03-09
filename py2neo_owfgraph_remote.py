__author__ = 'Sebastian Sanchez Perez-Moreno. Email: s.sanchezperezmoreno@tudelft.nl'
from py2neo_functions import create_property, create_node, create_relationship, delete_relationship, delete_node, change_relationship, find, change_label, neighbours, change_property
from py2neo import Graph
owfgraph = Graph("http://neo4j:kluyverwegwind@owfgraph.lr.tudelft.nl:7474/db/data/")
exe = owfgraph.cypher.execute

avail = {'label': 'attribute',

             'name': 'human activities on site',

             'description': 'human activities on the site.',

             'author': 'sebastian',

             'unit': '',

             'domain': '',

             'value': '',

             'expression': '',

             'reference': '',

             'note': ''}

# find('radius')

# change_label('site', 'Attribute', 'Object')

# change_relationship('attribute', 'availability', 'specifies', 'part_of', 'object', 'environment')

# create_node(distance)

# del_relationship('variable', 'distance to coast', 'describes', 'object', 'site')

# delete_node('attribute', 'name')

create_relationship('variable', 'inertia coefficient', 'describes', 'attribute', 'structure of the support structure')

# create_node(avail)

# create_property('attribute', 'availability', 'name', 'availability of OWF')

# change_property('attribute', 'availability', 'name', 'availability of OWF')


# del_node('object', 'foundation')

# neighbours('attribute', 'availability of owf')

print(exe("match (n:Variable) where n.name contains \'cable\' return n"))