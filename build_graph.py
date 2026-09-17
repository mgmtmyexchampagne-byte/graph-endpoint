import rdflib


def build_graph():
    # Initialize Graph
    graph = rdflib.Graph()

    # Load RDF Turtle File
    graph.parse("artist.ttl", format="turtle")

    # Export as JSON-LD for search engines
    graph.serialize(destination="artist.jsonld", format="json-ld", encoding="utf-8")

    print(f"Graph built successfully! Exported artist.jsonld ({len(graph)} triples).")


if __name__ == "__main__":
    build_graph()
