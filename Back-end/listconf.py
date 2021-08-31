import mysql.connector
import stat
import sys
import re
sys.path.append("Connexions")
from Connexionssh import Connexionssh
import paramiko

class listfiles(Connexionssh):
    
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
    
    def insertintodbinfo(self,id,x):
    
       #connexion database
        connection = mysql.connector.connect(host="localhost",
                                            database="newbase",
                                            user="root",
                                            password="")

        mycursor = connection.cursor()

        name = x["ServerName"]

        sql = "INSERT INTO sitewebinfo (server_name,site_name,url_website, directory_path) VALUES (%s,%s,%s,%s)"
        val = (id,name[0:-4],x["ServerName"],x["Documentroot"])
        mycursor.execute(sql, val)

        connection.commit()
    
    def select(self):
        dataBase = mysql.connector.connect(host="localhost",
                                        database="newbase",
                                        user="root",
                                        password="")
    
        cursorObject = dataBase.cursor() 
        
        # selecting query
        query = "SELECT name,host,username,password FROM serverinfo"
        cursorObject.execute(query)
        
        myresult = cursorObject.fetchall()
        
        # disconnecting from server
        dataBase.close()

        return myresult
    
    def parsing_root_info(self,config_path):
        sftp = self.ssh.open_sftp()
        try:
            with sftp.open(config_path) as fh:
                content = fh.read().decode('utf-8')
            ServerName = r'\tServerName\s*([a-zA-Z1-9.]*)'
            Documentroot = r'\tDocumentRoot\s*([/a-zA-Z1-9]*)'         
            sitweb_name = re.search(ServerName,content).group(1)
            documentroot = re.search(Documentroot,content).group(1)
            return {'ServerName':sitweb_name , 'Documentroot':documentroot}

        except FileNotFoundError:
            print('File Not Found,',config_path)
            sys.exit(1)

        except PermissionError:
            print('Unable To read Permission Denied,',config_path)
            sys.exit(1)

        except AttributeError:
            print('Parsing Error conf seems to be corrupt,')
            sys.exit(1)


if __name__ == "__main__":
    
    ssh = listfiles(hostname='test-VirtualBox', username='test', password=' ')
    #ssh.connect()

    #files = ssh._get_all_files_in_remote_dir("/etc/apache2/sites-enabled")

    #print(ssh.select()[-1])
    server = ssh.select()[-1]

    test = listfiles(hostname=server[1] , username=server[2], password=server[3])
    test.connect()


    files = test._get_all_files_in_remote_dir("/etc/apache2/sites-enabled")
    print(files)

    for i in files :
        if i != '/etc/apache2/sites-enabled/000-default.conf':
            x = test.parsing_root_info(i)
            print(x)
            test.insertintodbinfo(server[0],x)
    
    ssh.close()
    test.close()