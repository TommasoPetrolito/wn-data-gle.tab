#coding: utf-8
## in ann, maith, ábalta, cumasach, i gcumas, inniúil 
#first occurring line with # is a list of Irish lemma_names
#msgctxt "00001740 a"
#msgctxt "dddddddd p"
#msgid "being on the point of death; breathing your last"
#msgstr ""
# msgid is the English definition, msgstr is the Irish definition (available only for nouns)

import codecs
i = codecs.open('ga-data.po', 'r', 'utf-8')
o = codecs.open('wn-data-gle.tab', 'w', 'utf-8')
lines = i.readlines()
sharf = "#"
syn_flag = "msgctxt"
def_flag = "msgstr"
zero_or_many = 'msgstr ""'
defs_flag = False
sharf_found = False
for line in lines:	
	if sharf in line:
		if not sharf_found:
			if defs_flag:
				c = 0
				for definition in definitions:
					o.write(synset+'\tgle:def\t'+str(c)+'\t'+definition+'\n')
					c = c + 1
				definitions = []
				defs_flag = False
			sharf_found = True
			lemmas_line = line[2:-1]
			lemmas = lemmas_line.split(", ")
		else:
			sharf_found = False
	if syn_flag in line:
		synset = line[9:-2]
		for lemma in lemmas:
			o.write(synset+'\tgle:lemma\t'+lemma+'\n')
	if def_flag in line:
		if zero_or_many not in line:
			defi = line[8:-2]
			o.write(synset+'\tgle:def\t'+"0"+'\t'+defi+'\n')
		else:
			defs_flag = True
			definitions = []
	if line[0] == '"' and defs_flag:
		definitions.append(line[1:-2])
	
