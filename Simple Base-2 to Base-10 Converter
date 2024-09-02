print('Simple Base-2 to Base-10 Converter')
print('_________________________________________\n')


base2 = input('Input your base-2 number : ')

# สร้าง list ว่าง
number_list = []

# ลูปเก็บตัวเลขแต่ละหลักเข้าไปใน list
for i1 in base2:
    number_list.append(i1)

# แปลงเลขแต่ละตัวในลิสต์เป็นจำนวนเต็ม
number_list = list(map(int, number_list))

# ความยาวใน list
number_len = len(number_list)

sum = []
current_index = 0

for num in number_list:
    num + 1
    number_len -= 1
    sum.append(num * 2 ** number_len)
    print('Index ',current_index,' is ',num,'x',2,'^',number_len,'=',sum[current_index])
    current_index += 1

print('\n--------------------------------\n')

som = 0
for io in sum:
    som += io

h = str(sum)[1:-1]
h = h.replace(',',' +')
print(h,'=',som)
