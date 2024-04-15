def decode(file_path):
    with open(file_path, 'r') as file:
        input_dict = {int(number): word.strip() for number, word in (line.split() for line in file)}

    step, subsets = 1, []
    numbs = list(range(1, len(input_dict) + 1))

    while numbs:
        if len(numbs) >= step:
            subsets.append(numbs[:step])
            numbs = numbs[step:]
            step += 1
        else:
            return False

    integers = [sublist[-1] for sublist in subsets if sublist]

    return ' '.join(str(input_dict[key]) for key in integers if key in input_dict)

print(decode('funny.txt'))

