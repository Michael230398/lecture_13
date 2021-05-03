def recursive_ntho_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        output = recursive_ntho_fibo(n-1) + recursive_ntho_fibo(n-2)

        return output



def main():
   number = int(input("Zadejte číslo:"))
   while number < 1:
       print("Zadali jste neplatné číslo.")
       number = int(input("Zadejte číslo: "))
   else:
       return print(recursive_ntho_fibo(number - 1))


if __name__ == '__main__':
    main()
