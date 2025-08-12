def print_employee_details(employee_data):
    # Write code here
    if len(employee_data) == 0:
        print("No data available")
    else:
        for key, value in employee_data.items():
            print(f'{key}: {value}')