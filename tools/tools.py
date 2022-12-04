def script_to_string(filename):
    script_str = ""
    with open(filename, 'r') as f:
        for line in f.readlines():
            script_str+=(line+";")