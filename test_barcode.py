#TEST
barcode = "ATGCATGC"
seq = "ATGCATGCAAAACCC"

import re
match = re.sub(barcode,"",seq)

print(seq)
print(match)
