import re
cc=input("Enter CC number:")
match=re.search(r'[4-6]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}',cc)
if(match):
    if(cc[4]=='-'):
        cc=cc.replace('-','')
    l=len(cc)
    for i in range(0,l-3,1):
        flag=0
        for j in range(i+1,i+3,1):
            if cc[i]==cc[j]:
                flag+=1
        if flag>=4:
           print("Invalid Card")
           exit()
    print("Valid Card")    
else:
    print("Invalid Card")
