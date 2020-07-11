import smtplib

to = input("Enter the email:\n")

content = input("Enter the content \n")
def sendMail (to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ganesh.btb142000@gmail.com','Ganesh_01liv')
    server.sendmail('ganesh.btb142000@gmail.com',to,content)
    server.close()

sendMail(to,content)

# Enable Less Secure Apps on Gmail/ Google Account