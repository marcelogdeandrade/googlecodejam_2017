INPUT_FILE = 'C-small-1-attempt1.in'
OUTPUT_FILE = 'C-small-1-attempt1.out'


def read_file():
    with open(INPUT_FILE) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        content = [x.split() for x in content]
        f.close()
    return content


def find_position(x, k):
    index = len(x) / 2
    if k <= 1:
        index = index = len(x) / 2
        return [int(len(x) - index - 1), int(index)]
    return find_position(x[:index], k / 2)


def main():
    with open(OUTPUT_FILE, 'w') as f:
        file_in = read_file()
        size_file = int(file_in[0][0])
        for i in range(1, size_file + 1):
            N = int(file_in[i][0])
            K = int(file_in[i][1])
            bathroom = '0' * N
            pos = find_position(bathroom, K)
            res1 = max(pos[0], pos[1])
            res2 = min(pos[0], pos[1])
            f.write('Case #{0}: {1} {2} \n'.format(i, res1, res2))

main()
