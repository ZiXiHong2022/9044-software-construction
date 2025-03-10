#!/usr/bin/env python3

import sys
import re

def match_option(argv):
    if len(argv) < 2:
        print("Usage: eddy.py '<option>' '<command>'")
        sys.exit(1) 

    options = {
        'command': None,
        'print': True,  
        'digit_line': None,
        'regex_line': None,
        'substitution': None,
        'global_replace': False,
        'sub_line': None
    }

    for option in argv[1:]:
        if option == "-n":
            options['print'] = False
        elif option != "-":
            options['command'] = option
            
            if 's/' in option:
                parts = option.split('s/', 1)
                sub_part = 's/' + parts[1]
                if parts[0].isdigit():
                    options['sub_line'] = int(parts[0])
                elif parts[0].startswith('/') and parts[0].endswith('/'):
                    options['sub_line'] = re.compile(parts[0][1:-1])
                
                sub_parts = sub_part[2:].rsplit('/', 2)
                pattern, replacement, flags = sub_parts[0], sub_parts[1], sub_parts[2] if len(sub_parts) > 2 else ""
                options['substitution'] = {'pattern': pattern, 'replacement': replacement}
                options['global_replace'] = 'g' in flags
            elif options['command'][-1] in ['q', 'd', 'p']:
                number = options['command'][:-1]
                if number.isdigit():
                    options['digit_line'] = int(number)
                elif number.startswith('/') and number.endswith('/'):
                    options['regex_line'] = re.compile(number[1:-1])

    return options

def process_command(options):
    processed_lines = []
    for line_number, line in enumerate(sys.stdin, 1):
        line = line.strip()
        digit = options['digit_line'] is not None and line_number == options['digit_line']
        regex = options['regex_line'] and options['regex_line'].search(line)
    
        if options['substitution']:
            line = apply_substitution(line, options, line_number)

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
        processed_lines.append(line)

    # 处理最后一行的命令
    last_line = processed_lines[-1] if processed_lines else None
    if options['command'] == '$d' and not options['print']:
        processed_lines.pop()
    elif options['command'] == '$p' and not options['print']:
        print(last_line)

    # 打印处理后的行
    """if options['print']:
        for line in processed_lines:
            print(line)"""

def apply_substitution(line, options, line_number):
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

    return line

def main():
    options = match_option(sys.argv)
    process_command(options)

if __name__ == "__main__":
    main()
