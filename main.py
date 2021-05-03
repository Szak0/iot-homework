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


def get_match(joined_actual_rows):
    unknown = '?'
    value = REVERSED_DB.get(joined_actual_rows, unknown)
    return value


def collect_account_numbers(max_digit = 9):
    entries = get_data().split('\n\n')
    output = []
    
    for entry in entries:
        print(entry)
        start = 0
        end = 3
        number = ''
        joined_actual_rows = ''
        for i in range(max_digit):
            actual_rows = []
            for row in entry.split('\n'):
                if len(row) > 0:
                    current_slice = ''.join(row[start:end])
                    actual_rows.append(current_slice)
                    
            joined_actual_rows = ''.join(actual_rows)
            value = get_match(joined_actual_rows)

            start += 3
            end += 3
            number += value

        start, end = 0, 3
        output.append(number)
        number = ''
    return output


def main():
    account_numbers = collect_account_numbers()
    print(account_numbers)


if __name__ == '__main__':
    main()