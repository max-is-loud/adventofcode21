def process_data(filename):
    with open(filename, 'r') as f:
        data = []
        for i in f.read().splitlines():
            data.append(int(i))
        return data     

def sonar_sweep(input):
    count = 0
    x = input[0]
    for m in input:
        if m > x:
            count += 1
            x = m
        else:
            x = m
    print(count)

data = process_data('./d1_input.txt')
sonar_sweep(data)
