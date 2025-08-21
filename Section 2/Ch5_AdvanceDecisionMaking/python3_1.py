def compare_strings(str1, str2):
    # Write code here
    is_substring = (str1 in str2)
    starts_with = (str2.startswith(str1))
    ends_with = (str2.endswith(str1))
    is_equal = (str1.lower() == str2.lower())
    answer_dict = {
        "is_substring": is_substring,
        "starts_with": starts_with,
        "ends_with": ends_with,
        "is_equal": is_equal
    }
    return (answer_dict)