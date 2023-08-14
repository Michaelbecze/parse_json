import json

with open("example.json") as the_data:
    interface_data = the_data.read()

#makes the json a python dictionary
interface_dict = json.loads(interface_data)

#make an edit to the dictionary
interface_dict["interface"]["name"] = "new name"

#save to the json file
with open("example.json", "w") as fh:
    json.dump(interface_dict, fh)

print(interface_dict)


