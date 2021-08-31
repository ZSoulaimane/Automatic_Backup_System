import urllib.request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import mysql.connector



class PingingSystem(object):

    def pinging(self):
        
        lists=[]
        listwebsite = self.returnWebSites()
        lens = len(listwebsite)

        for i in range (lens):
            try:
                x = urllib.request.urlopen(listwebsite[i][1]).getcode()

                if (x==200 and listwebsite[i][2]!="True"):
                    self.updateStatus("True",listwebsite[i][1])
                    self.insertintopinging(listwebsite[i][0],"True")

            except:
                if(listwebsite[i][2]!="False"):
                    self.updateStatus("False",listwebsite[i][1])
                    lists.append(listwebsite[i][1])
            
        #self.mail(x) take of the '#' to send mails


    def returnWebSites(self):
        dataBase = mysql.connector.connect(host="localhost",
                                        database="newbase",
                                        user="root",
                                        password="")
    
        cursorObject = dataBase.cursor() 
        
        # selecting query
        query = "SELECT site_id,url_website,webstatus FROM sitewebinfo"
        cursorObject.execute(query)
        
        myresult = cursorObject.fetchall()
        
        # disconnecting from server
        dataBase.close()

        return myresult



    def updateStatus(self,status,siteweb):

        #connexion database
        connection = mysql.connector.connect(host="localhost",
                                        database="newbase",
                                        user="root",
                                        password="")


        mycursor = connection.cursor()

        sql = "UPDATE sitewebinfo SET webstatus = %s where url_website= %s" # inner join to siteweb
        val = (status,siteweb)
        mycursor.execute(sql, val)

        connection.commit()



    def insertintoerrormessage(self,website):
        
        #connexion database
        connection = PingingSystem("localhost","newbase","root","")
        connection.connexion()

        mycursor = connection.cursor()

        mycursor.execute("INSERT INTO errormsg (msg) VALUES ('{}')".format(website))

        connection.commit()


    def insertintopinging(self,id,status):
            
        #connexion database
        connection = PingingSystem("localhost","newbase","root","")
        connection.connexion()

        mycursor = connection.cursor()

        mycursor.execute("INSERT INTO pinging (id,status) VALUES ('{}')".format(id,status))

        connection.commit()



    def mail(self,x):
        mail_content = "the web sites "+ str(x) +" are down it should be restared in order to back it up on it's time\n thanks!"

        sender_address = 'soulaimane.studies@gmail.com' # your Email
        sender_pass = '' #your password here
        receiver_address = 'zar.Soulaimane@gmail.com'

        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'A Web Site is Down'

        message.attach(MIMEText(mail_content, 'plain'))

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass) 
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()

if __name__== "__main__":
    ss = PingingSystem()

    ss.pinging()
