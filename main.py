
''''' Task 2
input_number = int(input("Введите трёхзначное число: "))
third_num = input_number % 10
second_num = int((input_number / 10) % 10)
first_num = int((input_number / 100) % 10)
sum = third_num + second_num + first_num
print(sum)
'''''

''''' Task 4
total_cranes = int(input("введите количество журавликов "))
print(total_cranes)
equal_cranes = (total_cranes / 3)
katya_cranes = equal_cranes * 2
petya_cranes = equal_cranes / 2
sereja_cranes = petya_cranes
print(petya_cranes)
print(katya_cranes)
print(sereja_cranes)
'''

''''' Task 6
ticket_num = int(input("Введите номер билетика: "))
 
first_half_ofticket = int(ticket_num / 1000)
third_num = first_half_ofticket % 10
second_num = int((first_half_ofticket / 10) % 10)
first_num = int((first_half_ofticket / 100) % 10)

first_half_sum = third_num + second_num + first_num

second_half_ofticket = int(ticket_num % 1000)
sixth_num = second_half_ofticket % 10
fifth_num = int((second_half_ofticket / 10) % 10)
fourth_num = int((second_half_ofticket / 100) % 10)

second_half_sum = sixth_num + fifth_num + fourth_num

if(first_half_sum == second_half_sum):
    print("ваш билетик счастливый!")
else: print("повезёт в следующий раз")
'''''

''''' Task 8
length_slices = int(input("Введите количество долек по длине: "))
width_slices = int(input("Введите количество долек по ширине: "))
number_of_slices = int(input("Сколько долек вы хотите: "))

if(number_of_slices % length_slices == 0 or number_of_slices % width_slices == 0):
    print("yes")
else:print("no")
'''''
