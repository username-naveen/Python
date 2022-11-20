a = input().split();

#a = [0,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,0,1];
b = [];

if len(a)>2:
    while((len(b) < len(a)-2) == True):
        for i in range(0,len(a)-2):
            #print(i)
            b += [str(a[i])+str(a[i+1])+str(a[i+2])];
    print(b)
        
    happy = ['110','011','001','100','000','111'];
    # unhappy = ['010','101'];
    happy_no = 0;

    for i in range(0, len(b)):
        if (b[i] in happy) == True:
            happy_no += 1;

    print(format(happy_no/len(a),".3f"))


elif len(a) == 2:
    if a[0] == a[1]:
        print(1);
    else:
        print(0);        