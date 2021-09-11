a = int(input("Nhập vào số nguyên dương a = "));
if (a<2):
    print('a không phải số nguyên tố ');
if(a==2):
    print('a là số nguyên tố');
t=0;
if(a>2):
    for i in range(3,a,2):
        if(a % i == 0):
            t=t+1;
if(t==0):
    print('a là số nguyên tố');
else:
    print('a không phải số nguyên tố');
