def get_emp_data(path):
    with open(path, 'r') as file:
        emp_ids = file.read()
        return emp_ids.split()

