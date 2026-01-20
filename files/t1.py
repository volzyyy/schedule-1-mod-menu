import json


def viewbank(filename1):
    with open(fr"{filename1}\Money.json","r",encoding="utf-8") as f:
             data = json.load(f)  # read
             print(data["OnlineBalance"])
def getmoneybank(money,filename1):
       with open(fr"{filename1}\Money.json", "r+", encoding="utf-8") as f:
                data = json.load(f)  # read
                data["OnlineBalance"] = float(money)
                f.seek(0)               
                json.dump(data, f,indent=4)      
                f.truncate()            
