# DeLab
Proyecto 2 de SDN

A continuacion se explica el trabajo que realiza cada funcion creada:

def get_Organizations(): "Se encarga de realizar una solicitud a las organizaciones de la API de meraki"

def Name_Organizations(): "Se encargar de recibir la palabra "DeLab" (Nombre de la organizacion que queremos trabajar) y compararla con todas las organizaciones letra a letra hasta coincidir con la organizacion en cuestion"

def getOrganizationDevices(String_DeLab): "Se encarga de recibir el nombre de la organizacion en cuestion y acceder a los dispositivos de la misma"

def Type_Device(): " Se encargar de guardar en una lista todas las caracteristicas de los equipos "wireless" y "appliance" con el nombre de saved_devices=[]"

Ademas para las funciones "ef get_Organizations():" y "def getOrganizationDevices(String_DeLab):" se hizo uso del metodo raise_for_status(), el cual arroja a la salida de un print un "None" si hubo una conexion satisfactoria con la API
