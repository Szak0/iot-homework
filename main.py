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
         '|_|',
    
    'A': ' _ '+
         '|_|'+
         '| |',
    
    'B': ' _ '+
         '|_\\'+
         '|_/',
    
    'C': ' _ '+
         '|  '+
         '|_ ',
    
    'D': ' _ '+
         '| \\'+
         '|_/',
    
    'E': ' _ '+
         '|_ '+
         '|_ ',
    
    'F': ' _ '+
         '|_ '+
         '|  '
}

REVERSED_DB = {v: k for k, v in ACCOUNTING_NUMBERS.items()}


from itertools import product


def get_data(filename='printer_output.txt'):
    with open(filename, 'r') as data:
        return data.read()


def calc_checksum(entry_num):
    valid = True
    sum_ = 0
    for i in range(1, len(entry_num)+1):
        multi = 10 - i
        num = entry_num[i - 1]
        sum_ += multi * int(num, 16)
        valid = sum_ % 11 == 0
    return valid


def get_match(joined_actual_rows):
    unknown = '?'
    value = REVERSED_DB.get(joined_actual_rows, unknown)
    return value


def replace_char_at_index(org_str, index, replacement):
    new_str = org_str
    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str


def save_to_file(entries):
    with open('outfile.txt', 'w') as outfile:
        out = ''
        for entry in entries:
            original = entry[0]
            sign = entry[1]
            if len(entry) > 2:
                text = f'{original} {sign} {str(entry[2])}'
                out += text + '\n'
                print(text)
            else:
                text = f'{original} {sign}'
                out += text + '\n'
                print(text)
        outfile.write(out)
        outfile.close()


def start_validation(number_strings, nums):
    fixed_unvalid = []
    replacements = ['|', '_', ' ']
    unknown = '?'
    valid = True
    illegal = False
    if unknown in nums:
        illegal = True
    else:
        valid = calc_checksum(nums)

    if not valid:
        possible_numbers = []
        for i, (num, num_string) in enumerate(zip(nums, number_strings)):
            for j, char in enumerate(num_string):
                for replacement in replacements:
                    if replacement != char:
                        new_entry = replace_char_at_index(num_string, j, replacement)
                        possible_number = get_match(new_entry)
                        if possible_number != unknown:
                            possible_numbers.append(nums[:i] + possible_number + nums[i + 1:])
        
        valid_combinations = list(filter(calc_checksum, possible_numbers))

    elif illegal:
        possible_numbers = []
        for num, num_string in zip(nums, number_strings):
            if num != unknown:
                possible_numbers.append([num])
                continue
            
            possible_values = []
            for i, char in enumerate(num_string):
                for replacement in replacements:
                    if replacement != char:
                        new_entry = replace_char_at_index(num_string, i, replacement)
                        possible_number = get_match(new_entry)
                        if possible_number != unknown:
                            possible_values.append(possible_number)
            possible_numbers.append(possible_values)
        
        possible_numbers = list(product(*possible_numbers))
        valid_combinations = list(filter(calc_checksum, possible_numbers))

    else:
        valid_combinations = [nums]

    if len(valid_combinations) == 1:
        return ''.join(valid_combinations[0]), ''
    elif len(valid_combinations) == 0:
        if unknown in nums:
            return nums, 'ILL'
        else:
            return nums, 'ERR'
    else:
        return nums, 'AMB', valid_combinations



def collect_account_numbers(max_digit):
    entries = get_data().split('\n\n')
    output = []
    collection = []
    for entry in entries:
        collection_inner = []
        start = 0
        end = 3
        number = ''
        joined_actual_rows = ''
        for i in range(max_digit):
            current_digits = []
            actual_rows = []
            for row in entry.split('\n'):
                if len(row) > 0:
                    current_slice = ''.join(row[start:end])
                    actual_rows.append(current_slice)
                    joined_actual_rows = ''.join(actual_rows)
                    current_digits.append(joined_actual_rows)
            
            collection_inner.append(joined_actual_rows)
            value = get_match(joined_actual_rows)
            start += 3
            end += 3
            number += value
        collection.append((collection_inner, number))
        
        start, end = 0, 3
        output.append(number)
        number = ''
    #print(collection)
    return collection


def get_validate(entries):
    validated = []
    for entry in entries:
        entry_num = start_validation(*entry)
        #print(f"entry: {entry[0]} result: {entry_num}")
        validated.append(entry_num)
    save_to_file(validated)


def main():
    max_digit = 9
    account_numbers = collect_account_numbers(max_digit)
    get_validate(entries=account_numbers)


if __name__ == '__main__':
    main()