def to_list_name(name):
    return name.split('_')

def get_path_row_from_name(name):
    lname = to_list_name(name)
    path = lname[2][:3]
    row = lname[2][3:]
    return (path, row)

def get_acquisition_time(name):
    return to_list_name(name)[3]

def get_processing_date(name):
    return to_list_name(name)[4]

def get_collection_number(name):
    return to_list_name(name)[5]

def get_collection_category(name):
    return to_list_name(name)[6]

def get_satellite(name):
    return to_list_name(name)[0]


