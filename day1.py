def process_data(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def sonar_input(input):
    count = 0
    x = int(input[0])
    for m in input:
        if int(m) > x:
            count += 1
            x = int(m)
        else:
            x = int(m)
    print(count)

process_data('/d1_input.txt')
sonar_input(data)