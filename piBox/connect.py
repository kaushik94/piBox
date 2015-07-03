import paramiko
import os

class SSHConnection(object):
 
    #----------------------------------------------------------------------
    def __init__(self, host, username, password, port=22):
        """Initialize and setup connection"""
        self.sftp = None
        self.sftp_open = False
 
        # open SSH Transport stream
        self.transport = paramiko.Transport((host, port))
 
        self.transport.connect(username=username, password=password)
 
    #----------------------------------------------------------------------
    def _openSFTPConnection(self):
        """
        Opens an SFTP connection if not already open
        """
        if not self.sftp_open:
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            self.sftp_open = True
 
    #----------------------------------------------------------------------
    def get(self, remote_path, local_path=None):
        """
        Copies a file from the remote host to the local host.
        """
        self._openSFTPConnection()        
        self.sftp.get(remote_path, local_path)        
 
    #----------------------------------------------------------------------
    def put(self, local_path, remote_path=None):
        """
        Copies a file from the local host to the remote host
        """
        self._openSFTPConnection()
        self.sftp.put(local_path, remote_path)

    def remove(self, local_path, remote_path=None):
        self._openSFTPConnection()
        if local_path in self.sftp.listdir('./'):
            self.sftp.remove(local_path.split('/')[-1], remote_path) 

    #----------------------------------------------------------------------
    def close(self):
        """
        Close SFTP connection and ssh connection
        """
        if self.sftp_open:
            self.sftp.close()
            self.sftp_open = False
        self.transport.close()

def connect(source, remove=False):
    f = open('server.conf','r')
    info = f.readlines()
    host = info[0].split(':')[0]
    username = info[1].strip('\n')
    pw = info[2].strip('\n')
    path = os.getcwd().split('/')
    path = '/'.join(path[:-1])+'/Box/'
    origin = path + source
    # origin = '/Users/ghost/Desktop/piBox/test/test.txt'
    dst = './Desktop/chutiyaap/' + source
 
    ssh = SSHConnection(host, username, pw)
    # ssh.exec_command('ls -l')
    if not remove:
        ssh.put(origin, dst)
    else:
        ssh.remove(origin, dst)
    ssh.close()