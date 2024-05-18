num=int(input("Введіть число"));
if num>9999 or num<1000:
    print("Це не 4-ох значне число")
else:
    num_1 = num // 1000;
    num_2 = num // 100 % 10;
    num_3 = num // 10 % 10;
    num_4 = num % 10;
    print(num_1);
    print(num_2);
    print(num_3);
    print(num_4);



