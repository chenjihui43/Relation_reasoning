import json


# 获得人物列表，列表内包含所有人物，但是有重复
def get_character_arr():
    with open("data/relation.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        character_arr = []
        for entry in data:
            character_arr.append(entry["entity_1"])
            character_arr.append(entry["entity_2"])
    return character_arr


def test():
    data = get_character_arr()
    character_set = set(data)
    print(data)
    print(character_set)
    print(len(character_set))
    print(len(data))


if __name__ == "__main__":
    test()
    a=10
