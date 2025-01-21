
def get_dict_val(d, key, default):
    if key in d:
        return d[key]
    return default


def get_dict_val_path(dt, key, default_val):
    keys = key.split(".")
    mydt = dt
    res = default_val
    for key in keys:
        val = get_dict_val(mydt, key, None)
        if val == None:
            return default_val
        res = val
        mydt = val
    return res
