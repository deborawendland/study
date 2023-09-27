import settings
import numpy as np
import encode.binary as binary

def read_input_file():
    file_bytes = np.fromfile(settings.INPUT_FILE, dtype = "uint8")
    return np.unpackbits(file_bytes)

def write_output_file(output):
    with open(f'{settings.OUTPUT_FOLDER}/output_{settings.L}', "w") as file:
        file.write(output)

def main():

    file_bits = read_input_file()
    content_encoded = binary.enconde_file(file_bits)
    output = binary.build_output(content_encoded)
    write_output_file(output)


if __name__ == '__main__':
    main()