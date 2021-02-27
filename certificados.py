#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen
import pandas as pd
import os

def generate_certificate(name, nombre_archivo):
    file = open("certificado_modelo.svg", "r", encoding="utf-8")
    content = file.read()

   #line = contenido_a_modificar #"""style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:85.33333588px;font-family:'Playfair Display';-inkscape-font-specification:'Playfair Display Italic';text-align:center;baseline-shift:baseline;text-anchor:middle">%s</flowPara></flowRoot><image"""

    #content[linea] = line % name

    file = open("certificados generados/%s.svg" % name, "w+", encoding="utf-8")

    file.write(content % name)
    file.close()

    x = Popen(['C:\Program Files\Inkscape\inkscape', "certificados generados/%s.svg" % name, \
       '--export-pdf=certificados generados/%s.pdf' % nombre_archivo])

    x.communicate()

    os.remove("certificados generados/%s.svg" % name)


#print(content)

primera_vez = input("Regenerar el svg? (y/n)")

if primera_vez=="y":
    x = Popen(["C:\Program Files\Inkscape\inkscape","-z", "-f", "certificado_modelo.pdf","-l","certificado_modelo.svg"])
    x.communicate()

#contenido_a_modificar = input("Ingrese contenido, con un %s en el nombre del participante:")

input("Modificar el svg y tocar enter....")

file = pd.read_excel("certificados.xlsx")

content = file.to_dict("records")

for file in content:
    print(file)
    nombre = file["Nombre Certificado"]
    nombre_archivo = file["Nombre Archivo"]
    print("Generando %s" % nombre)
    generate_certificate(nombre, nombre_archivo)

filename = "certificado_modelo.svg"



