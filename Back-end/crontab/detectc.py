import re
import os
import sys


def lastline():
    os.system('grep CRON /var/log/syslog >> sheet.txt')

    try:
        with open('hh.txt') as f:
            for line in f:
                pass
            last_line = line
        comment = r'# [a-zA-Z0-9-.]*'
        print(last_line)
        comment = re.search(comment,last_line).group()
        os.system('rm hh.txt')


    except FileNotFoundError:
        print('File Not Found')
        os.system('rm hh.txt')
        sys.exit(1)

    except PermissionError:
        print('Unable To read Permission Denied,')
        os.system('rm hh.txt')
        sys.exit(1)
        
    except AttributeError:
        print('Parsing Error wp-config seems to be corrupt,')
        os.system('rm hh.txt')
        sys.exit(1)

    return comment[2:]
#print(type(comment))

#f = open("/home/soulaimane/Desktop/working/demofile2.txt", "a+")
#f.write(comment[2:]+'\n')
#f.close()

