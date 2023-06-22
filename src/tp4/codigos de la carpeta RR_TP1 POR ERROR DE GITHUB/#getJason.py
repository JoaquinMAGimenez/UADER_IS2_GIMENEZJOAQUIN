#getjason.py
# uncompyle6 version 3.9.0
# Python bytecode version base 2.7
# Decompiled from: Python 3.7.9
# Embedded file name: getJason.py
import json
import sys
import random

def ayuda():
    print('-Para la ejecucion del programa se necesita pasarle un archivo json con los token')
    print('-el archivo devolvera un token a utilizar')
    print('-Si se encuentran 2 tokens o mas en json se debe modificar el programa para que los lea')
try:
    jsonfile = sys.argv[1]
    if (jsonfile == '-h'):
        ayuda()
    else:
    
        with open(jsonfile, 'r') as (myfile):
            data = myfile.read()
        obj = json.loads(data)
        index = random.randint(1, 2)
        print(str(obj['token' + str(index)]))
        
except:
    print('Ingrese una fuente de tokens o -h para obtener ayuda')