from dotenv import load_dotenv
load_dotenv()
import os
import smtplib
from email.message import EmailMessage

USER_ADDRESS = os.environ.get('EMAIL_ADDRESS')
USER_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_TO = os.environ.get('EMAIL_TO')

msg = EmailMessage()
msg['Subject'] = 'Teste envio de e-mail II'
msg['From'] = USER_ADDRESS
msg['To'] = EMAIL_TO
msg.set_content('Olá, me chamo Taylon Camargo.\nVocê está recebendo o meu e-mail via script python.')

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(USER_ADDRESS, USER_PASSWORD)

        smtp.send_message(msg)

    print("E-mail enviado com sucesso.")
except Exception as e:
    print("Erro ao enviar o e-mail.")
    print(e)




