# wn-data-gle.tab
A tab version of Irish Wordnet (wordnet-gaeilge) compatible with OMW (Open Multilingual Wordnet) database.
It was extracted from the wordnet-gaeilge google code repository data: https://code.google.com/archive/p/wordnet-gaeilge/

The python script maketable.py was used to produce a tab version of the Wordnet data, in order to make it easy to re-use within other projects or tasks.

The original files containing the wordnet data, ga-data.adj.po, ga-data.adv.po, ga-data.noun.po, ga-data.verb.po, have been concatenated (the first title lines of each file have been deleted before) to produce the maketable.py input file: ga-data.po

The tab format is the one used within the Open Multilingual Wordnet (OMW) project: http://compling.hss.ntu.edu.sg/omw/.
All the synsets were provided with PWN (Princeton WordNet) 3.0 IDs.

Some statistics:

33472 Synsets

36348 Words

85967 Senses

With regard to the License, the one specified in the original readme file is GNU FDL (Free Document Foundation), usually not used for software, probably because the main purpose of the original resource is a paper Dictionary/Thesaurus.

The GPL GNU General Public License is the obvious natural complement of GNU FDL for software resources (they are equivalent in terms of legal rights on the resources).

It is not a case that at the google code page of the same resource https://code.google.com/archive/p/wordnet-gaeilge/ the license provided is GPL GNU General Public License instead.

So I redistribute under the same license: GNU General Public License v.3.

This means, in short, that you have the freedom to copy and redistribute the data, with or without modification, as long as you do so under the same license. 

Tommaso Petrolito (tommasouni at gmail dot com)

Here you can find the readme text with description and contacts information provided by the original author (Kevin P. Scannell):
----------------------------------------------------------------------------
Líonra Séimeantach na Gaeilge: an Irish language semantic network.
Copyright (C) 2003, 2006, 2007 Kevin P. Scannell (kscanne at gmail dot com)

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.2
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover
Texts.  A copy of the license is included in the section entitled
"GNU Free Documentation License".

Consult the web page

   http://borel.slu.edu/lsg/

for detailed information and installation instructions.

