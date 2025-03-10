#!/usr/bin/env python3

import sys
import re
# test argument usage if it correct
if len(sys.argv) < 2:
    print("usage: eddy [-i] [-n] [-f <script-file> | <sed-command>] [<files>...]")
    sys.exit(1) 

def match_option(argv):
    # Create options dictionary
    options = {
        'command': None,
        'print': True,  
        'digit_line': None,
        'regex_line': None,
        'substitution' : None,
        'global': None,
        'sub_line' : None,
        'address': None
    }

    # Process the command-line arguments
    for option in argv[1:]:
        if option == "-n":
            options['print'] = False
        elif option == "-": # different options
            pass
        else:
            options['command'] = option


            # set up substitution condition 
            if 's/' in option:
                parts = option.split('s/', 1) # delimit with slash
                sub_part = 's/' + parts[1]
                if parts[0].isdigit():  # There is a line number before 's/'
                    options['sub_line'] = int(parts[0]) # line_number 
                else:
                    if parts[0].startswith('/') and parts[0].endswith('/'): # regex
                        options['sub_line'] = re.compile(parts[0][1:-1])
                
                # Parse the substitution part
                sub_parts = sub_part[2:].rsplit('/', 2)
                if len(sub_parts) == 3:
                    pattern, replacement, flags = sub_parts 
                    options['substitution'] = {'pattern': pattern, 'replacement': replacement} # create a dictionary substitution 
                    options['global_replace'] = 'g' in flags
            else:

                # Parse the command part and process the data before command
                if options['command'] and options['command'][-1] in ['q', 'd', 'p'] or options['command'] in ['s']:
                    number = options['command'][:-1]
                    if number.isdigit():
                        options['digit_line'] = int(number)
                    elif number.startswith('/') and number.endswith('/'):
                        options['regex_line'] = re.compile(number[1:-1])
                    

                        

    return options

def process_command(options):

    # try to make a condition for address
    """ total_lines = list(sys.stdin)
    last_line = total_lines[len(total_lines)-1]
    if options['print'] is True:
        if options['command'] == '$d':
            total_lines.pop()
        elif options['command'] == '$p':
            total_lines.append(last_line)
    else:

        if options['command'] == '$p':
            print(last_line)
 """
    process_line = []

    line_number = 0 # read the data from standard input
    for line in sys.stdin:
        line_number += 1
        line = line.strip()
        process_line.append(line) # add it into list 
        # check if the line_number or regex exist and match the specifed condition
        digit = options['digit_line'] is not None and line_number == options['digit_line'] 
        regex = options['regex_line'] and options['regex_line'].search(line)
        

        # check if the substitution not None in option 
        if options['substitution']:
            pattern = options['substitution']['pattern']
            replacement = options['substitution']['replacement']

            
            # substitution regular mode(without line_number before s/) 
            if options['sub_line'] is None or options['sub_line'] == line_number:   
                if options['global_replace']:
                    line = re.sub(pattern, replacement, line)
                   
                else:
                    line = re.sub(pattern, replacement, line, count=1)

            else:
                # special situation 
                if isinstance(options['sub_line'], re.Pattern):
                    if options['sub_line'].search(line):
                        if options['global_replace']:
                            line = re.sub(pattern, replacement, line)
                        else:
                            line = re.sub(pattern, replacement, line, count=1)

            #After looping through the modified result, print it out
            print(line) 





        # Decide on p q d
        # Conditional printing: if the command ends with 'p', print each line unconditionally
        if options['command'] and options['command'].endswith('p'):
            if options['print'] is True:
                print(line)
                if digit or regex :
                    print(line)
                elif options['command'] == 'p':
                    print(line)
            else:
                if digit or regex :
                    print(line)


                    
        # Conditional quitting: if the command ends with 'q', and break the loop if meet the specificed condition
        if options['command'] and options['command'].endswith('q'):
            print(line)
            if digit or regex:
                break
        
        # if the command ends with 'd' , will continue (not print if meet the specificed condition)
        if options['command'] and options['command'].endswith('d'):
            if options['print'] is True:
                if digit or regex:
                    continue
                elif options['command'] == 'd':
                    continue
                print(line)
            else:
                if digit or regex :
                    continue




    last_line = process_line[len(process_line)-1]
    if options['print'] is True:
        if options['command'] == '$d':
            process_line.pop()
        elif options['command'] == '$p':
            process_line.append(last_line)
    else:

        if options['command'] == '$p':
            print(last_line)




def main():
    options = match_option(sys.argv)
    process_command(options)




if __name__ == "__main__":
    main()


