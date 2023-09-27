from bitstring import BitArray
from model.read import Read

def enconde_file(file_bits, line_size):
    # encodes file separating each read according to L (line_size), 
    # for each read/line it will get the respective number of bytes (len_bytes*line_size)
    # checks if there are not enough bytes to complete a line/read
    # if there are it continues and encodes 8 bits a time (1 byte)
    # it creates arrays of L Reads, which are populated in encode_byte

    print ('encoding file')
    len_byte = 8 #bits
    
    result = list()
    for line in range(0, int(len(file_bits)), len_byte*line_size): #line
        read = Read()
        for byte in range(0, len_byte*line_size, len_byte): #byte
            bits = []
            if line + byte >= len(file_bits):
                break
            encode_byte(read, file_bits[line+byte : line+byte+len_byte]) #subarray with the respective 8 bits
        result.append(read)
    return result


def encode_byte(read, b):
    read.add_nucleotide(encode_nucleotide(b[:2]))
    read.add_confidence(encode_confidence(b[2:]))

def encode_nucleotide(b):
    # encodes the firts two bits into a nucleotide
    if b[0] == 0:
        if b[1] == 0:
            return 'A'  # 00
        else:
            return 'C'  # 01
    else:
        if b[1] == 0:
            return 'G'  # 10
        else:
            return 'T'  # 11

def encode_confidence(b):
    # encodes the last 6 bits in a confidence number, which is encoded in ASCII
    if len(b) != 6:
        raise TypeError('Expected len() = 6, got {size} in array {array}'.format(size = len(b), array = b))
    else: 
        confidence_int = BitArray(b)    # transforms from an array to an int
        return(chr(confidence_int.uint + 33)) #encodes to ASCII

def build_output(result):
    output = ''
    count = 1
    for read in result:
        output = output + read.to_string(count)
        count += 1
    return output
