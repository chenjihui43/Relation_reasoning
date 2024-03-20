from py2neo import Graph

graph = Graph("http://localhost:7474", auth=("neo4j", "qmqn87158719"), name="hanwudi")


def delete_all_node():
    graph.run("match(n)detach delete n")


if __name__ == "__main__":
    delete_all_node()
