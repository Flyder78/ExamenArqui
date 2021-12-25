import smtplib

message='Hola este es un cronjob'
server =smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('yojamasxdpoder@gmail.com','2qa1ws..**')
server.sendmail('yojamasxdpoder@gmail.com','flydlerlegueoflegends@gmail.com',message)
server.quit()
print('Correo enviado')