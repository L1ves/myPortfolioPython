from turtle import *
def turtle_controller(do,val):
    do = do.upper()
    if do == 'F':
        forvard(val)
    elif do == 'B':
        backvard(val)
    elif do == 'R':
        right(val)
    elif do == 'L':
        left(val)
    elif do == 'U':
        penup()
    elif do == 'D':
        pendown()
    elif do == 'N':
        reset()
    else:
        print('unrecognised command')
def string_artist(program):
    cmd_list = program.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        print(command, ":", cmd_type, num)
        turtle.controller(cmd_type, num)
