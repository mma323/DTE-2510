#Usikker på om oppgaven ble levert i WiseFlow, legger ved i tilfelle
def is_prime(n):
    if n > 1:   #Primtall er større enn 1
    
        #Primtall dersom n ikke er delelig på noe tall mellom n og n/2
        for i in range(2, int(n / 2) + 1):
    
            if (n % i) == 0:
                return False
        else:
            return True
    
    else:
        return False

def is_prime_reversed(n):
    n = str(n)        #n[::-1] funker kun på strings
    n_reversed = n[::-1]    
    n_reversed = int(n_reversed)    #is_prime funker ikke på strings
    n_reversed_is_prime = is_prime(n_reversed)

    return n_reversed_is_prime

def main():
    n = 0
    count = 1
    while count <= 20:
        if is_prime(n) and is_prime_reversed(n):
            print(n, end=" ")
            if count % 5 == 0:
                print()
            count +=1
        n += 1

if __name__ == "__main__":
    main()