from bitstring import BitArray

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