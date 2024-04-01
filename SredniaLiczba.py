def SredniaLiczba(N):
    if N == 0:
        return "Niepoprawnie ilosc liczb"
    list_of_numbers = []
    for i in range(N):
        n = int(input("Enter a number: "))
        list_of_numbers.append(n)
    print(f"Srednia liczb wynosi {sum(list_of_numbers)/N}")
