#!/usr/bin/python3

# REALIZADO POR GABRIEL ARTERO MONSALVATJE Y CARLOTA RUIZ DE CONEJO DE LA SEN

import logging
import sys
from subprocess import call
import os


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('pc2')


# GUARDAMOS EL VALOR DE LA VARIABLE DE ENTORNO
numeroGrupo = os.environ.get("GROUP_NUMBER")

# COMANDOS NECESARIOS PARA LA PUESTA EN MARCHA DE LA APLICACIÓN	
call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])
logger.debug("Repositorio clonado correctamente")

# ACTUALIZAMOS EL SISTEMA
call(["sudo", "apt-get", "update"])
logger.debug("Sistema actualizado")

# INSTALAMOS PIP
call(["sudo", "apt-get", "install", "python3-pip"])
logger.debug("pip se ha instalado correctamente")

# AÑADIMOS LOS REQUIREMENTS NECESARIOS
call(["pip3", "install", "-r", "practica-creativa2/bookinfo/src/productpage/requirements.txt"])
logger.debug("Las dependencias han sido instaladas")


# MODIFICAMOS EL TITULO DE LA APLICACION
call(["cp", "practica-creativa2/bookinfo/src/productpage/templates/productpage.html", "practica-creativa2/bookinfo/src/productpage/templates/productpageCopia.html"])
fCopia = open("practica-creativa2/bookinfo/src/productpage/templates/productpageCopia.html", 'r')
fOriginal = open("practica-creativa2/bookinfo/src/productpage/templates/productpage.html", 'w')
for line in fCopia:
    if "{% block title %}Simple Bookstore App{% endblock %}" in line:
        fOriginal.write("{% block title %}Simple Bookstore App - GRUPO " + numeroGrupo + "{% endblock %}")
    else:
        fOriginal.write(line)
fOriginal.close()
fCopia.close()
logger.debug("Se ha actualizado el título de la aplicación")


# ARRANCAMOS LA APLICACIÓN
call(["python3", "practica-creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"])
logger.debug("La aplicación se está ejecuntando correctamente. Puede acceder a ella desde https://<ip-publica>:9080/productpage")