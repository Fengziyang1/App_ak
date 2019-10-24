with open("../data/data_login.txt", "r", encoding="utf-8") as f:
    r = f.readlines()
    arr = []
    read_data = r
    read_data = read_data[1:]
    print(read_data)
    for data in read_data:
        arr.append(tuple(data.strip().split(",")))
    print(arr)
