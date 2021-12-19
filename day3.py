from process_data import process_data

data = process_data('d3_input.txt')

def find_common_bit(bits,operation):
    
    one = 0  # count of ones.
    zero = 0 # count of zeroes.

    for bit in bits:
        
        if bit == '1':
            one += 1
        else:
            zero += 1
    if operation == '>':
        if zero > one:
            return '0'
        elif zero < one:
            return '1'
        else:
            return '1'
    else:
        if zero < one:
            return '0'
        elif zero > one:
            return '1'
        else:
            return '0'        

def power_consumption(data, rate, bit_position=0, output=None):

    bitstring_length = len(data[0]) - 1
    print(f'Bitstring Length: {len(data[0]) - 1}')
    print(f'Bit Position: {bit_position}')
    
    if output == None:  # Create output persistent object.
        output = ''

    #check all bits a specified index position in the supplied array and return the most common occurence.
    bits_to_check = [bit for bitstring in data for bit in bitstring[bit_position]] # grabs all the the bits at an index position for each column, and sticks in a new list.
    
    if rate == 'gamma':
        output += find_common_bit(bits_to_check, '>')
    else:
        output += find_common_bit(bits_to_check, '<')
    
    if bit_position >= int(bitstring_length):
        return int(output,2)
    else:
        return power_consumption(data, rate, bit_position + 1, output)

def ls_rating(data, gas, bit_position=0, index=None, output=None):
    
    #init function
    if output == None: output = ''
    if index == None: index = 0 

    bitstring_length = len(data[0]) - 1

    bits_to_check = [bit for bitstring in data for bit in bitstring[bit_position]] # Grabs the bit at the current index position from each list item.
    if gas == 'o2':
        common = find_common_bit(bits_to_check, '>')
    else:
        common = find_common_bit(bits_to_check, '<')

    output = [bitstring for bitstring in data if common in bitstring[bit_position]]
    
    if bit_position >= int(bitstring_length) or len(output) == 1:
        return int(output[0],2)
    else:
        return ls_rating(output, gas, bit_position + 1, index + 1, output)

gamma = power_consumption(data,'gamma')
epsilon = power_consumption(data,'epsilon')
o2 = ls_rating(data, 'o2')
co2 = ls_rating(data, 'co2')

print(f'Submarine power consumption: {gamma * epsilon}')
print(f'Life support rating: {o2 * co2}')