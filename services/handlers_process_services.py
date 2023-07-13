from utility.handlers_process_utils import handle_error, raise_error

def split_fullname(fullname):
    if fullname == "":
        raise_error("Variable name is empty")
    else:
        try:
            name_list = fullname.split()
            if len(name_list) == 1:
                handle_error("User has no surname")
                return name_list[0], "", ""
            if len(name_list) > 2:
                return name_list[0], name_list[1], name_list[2]
            else:
                return name_list[0], name_list[1], ""
        except:
            raise_error("Problem getting out user name and surnname")