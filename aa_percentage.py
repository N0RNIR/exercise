def aa_percentage(prot, aa):
	""" Calculates the percent of a particular residue within the protein sequence"""	
	prot = prot.upper()				# sets the prot seq to capital letters
	aa = aa.upper()					# sets the residue of interest to capital letter
	aa_count = prot.count(aa)			# counts the number of times the aa of interest occurs within prot seq
	print('AA count: ' , aa_count)			# print the total sum of aa of interest
	prot_len = len(prot)				# calculates the length of the prot seq
	aa_percent = (aa_count/ prot_len) * 100		# calculates the % of the aa of interest by diving the sum of the residues by the overall length and multiplying by 100
	return aa_percent				# return the percentage 
