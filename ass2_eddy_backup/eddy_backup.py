#!/usr/bin/env python3

import sys
import re

if len(sys.argv) < 2:
    print("Usage: eddy.py '<option>' '<command>'")
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
        'sub_line' : None
    }

    # Process the command-line arguments
    for option in argv[1:]:
        if option == "-n":
            options['print'] = False
        elif option == "-":
            pass
        else:
            options['command'] = option
            
            if 's/' in option:
                parts = option.split('s/', 1)
                sub_part = 's/' + parts[1]
                if parts[0].isdigit():  # There is a line number before 's/'
                    options['sub_line'] = int(parts[0])
                else:
                    if parts[0].startswith('/') and parts[0].endswith('/'):
                        options['sub_line'] = re.compile(parts[0][1:-1])
                
                # Parse the substitution part
                sub_parts = sub_part[2:].rsplit('/', 2)
                if len(sub_parts) == 3:
                    pattern, replacement, flags = sub_parts
                    options['substitution'] = {'pattern': pattern, 'replacement': replacement}
                    options['global_replace'] = 'g' in flags
            else:



                if options['command'] and options['command'][-1] in ['q', 'd', 'p'] or options['command'] in ['s']:
                    number = options['command'][:-1]
                    if number.isdigit():
                        options['digit_line'] = int(number)
                    elif number.startswith('/') and number.endswith('/'):
                        options['regex_line'] = re.compile(number[1:-1])

    return options

def process_command(options):
    line_number = 0
    for line in sys.stdin:
        line_number += 1
        line = line.strip()
        digit = options['digit_line'] is not None and line_number == options['digit_line']
        regex = options['regex_line'] and options['regex_line'].search(line)
        
        if options['substitution']:
            pattern = options['substitution']['pattern']
            replacement = options['substitution']['replacement']

            

            if options['sub_line'] is None or options['sub_line'] == line_number:   
                if options['global_replace']:
                    line = re.sub(pattern, replacement, line)
                   
                else:
                    line = re.sub(pattern, replacement, line, count=1)

            else:
                if isinstance(options['sub_line'], re.Pattern):
                    if options['sub_line'].search(line):
                        if options['global_replace']:
                            line = re.sub(pattern, replacement, line)
                        else:
                            line = re.sub(pattern, replacement, line, count=1)


            #循环过后修改之后的结果print出来
            print(line) 






        #对p q d判定
        # 条件打印: 如果命令以 'p' 结尾，无条件打印每行
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
        #条件推出，如果命令以'q'结尾，在匹配模式和特殊次数下退出
        if options['command'] and options['command'].endswith('q'):
            print(line)
            if digit or regex:
                break
        

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

def main():
    options = match_option(sys.argv)
    process_command(options)

if __name__ == "__main__":
    main()
