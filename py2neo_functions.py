# -- Every node requires at least a label, a name, a description and an author. The rest are optional but desired.

from py2neo import Graph
owfgraph = Graph("http://neo4j:kluyverwegwind@owfgraph.lr.tudelft.nl:7474/db/data/")
# owfgraph = Graph("http://neo4j:neo4j@localhost:7474/db/data/")
exe = owfgraph.cypher.execute


def make_node(label, name, description, author, **keywords):
        extra = ''
        for key in keywords.keys():
            extra += ', ' + key + ':"' + keywords[key] + '"'
        print(exe(
            'CREATE (n:' + label.title() + '{name:"' + name + '", description:"' + description + '", author:"' + author + '"' + extra + '}) return labels(n), n.name'))


# Create a new node with a dictionary as defined below.
# node_name = {'label': 'procedure',
#
#          'name': 'name_ex1',
#
#          'description': 'zGikkiG GG escedesc',
#
#          'author': 'sebastian',
#
#          'unit': '',
#
#          'domain': '',
#
#          'value': '',
#
#          'expression': 'sebast',
#
#          'reference': '',
#
#          'note': ''}

def create_node(node_name):
    node2 = {key: node_name[key] for key in node_name.keys() if node_name[key] != ''}
    order = 'make_node('
    i = 0
    for key in node2.keys():
        if i == 0:
            order += key + '="' + node2[key] + '"'
        else:
            order += ', ' + key + '="' + node2[key] + '"'
        i = 1
    order += ')'
    exec(order, globals(), locals())


# Add a missing property to an existing node. Requires node's label and name, and property and value to be added.
def create_property(label, name, property_key, property_value):
    print exe('MATCH (n:' + label.title() + '{name:\'' + name + '\'}) SET n.' + property_key + '=\'' + property_value +
              '\' return labels(n) as Label, n.' + property_key + ' as ' + property_key.title())


# Delete relationship between two nodes. Requires source and target's label and name, and relationship type.
def delete_relationship(label_source, name_source, relationship, label_target, name_target):
    exe('MATCH (n:' + label_source.title() + '{name:\'' + name_source + '\'})-[k:' + relationship.upper() + ']-(o:' +
        label_target.title() + '{name:\'' + name_target + '\'}) DELETE k')
    print('Relationship deleted: (' + name_source + ') -- [' + relationship.upper() + '] --> (' + name_target + ')')


# Delete node with relationships. Requires node's label and name.
def delete_node(label, name):
    exe('MATCH (n:' + label.title() + '{name:\'' + name + '\'}) DETACH DELETE n')
    print 'Node deleted: (' + label.title() + '{name: \'' + name + '\')'


# Create relationship between existing nodes by defining the node's label and name and relationship type.
def create_relationship(label_source, name_source, relationship, label_target, name_target):
    exe('MATCH (n:' + label_source.title() + '{name:\'' + name_source + '\'}), (o:' + label_target.title() + '{name:\'' + name_target + '\'}) CREATE (n)-[r:' + relationship.upper() + ']->(o)')
    print 'Relationship created: (' + name_source + ') -- [' + relationship.upper() + '] --> (' + name_target + ')'

# Change the label of a relationship in case a mistake has been made.
def change_relationship(label_source, name_source, old_relationship, new_relationship, label_target, name_target):
    exe('MATCH (n:' + label_source.title() + '{name:\'' + name_source + '\'})-[k:' + old_relationship.upper() + ']-(o:' +
        label_target.title() + '{name:\'' + name_target + '\'}) CREATE (n)-[k2:' + new_relationship.upper() + ']->(o) WITH k DELETE k')
    print 'Relationship changed to: (' + name_source + ') -- [' + new_relationship.upper() + '] --> (' + name_target + ')'

# Function to find all nodes that include 'name' in their names. This search is case insensitive.
def find(name):
    print exe('match (n) where n.name =~  \'(?i).*' + name + '.*\' return labels(n) as Label, n.name as Name')

# Function to see all nodes connecting up to 2 degrees from a particular node, given its label and name. Both are case insensitive.
def neighbours(label, name):
    print exe('match p=(n:' + label.title() + ')--(m) where n.name =~  \'(?i).*' + name + '.*\' return distinct m.name as Source, labels(m) as Type_Source')

# Change the label of a node
def change_label(name, old_label, new_label):
    print exe('MATCH (n:' + old_label.title() + '{name:\'' + name + '\'}) SET n:' + new_label.title() + ' REMOVE n:' + old_label + ' RETURN n')

# Same function to change or create a property of a node. Added to avoid confusion.
def change_property(label, name, property_key, property_value):
    return create_property(label, name, property_key, property_value)

if __name__ == '__main__':
    from vis import draw
    # -- When a key is not needed, the value can be left empty as '', or delete the key altogether. The outcome is the same.
    # -- The label is NOT case sensitive. So 'variAblE' is converted into 'Variable'.
    node1 = {'label': 'procedure',

             'name': 'name_ex1',

             'description': 'zGikkiG GG escedesc',

             'author': 'sebastian',

             'unit': '',

             'domain': '',

             'value': '',

             'expression': 'sebast',

             'reference': '',

             'note': ''}

    # add_node(node1)
    # add_property('object', 'name_ex3', 'note', 'Insert a note here.')
    # add_relationship('object', 'name_ex3', 'KIND_OF', 'attribute', 'name_ex2')
    # del_relationship('object', 'name_ex3', 'KIND_OF', 'attribute', 'name_ex2')

    query = "match (m:Model)-[]-(v) where m.name={name} return v.name as Variable"

    # print exe(query, name='m31')