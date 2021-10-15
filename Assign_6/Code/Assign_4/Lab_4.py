#Samuel Yohannes
#Friday October 5th at 3:30 P.M
#Caesar Cipher with endcoding and decoding functionality

#start function for most output
def start():
    print('Welcome to Caesar Cipher\ne = encode a message\nd = decode the message\nq = quit')
    c = input('Please enter your choice: ')
    if c == 'q':
        print ('Caesar Thanks You!')
        return c
    s = input('Enter the string to encode: ')
    r = int(input('Enter the amount to shift: '))
    print(f'Original Message: {s}\nEncoded Message: {encode(c,s,r)}')
    print()
    return ''
#encode for all logic   
def encode(c,s,r):
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    a = ''
    ss = [char for char in s]
    if c == 'e':
        for i in range(len(ss)):
            for j in range(len(alph)):
                if (ss[i] == alph[j]):
                    a += alph[(j+r)]
        return a
    elif c == 'd':
        for i in range(len(ss)):
            for j in range(len(alph)):
                if (ss[i] == alph[j]):
                    a += alph[(j-r)]
        return a
#program starts here
cont = start()
while cont != 'q':
    cont = start()
