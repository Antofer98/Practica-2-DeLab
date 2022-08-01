import requests
import json
from pprint import pp
import csv
from time import time, ctime, sleep


## Definimos la cabecera para la API de Meraki##

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

#####Funcion para listar todas las organizaciones a la cuales tenemos acceso#####
url='https://api.meraki.com/api/v1/organizations' #Se busca en la documentacion de la API
def get_Organizations():
    response = requests.request('GET', url, headers=headers, data = None)
    ##r = requests.get(url, headers=headers, data = None) #Solicitud a traves de Header
    response_json = json.loads(response.text)
    print('Si a continuacion la palabra que se vizualiza es: None, quiere decir que la consulta de las organizaciones de la API se realizo de manera existosa: \n',response.raise_for_status() )
    return response_json
response_json = get_Organizations()


def Name_Organizations(): #Busca el nombre de DeLab asociado a la organizacion y devuelve el ID
    DeLab=[]
    for i in range(len(response_json)):
        if(response_json[i]['name']=="DeLab"):    	    
            DeLab.append(response_json[i])
        DeLab.append(0)
    return DeLab[0]['id']
String_DeLab=Name_Organizations()


def getOrganizationDevices(String_DeLab): #Consulta los dispositivos de DeLab
    url1="https://api.meraki.com/api/v1/organizations/organizationId/devices".replace('organizationId', String_DeLab)
    response= requests.request('GET', url1, headers=headers, data = None)
    json_1= json.loads(response.text)
    print('Si a continuacion la palabra que se vizualiza es: None, quiere decir que se accedio correctamente a la organizacion DeLab: \n',response.raise_for_status() )
    return json_1
json_1= getOrganizationDevices(String_DeLab)    

def Type_Device(): #Consulta los Devices de la API y retorna una lista con las caracteristicas de los equipos de "wireless" y "appliance"
    saved_devices=[]
    for i in range(len(json_1)):
        if json_1[i]['productType']=='wireless' or json_1[i]['productType']=='appliance':
            saved_devices.append(json_1[i])
    return saved_devices
json_1=Type_Device()

with open('inventario.csv', 'w', newline='') as file:
     writer = csv.writer(file, delimiter=';')
     writer.writerow(json_1)
     print('Se creo el archivo .csv de diccionario que contiene las especificaciones de los dispositivos')
