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


REVERSED_DB = {v: k for k, v in ACCOUNTING_NUMBERS.items()}


def get_data(filename='printer_output.txt'):
    with open(filename, 'r') as data:
        return data.read()


def get_match(joined_actual_rows):
    unknown = '?'
    value = REVERSED_DB.get(joined_actual_rows, unknown)
    return value


def save_to_file(entries):
    with open('outfile.txt', 'w') as outfile:
        for entry in entries:
            outfile.write(entry + '\n')
        outfile.close()


def get_validate(entries):
    validated = []
    illegible_items = []
    for entry in entries:
        
        if "?" in entry:
            illegible = True
        else:
            illegible = False
            valid = True
            sum = 0
            for i in range(1, len(entry)+1):
                multi = 10 - i
                num = entry[i - 1]
                sum += multi * int(num)
                valid = sum % 11 == 0
                
        if illegible:
            illegible_items.append(entry)
            entry = f'%s %s' % (entry, ' ILL')
        elif not valid:
            illegible_items.append(entry)
            entry = f'%s %s' % (entry, ' ERR')

        validated.append(entry)
    return validated


def collect_account_numbers(max_digit):
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
        output.append((number, entries))
        number = ''
    print(output)
    return output


def main():
    max_digit = 9
    account_numbers = collect_account_numbers(max_digit)
    ##validated = get_validate(account_numbers)
    ##save_to_file(validated)
    ##print(validated)


if __name__ == '__main__':
    main()