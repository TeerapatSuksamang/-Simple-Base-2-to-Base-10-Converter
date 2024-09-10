print('Simple Base-2 to Base-10 Converter')
print('_________________________________________\n')

while True:
    base2 = input('Input your base-2 number : ')

    # เช็คตัวเลขทั้งหมดที่รับเข้ามาว่ามีแค่เลขฐาน 2 ใช่หรือไม่
    if all(input_check in '01' for input_check in base2):
        break
    else:
        print('\nEnter only base 2 numbers!!')

# สร้าง list ว่างสำหรับเก็บเลขแต่ละตำแหน่ง
number_list = []

# ลูปเก็บตัวเลขแต่ละหลักเข้าไปใน list
for i1 in base2:
    number_list.append(i1)

# แปลงเลขแต่ละตัวในลิสต์เป็นจำนวนเต็ม
number_list = list(map(int, number_list))

# ความยาวใน list (จำนวนหลักของเลขที่รับมา)
number_len = len(number_list)

# list สำหรับเก็บค่าผลลัพธ์ของแต่ละหลัก
sum = []

# สำหรับวนลูปเพื่อแสดงค่าแต่ละหลักใน sum[]
current_index = 0

# ลูปคำนวนเลขฐาน 10 ของแต่ละหลัก
for num in number_list:
    num + 1
    number_len -= 1
    # คำนวนเลขฐาน10 และแสดงสมการ
    sum.append(num * 2 ** number_len) 
    print('Index ',current_index,' is ',num,'x',2,'^',number_len,'=',sum[current_index])
    current_index += 1

print('\n--------------------------------\n')

# คำนวนผลรวมทั้งหมด
result = 0
for i2 in sum:
    result += i2

# map(str, sum) แปลงค่าใน sum เป็น string
# จัดรูปแบบสมการ ใช้ join รวมค่าใน list เป็นข้อมูลเดียวกันและคั่นระหว่างค่าด้วย +
equation = ' + '.join(map(str, sum))
print(equation,'=',result)
