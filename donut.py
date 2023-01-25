li=[]
li2=[]
with open("D:\mesh\mesh.csv") as file:
    data=file.readlines()
    for i in data:
            a=i.split(";")
            print(a)
            li.append((float(a[0])*100,float(a[1])*100,float(a[2][:-2])*100))
        
    print(li)