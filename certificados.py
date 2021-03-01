#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen
import pandas as pd
import os

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

for file in content:
    nombre = file["Nombre Certificado"]
    nombre_archivo = file["Nombre Archivo"]
    print("Generando %s" % nombre)
    print(file)
    generate_certificate(nombre, nombre_archivo)



