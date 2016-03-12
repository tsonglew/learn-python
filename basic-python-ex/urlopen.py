#!usr/bin/env python


from urllib import urlopen


def main():
    '''the urlopen method.'''
    f = urlopen('http://'            # protocol
            'localhost'              # hostname
            ':8000'                  # port
            '/cgi-bin/friend2.py')   # file


if __name__ == '__main__':
    main()
