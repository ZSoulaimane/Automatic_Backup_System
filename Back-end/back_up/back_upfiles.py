import os
import stat
import sys
sys.path.append("Connexions")
sys.path.append("crontab")
from detectc import lastline
from Connexionssh import Connexionssh
import mysql.connector
import paramiko
from stat import S_ISDIR, S_ISREG
import re
import datetime


class getfiles(Connexionssh):

    def execute_cmd(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)

        res, err = stdout.read(), stderr.read()
        result = res if res else err

        return result.decode()




    def _sftp_get(self, remotefile, localfile):
        sftp = paramiko.SFTPClient.from_transport(self.t)
        sftp.get(remotefile, localfile)




    def _get_all_files_in_remote_dir(self, remote_dir):
        sftp = paramiko.SFTPClient.from_transport(self.t)
        all_files = list()
        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]

        files = sftp.listdir_attr(remote_dir)
        for file in files:
            filename = remote_dir + '/' + file.filename

            if stat.S_ISDIR(file.st_mode):  # Recursive processing if it is a folder
                all_files.extend(self._get_all_files_in_remote_dir(filename))
            else:
                all_files.append(filename)

        return all_files



    def insertserverdate(self,s,d):

        
       #connexion database
        connection = mysql.connector.connect(host="localhost",
                                            database="newbase",
                                            user="root",
                                            password="")

        mycursor = connection.cursor()
        x = "'"+s+"'"

        sql = "SELECT saving_date FROM serverinfo WHERE server_name = %s"
        val = (x)
        mycursor.execute(sql, val)
        
        myresult = mycursor.fetchall()

        sql = "INSERT INTO serverinfo (saving_date) VALUES (%s) WHERE server_name = %s"
        vals = (str(d) , x)
        mycursor.execute(sql, vals)

        sql = "INSERT INTO serverinfo (last_saving_date) VALUES (%s) WHERE server_name = %s"
        vale = (myresult, x)
        mycursor.execute(sql, vale)

        connection.commit()


    
    def insertsitedate(self,site,server,d):
            
        connection = mysql.connector.connect(host="localhost",
                                            database="newbase",
                                            user="root",
                                            password="")

        mycursor = connection.cursor()
        x = "'"+site+"'"

        sql = "SELECT saving_date FROM websiteinfo WHERE site_name = %s"
        val = ()
        mycursor.execute(sql, val)
        
        myresult = mycursor.fetchall()

        sql = "INSERT INTO websiteinfo (saving_date) VALUES (%s) WHERE site_name = %s"
        vals = (str(d) , x)
        mycursor.execute(sql, vals)

        sql = "INSERT INTO websiteinfo (last_saving_date) VALUES (%s) WHERE site_name = %s"
        vale = (myresult, x)
        mycursor.execute(sql, vale)


        self.insertserverdate(self,server,d)

        connection.commit()


    def insertdbinfo(self,path,dict,status):
    
        
       #connexion database
        connection = mysql.connector.connect(host="localhost",
                                            database="newbase",
                                            user="root",
                                            password="")

        mycursor = connection.cursor()

        sql = "INSERT INTO databaseinfo VALUES (%s,%s,%s,%s,%s,%s)"
        vals = (path, dict['dbname'], dict['dbuser'], dict['dbpass'], dict['dbhost'],status)
        mycursor.execute(sql, vals)


        connection.commit()




    def select(self):
        comment = "'"+lastline()+"'"
        dataBase = mysql.connector.connect(host="localhost",
                                        database="newbase",
                                        user="root",
                                        password="")
    
        cursorObject = dataBase.cursor() 
        
        # selecting query
        query = "SELECT name, type, status, server_name FROM back_up WHERE comments="+comment
        cursorObject.execute(query)
        
        myresult = cursorObject.fetchall()
        
        # disconnecting from server
        dataBase.close()

        return myresult




    def selectserver(self,name):
        dataBase = mysql.connector.connect(host="localhost",
                                        database="newbase",
                                        user="root",
                                        password="")
    
        cursorObject = dataBase.cursor() 
        
        # selecting query
        query = "SELECT host, username, password, path FROM serverinfo WHERE status='True' and name='"+name+"'"
        val = (name)
        cursorObject.execute(query, val)
        myresult = cursorObject.fetchall()
        
        # disconnecting from server
        dataBase.close()

        return myresult





    def selectwebsite(self,name):
        dataBase = mysql.connector.connect(host="localhost",
                                        database="newbase",
                                        user="root",
                                        password="")
    
        cursorObject = dataBase.cursor() 
        
        # selecting query
        query = "SELECT server_name, host, username, password, directory_path  FROM sitewebinfo inner join serverinfo on sitewebinfo.server_name=serverinfo.name WHERE webstatus='True' and site_name='"+name+"'"
        val = (name)
        cursorObject.execute(query, val)
        
        myresult = cursorObject.fetchall()
        
        # disconnecting from server
        dataBase.close()

        return myresult




    def selectservername(self):
        dataBase = mysql.connector.connect(host="localhost",
                                        database="newbase",
                                        user="root",
                                        password="")
    
        cursorObject = dataBase.cursor() 
        
        # selecting query
        query = "SELECT server_name FROM back_up WHERE status='False' and server_name !='NULL'"
        cursorObject.execute(query)
        myresult = cursorObject.fetchall()
        
        # disconnecting from server
        dataBase.close()

        return myresult

#--------------------------------------------------------------------------------------------------------


    # Back Up website
    def backserver(self,path):
        #path
        cmd = 'cd '+path[0]+' && zip -r /home/soulaimane/Desktop/example.zip '+path[1]
        ssh.execute_cmd(cmd)

        ssh._sftp_get('/home/soulaimane/Desktop/example.zip','example.zip')

        cmd='rm /home/soulaimane/Desktop/example.zip'
        ssh.execute_cmd(cmd)




    # Back Up server
    def backwebsite(self,path,txtpath):
        #path
        cmd = 'cd '+path+' && zip -r /home/soulaimane/Desktop/example1.zip'+txtpath
        ssh.execute_cmd(cmd)

        ssh._sftp_get('/home/soulaimane/Desktop/example1.zip','example1.zip')

        cmd='rm /home/soulaimane/Desktop/example.zip'
        ssh.execute_cmd(cmd)
    
#------------------------------------------------------------------------------------------------------------------


    def sftpr(self,remote_dir):
        sftp = paramiko.SFTPClient.from_transport(self.t)
        files = sftp.listdir_attr(remote_dir)
        lists=[]

        for entry in sftp.listdir_attr(remote_dir):
            mode = entry.st_mode
            if S_ISDIR(mode):
                lists.append(entry.filename)
                
        return lists



    # split function
    def splits(self,path):
        path = path[1:]
        x = path.split("/")
        text = ""

        for i in range(len(x)-1) :
            text = text+"/"+x[i]

        h = []
        h.append(text)
        h.append(x[-1])
        return h


#------------------------------------------- db BackUp ------------------------------------------------------------------------------------------------

    def parsing_db_info(self, location):
        sftp = self.ssh.open_sftp()
        config_path = location+"/wp-config.php"
        try:
            with open(config_path) as fh:
                content = fh.read()
            regex_db = r'define\(\s*?\'DB_NAME\'\s*?,\s*?\'(.*?)\'\s*?'
            regex_user = r'define\(\s*?\'DB_USER\'\s*?,\s*?\'(.*?)\'\s*?'
            regex_pass = r'define\(\s*?\'DB_PASSWORD\'\s*?,\s*?\'(.*?)\'\s*?'
            regex_host = r'define\(\s*?\'DB_HOST\'\s*?,\s*?\'(.*?)\'\s*?'         
            db_name = re.search(regex_db,content).group(1)
            db_user = re.search(regex_user,content).group(1)
            db_pass = re.search(regex_pass,content).group(1)
            db_host = re.search(regex_host,content).group(1)

            return {'dbname':db_name , 'dbuser':db_user , 'dbpass':db_pass , 'dbhost':db_host}

        except FileNotFoundError:
            print('File Not Found,',config_path)
            sys.exit(1)

        except PermissionError:
            print('Unable To read Permission Denied,',config_path)
            sys.exit(1)
            
        except AttributeError:
            print('Parsing Error wp-config seems to be corrupt,')
            sys.exit(1)
    
    def export(self,parse,location):
        #os.system(f'mysqldump --user={x[0][1]} --password={x[0][2]} {x[0][1]} > {x[0][1]}.sql')
        os.system('mysqldump --column-statistics=0 --user='+parse['dbuser']+' --password='+parse['dbpass']+' '+parse['dbname']+' > file.sql')
        ssh._sftp_put('file.sql', location+"/database.sql")
        os.system('rm file.sql')
        #subprocess.Popen('mysqldump -h localhost -P  -u -root newbase > appdb.sql', shell=True)
    

    def _sftp_put(self, remotefile, localfile):
        sftp = paramiko.SFTPClient.from_transport(self.t)
        sftp.put(remotefile, localfile)





if __name__ == "__main__":
    x = datetime.datetime.now()

    ssh = getfiles(hostname='soulaimane-VirtualBox', username='soulaimane', password=' ')
    ssh.connect()

    #cmd = 'cd /var && zip -r /home/test/Desktop/example.zip www'
    #ssh.execute_cmd(cmd)
    
    #ssh._sftp_get('/home/test/Desktop/example.zip','example.zip')

    #cmd='rm /home/test/Desktop/example.zip'
    #ssh.execute_cmd(cmd)

    back_ups = ssh.select()
    print(back_ups)

    for i in range (len(back_ups)):

        if (back_ups[i][2] == 'False' and back_ups[i][1] == 'SERVER'):
            y = ssh.selectserver(back_ups[i][0])


                     # update saving date,last saving
#---------------------------------------------------------------
            ssh.insertserverdate(back_ups[i][0], x)
#---------------------------------------------------------------
            directory = ssh.sftpr(y[0][3])
            for i in directory:
                path = y[0][3]+'/'+i
                
                parse = ssh.parsing_db_info(path)
        
                if parse['dbpass'] != 'password_here':
                    ssh.export(parse,path)
                    ssh.insertdbinfo(path,parse,'True')
                else :
                    ssh.insertdbinfo(path,parse,'False')


            splite = ssh.splits(y[0][3])
            ssh.backserver(splite)
    

    listservers = set(ssh.selectservername())

    for j in listservers :
        server = ssh.selectserver(str(j))
                        # update saving date,last saving
#---------------------------------------------------------------
        ssh.insertsitedate()
#---------------------------------------------------------------


        loops = getfiles(hostname= server[0],username= server[1],password= server[2])
        liste=[]

        for i in range (len(back_ups)):
            if (back_ups[i][2] == 'False' and back_ups[i][1] == 'WEBSITE' and back_ups[i][3] == j[0]):
                y = loops.selectwebsite(back_ups[i][0])
                liste.append(y[0])

                # update saving date,last saving
#---------------------------------------------------------------
                ssh.insertsitedate(y[0],j,x)
#---------------------------------------------------------------

        txtpath = ""

        for i in liste :
            parse = loops.parsing_db_info(i[4])
            if parse['dbpass']!='password_here':
                loops.export(parse,i[4])
                loops.insertdbinfo(i[4],parse,'True')
            else :
                loops.insertdbinfo(i[4],parse,'False')

            
            splitpath= loops.splits(i[4])
            txtpath = txtpath+" "+splitpath[1]
        
        loops.backwebsite(splitpath[0],txtpath)

        loops.close()

    ssh.close()