import string
import random
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
def get_random_characters(n):
    return random.sample(string.ascii_letters, n)
ran=get_random_characters(3)
ranchars=""
for i in ran:
    ranchars=ranchars+i
msg=input("Enter Your Secret msg here - ")
msg=list(msg)
if(len(msg)<=3):
    msg1=""
    msg=msg1.join(reversed(msg))
else:
    fletter=msg.pop(0)
    msg.append(fletter)
    msg.insert(0,ranchars)
    msg.insert(len(msg),ranchars)
msg=listToString(msg)
print("Your Encoded Msg is\n",msg)
msg=list(msg)
if(len(msg)<=3):
    msg1=""
    msg=msg1.join(reversed(msg))
    print("Your decoded msg is\n",msg)
else:
   msg=msg[3:]
   msg=msg[:len(msg)-3]
   lletter=msg.pop(len(msg)-1)
   msg.insert(0,lletter)
msg=listToString(msg)
print("Your Decoded Msg is\n",msg)

   
   

    






