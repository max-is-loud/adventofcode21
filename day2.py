def process_data(filename):
    with open(filename, 'r') as f:
        data = []
        for i in f.read().splitlines():
            data.append(i)
        return data

def process_instructions(data):
    #turn data into list of tuples
    instructions = []
    for item in data:
        instructions.append(tuple(item.split(" ")))
    return instructions

def process_commands(cmd):
    #part 1 solution
    horz = 0
    dpth = 0
    for x in cmd:
        print(horz)
        print(dpth)
        if x[0] == 'forward':
            horz += int(x[1])
        elif x[0] == 'down':
            dpth += int(x[1])
        elif x[0] == 'up':
            dpth -= int(x[1])
    print(horz * dpth)

def aim_change(dir,amt, aim):
    aim = aim
    if dir == 'down':
        aim = aim + int(amt)
    elif dir == 'up':
        aim = aim - int(amt)
    return(aim)

def new_process_commands(cmd):
    #part 2 solution
    horz = 0
    dpth = 0
    aim = 0
    for dir,amt in cmd:
        if dir == 'down' or dir == 'up':
            aim = aim_change(dir,int(amt), aim)
        elif dir == 'forward':
            if aim == 0:
                horz += (int(amt))
            else:
                horz += int(amt)
                dpth += int(amt) * aim      

        print(f'Horizontal: {horz}')
        print(f'Depth: {dpth}')
        print(f'Aim: {aim}')
       
    print(horz * dpth)
    