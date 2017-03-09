from py2neo import Node, Relationship, Graph
from cost_breakdown.parse_cost_NREL import password

# owfgraph = Graph("https://ssanchezperezm:"+password+"@rw.owfgraph.lr.tudelft.nl:80/db/data/")
localgraph = Graph("http://ssanchezperezm:"+password+"@localhost:7471/db/data/", bolt=False)
localgraph2 = Graph("http://neo4j:"+password+"@localhost:7474/db/data/")

# exe = owfgraph.run
exe = localgraph.run
exe2 = localgraph2.run
#

class DESCRIBES(Relationship): pass
class APPEARS_IN(Relationship): pass
class VARIANT_OF(Relationship): pass
class PART_OF(Relationship): pass
class INPUT_TO(Relationship): pass
class OUTPUT_OF(Relationship): pass
class CAUSES(Relationship): pass
class AFFECTS(Relationship): pass
class INSTRUCTS(Relationship): pass
class MODIFIES(Relationship): pass
class MEASURES(Relationship): pass
class RELATES_TO(Relationship): pass


def make_node(label, name, author, **keywords):
        extra = ''
        for key in keywords.keys():
            extra += ', ' + key + ':"' + keywords[key] + '"'
        exe('CREATE (n:' + label.title() + '{name:"' + name + '", author:"' +
            author + '"' + extra + '}) return labels(n), n.name').dump()


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
    exe('MATCH (n:' + label.title() + '{name:\'' + name + '\'}) SET n.' + property_key + '=\'' + property_value +
              '\' return labels(n) as Label, n.' + property_key + ' as ' + property_key.title()).dump()


# Delete relationship between two nodes. Requires source and target's label and name, and relationship type.
def delete_relationship(label_source, name_source, relationship, label_target, name_target):
    exe('MATCH (n:' + label_source.title() + '{name:\'' + name_source + '\'})-[k:' + relationship.upper() + ']-(o:' +
        label_target.title() + '{name:\'' + name_target + '\'}) DELETE k')
    print('Relationship deleted: (' + name_source + ') -- [' + relationship.upper() + '] --> (' + name_target + ')')


# Delete node with relationships. Requires node's label and name.
def delete_node(label, name):
    exe('MATCH (n:' + label.title() + '{name:\'' + name + '\'}) detach DELETE n')
    # print('Node deleted: (' + label.title() + '{name: \'' + name + '\')')


# Create relationship between existing nodes by defining the node's label and name and relationship type.
def create_relationship(label_source, name_source, relationship, label_target, name_target):
    print('MATCH (n:' + label_source.title() + '{name:\'' + name_source + '\'}), (o:' + label_target.title() +
        '{name:\'' + name_target + '\'}) CREATE (n)-[r:' + relationship.upper() + ']->(o)')
    exe('MATCH (n:' + label_source.title() + '{name:\'' + name_source + '\'}), (o:' + label_target.title() +
        '{name:\'' + name_target + '\'}) CREATE (n)-[r:' + relationship.upper() + ']->(o)')
    print('Relationship created: (' + name_source + ') -- [' + relationship.upper() + '] --> (' + name_target + ')')


# Change the label of a relationship in case a mistake has been made.
def change_relationship(label_source, name_source, old_relationship, new_relationship, label_target, name_target):
    exe('MATCH (n:' + label_source.title() + '{name:\'' + name_source + '\'})-[k:' + old_relationship.upper() +
        ']-(o:' + label_target.title() + '{name:\'' + name_target + '\'}) CREATE (n)-[k2:' + new_relationship.upper() +
        ']->(o) WITH k DELETE k')
    print('Relationship changed to: (' + name_source + ') -- [' + new_relationship.upper() + '] --> (' + name_target +
          ')')


# Function to find all nodes that include 'name' in their names. This search is case insensitive.
def find(name):
    exe('match (n) where n.name =~  \'(?i).*' + name + '.*\' return labels(n) as Label, n.name as Name').dump()


# Function to see all nodes connecting up to 2 degrees from a particular node, given its label and name. Both are case
# insensitive.
def neighbours(label, name):
    exe('match p=(n:' + label.title() + ')--(m) where n.name =~  \'(?i).*' + name +
        '.*\' ''return distinct m.name as Source, labels(m) as Type_Source').dump()


# Change the label of a node
def change_label(old_label, name, new_label):
    exe('MATCH (n:' + old_label.title() + '{name:\'' + name + '\'}) SET n:' + new_label.title() + ' REMOVE n:' +
        old_label + ' RETURN n').dump()


# Same function to change or create a property of a node. Added to avoid confusion.
def change_property(label, name, property_key, property_value):
    return create_property(label, name, property_key, property_value)

def add_label(label, name, new_label):
    exe('match (n:' + label.title() + '{name:\'' + name + '\'}) set n:' + new_label + ' return n').dump()


# def delete_property():

if __name__ == '__main__':

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

    # find('radius')

    # change_label('site', 'Attribute', 'Object')

    # change_relationship('attribute', 'availability', 'specifies', 'part_of', 'object', 'environment')

    # create_node(distance)

    # del_relationship('variable', 'distance to coast', 'describes', 'object', 'site')

    # delete_node('attribute', 'name')

    # create_relationship('variable', 'distance to coast', 'describes', 'attribute', 'geographic location of site')

    # create_node(avail)

    # create_property('attribute', 'availability', 'name', 'availability of OWF')

    # change_property('attribute', 'availability', 'name', 'availability of OWF')

    # del_node('object', 'foundation')

    # neighbours('attribute', 'availability of owf')
    # exe("create (n:Variable:Nrelcostbreakdown{name:'Capital Expenditures (CapEx) cost', domain:'real', unit:'¤', author:'sebastian', desc:'All installed costs incurred prior to commercial operations date (COD). CapEx components include turbine, BOS, and soft costs.'})").dump()
    # exe("match (n:Maintenance) return n.name").dump()
