def bitstuffing(data):
    stuffed_data = ""
    count = 0
    for bit in data:
        stuffed_data += bit
        if bit == '1':
            count += 1
            if count == 5:  
                stuffed_data += '0'  
                count = 0  
        else:
            count = 0  
    
    return stuffed_data

def bitdestuffing(stuffed_data):
    destuffed_data = ""
    count = 0 
    i = 0
    while i < len(stuffed_data):
        destuffed_data += stuffed_data[i]
        if stuffed_data[i] == '1':
            count += 1
            if count == 5 and i + 1 < len(stuffed_data) and stuffed_data[i + 1] == '0':
                i += 1
                count = 0
        else:
            count = 0
        
        i += 1
    
    return destuffed_data


msg = input('Enter a binary message (0s and 1s): ')
print('Original message:', msg)


stuffed_msg = bitstuffing(msg)
print('After bit stuffing:', stuffed_msg)

destuffed_msg = bitdestuffing(stuffed_msg)
print('Message after bit destuffing:', destuffed_msg)
