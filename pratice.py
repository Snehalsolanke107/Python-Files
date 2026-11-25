product_id_start = int(input("Enter Start product ID :"))
product_id_end= int(input("Enter End product ID :"))

even_list = []
odd_list = []

even_sum = 0
odd_sum = 0

even_sum_list = []
odd_sum_list = []

for pid in range(product_id_start,product_id_end+1):
    if pid % 2 == 0:
        even_list.append(pid)
        even_sum+=pid
        even_sum_list.append(even_sum)
    if pid % 2 != 0:
        odd_list.append(pid)
        odd_sum+=pid
        odd_sum_list.append(odd_sum)
print(f"even List : {even_list}")
print(f"even Sum : {even_sum}")
print(f"even sum List : {even_sum_list}")
print(f"odd List : {odd_list}")
print(f"odd Sum : {odd_sum}")
print(f"odd sum List : {odd_sum_list}")

