
import json
def view_inv(filename1):
    with open(fr"{filename1}\Players\Player_0\Inventory.json","r",encoding="utf-8") as f:
                data = json.load(f)
                for x in data["Items"]:
                    item = json.loads(x)  # parse string as JSON
                    print(f"Name: {item['ID']}, Quantity: {item['Quantity']}, Packing type: {item.get('PackagingID', 'N/A')}")
def change_inv(filename1):
       with open(fr"{filename1}\Players\Player_0\Inventory.json", "r+", encoding="utf-8") as f:
                data = json.load(f)

                inp = input("Choose item ID to change: ")
                new_qty = int(input("Choose new quantity: "))

                for i, x in enumerate(data["Items"]):
                    item = json.loads(x)

                    if item.get("ID") == inp:
                        item["Quantity"] = new_qty
                        data["Items"][i] = json.dumps(item)
                        break

                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
