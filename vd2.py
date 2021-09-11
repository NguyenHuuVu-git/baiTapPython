a=int(input("Nhập a = "));
b=int(input("Nhập b = "));
c=int(input("Nhập c = "));
print('phương trình là :',a,'x^2+ ',b, 'x + ' ,c, '= 0');
if (a==0):
    if(b==0):
        print('Phương trình vô nghiệm');
    else:
        print('Phương trình có nghiệm x = ', +(-c/b));
delta = b*b - 4*a*c;
if (delta > 0):
    x1 = (float)((-b+sqrt(delta)) / (2*a));
    x2 = (float)((-b-sqrt(delta)) / (2*a));
    print('Phương trình có hai nghiệm là x1 = ',x1, ' và x2 = ',x2);
elif (delta == 0):
    x = (-b / (2*a));
    print('Phương trình có nghiệm kép là: x1 = x2 = ',x);
else:
    print('Phương trình vô nghiệm');
