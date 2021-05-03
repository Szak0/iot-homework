ACCOUNTING_NUMBERS = {
    '1': '   '+
         '  |'+
         '  |',
    '2': ' _ '+
         ' _|'+
         '|_ ',
    '3': ' _ '+
         ' _|'+
         ' _|',
    '4': ' _ '+
         '|_|'+
         '  |',
    '5': ' _ '+
         '|_ '+
         ' _|',
    '6': ' _ '+
         '|_ '+
         '|_|',
    '7': ' _ '+
         '  |'+
         '  |',
    '8': ' _ '+
         '|_|'+
         '|_|',
    '9': ' _ '+
         '|_|'+
         ' _|',
    '0': ' _ '+
         '| |'+
         '|_|'
}


def get_data(filename='printer_output.txt'):
    with open(filename, 'r') as data:
        return data.read()


def main():
    pass


if __name__ == '__main__':
    main()