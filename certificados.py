#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen
import pandas as pd
import os
from pathlib import Path


def generate_certificate(name, nombre_archivo):
    file = open("certificado_modelo.svg", "r", encoding="utf-8")
    content = file.read()

    file = open("certificados generados/%s.svg" % name, "w+", encoding="utf-8")

    file.write(content % name)
    file.close()

    x = Popen(['C:\Program Files\Inkscape\inkscape', "certificados generados/%s.svg" % name, \
       '--export-pdf=certificados generados/%s.pdf' % nombre_archivo])

    x.communicate()

    os.remove("certificados generados/%s.svg" % name)



# Descomentar si se desea generar un .svg en base al modelo_certificado.pdf
#
#primera_vez = input("Regenerar el svg? (y/n)")
#if primera_vez=="y":
#    x = Popen(["C:\Program Files\Inkscape\inkscape","-z", "-f", "certificado_modelo.pdf","-l","certificado_modelo.svg"])
#    x.communicate()


file = pd.read_excel("certificados.xlsx")

content = file.to_dict("records")
regenerar = 0
while ((regenerar != "y") and  (regenerar != "n")):
    regenerar = input("Desea regenerar los certificados ya existentes? (y/n)")


for file in content:
    nombre = file["Nombre Certificado"]
    nombre_archivo = file["Nombre Archivo"]

    if ( Path('certificados generados/'+ str(nombre_archivo) +'.pdf').is_file() and (regenerar == "n") ):
        print("El archivo de", nombre, "ya habia sido generado")

    else: 
        print("Generando %s" % nombre)
        print(file, "\n")
        generate_certificate(nombre, nombre_archivo)

print("Certificados Generados !!!")

