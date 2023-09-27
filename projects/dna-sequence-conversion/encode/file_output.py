def create_read(line, count):
    nucleotides = ''
    confidences = ''

    for letter in line:
        nucleotides = nucleotides + letter['nucleotide']
        confidences = confidences + letter['confidence']

    return f'''@READ_{count}
{nucleotides}
+READ_{count}
{confidences}
'''
    

def build_output(result):
    output = ''
    count = 1
    for line in result:
        output = output + create_read(line, count)
        count += 1
    return output
