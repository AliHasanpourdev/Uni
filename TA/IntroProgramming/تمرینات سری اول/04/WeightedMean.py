lists = []

for _ in range(5):
    user_input = input( )
    current_list = list(map(float, user_input.split()))
    lists.append(current_list)

total1 = sum(num * weight for num, weight in lists)
total2 = sum(weight for _, weight in lists)

answer = round(total1 / total2, 4)
print(answer)
