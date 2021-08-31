#!/usr/bin/env python
import mysql.connector
from crontab import CronTab
import uuid

class cron(object):
    def select(self):
        
        dataBase = mysql.connector.connect(host="localhost",
                                        database="newbase",
                                        user="root",
                                        password="")

        cursorObject = dataBase.cursor() 

        # selecting query
        query = "SELECT minute, hour, day_Month, Month, day_Week, status FROM back_up WHERE status='False'"
        cursorObject.execute(query)
        myresult = cursorObject.fetchall()

        # disconnecting from server
        dataBase.close()

        return myresult
    

    def ajouterCrontab(self,key):

        liste = self.select()
        timing = liste[0][:-1]
        cronj = ""
        for i in timing:
            if i:
                cronj = cronj +i + ' '
            else:
                cronj = cronj + '* '


        my_cron = CronTab(user='soulaimane')

        job = my_cron.new(command='/bin/python3 /home/soulaimane/Desktop/working/crontab/back_upfiles.py', comment=str(key))
        job.setall(cronj[:-1])
        
        my_cron.write()
        return cronj
    


    def ajoutcronjobbase(self,time,key):
        connection = mysql.connector.connect(host="localhost",
                                            database="newbase",
                                            user="root",
                                            password="")

        mycursor = connection.cursor()

        sql = "INSERT INTO crontab (execution_time,comment) VALUES (%s,%s)"
        val = (time,key)
        mycursor.execute(sql, val)

        connection.commit()
    



    def updateback(self,key):
        connection = mysql.connector.connect(host="localhost",
                                    database="newbase",
                                    user="root",
                                    password="")

        mycursor = connection.cursor()

        key = "'"+key+"'"

        sql = "UPDATE back_up SET status = 'True',comments="+key+" WHERE status = 'False'"
        mycursor.execute(sql)

        connection.commit()





if __name__ == "__main__":
    sh = cron()
    key = uuid.uuid4()
    time = sh.ajouterCrontab(str(key))
    sh.ajoutcronjobbase(time,str(key))
    sh.updateback(str(key))