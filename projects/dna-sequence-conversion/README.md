# DNA SEQUENCE CONVERSION

This program aims to convert a binary file into a FASTQ file containing of L-sized reads, which includes the nucleotide and its confidence on the correctness of the read. 


## Initial Setup:
- In `settings.py` set:
    - `INPUT_FILE = 'data/input/input'`, file to be processed 
    - `OUTPUT_FOLDER = 'data/output'`, folder to create processed file as `output_{L}`, where L is the size of the line
    - `L = 7`, size of the line of FASTQ output file

### Run Docker:
- Build image: `docker build -t dna .`
- Run container: `docker run --rm -it dna`
- Run tests: `python -m pytest tests` 
- Run app: `python app.py`

### Requirements: 
- Python: 3.11.1
- Numpy: 1.26.0
- Bitstring: 4.1.2
- Pytest: 7.4.2
- install requirements: `pip install -r requirements.txt`

developed by: Debora Daniela Wendland Amorim