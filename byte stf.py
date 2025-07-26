def charstuff(flagbyte, escbyte, payload):
    x = payload.replace(escbyte, escbyte * 2)
    y = x.replace(flagbyte, escbyte + flagbyte)
    return flagbyte + y + flagbyte

def chardestuff(flagbyte, escbyte, payload):
    x = payload.replace(escbyte * 2, escbyte)
    y = x.replace(escbyte + flagbyte, flagbyte)
    return y[1:-1]  

msg = input('Enter some message: ')
fb = input('Enter flag byte: ')
eb = input('Enter escape byte: ')

print('Original msg:', msg)

stf = charstuff(fb, eb, msg)
print('After char stuffing:', stf)

dstf = chardestuff(fb, eb, stf)
print('Message after destuffing:', dstf)
