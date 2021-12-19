def process_data(filename,datatype='str'):
    with open(filename, 'r') as f:
        if datatype == 'int':
            data = []
            for i in f.read().splitlines():
                data.append(int(i))
            return data
        elif datatype == 'str':
            data = []
            for i in f.read().splitlines():
                data.append(i)
            return data            