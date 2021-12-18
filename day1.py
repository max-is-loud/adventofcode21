def process_data(filename):
    with open(filename, 'r') as f:
        data = []
        for i in f.read().splitlines():
            data.append(int(i))
        return data     

def depth_increases(input):
    count = 0
    last = input[0]
    for num in input:
        if num > last:
            count += 1
            last = num
        else:
            last = num
    print(count)

def sonar_sums(input, output=None):
    if output == None:
        output = list()
    if len(input) < 3:
        return output
    else:
        output.append(sum(input[:3]))
        input.pop(0)
        return sonar_sums(input, output) 

data = process_data('./d1_input.txt')

sum_list = sonar_sums(data)
depth_increases(sum_list)




