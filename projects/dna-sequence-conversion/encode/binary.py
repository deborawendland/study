from bitstring import BitArray
import settings

def enconde_file(file_bits):
    letters_in_line = settings.L
    len_byte = 8
    
    result = []
    for line in range(0, int(len(file_bits)), len_byte*letters_in_line): #line
        letters = []
        for byte in range(0, len_byte*letters_in_line, len_byte): #byte
            bits = []
            for bit in range (0, len_byte): #bit
                bits.append(file_bits[line+byte+bit])
            letters.append(encode_byte(bits))
        result.append(letters)
    return result


def encode_byte(b):
    return {
        "nucleotide": encode_nucleotide(b[:2]),
        "confidence": encode_confidence(b[2:])
    }


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