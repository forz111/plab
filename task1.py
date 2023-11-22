with open("product_info.txt", "r") as f:
    data = [line.strip().split() for line in f]
    data = [(item[0], int(item[1]), item[2] == "True") for item in data]

data.sort(key=lambda x: x[0])

with open("output1.txt", "w") as f:
    for item in data:
        f.write(f"{item[0]} {item[1]} {str(item[2])}\n")

with open("output1.bin", "wb") as f:
    for item in data:
        f.write(f"{str(item[0])} {str(item[1])} {str(item[2])}\n".encode())

with open("output1.bin", "rb") as f:
    data = [line.decode().strip().split() for line in f]
    data = [(item[0], int(item[1]), item[2] == "True") for item in data]

data.sort(key=lambda x: x[1], reverse=True)

with open("output2.txt", "w") as f:
    for item in data:
        f.write(f"{item[0]} {item[1]} {str(item[2])}\n")
