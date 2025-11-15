a,b,c = map(float, input("nhap 3 canh tam giac").split())
if a + b > c and a + c > b and b + c > a: 
    print("day la 3 canh cua tam giac")
else:
    print("day khong phai 3 canh cua tam giac")
if a == b:
    print("tam giac can")
elif a ==b == c:
    print("tam giac deu")
else:
    print("tam giac thuong")

