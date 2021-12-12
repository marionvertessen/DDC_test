import json

import pyshacl
import rdflib
from pyld import jsonld
from pyshacl import validate

with open("context.json", 'r') as f:
    context = json.load(f)
with open("Test.json", 'r') as f:
    doc = json.load(f)

rdf = jsonld.to_rdf(doc, {
    'expandContext': context,  # contexte à appliquer
    'format': 'application/n-quads'})

with open("resultat.json", "w",  encoding="utf-8") as f:
    f.write(rdf)

with open("trace_model.shacl.ttl") as f:
    r = pyshacl.validate(
        f,
        shacl_graph="trace_model.shacl.ttl",
        data_graph_format="ttl",
        shacl_graph_format="ttl",
        debug=True,
        serialize_report_graph="ttl"
    )
    a,b,c = r
    print(a, b ,c )

#graphe = rdflib.Graph(f)
#graphe.open("store", create=True)
#graphe.parse("big.rdf")

# print out all the triples in the graph
#for subject, predicate, object in graphe:
   # print subject, predicate, object

