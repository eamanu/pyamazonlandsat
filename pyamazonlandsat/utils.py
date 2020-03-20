def to_list_name(name):
    return name.split('_')

def get_path_row_from_name(name):
    lname = to_list_name(name)
    path = lname[2][:3]
    row = lname[2][3:]

def get_satellite(name):
    return to_list_name(name)[0]


