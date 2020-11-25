from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from contadorPalabras import limpiarCaracteres
from contadorPalabras import contadorPalabras2
from contadorPalabras import convertirFecha
import pyautogui
import time
import random
import json
import csv
import collections
from wordcloud import WordCloud, ImageColorGenerator
from datetime import datetime
import matplotlib.pyplot as plt






url = 'https://www.youtube.com/watch?v=OqMrbhbkY9M&t=1s'

x_arrow = 1356
y_arrow = 718
csv_output = 'csvOutput.csv'

palabrasMap = {}
commentsTest = {}
commentsListJson = []
commentsListCsv = []
palabrasTotal = []

pyautogui.FAILSAFE = True
#print (pyautogui.size())
#print (pyautogui.position())
#random.randrange(1000, 9999)
#print (pyautogui.position()[0])



def start(url, x_arrow, y_arrow):
    now = datetime.now()
    print(now.time())
    palabrasTotalString = ''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(5)
    pyautogui.moveTo(x_arrow, y_arrow, duration = 1.1)
    contadorClicks = 0
    #while pyautogui.position()[0] == 1356: 
    while contadorClicks < 100:
        contadorClicks += 1
        time.sleep(random.randrange(1, 2))
        for y in range(random.randrange(10, 30)):
            pyautogui.click(pyautogui.position()[0],pyautogui.position()[1])
            #print (f'Clicks... {contadorClicks}')

    #if pyautogui.position()[0] != 1356:
    #time.sleep(random.randrange(1, 3))
    comentarios = driver.find_element_by_class_name('style-scope ytd-item-section-renderer').find_elements_by_class_name('style-scope ytd-comment-thread-renderer')
    tituloCanal = driver.find_element_by_class_name('style-scope ytd-channel-name').find_element_by_id('text-container').text
    suscriptoresCanal = driver.find_element_by_id('owner-sub-count').text 
    #document.querySelector('.style-scope ytd-channel-name').querySelector('#text-container').innerText
    tituloVideo = driver.find_element_by_tag_name('h1').find_element_by_tag_name('yt-formatted-string').text
    fechaVideo = driver.find_element_by_id('info').find_element_by_id('info-text').find_element_by_id('date').text
    visitasVideo = driver.find_element_by_id('info').find_element_by_id('info-text').find_element_by_id('count').text
    meGustaVideo = driver.find_element_by_id('info').find_elements_by_class_name('yt-simple-endpoint')[1].text
    noMeGustaVideo = driver.find_element_by_id('info').find_elements_by_class_name('yt-simple-endpoint')[2].text 
    #document.querySelector('#info').querySelectorAll('.yt-simple-endpoint')[x].innerText
    #published-time-text

    #document.querySelector('#info').querySelector('#info-text').querySelector('#date').innerText
    titulo = 'documental'
    fechaVideo = convertirFecha(fechaVideo)
    print(tituloVideo, fechaVideo, visitasVideo)
    print(f'Procesando {len(comentarios)} comentarios...')
    now = datetime.now()
    print(now.time())

    for x in range(len(comentarios)):
        user = comentarios[x].find_element_by_id('comment').find_element_by_id('body').find_element_by_id('main').find_element_by_id('header').find_element_by_id('header-author').find_element_by_id('author-text').find_element_by_tag_name('span').text
        comentario =  comentarios[x].find_element_by_id('comment').find_element_by_id('body').find_element_by_id('main').find_element_by_id('expander').find_element_by_id('content').find_element_by_id('content-text').text
        meGustaComentario = comentarios[x].find_element_by_id('body').find_element_by_id('main').find_element_by_id('action-buttons').find_element_by_id('toolbar').find_element_by_tag_name('span').get_attribute('innerHTML')
        meGustaComentario = meGustaComentario.replace(' ','')
        meGustaComentario = meGustaComentario.replace('\n','')
        #querySelector('#body').querySelector('#main').querySelector('#action-buttons').querySelector('#toolbar').querySelector('span').innerText
        #print('***************************')
        #print (f'Usuario: {user}')
        #print (f'MeGustaComentario: {meGustaComentario}')
        commentsListCsv.append((user, comentario))
        
        commentsListJson.append({'user':user, 'url':url, 'comment':comentario, 'meGustaComentario':meGustaComentario ,'tituloCanal':tituloCanal , 'suscriptoresCanal':suscriptoresCanal,'tituloVideo':tituloVideo,'fechaVideo':fechaVideo, 'visitasVideo':visitasVideo, 'meGustaVideo':meGustaVideo, 'noMeGustaVideo':noMeGustaVideo})
        '''
        print(user)
        print(comentario)
        print(likes)
        print(type(likes))
        '''
        palabras = comentario.split()
        
        for palabra in palabras:
            palabra = palabra.lower()
            palabra = limpiarCaracteres(palabra)
            if len(palabra) > 3:
                palabrasMap.update({palabra : 1})
                palabrasTotal.append(palabra)
                palabrasTotalString +=palabra +' '

    #print (palabrasMap)
    #contadorPalabras(palabrasMap)
    #print (palabrasTotal)
    #print(palabrasTotalString)
    #wordcloud = WordCloud(width=1024, height=1024, margin=0).generate(palabrasTotalString)
    #wordcloud.to_file(f'./nubes/july3p.png')
    '''
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()
    '''
    #contadorPalabras2(palabrasTotal)       

    save2json(titulo, commentsListJson)
    save2csv(titulo, commentsListCsv)

def save2json(titulo, commentsList):
    file = './salidas/'+titulo+'.json'
    with open (file,'w',encoding="utf-8") as outfile:
        print('Creando archivo json...')
        json.dump(commentsList, outfile, indent = 4)
        print(f'Comentarios guardados en {file}')
    now = datetime.now()
    print(now.time())

def save2csv(titulo, commentsList):
    file = './salidas/'+titulo+'.csv'
    with open (file,'wt',encoding='utf-8',newline='') as outfile:
        header = ['usuario','comentario']
        writer = csv.writer(outfile,quoting=csv.QUOTE_NONE, delimiter='\t',escapechar='\\')
        writer.writerow(header)
        print(f'Creando archivo de salida...')
        for x in range(len(commentsList)):
            #print(commentsList[x][0])
            csv_usuario = commentsList[x][0]
            csv_comentario = commentsList[x][1]
            writer.writerow([csv_usuario,csv_comentario])

        print('Archivo csv creado.')


start(url, x_arrow, y_arrow)


#nodeList de comentarios
#document.querySelector('.style-scope ytd-item-section-renderer').querySelectorAll('.style-scope ytd-comment-thread-renderer')
#querySelector('#comment').querySelector('#body').querySelector('#main').querySelector('#expander').querySelector('#content').querySelector('#content-text').innerText
#document.querySelector('.style-scope ytd-item-section-renderer').querySelectorAll('.style-scope ytd-comment-thread-renderer')[0].querySelector('#comment').querySelector('#body').querySelector('#main').querySelector('#expander').querySelector('#content').querySelector('#content-text').innerText

#titulo
#document.querySelector('#info').querySelector('#info-contents').querySelector('ytd-video-primary-info-renderer').querySelector('h1').innerText
#visitas y fecha del video
#fecha del video: 
#document.querySelector('#info').querySelector('#info-text').querySelector('#date').innerText
#visitas:
#document.querySelector('#info').querySelector('#info-text').querySelector('#count').innerText

#me gusta del video
#document.querySelector('#info').querySelector('#text').innerText

#me gusta + y -
#document.querySelector('#info').querySelectorAll('.yt-simple-endpoint')[x].innerText


#me gusta de cada comentario...
#document.querySelector('.style-scope ytd-item-section-renderer').querySelectorAll('.style-scope ytd-comment-thread-renderer')[0].querySelector('#body').querySelector('#main').querySelector('#action-buttons').querySelector('#toolbar').querySelector('span').innerText
