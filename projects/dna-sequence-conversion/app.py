import settings
import numpy as np
from encode import binary
import os

def read_input_file():
    print (f'reading file: {settings.INPUT_FILE}')
    file_bytes = np.fromfile(settings.INPUT_FILE, dtype = "uint8")
    return np.unpackbits(file_bytes)

def write_output_file(output):
    filepath =  os.path.join(settings.OUTPUT_FOLDER, f'output_{settings.L}')
    print (f'creating output file: {filepath}')
    with open(filepath, "w") as file:
        file.write(output)
    print ('...OK')

def main():

    file_bits = read_input_file()
    content_encoded = binary.enconde_file(file_bits, settings.L)
    output = binary.build_output(content_encoded)
    write_output_file(output)


if __name__ == '__main__':
    main()