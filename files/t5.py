import json
def view_pot_data(name,filename1):
    with open(fr"{filename1}\Properties\{name}.json","r+", encoding="utf-8") as f:
        data = json.load(f)
        for obj in data["Objects"]:
            bd = json.loads(obj["BaseData"])
            if obj["DataType"] != "PotData" or len(obj["AdditionalDatas"]) != 1:
                continue
            print("-"*30)
            print(bd["GUID"])
            print(obj["AdditionalDatas"][0]["Contents"])
