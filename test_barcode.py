# 10/26/2020
# Test barcode
import re # Regular expression 

f = open("./test_files/SRR11972514_1.fastq")
barcode = "GGAAAT"
cnt = 1
print(barcode)
for line in f:
	line = line.strip()
	if cnt == 1:
		# Sequence id
		pass
	if cnt == 2:
		# Sequence reads
		print(line)
		match = re.sub(barcode,"barcode!!!",line)
		print(match)
	if cnt == 3:
		# + sign
		pass
	if cnt == 4:
		# Sequence quality
		cnt = 0
	cnt += 1
f.close()
