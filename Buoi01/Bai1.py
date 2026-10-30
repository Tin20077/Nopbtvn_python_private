#A
math_score = 8
english_score = 7
python_score = 9

# TODO: cong ba diem roi chia 3
average_score = (math_score + english_score + python_score) / 3

# TODO: f-string, hai chu so thap phan
report = f"Diem trung binh: {average_score:.2f}"

# Đoạn mã tự kiểm tra
if average_score is None or report is None:
    print("Chua hoan thanh Bai A.")
else:
    assert average_score == 8
    assert report == "Diem trung binh: 8.00"
    print("Dat Bai A.")
minutes_text = "185"
#B
# TODO: Chuyen chuoi sang so nguyen, tinh gio va phut du
total_minutes = int(minutes_text)
hours = total_minutes // 60
remaining_minutes = total_minutes % 60

# Đoạn mã tự kiểm tra
if any(x is None for x in [total_minutes, hours, remaining_minutes]):
    print("Chua hoan thanh Bai B.")
else:
    assert isinstance(total_minutes, int)
    assert (hours, remaining_minutes) == (3, 5)
    print("Dat Bai B: 3 gio 5 phut.")
#Tuvietthem
# calculator.py

# Nhap thong tin tu ban phim
name = input("Nhap ten hoc sinh: ")
a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))

# In ket qua dung f-string
print(f"Hoc sinh: {name}")
print(f"Tong: {a + b} | Hieu: {a - b} | Tich: {a * b}")