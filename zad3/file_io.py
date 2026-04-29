def load_nodes(file_path: str) -> list[float]:
    nodes = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                nodes.append(float(line))

    return nodes