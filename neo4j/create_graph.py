from neo4j_config import graph
import json


# 生成人物节点和关系节点
def build_graph():
    # 创建角色
    with open("../spider/data/character_intro.json") as f:
        data = json.load(f)
        # print(data)
        for relation in data:
            # print(relation)
            # print(type(relation))
            # info=data[relation]
            # print(info)
            # print(type(info))
            info = data[relation]
            cypher = "MERGE(p:Person{name:'"+relation+"',"
            for attribute in info:
                cypher += attribute + ":'" + info[attribute] + "',"
            cypher = cypher[:-1]
            cypher += "})"
            # print(cypher)
            graph.run(cypher)

    # 创建关系
    with open("../spider/data/relation.json") as f:
        relations = json.load(f)
        for relation_dict in relations:
            head = relation_dict["entity_1"]
            tail = relation_dict["entity_2"]
            relationship = relation_dict["relationship"]
            relationship = relationship.replace(".", "")
            graph.run(
                "MATCH(head:Person),(tail:Person) \
            WHERE head.name='%s' AND tail.name='%s' \
            CREATE(head)-[r:%s]->(tail) return r"
                % (head, tail, relationship)
            )


if __name__ == "__main__":
    build_graph()
