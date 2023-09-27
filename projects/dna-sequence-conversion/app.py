import settings
import numpy as np
import encode.binary as binary
import encode.file as en_file

def read_input_file():
    file_bytes = np.fromfile(settings.INPUT_FILE, dtype = "uint8")
    return np.unpackbits(file_bytes)

def write_output_file(output):
    ''

def main():

    file_bits = read_input_file()
    per_line = settings.L
 
    len_byte = 8
    result = []
    for l in range(0, int(len(file_bits)), len_byte*per_line): #linha
        line = []
        for i in range(0, len_byte*per_line, len_byte): #byte
            bits = []
            for count in range (0, len_byte): #bit
                bits.append(file_bits[l+i+count])
            line.append(binary.encode_byte(bits))
        result.append(line)
    print (en_file.build_output_file(result))

    

if __name__ == '__main__':
    main()