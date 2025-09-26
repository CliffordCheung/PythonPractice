def calculate_average_score(scores):
    # Write code here
    if len(scores) == 0:
        return 0
    else:
        length = len(scores)
        total = sum(scores)
        average = total/length
        return average