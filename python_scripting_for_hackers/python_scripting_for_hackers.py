"""
DOCSTRING
"""
import ftplib
import gzip
import os
import socket
import sys
import urllib

try:
    import pygeoip
except ImportError:
    print('[!] Failed to import pygeoip.')
    try:
        choice = input('[*] Attempt to auto-install pygeoip? [y/N]')
    except KeyboardInterrupt:
        print('\n[!] User interrupted choice')
        sys.exit(1)
        if choice.strip().lower()[0] == 'y':
            print('[*] Attempting to install pygeoip ...')
            sys.stdout.flush()
            try:
                import pip
                pip.main(['install', '-q', 'pygeoip'])
                import pygeoip
                print('DONE')
            except Exception:
                print(FAIL)
                sys.exit(1)
        elif choice.strip().lower()[0] == 'n':
            print('[*] User denied auto-install.')
            sys.exit(1)
        else:
            print('[!] Invalid decicion.')
            sys.exit(1)

def geolocate():
    """
    DOCSTRING
    """


def network_connection():
    """
    DOCSTRING
    """
    s = socket.socket()
    s.connect('192.168.1.109', 22)
    answer = s.recv(1024)
    print(answer)
    s.close

def password_cracker():
    """
    DOCSTRING
    """
    server = input('What is the IP address of the FTP server:')
    print(server)
    user_name = input('What user name are you trying to crack:')
    print(user_name)
    password_list = ('Provide the path and file name for your password list')
    print(password_list)
    try:
        with open(password_list, 'r') as password:
            for word in password:
                word = word.strip('\r')
                try:
                    ftp = ftplib.FTP(server)
                    ftp.login(user_name.word)
                    print('You have conncted to the FTP server.')
                    print('The password is' + word)
                    ftp.quit
                except:
                    print('Still trying . . .')
    except:
        print('There is a word list error. Either it is an incorrect path or does not exist.')

def print_variables():
    """
    DOCSTRING
    """
    string_variable = 'Hackers-Arise is the best place to learn hacking.'
    integer_variable = 12
    floating_point_variable = 3.1415
    list_variable = [1, 2, 3, 4, 5]
    dictionary_variable = {'name':'OccupyTheWeb', 'value':27}
    print(string_variable)
    print(integer_variable)
    print(floating_point_variable)
    print(list_variable[3])

class Locator():
    """
    DOCSTRING
    """
    def __init__(self, url=False, ip=False, dat_file=False):
        """
        DOCSTRING
        """
        self.url = url
        self.ip = ip
        self.dat_file = dat_file
        self.target = ''

    def check_database(self):
        """
        DOCSTRING
        """
        if not self.dat_file:
            self.dat_file = '/usr/share/GeoIP/GeoLiteCity.dat'
        else:
            if not os.path.isfile(self.dat_file):
                print('[!] Failed to detect specified database.')
                sys.exit(1)
            else:
                return
        if not os.path.isfile(self.dat_file):
            print('[!] Default database detection failed.')
            try:
                choice = input('[*] Attempt to auto-install database [y/N]:')
            except KeyboardInterrupt:
                print('\n[!]User interrupted choice.')
                sys.exit(1)
            if choice.strip().lower()[0] == 'y':
                print('[*] Attempting to auto-install database ...')
                sys.stdout.flush()
                if not os.path.isdir('/usr/share/GeoIP'):
                    os.makedirs('/usr/share/GeoIP')
                try:
                    urllib.request('http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz',
                                   '/usr/share/GeoIP/GeoLiteCity.dat.gz')
                except Exception:
                    print('[FAIL]')
                    print('[!] Failed to download database.')
                    sys.exit(1)
                try:
                    with gzip.open('/usr/share/GeoIP/GeoLiteCity.dat.gz', 'rb') as compressed_dat:
                        with open('/usr/share/GeoIP/GeoLiteCity.dat', 'wb') as new_dat:
                            new_dat.write(compressed_dat.read())
                except IOError:
                    print('[FAIL]')
                    print('[!] Failed to decompress data')
                    sys.exit(1)
                os.remove('/usr/share/GeoIP/GeoLiteCity.dat.gz')
                print('[DONE] \n')
            elif choice.strip().lower()[0] == 'n':
                print('[!] User denied auto-install.')
                sys.exit(1)
            else:
                print('[!] Invalid choice.')
                sys.exit(1)

    def query(self):
        """
        DOCSTRING
        """
        if not not self.url:
            print('[*] Translating %s:' % (self.url))
            sys.stdout.flush()
            try:
                self.target += socket.gethostbyname(self.url)
                print(self.target)
            except Exception:
                print('\n [!] Failed to resolve URL')
                return
        else:
            self.target += self.ip
        try:
            print('[*] Querying for records of %s ... \n' % (self.target))
            query_obj = pygeoip.GeoIP(self.dat_file)
            for key, val in query_obj.record_by_addr(self.target).items():
                print('%s: %s' % (key, val))
            print('\n [*] Query complete.')
        except Exception:
            print('\n [!] Failed to retrieve records.')
            return

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='IP Geolocate Tool')
    parser.add_argument(
        '--url', help='Locate IP based on URL.', action='store', default=False, dest='url')
    parser.add_argument(
        '-t', '--target', help='Locate the specified IP.', action='store', default=False, dest='ip')
    parser.add_argument(
        '--dat', help='Custom database file path.', action='store', default=False, dest='dat_file')
    args = parser.parse_args()
    if ((not not args.url) and (not not args.ip)) or ((not args.url) and (not args.ip)):
        parser.error('Invalid target specification.')
    try:
        locator_object = Locator(url=args.url, input=args.ip, datfile=args.dat_file)
        locator_object.check_database()
        locator_object.query()
    except Exception:
        print('\n\n [!] Unknown error occured.')
        sys.exit(1)
    except KeyboardInterrupt:
        print('\n\n [!] Unexpected user interrupt.')
        sys.exit(1)
