def frequency_counter(data_list):
    # Create an empty dictionary to store the frequencies
    frequency_dict = {}

    # Loop through the list and update the frequencies
    for item in data_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    # Return the frequency dictionary
    return frequency_dict