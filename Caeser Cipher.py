def alphabet_creator():
    table = {}
    ctr=0
    table['a']=ctr
    for i in 'bcdefghijklmnopqrstuvwxyz':
        ctr+=1
        table[i]=ctr
        
    return table

def output_table():                                 #Main hash table
    table = {}
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0,26):
        table[i]=s[i]
    return table

def hash_func_encr(alpha,key):
    hash_key = (alpha+key)%26
    return hash_key

def hash_func_decr(alpha,key):
    hash_key = (alpha-key)%26
    return hash_key

def encrypt(text,shift):
    check = alphabet_creator()
    fin = output_table()
    encrypt=''
    text = text.replace(" ","")
    for i in text:
        val = check[i]
        key = hash_func_encr(val,shift)
        encrypt+=fin[key]
    return encrypt

def decrypt(text,shift):
    check = alphabet_creator()
    fin = output_table()
    decrypt = ''
    text = text.replace(" ","")
    for i in text:
        val = check[i]
        key = hash_func_decr(val,shift)
        decrypt+=fin[key]
    return decrypt

print('**************************Caeser Cipher Implementation By Keshav Dev Kapil**************************')
t=1
while t==1:
    print("What do you want to do\n1)Encrypt the text\n2)Decrypt the text\n3)Exit")
    choice = int(input("Enter serial no. of your choice: "))
    if choice==1:
        text_ = input("enter text to encrypt: ").lower()
        shift = int(input("enter shift to encrypt: "))
        print("encrypted text is: ",encrypt(text_,shift),"\n\n")
    elif choice==2:
        text_ = input("enter text to decrypt: ").lower()
        shift = int(input("enter shift to decrypt: "))
        print("decrypted text is: ",decrypt(text_,shift),"\n\n")
    elif choice == 3:
        print("quitting program")
        t=0
    else:
        print("enter valid choice")







    


