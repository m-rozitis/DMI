meta = open("meta.bin","rb")
meta.seek(0)
data = open("data.bin","rb")
data.seek(0)
k=0

while 1:
	m = meta.read(1)
	if not m:
		break

	k=k+ord(m)

	data.seek(k)
	d = data.read(1)
	if not d:
		break
	
	a = meta.read(1)
			
	x = ord(d) ^ ord(a)
	print chr(x),

meta.close()
data.close()
