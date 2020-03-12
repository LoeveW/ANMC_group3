def op_converter(source):
	dest = [0]*22

	dest[:8] = source[:8]
	dest[8] = source[16] # output level
	dest[9] = source[17] # mode
	dest[10] = source[18] # f coarse
	dest[11] = source[19] # f fine
	dest[12] = source[20] # osc detune
	dest[13] = source[8] # break point
	dest[14] = source[9] # l scale dep
	dest[15] = source[10] # r scale dep
	dest[16] = source[11] # l key scale
	dest[17] = source[12] # r key scale
	dest[18] = source[13] # kbd rate scaling
	dest[19] = source[14] # amp mode sensitivity
	dest[20] = source[15] # key vel sensitivity
	dest[21] = 1 # always ON

	return dest

def syx_to_rm(source):
	dest = [-1]*155

	dest[15:23] = source[126:134] # PITCH EG "" ""
	dest[14] = source[143] # PITCH MOD SENSITIVITY
	dest[4:13] = source[134:143] # ALGORITHM # -> LFO

	# unsure
	dest[13] = source[144] # transpose

	# artificial
	dest[0] = 1 # cutoff (verified: it doesn't change, why?)
	dest[1] = 0 # resonance
	dest[2] = 1 # output (verified: has to be 1)
	dest[3] = .5 # master tune

	for i in range(6):
		op_i = source[(5-i)*21:(5-i+1)*21]
		dest_op_i = op_converter(op_i)
		dest[23+i*22:23+(i+1)*22] = dest_op_i

	for i,param in enumerate(dest):
		if param==-1:
			print(i, param)

	return dest

