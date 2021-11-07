import sys
import json
from collections import Counter

def find_keys(iterable):
    """συνάρτηση με αναδρομή που βρίσκει τα κλειδία των λεξικών απο μια εμφωλευμένη δομη λεξικών και λιστων."""
    # έλεγχος για περίπτωση λεξικού
    if isinstance(iterable, dict):
        for key, value in iterable.items():
            yield key
            for ret in find_keys(value):
                yield ret
    # έλεγχος για περίπτωση λίστας
    elif isinstance(iterable, list):
        for el in iterable:
            for ret in find_keys(el):
                yield ret

if __name__ == '__main__':
    #διαβασμα ονόματος αρχείου απο τη γραμμή εντόλων.
    filename=sys.argv[1] if len(sys.argv)==2 else None
    if filename:
        with open(filename, "r") as f:
            sample = f.read()
    else:
        with open("sample.txt", "r") as f:
            sample = f.read()
    s=json.loads(sample)
    #κλήση της συνάρτησης για τα περιεχώμενα του αρχείου.
    print(list(find_keys(s)))
    a = list(find_keys(s))
    duplicate_dict = Counter(a)
    print(duplicate_dict)