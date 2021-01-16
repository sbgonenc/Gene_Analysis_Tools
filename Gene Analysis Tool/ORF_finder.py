#invalid seq
"""DNA_input = "atccacgatcctatgtagcatctagcagctactacagctcagagactagctacgagctaatacgatcgvat" \
           "cgtacgtacgatctcgactagcatcgactagtctagcatctagcgatctactagcgatcatcgagctactagcg" \
           "actatgcagtcagctagcatcgatcgagccgatcatcgatctatcgatcagcatcgactgcatcgatcgtagctag" \
           "ctacggcgacgtatgtctgatctgtgatcgatgctagctagctgatcgagctatcgatgcgatgctatcgatcgatg" \
           "ctgagtctgagcttagctagctagctagctagctatgatcgtacgtagctgatcgtagctacgtagctacgtagctacgtaa".upper()"""
#valid sequence "v" is changed to "c" at position 69
"""DNA_input = "atccacgatcctatgtagcatctagcagctactacagctcagagactagctacgagctaatacgatcgcat" \
           "cgtacgtacgatctcgactagcatcgactagtctagcatctagcgatctactagcgatcatcgagctactagcg" \
           "actatgcagtcagctagcatcgatcgagccgatcatcgatctatcgatcagcatcgactgcatcgatcgtagctag" \
           "ctacggcgacgtatgtctgatctgtgatcgatgctagctagctgatcgagctatcgatgcgatgctatcgatcgatg" \
           "ctgagtctgagcttagctagctagctagctagctatgatcgtacgtagctgatcgtagctacgtagctacgtagctacgtaa".upper()"""
#DNA  updated
DNA_input = 'ttacgtagctacgtagctacgtagctacgatcagctacgtacgatc' \
            'atagctagctagctagctagctaagctcagactcagcatcgatcga' \
            'tagcatcgcatcgatagctcgatcagctagctagcatcgatcaca' \
            'gatcagacatacgtcgccgtagctagctacgatcgatgcagtcgatgct' \
            'gatcgatagatcgatgatcggctcgatcgatgctagctgactgcatagt' \
            'cgctagtagctcgatgatcgctagtagatcgctagatgctagactagtcgatgcta' \
            'gtcgagatcgtacgtacgatcgatcgtattagctcgtagctagtctctgagctgtagtagct' \
            'gctagatgctacataggatcgtggat'.upper()
DNA = DNA_input
def DNA_checker():
    sequence = "ACGTN"
    counter = 0
    positioner= []
    DNA_seq = []
    for position, letter in enumerate(DNA_input):
        if not letter in sequence:
            print("{} is an invalid base at position {}".format(
                letter, str(position + 1)))
        else:
            positioner.append((position + 1))
            DNA_seq.append(letter)
            counter += 1

    if counter == len(DNA_input):
        DNA_seq = "".join(str(x) for x in DNA_seq)
        return DNA_seq, positioner
    else:
        return False

def reverse_complement(DNA):
    complement = {"A": "T", "T": "A",
              "G":"C", "C": "G", 'N':'N'}
    complement_seq = (''.join(complement[x] for x in DNA
                   if x in complement.keys()))
    reverse_seq = complement_seq[::-1]
    return reverse_seq

def frames(DNA, frame):
    fr_start, fr_end = [], []
    for s in range(0, len(DNA)):
        if (DNA[s:s + 3] == "ATG" and s % 3 == frame):
            for i in range(s, len(DNA)):
                if i % 3 == frame:
                    if (DNA[i:i + 3] == "TAA") or (DNA[i:i + 3] == "TAG") or (
                            DNA[i:i + 3] == "TGA"):
                        if s + 30 < i:
                            fr_start.append(s + 1)
                            fr_end.append(i + 3)
                            if len(fr_end) >=1:
                                for c in range(0,len(fr_end)-1):
                                    if (s+ 30 < fr_end[c]):
                                        fr_start.pop()
                                        fr_end.pop()
                                        break
                            break
                        elif s < i:
                            break
        else:
            continue
    return fr_start, fr_end


def n_positioner(DNA, frame):
    bases, start, stop = frames(DNA, frame), [], []
    for c in range(len(bases[0])):
        start.append(len(DNA)-bases[0][c]+1)
        stop.append(len(DNA)-bases[1][c]+1)
    return start, stop


def nuclen(DNA, frame):
    nuclen, start, stop = frames(DNA,frame), [], []
    place = []
    start.append(frames(DNA,frame)[0])
    stop.append(frames(DNA,frame)[1])
    for c in range(len(nuclen[1])):
        place.append(stop[0][c]-start[0][c]+1)
    return place


def aalen(DNA, frame):
    aalen = nuclen(DNA, frame)
    res = []
    for aa in aalen:
        res.append(int(aa/3 -1))
    return res


def printer(reverse, DNA,frame):
    let = frames(DNA,frame)
    nt = nuclen(DNA, frame)
    aa = aalen(DNA, frame)
    strand = ""
    start = ""
    stop = ""
    if reverse == 0:
        strand = "-"
        for c in range(len(let[1])):
            start = n_positioner(DNA,frame)[0][c]
            stop = n_positioner(DNA,frame)[1][c]
            print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t  {}".format(strand, str(frame + 1), str(start),
                                                  str(stop), str(nt[c]), str(aa[c])

                                                  ))
    elif reverse == 1:
        strand = "+"
        for c in range(len(let[1])):
            start = let[0][c]
            stop = let[1][c]
            print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t  {}".format(strand, str(frame+1), str(start),
                                              str(stop), str(nt[c]), str(aa[c])

            ))

def program_start():
    if not DNA_checker():
        print("This is an invalid sequence, please enter a valid DNA sequence")
        return 0
    else:
        print("Strand\tFrame\tStart\tStop\tnt length aa length")
        printer(1, DNA_input, 0)
        printer(1, DNA_input, 1)
        printer(1, DNA_input, 2)
        printer(0, reverse_complement(DNA_input), 0)
        printer(0, reverse_complement(DNA_input), 1)
        printer(0, reverse_complement(DNA_input), 2)


program_start()