""" This function creates a pyramid from a text file with a word and its corresponding number.
The text files in this repo are the ones used to illustrate how this function works. This function requires 
a .txt file as its input."""
def create_dictionary_from_text_file(file_path):
    """
    Reads a text file and creates a dictionary from its contents.

    Parameters:
        file_path (str): The path to the text file containing word-number pairs.

    Returns:
        dict: A dictionary mapping numbers to words.
    """
    with open(file_path, 'r') as file:
        my_dict = {}
        for line in file:
            number, word = line.strip().split()
            number = int(number)
            my_dict[number] = word
    
    return my_dict


def create_staircase(nums):
    """
    Creates a staircase pattern from a list of numbers.

    Parameters:
        nums (list): A list of integers.

    Returns:
        list: A list of lists representing a staircase pattern of integers.
    """
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
    """
    Returns the last number of each sublist in a list of lists.

    Parameters:
        list_of_lists_ (list): A list of lists.

    Returns:
        list: A list containing the last element of each sublist.
    """
    last_numbers = [sublist[-1] for sublist in list_of_lists_]
    return last_numbers


def match_integers_to_string(input_dict, integers):
    """
    Matches integers to strings based on a dictionary.

    Parameters:
        input_dict (dict): A dictionary mapping integers to strings.
        integers (list): A list of integers.

    Returns:
        str: A string containing the matched words separated by spaces.
    """
    values = [str(input_dict[key]) for key in integers if key in input_dict]
    result_string = ' '.join(values)
    return result_string


def decode(file_path):
    """
    Decodes a message stored in a text file.

    Parameters:
        file_path (str): The path to the text file containing word-number pairs.

    Returns:
        str: The decoded message.
    """
    dict_ = create_dictionary_from_text_file(file_path)
    numbs = list(range(1, (len(dict_)+1)))
    list_of_lists = create_staircase(numbs)
    integers_ = get_last_numbers(list_of_lists)
    decoded_str = match_integers_to_string(dict_, integers_)
    return decoded_str

print(decode('coding_qual_input.txt'))
