def jumlah_bilangan_prima_in_range(start, end):
    # Fungsi untuk mengecek apakah suatu bilangan adalah prima
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Menambahkan bilangan prima dalam rentang
    total_sum = 0
    for i in range(start, end + 1):
        if is_prime(i):
            total_sum += i
    return total_sum

# Contoh penggunaan
input_start = int(input("Masukkan batas awal: "))
input_end = int(input("Masukkan batas akhir: "))
print("Jumlah bilangan prima dalam rentang tersebut adalah:", jumlah_bilangan_prima_in_range(input_start, input_end))
