def ctab():
    with open("scrapes.txt", "r") as f:
    lines = f.readlines()
    for i in lines:
        for word in i:
            if word in ["join","now","try","click","here","avail","register","open"]:
                print i
                break
    



