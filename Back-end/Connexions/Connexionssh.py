import paramiko

class Connexionssh(object):

    def __init__(self, hostname, port=22, username=None, password=None, timeout=30):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout

        self.ssh = paramiko.SSHClient()

        self.t = paramiko.Transport(sock=(self.hostname, self.port))
    
        #a sample connecion to the server
    def _password_connect(self):
    
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.hostname, port=22, username=self.username, password=self.password)

        self.t.connect(username=self.username, password=self.password)  # sptf Remote Transfer Connection
    

    #if we need a private Host keys
    def _key_connect(self):
        self.pkey = paramiko.RSAKey.from_private_key_file('/home/roo/.ssh/id_rsa', )
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.hostname, port=22, username=self.username, pkey=self.pkey)

        self.t.connect(username=self.username, pkey=self.pkey)

    def connect(self):
        try:
            self._key_connect()
        except:
            print('ssh key connect failed, trying to password connect...')
            try:
                self._password_connect()
            except:
                print('ssh password connect faild!')

    def close(self):
        self.t.close()
        self.ssh.close()
    
if __name__ == "__main__":
    ssh = Connexionssh(hostname='test-VirtualBox', username='test', password=' ')
    ssh.connect()