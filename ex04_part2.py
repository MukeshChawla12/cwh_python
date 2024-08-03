st=input("Enter your secret message here - ")
coding=input("1 for Encode \n2 for Decode ")
words=st.split(" ")
if(coding=="1"):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1="jkl"
            r2="poi"
            word= r1 +word[1:]+word[0]+r2
            nwords.append(word)
            
        else:
            word=word[::-1]
            nwords.append(word)
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            strnew=word[3:-3]
            strnew=strnew[-1]+strnew[:-1]
            nwords.append(strnew)
        else:
            word=word[::-1]
            nwords.append(word)
    print(" ".join(nwords))



