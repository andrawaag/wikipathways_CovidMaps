import requests
import os

if not os.path.isdir("gpml"):
    os.makedirs("gpml")

headers = {
    'Content-Type': 'text/plain',
}

for sbml in os.listdir("submaps/"):
    if sbml.endswith(".xml"):
        print(sbml.replace(".xml", ".gpml"))
        with open('submaps/'+sbml, 'rb') as f:
            data = f.read()
            response = requests.post('https://minerva-service.lcsb.uni.lu/minerva/api/convert/CellDesigner_SBML:GPML', headers=headers, data=data)
            with open('gpml/'+sbml.replace(" ", "_").replace(".xml", ".gpml"), 'w') as fo:
                print(fo.write(response.text))