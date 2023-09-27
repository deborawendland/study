from bitstring import BitArray
from model.read import Read
from settings import L as line_size

def enconde_file(file_bits):
    len_byte = 8
    
    result = list()
    for line in range(0, int(len(file_bits)), len_byte*line_size): #line
        read = Read()
        for byte in range(0, len_byte*line_size, len_byte): #byte
            bits = []
            for bit in range (0, len_byte): #bit
                bits.append(file_bits[line+byte+bit])
            encode_byte(read, bits)
        result.append(read)
        read = ''
    return result


def encode_byte(read, b):
    read.add_nucleotide(encode_nucleotide(b[:2]))
    read.add_confidence(encode_confidence(b[2:]))

def encode_nucleotide(b):
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
    confidence_int = BitArray(b)
    return(chr(confidence_int.uint + 33))

def build_output(result):
    output = ''
    count = 1
    for read in result:
        output = output + read.to_string(count)
        count += 1
    return output
