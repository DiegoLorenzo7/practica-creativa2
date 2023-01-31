#!/usr/bin/python3

import logging
import sys
from subprocess import call
import os

# ACTUALIZAMOS EL VALOR DE LA VARIABLE DE ENTORNO
numeroGrupo = os.environ.get("GROUP_NUMBER")

# CLONAMOS EL REPOSITORIO	
call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])

# ACTUALIZAMOS EL SISTEMA
call(["sudo", "apt-get", "update"])

# INSTALAMOS EL ADMINISTRADOR DE PAQUETES PIP
call(["sudo", "apt-get", "install", "python3-pip"])

# AÑADIMOS LOS REQUIREMENTS
call(["pip3", "install", "-r", "practica_creativa2/bookinfo/src/productpage/requirements.txt"])

# MODIFICAMOS EL TITULO DE LA APLICACION
call(["cp", "practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "practica_creativa2/bookinfo/src/productpage/templates/productpageCopia.html"])
fCopia = open("practica_creativa2/bookinfo/src/productpage/templates/productpageCopia.html", 'r')
fOriginal = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", 'w')
for line in fCopia:
    if "{% block title %}Simple Bookstore App{% endblock %}" in line:
        fOriginal.write("{% block title %}Simple Bookstore App - GRUPO " + numeroGrupo + "{% endblock %}")
    else:
        fOriginal.write(line)
fOriginal.close()
fCopia.close()

# ARRANCAMOS LA APLICACIÓN
call(["python3", "practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"])
