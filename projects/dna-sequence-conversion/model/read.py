class Read:

    def __init__(self, nucleotides=None, confidences=None):
        if nucleotides:
            self.nucleotides = nucleotides
        else:
            self.nucleotides = []

        if confidences:
            self.confidences = confidences
        else:
            self.confidences = []

    def set_nucleotides(self, nucleotides):
        self.nucleotides = nucleotides
    
    def set_confidences(self, confidences):
        self.confidences = confidences

    def get_nucleotides(self):
        return self.nucleotides

    def get_confidences(self):
        return self.confidences
    
    def add_nucleotide(self, nucleotide):
        self.nucleotides.append(nucleotide)
    
    def add_confidence(self, confidence):
        self.confidences.append(confidence)

    def to_string(self, count):
        return '''@READ_{count}
{nucleotides}
+READ_{count}
{confidences}
'''.format(count=count, nucleotides=''.join(self.nucleotides), confidences=''.join(self.confidences))