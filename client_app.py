# importing required modules 
from flask import Flask,abort,jsonify,request,session,Response
from xml.etree import cElementTree as ET
from zipfile import ZipFile 
import os
    

app = Flask(__name__)

@app.route('/aadhaar_upload',methods = ['POST'])

def main():
    headers = request.headers
    apikey = headers.get("api-key")
    org_id = headers.get("org-id")
    print(apikey,org_id)
    data = request.get_json(force=True)
    aadhaar = data['aadhaar']
    share_code = data['share_code']
    # specifying the zip file name 
    file_path = data['file']
    password = b'1234'

    try:
        folder = file_path.split(".zip")[0]
        os.mkdir(folder)
    except FileExistsError:
        folder = file_path.split(".zip")[0]


    # opening the zip file in READ mode 
    with ZipFile(file_path, 'r') as zip: 
        # printing all the contents of the zip file 
        zip.printdir() 

        # extracting all the files 
        print('Extracting all the files now...') 
        zip.extractall(path= folder, pwd=password) 
        print('Done!') 

    file_name = folder.split("/")[-1]
    tree = ET.parse(f"{folder}/{file_name}.xml")
    root = tree.getroot()
    page = root.findall('UidData')[0]
    print("dob = ",page.find('Poi').get('dob'))
    print("e = ",page.find('Poi').get('e'))
    print("gender = ",page.find('Poi').get('gender'))
    print("m = ",page.find('Poi').get('m'))
    print("name = ",page.find('Poi').get('name'))
    print("careof = ",page.find('Poa').get('careof'))
    print("country = ",page.find('Poa').get('country'))
    print("dist = ",page.find('Poa').get('dist'))
    print("house = ",page.find('Poa').get('house'))
    print("landmark = ",page.find('Poa').get('landmark'))
    print("loc = ",page.find('Poa').get('loc'))
    print("pc = ",page.find('Poa').get('pc'))
    print("po = ",page.find('Poa').get('po'))
    print("state = ",page.find('Poa').get('state'))
    print("street = ",page.find('Poa').get('street'))
    print("subdist = ",page.find('Poa').get('subdist'))
    print("vtc = ",page.find('Poa').get('vtc'))

    return jsonify(dob = page.find('Poi').get('dob'),
                   e = page.find('Poi').get('e'),
                   gender = page.find('Poi').get('gender'),
                   m = page.find('Poi').get('m'),
                   name = page.find('Poi').get('name'),
                   careof = page.find('Poa').get('careof'),
                   country = page.find('Poa').get('country'),
                   dist = page.find('Poa').get('dist'),
                   house = page.find('Poa').get('house'),
                   landmark = page.find('Poa').get('landmark'),
                   loc = page.find('Poa').get('loc'),
                   pc = page.find('Poa').get('pc'),
                   po = page.find('Poa').get('po'),
                   state = page.find('Poa').get('state'),
                   street = page.find('Poa').get('street'),
                   subdist = page.find('Poa').get('subdist'),
                   vtc = page.find('Poa').get('vtc'))

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    #sess.init_app(app)

    app.run("0.0.0.0",debug=True)
    
    
### USAGE ###

## RUN THIS IN ANOTHER SCRIPT

# import requests

# url = "http://127.0.0.1:5000"

# response = requests.request("POST", url)

# print(response.text)
