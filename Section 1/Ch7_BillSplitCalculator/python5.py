print("Bill Split Calculator")

var1 = float(input())
var2 = float(input())
var3 = int(input())

total = var1 * (1 + var2/100)
perpax = total/var3
print(f"Total (including tip): ${total}")
print(f"Each person pays: ${perpax}")