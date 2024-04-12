def create_dictionary_from_text_file(file_path):
    with open(file_path, 'r') as file:
        my_dict = {}
        for line in file:
            number, word = line.strip().split()
            number = int(number)
            my_dict[number] = word
    
    return my_dict

def create_staircase(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False
      
    return subsets

def get_last_numbers(list_of_lists_):
    last_numbers = [sublist[-1] for sublist in list_of_lists_]
    return last_numbers

def match_integers_to_string(input_dict, integers):
    values = [str(input_dict[key]) for key in integers if key in input_dict]
    result_string = ' '.join(values)
    return result_string

def decode(file_path):
    dict_ = create_dictionary_from_text_file(file_path)
    numbs = list(range(1, (len(dict_)+1)))
    list_of_lists = create_staircase(numbs)
    integers_ = get_last_numbers(list_of_lists)
    decoded_str = match_integers_to_string(dict_, integers_)
    return decoded_str

print(decode('coding_qual_input.txt'))
