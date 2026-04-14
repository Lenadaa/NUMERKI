def matrix(file_name):
    data = []
    with open(file_name) as f:
        for line in f:
            line = line.replace('|', '')
            if line.strip():
                data.append(list(map(float, line.split())))

    A = [row[:-1] for row in data]
    b = [row[-1] for row in data]
    return A, b

