from model.read import Read
class TestRead:
    
    def test_append_nucleotides(self):
        read = Read()
        read.add_nucleotide('A')
        read.add_nucleotide('C')
        read.add_nucleotide('A')
        read.add_nucleotide('T')
        assert read.get_nucleotides() == ['A', 'C', 'A', 'T']
   
    def test_append_confidences(self):
        read = Read()
        read.add_confidence('6')
        read.add_confidence('R')
        read.add_confidence('*')
        read.add_confidence('1')
        assert read.get_confidences() == ['6', 'R', '*', '1']    
    
    def test_to_string(self):
        count = 1

        read = Read()
        read.add_nucleotide('A')
        read.add_nucleotide('C')
        read.add_nucleotide('T')

        read.add_confidence('R')
        read.add_confidence('*')
        read.add_confidence('1')

        str_test = f'''@READ_{count}
ACT
+READ_{count}
R*1
'''
        assert read.to_string(count) == str_test