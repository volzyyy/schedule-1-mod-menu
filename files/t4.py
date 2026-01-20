
import json
def change_storage(name,filename1):
    with open(fr"{filename1}\Properties\{name}.json","r+", encoding="utf-8") as f:
        data = json.load(f)
        found = False

        inp = input("Enter storage GUID: ").strip()

        for obj in data["Objects"]:
            if obj["DataType"] != "PlaceableStorageData":
                continue

            bd = json.loads(obj["BaseData"])

            if bd["GUID"] == inp:
                print("\n✅ STORAGE FOUND")

                for i, item_str in enumerate(bd["Contents"]["Items"]):
                    item = json.loads(item_str)
                    print(f"Slot {i}: {item['ID']} x{item['Quantity']}")

                slot = int(input("Choose slot: "))
                new_qty = int(input("Change quantity: "))

                item = json.loads(bd["Contents"]["Items"][slot])
                item["Quantity"] = new_qty
                bd["Contents"]["Items"][slot] = json.dumps(item)

                # write BaseData back
                obj["BaseData"] = json.dumps(bd)

                found = True
                break

        if not found:
            print("❌ No storage with that GUID")
        else:
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            print("💾 Saved successfully")
