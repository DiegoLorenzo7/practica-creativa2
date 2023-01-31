#! /usr/bin/python
from subprocess import call
import os
import sys

# Descargamos el repositorio 

call (["git", "clone", "https://github.com/DiegoLorenzo7/practica-creativa2"])

#instalamos pip
call(["sudo", "apt-get", "install", "python3-pip"])


# Instalamos dependencias 

call (["pip", "install", "-r" , "practica-creativa2/bookinfo/src/productpage/requirements.txt"])

#Creamos la variable del entorno
os.environ['GROUP_NUMBER']="37"
num_grupo= str(os.environ.get('GROUP_NUMBER'))

#Modificamos el titulo
call (["cp", "practica-creativa2/bookinfo/src/productpage/templates/productpage.html",
"practica-creativa2/bookinfo/src/productpage/templates/productpageCopy.html"])
fCopia = open ("practica-creativa2/bookinfo/src/productpage/templates/productpageCopy.html", 'r')
fOriginal = open ("practica-creativa2/bookinfo/src/productpage/templates/productpageCopy.html", 'w')
for line in fCopia:
        if "{% block title %} Simple Bookstore App{& endblock %}" in line:
             fOriginal.write("{% block title %} Simple Bookstore App - GRUPO " + num_grupo + "{% endblock %}") 
        else: fOriginal.write(line)
fOriginal.close()
fCopia.close()
#Lanzamos la aplicacion
call (["python3", "practica-creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"])
