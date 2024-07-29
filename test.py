import json

json_string = '{"name": "subhash","age": "22","dob": "07/06/2002","gender": "male"}'
data2 = json.loads(json_string)

val = input()

if(val=='name'):
    print (data2['name'])
elif (val == 'age'):
    print(data2['age'])
elif (val == 'dob'):
    print(data2['dob'])
elif (val == 'gender'):
    print(data2['gender'])
else:
    print("Enter Valid Credentials!!")
