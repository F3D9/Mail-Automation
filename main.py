import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from colorama import Fore

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

addressees = []


def send_email():
    
    #Get the email and the password of the sender
    variable2 = False
    EMAIL_ADDRESS = input(Fore.GREEN + "your email: " )
    while variable2 == False:
            if "@" in EMAIL_ADDRESS:

                variable2 = True
            else: 
                print(Fore.RED +"That's not an adress" )
                EMAIL_ADDRESS = input(Fore.GREEN + "adress email: ")
    
    
    print(Fore.GREEN + "This program DOES NOT SAVE YOUR PASSWORD, if you want to be sure you can see the database.")
    print("The password is a google application password, you can get it from here: ")
    print(Fore.BLUE + "https://acortar.link/qCCPPg")
    EMAIL_PASSWORD = input(Fore.GREEN + "your password: ")
    
    addressees.clear()
    
    #Get the mensaje and the number of addressees
    title = input(Fore.GREEN + "Subject: ")
    message = input("Message: ")    
    try:
        persons = int(input(Fore.GREEN + "how many addressees: "))
    except ValueError:
        while(type(persons) != int()):
            print(Fore.RED + "Only numbers")
            persons = int(input(Fore.GREEN + "how many addressees: "))
    
    
    #Get the addressees
    for i in range(persons):
        adress_email = input(Fore.GREEN + "adress email: ")
        variable = False
        while variable == False:
            if "@" in adress_email:
                addressees.append(adress_email)
                variable = True
            else: 
                print(Fore.RED + "That's not an adress")
                adress_email = input(Fore.GREEN + "adress email: ")

    for person in addressees:
        try:
            # Create the message
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = person
            msg['Subject'] = title

            # Body of the mail
            msg.attach(MIMEText(message, 'plain'))

            # Conect with the server
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
                print(Fore.GREEN + f"Correo enviado a {person}")
            
            #Create the register in the data base
        
            conn = sqlite3.connect("dataBase.db")
            cur = conn.cursor()
            
            cur.execute(f"INSERT INTO Registers (SendersMail,Subject,Message,RecipentsMail) VALUES ('{EMAIL_ADDRESS}','{title}','{message}','{person}')")
            conn.commit()
                
            cur.close()    
            
        except Exception as e:
            print(Fore.RED + f"Error al enviar correo a {person}: {e}")

        

send_email()





        

    
















































