#!usr/bin/env python


'''the string template'''


from string import Template


def main():
    '''the string template.'''
    s = Template('There are ${howmany} ${lang} Quotation Symbols')
    print s.substitute(lang='Python', howmany=3)


if __name__ == '__main__':
    main()
