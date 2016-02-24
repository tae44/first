import paramiko

def ssh():
    host = input('Enter the host ip: ')
    user = input('Enter the user: ')
    passwd = input('Enter the password: ')
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(host,username=user,password=passwd)
    choose = input('Use command or ftp: ')
    if choose == 'command':
        comm = input('Enter the command: ')
        i, j, k = c.exec_command(comm)
        print(j.readlines())
        c.close()
    elif choose == 'ftp':
        ftp = c.open_sftp()
        choose_ftp = input('get or pull: ')
        if choose_ftp == 'get':
            get_file = input('Which file do you get: ')
            local_path = input('Where do you want to put: ')
            ftp.get(get_file, local_path)
            ftp.close()
        elif choose_ftp == 'pull':
            pull_file = input('Which file do you pull: ')
            remote_path = input('Where do you want to put: ')
            ftp.put(pull_file, remote_path)
            ftp.close()

ssh()
