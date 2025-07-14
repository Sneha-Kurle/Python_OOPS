import json
week={1:'Sunday', 2:'Monday',3:'tuesday',4:'wednesday',5:'thursday', 6:'Friday',7:'Saturday'}
file_name="C:\\Users\\sneha\\OneDrive\\Desktop\\file.json"
with open(file_name, 'w') as file:
    json.dump(week, file, indent=5)
    print(f"the json file '{file_name}' has created")