#!/usr/bin/python3

import logging
import sys
from subprocess import call
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('pc2')

# ACTUALIZAMOS EL VALOR DE LA VARIABLE DE ENTORNO
numeroGrupo = os.environ.get("GROUP_NUMBER")

# CLONAMOS EL REPOSITORIO	
call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])
logger.debug("Repositorio clonado")

# ACTUALIZAMOS EL SISTEMA
call(["sudo", "apt-get", "update"])
logger.debug("El sistema se ha actualizado")

# INSTALAMOS EL ADMINISTRADOR DE PAQUETES PIP
call(["sudo", "apt-get", "install", "python3-pip"])
logger.debug("pip se ha instalado")

# AÑADIMOS LOS REQUIREMENTS
call(["pip3", "install", "-r", "practica_creativa2/bookinfo/src/productpage/requirements.txt"])
logger.debug("Las dependencias han sido instaladas")

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
logger.debug("El titulo de la aplicación ha sido actualizado")

# ARRANCAMOS LA APLICACIÓN
call(["python3", "practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"])
logger.debug("La aplicación se está ejecuntando correctamente. Puede acceder a ella desde https://<ip-publica>:9080/productpage")
