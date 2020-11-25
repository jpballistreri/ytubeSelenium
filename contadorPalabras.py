import operator
import json

def limpiarCaracteres(palabra):
	chars=',."!¡¿?:;()-*='	
	vocalesAcento = 'áéíóú'

	for char in chars:
		palabra = palabra.replace(char,'')

	palabra.replace("'","")

	for char in vocalesAcento:

		if char == 'á':
			palabra = palabra.replace(char,'a')
		elif char == 'é':
			palabra = palabra.replace(char,'e')
		elif char == 'í':
			palabra = palabra.replace(char,'i')
		elif char == 'ó':
			palabra = palabra.replace(char,'o')
		elif char == 'ú':
			palabra = palabra.replace(char,'u')

	#print (len(palabra.split()))
	return palabra

def contadorPalabras(palabrasMap): 
	for (key, value) in palabrasMap.items():
		contador = value
		contador += 1
		palabrasMap.update({key : contador })
	
	for (key, value) in palabrasMap.items():
		print(f'{key} : {value}')

	
def contadorPalabras2(listaPalabras):
	frecuenciaPalabras = []
	frecuenciaPalabrasFinal = []
	frecuenciaListJson = []

	for palabra in listaPalabras:
		frecuenciaPalabras.append((palabra, listaPalabras.count(palabra)))

	frecuenciaPalabras = sorted(frecuenciaPalabras, reverse = 1, key = lambda x: x[1])	
	
	
	for i in frecuenciaPalabras:
		if i not in frecuenciaPalabrasFinal:
			frecuenciaPalabrasFinal.append(i)

	print(f'\nSe necontraron {len(listaPalabras)} palabras.\n')
	print(f'10 palabras más usadas... ')
	for x in range(10):
		print (frecuenciaPalabrasFinal[x])

	for palabra in frecuenciaPalabrasFinal:
		frecuenciaListJson.append({palabra[0]:palabra[1]})

	#print (frecuenciaListJson)

	save2json('test', frecuenciaListJson)

	#for x in range(len(frecuenciaPalabras)):


def save2json(titulo, commentsList):
    file = titulo+'.json'
    with open (file,'w',encoding="utf-8") as outfile:
        print('Creando archivo json...')
        json.dump(commentsList, outfile, indent = 4)
        print(f'Comentarios guardados en {file}')


def convertirFecha(fecha):
	fecha = fecha.split()
	dia = fecha[0].replace('•','')
	mes = fecha[1]
	if 'ene' in mes:
		mes = '01'
	elif 'feb' in mes:
		mes = '02'
	elif 'mar' in mes:
		mes = '03'
	elif 'abr' in mes:
		mes = '04'
	elif 'may' in mes:
		mes = '05'
	elif 'jun' in mes:
		mes = '06'
	elif 'jul' in mes:
		mes = '07'
	elif 'ago' in mes:
		mes = '08'
	elif 'sep' in mes:
		mes = '09'
	elif 'oct' in mes:
		mes = '10'
	elif 'nov' in mes:
		mes = '11'
	elif 'dic' in mes:
		mes = '12'
	anio = fecha[2]
	fecha = f'{dia}/{mes}/{anio}'
	return fecha




