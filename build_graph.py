import json

import rdflib


def build_graph():
    # Initialize Graph
    graph = rdflib.Graph()

    # Load RDF Turtle File
    graph.parse("artist.ttl", format="turtle")

    # Export as JSON-LD for search engines
    jsonld_data = graph.serialize(format="json-ld")
    with open("artist.jsonld", "w", encoding="utf-8") as output_file:
        output_file.write(jsonld_data)

    print(f"Graph built successfully! Exported artist.jsonld ({len(graph)} triples).")


if __name__ == "__main__":
    build_graph()