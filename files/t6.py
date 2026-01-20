import json

def change_pot_data(name, filename1):
    path = fr"{filename1}\Properties\{name}.json"

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    inp = input("Enter pot GUID: ").strip()
    changed = False

    for obj in data["Objects"]:
        if obj["DataType"] != "PotData" or len(obj["AdditionalDatas"]) != 1:
            continue

        bd = json.loads(obj["BaseData"])
        if bd["GUID"] == inp:
            print("\n✅ POT FOUND")
            print("Option 1: Change seed id")
            print("Option 2: Change growth progress")
            print("Option 3: Change soil uses")
            inpp = input("Choose choice: ")
            if inpp == "1":
                new_seed = input("Change seed ID: ").strip()

                seedi = json.loads(obj["AdditionalDatas"][0]["Contents"])
                seedi["Seed"]["ItemID"] = new_seed

                # write it back into Contents
                obj["AdditionalDatas"][0]["Contents"] = json.dumps(seedi, indent=4)

                changed = True
                break
            if inpp == "2":
                gp = float(input("Enter growth (0-1): "))
                bd["PlantData"]["GrowthProgress"] = gp
                # write BaseData back
                obj["BaseData"] = json.dumps(bd)
                changed = True
            if inpp == "3":
                rs = int(input("Change amout of remaining soil uses: "))
                bd["RemainingSoilUses"]=rs
                obj["BaseData"] = json.dumps(bd)
                changed = True
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("💾 Saved successfully")
    else:
        print("❌ Pot not found")
