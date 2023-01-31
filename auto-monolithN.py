#!/usr/bin/python


#PRACTICA CREATIVA 2


#CDPS

import sys
from subprocess import call 
import os

# Descargamos el repositorio 

call (["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])

#instalamos pip
call(["sudo", "apt-get", "install", "python3-pip"])


call(["sudo", "apt-get", "update"])
# Instalamos dependencias 

call (["pip3", "install", "-r" , "practica-creativa2/bookinfo/src/productpage/requirements.txt"])



#Guardamos la variable del entorno

num_grupo= str(os.environ.get ("GROUP_NUMBER"))



#Cambiamos titulo 
call (["cp", "practica-creativa2/bookinfo/src/productpage/templates/productpage.html",
"practica-creativa2/bookinfo/src/productpage/templates/productpageCopia.html"])
fCopia = open ("practica-creativa2/bookinfo/src/productpage/templates/productpageCopia.html", 'r')
fOriginal = open ("practica-creativa2/bookinfo/src/productpage/templates/productpageCopia.html", 'w')
for line in fCopia:
        if "{% block title %} Simple Bookstore App{& endblock %}" in line:
             fOriginal.write("{% block title %} Simple Bookstore App - GRUPO " + num_grupo + "{% endblock %}") 
        else: fOriginal.write(line)
fOriginal.close()
fCopia.close()



# Arrancamos aplicacion

call (["python3", "practica-creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"])
