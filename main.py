import json

import rdflib
from pyld import jsonld
from pyshacl import validate

with open("context.json", 'r') as f:
    context = json.load(f)
with open("blabla.json", 'r') as f:
    doc = json.load(f)

rdf = jsonld.to_rdf(doc, {
    'expandContext': context,  # contexte à appliquer
    'format': 'application/n-quads'})

with open("resultat.json", "w") as f:
    f.write(rdf)

with open("trace_model.shacl.ttl") as f:
    r = validate(rdf,
                 shacl_graph="trace_model.shacl.ttl",
                 abort_on_first=False,
                 allow_warnings=False,
                 meta_shacl=False,
                 advanced=False,
                 js=False,
                 debug=False)
    a,b,c = r
    print(a, b ,c )

#graphe = rdflib.Graph(f)
#graphe.open("store", create=True)
#graphe.parse("big.rdf")

# print out all the triples in the graph
#for subject, predicate, object in graphe:
   # print subject, predicate, object

