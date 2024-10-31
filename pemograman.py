def bilangan_prima_berikutnya(n):
    # Fungsi untuk mengecek apakah suatu bilangan adalah prima
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # Mencari bilangan prima berikutnya
    n += 1
    while not is_prime(n):
        n += 1
    return n

# Contoh penggunaan
input_number = int(input("Masukkan bilangan: "))
print("Bilangan prima berikutnya adalah:", bilangan_prima_berikutnya(input_number))
