1- Tener el certificado modelo en .jpg, .png o .svg.
	(Basili: Con .svg el 1C2020 me fallaba y cuando probe con .png anduvo bien)
2- Colocar en "participantes.xlsx" los nombres de los participantes. En la primer columna colocar el 
   nombre que aparecerá en el certificado y en la segunda el nombre con la que se exportará el archivo. 
3- Con inkscape (versiones 0.92.x, preferentemente la 0.92.5) abrimos el certificado modelo y 
   agregamos como texto "%s" donde queremos colocar el nombre y le asignamos la font, el tamaño 
   y la configuración deseada. Luego lo guardamos como modelo_certificado.svg.
4- Abrimos con un editor de texto plano (Ej: Visual studio Code) el modelo_certificado.svg y al final debería
   aparecer la configuración del texto del nombre. Donde indique "font_size:" modificamos el número que diga 
   por "%d". Revisar que antes del llamado a la función que genera los certificados hay una función que calcula
   en función del largo del nombre el tamaño de la letra, puede ser necesario que se la modifique.
5- Ejecutar el codigo "python certificado.py".
6- Indicar por "Y" o "N" si se desean remplazar los certificados que ya se encuentran en certificados 
   generados por los nuevos con el mismo nombre.  
7- Para cada alumno el código:
	a- Se va a crear un nombrealumno.svg donde copiara el certificado
           modelo.
	b- Se remplazará el %s por el nombre del alumno en cuestión.
	c- Se lo exportara como nombrealumno.pdf en la carpeta certificados generados sólo si no
	   existe el archivo ó si ya existe pero el usuario quiere regenerarlo.
	d- Se borrará el nombrealumno.svg.


Proyecto basado en: https://github.com/IEEESBITBA/certificate-generator