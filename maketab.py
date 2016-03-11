#coding: utf-8
## in ann, maith, ábalta, cumasach, i gcumas, inniúil 
#first occurring line with # is the list of Irish lemma_names
#msgctxt "00001740 a"
#If 'msgctxt' occurs in the line, it means that the line contains a PWN 3.0 synset id
#msgid "being on the point of death; breathing your last"
#msgstr ""
#if 'msgid' occurs in the line, the line contains the English definition, msgstr is the Irish definition instead

import codecs
i = codecs.open('ga-data.po', 'r', 'utf-8') #input file
o = codecs.open('wn-data-gle.tab', 'w', 'utf-8') #output file
lines = i.readlines() #let's read all the lines in the file
sharf = "#"  #let's define some flag strings that we expect to find in the lines
syn_flag = "msgctxt"
def_flag = "msgstr"
zero_or_many = 'msgstr ""'
defs_flag = False # let's define some flag variables to manage some cases of lines that are False Positive
sharf_found = False
for line in lines:	# let's look each line in the document
	if sharf in line: # if there is a #
		if not sharf_found: #if there is a # and I had not found it before
			if defs_flag: #if in the previous group of line (referring to the previous synset) there was a set of definitions (zero or more than one definition)
				c = 0
				for definition in definitions:
					o.write(synset+'\tgle:def\t'+str(c)+'\t'+definition+'\n') #print all the definitions of the previous group of lines
					c = c + 1
				definitions = []
				defs_flag = False #let's remember that now we can reset the 'zero-or-more-than-one-definitions' flag
			sharf_found = True #let's remember that now we have found the first # that is the one interesting for us with the Irish lemmas
			lemmas_line = line[2:-1] #let's take the list of lemmas
			lemmas = lemmas_line.split(", ") #let's split, we can not print yet, we need the synset id first
		else:
			sharf_found = False #otherwise it means we have found the second # line containing English lemmas, we don't need this, just reset the flag variable and skip
	if syn_flag in line: #if there is a synset id
		synset = line[9:-2] #let's take the synset id
		for lemma in lemmas: #now we can print the lemmas we collected up to this moment
			o.write(synset+'\tgle:lemma\t'+lemma+'\n')
	if def_flag in line: #if there is a 'msgstr' string in the line
		if zero_or_many not in line: #if it is not a 'msgstr ""' line (so there is exactly one definition for the given synset)
			defi = line[8:-2] #let's take the definition
			o.write(synset+'\tgle:def\t'+"0"+'\t'+defi+'\n') #let's print the definition
		else:
			defs_flag = True #if it is a 'msgstr ""' line (so there are zero or more than one definitions for the given lemma)
			definitions = [] #let's initialize to empty list the definitions
	if line[0] == '"' and defs_flag: #if we are in a 'zero-or-more-than-one-definitions' case and this is actually the following line with one of the definitions
		definitions.append(line[1:-2]) #append the definition
i.close
o.close
