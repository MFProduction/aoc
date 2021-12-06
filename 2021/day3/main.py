binary_inputs = [[], [], [], [], [], [], [], [],[],[],[],[]]
bi = []
with open("input.txt") as file:
    for line in file:
        l = list(line.rstrip('\n'))
        bi.append(l)
        for i in range(12):
            binary_inputs[i].append(int(l[i]))

def power_consuption(binary_inputs):
    gamma_rate = []
    epsilon_rate = []
    for input in binary_inputs:
        x = 0
        y = 0
        for bx in input:
            if bx == 0:
                x += 1
            else:
                y += 1
        if x > y:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        else:
            gamma_rate.append(0)
            epsilon_rate.append(1)

    gama_rate_dec = int("".join(str(x) for x in gamma_rate), 2)
    epsilon_rate_dec = int("".join(str(x) for x in epsilon_rate), 2)
    return(gama_rate_dec*epsilon_rate_dec)

def co2 (binary_inputs):
    for input in binary_inputs:
        # print(input)
        for bit in input:
            print(int(bit))
        print("--------------------------------")
co2(bi)
# print(power_consuption(binary_inputs))
