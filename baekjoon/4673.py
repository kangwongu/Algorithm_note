self_number_list = list(map(int, range(1, 10001)))

for i in range(1, 10001):
    N = (i) + (i//1000) + (i % 1000 // 100) + (i % 100 // 10) + (i%10)

    if N in self_number_list:
        self_number_list.remove(N)

for self_number in self_number_list:
    print(self_number)