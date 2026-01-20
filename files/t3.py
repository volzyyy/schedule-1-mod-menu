import json
def view_storage(name,filename1):
     with open(fr"{filename1}\Properties\{name}.json","r") as f:
          data = json.load(f)
          #print(data["Objects"])
          for obj in data["Objects"]:
               if obj["DataType"] == "PlaceableStorageData":
                    bd = json.loads(obj["BaseData"])
                    stringitem= json.loads(bd["ItemString"])
                    if stringitem["ID"] != "bed":
                         if stringitem["ID"] == "smallstoragerack":
                              print("-"*30)
                              print(stringitem["ID"])
                              print(bd["GUID"])
                              for x in range(6):
                                   tfe = json.loads(bd["Contents"]["Items"][x])
                                   print(tfe["ID"],tfe["Quantity"])
                         elif stringitem["ID"] == "mediumstoragerack":
                              print("-"*30)
                              print(stringitem["ID"])
                              print(bd["GUID"])
                              for x in range(6):
                                   tfe = json.loads(bd["Contents"]["Items"][x])
                                   print(tfe["ID"],tfe["Quantity"])
                         elif stringitem["ID"]== "largestoragerack":
                              print("-"*30)
                              print(stringitem["ID"])
                              print(bd["GUID"])
                              for x in range(6):
                                   tfe = json.loads(bd["Contents"]["Items"][x])
                                   print(tfe["ID"],tfe["Quantity"])
