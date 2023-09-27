import settings
import numpy as np
import encode.binary as binary


def main():

    file_bytes = np.fromfile(settings.INPUT_FILE, dtype = "uint8")
    file_bits = np.unpackbits(file_bytes)
    per_line = settings.L
 
    len_byte = 8
    result = []
    for l in range(0, int(len(file_bits)), len_byte*per_line): #linha
        line = []
        for i in range(0, len_byte*per_line, len_byte): #byte
            bits = []
            for count in range (0, len_byte): #bit
                bits.append(file_bits[l+i+count])
                # print(f'i= {i}')
                # print(f'l= {l}')
                # print(f'count= {count}')
            line.append(binary.encode_byte(bits))
        result.append(line)
        # print (line)
        # break
    print (result)

if __name__ == '__main__':
    main()