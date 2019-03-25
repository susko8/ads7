def check_route_and_find_problem(route):
    n = len(route)
    max = 2147483647  # INT_MAX
    min = -2147483648  # INT_MIN
    flag = True

    for i in range(1, n):
        booleans = [route[i] > route[i - 1], route[i] > min, route[i] < max, route[i] < route[i - 1], route[i] > min,
                    route[i] < max]
        if (route[i] > route[i - 1] and
                route[i] > min and route[i] < max):
            min = route[i - 1]
        elif (route[i] < route[i - 1] and
              route[i] > min and route[i] < max):
            max = route[i - 1]
        else:
            flag = False
            break
    if flag:
        print("BST je validny")
    else:
        print("Neexistujte BST s takouto cestou")
    return i, min, max, route[i], booleans


file = open('vstup.txt', 'r')
filecontent = file.read().splitlines()
file.close()

route = []
for line in filecontent:
    route.append(int(line))

index, min, max, value, booleans = check_route_and_find_problem(route)

print(check_route_and_find_problem(route))

print(booleans)
print('problemovy index', index - 1)
print('hodnota na tomto indexe', route[index - 1])
print('hodnota na o jedno mensom indexe', route[index - 2])
print('hodnota na o jedno vacsom indexe', route[index])
print('min', min)
print('max', max)

# 631102 je prvy invalidny vstup, vsetko vyssie zbieha, pretoze min, max interval mi ostane v rozumnych medziach
route[index - 1] = 631104
print(check_route_and_find_problem(route))
