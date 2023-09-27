from encode import binary
from model.read import Read


class TestEncodeBinary:
    # def test_build_input(self):
    
    def test_encode_confidence_0(self):
        assert binary.encode_confidence([0, 0, 0, 0, 0, 0]) == '!'
    
    def test_encode_confidence_32(self):
        assert binary.encode_confidence([1, 0, 0, 0, 0, 0]) == 'A'

    def test_encode_nucleotide_a(self):
        assert binary.encode_nucleotide([0, 0]) == 'A'
    
    def test_encode_nucleotide_c(self):
        assert binary.encode_nucleotide([0, 1]) == 'C'
        
    def test_encode_nucleotide_g(self):
        assert binary.encode_nucleotide([1, 0]) == 'G'

    def test_encode_nucleotide_t(self):
        assert binary.encode_nucleotide([1, 1]) == 'T'

    def test_encode_file_l1(self):
        file_bits = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]
        reads = binary.enconde_file(file_bits, 1)
        test_reads = [
            Read(['A'], ['!']),
            Read(['T'], ['A']),
            Read(['T'], ['"']),
            Read(['C'], ['`'])
        ]

        for i in range(0,4):
            assert reads[i].get_nucleotides() == test_reads[i].get_nucleotides()
            assert reads[i].get_confidences() == test_reads[i].get_confidences()
    
    def test_encode_file_l2(self):
        file_bits = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]
        reads = binary.enconde_file(file_bits, 2)
        test_reads = [
            Read(['A', 'T'], ['!', 'A']),
            Read(['T', 'C'], ['"', '`']),
        ]

        for i in range(0,2):
            assert reads[i].get_nucleotides() == test_reads[i].get_nucleotides()
            assert reads[i].get_confidences() == test_reads[i].get_confidences()
    

    def test_encode_file_l3(self):
        file_bits = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]
        reads = binary.enconde_file(file_bits, 3)
        test_reads = [
            Read(['A', 'T', 'T'], ['!', 'A', '"']),
            Read(['C'], ['`'])
        ]

        for i in range(0,2):
            assert reads[i].get_nucleotides() == test_reads[i].get_nucleotides()
            assert reads[i].get_confidences() == test_reads[i].get_confidences()
    

    def test_encode_file_l4(self):
        file_bits = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]
        reads = binary.enconde_file(file_bits, 4)
        test_reads = [
            Read(['A', 'T', 'T', 'C'], ['!', 'A', '"', '`']),
        ]

        for i in range(0,1):
            assert reads[i].get_nucleotides() == test_reads[i].get_nucleotides()
            assert reads[i].get_confidences() == test_reads[i].get_confidences()