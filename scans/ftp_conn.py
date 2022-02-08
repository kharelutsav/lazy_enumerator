import ftplib
# from scans.ftp_controller import ftp_contorller

def ftp_conn(target):

    conn = ftplib.FTP()
    value = f'{target}'

    conn.connect(value, 21)

    try:
        conn.login('anonymous', 'anonymous')

        with open('21.txt', 'a') as ftp:
            ftp.write('\n\n [ FTP SCAN ] directory listing \n\n')
            ftp.write(conn.pwd())
    except:
        return
