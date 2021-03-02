1- Tener el certificado modelo en .jpg, .png o .svg.
2- Colocar en "participantes.xlsx" los nombres de los participantes. En la primer columna colocar el 
   nombre que aparecerá en el certificado y en la segunda el nombre con la que se exportará el archivo. 
3- Con inkscape (versiones 0.92.x, preferentemente la 0.92.5) abrimos el certificado modelo y 
   agregamos como texto "%s" donde queremos colocar el nombre y le asignamos la font, el tamaño 
   y la configuración deseada. Luego lo guardamos como modelo_certificado.svg
4- Ejecutar el codigo "python certificado.py".
5- Indicar por "Y" o "N" si se desean remplazar los certificados que ya se encuentran en certificados 
   generados por los nuevos con el mismo nombre.  
6- Para cada alumno el código:
	a- Se va a crear un nombrealumno.svg donde copiara el certificado
           modelo.
	b- Se remplazará el %s por el nombre del alumno en cuestión.
	c- Se lo exportara como nombrealumno.pdf en la carpeta certificados generados sólo si no
	   existe el archivo ó si ya existe pero el usuario quiere regenerarlo.
	d- Se borrará el nombrealumno.svg.


Proyecto basado en: https://github.com/IEEESBITBA/certificate-generator