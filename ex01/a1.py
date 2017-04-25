#!/usr/bin/python
#Luc Boillat 14-715-577
#Jan von der Assen 14-719-132

import glob
import lxml.etree as ET

def getfreqwords(indir, outfile):
    """
    opens all xml files one by one and parses them with lxml. every sentence of the books
    gets lemmatized and hashed and added to a dictionary, together with the number of
    occurences of that sentence in all the files. When all files have been iterated through,
    the program iterates through the files again, to find the actual sentences, based
    on the hashes. These sentences are then written to a file.
    """
    hashed_sents = {}
    #finds all files that end in mul.xml
    for xml_file in glob.glob(indir + '/*mul.xml'):

        with open(xml_file, encoding="utf-8") as xmlfile:
            #parses the file with lxml
            for _, sentence in ET.iterparse(xml_file, tag='s'):
                lemma_sentence = lemmatize_sent(sentence)
                hashed_sentence = hash(lemma_sentence)
                if hashed_sentence in hashed_sents:
                    hashed_sents[hashed_sentence] += 1
                elif hashed_sentence not in hashed_sents and len(sentence.findall("w")) > 5:
                    hashed_sents[hashed_sentence] = 1
                else:
                    pass
                #clears the node
                sentence.clear()
    #the dicionary get sorted and written to a list
    sentence_list = sorted(hashed_sents.items(), key=lambda x: x[1])
    hashed_sents.clear()

    #the list gets shortened
    short_sentence_list = sentence_list[-20:]
    sentence_list = []

    #the shortened list gets transferred into a dictionary again
    short_sentence_dic = {}
    for item in short_sentence_list:
        short_sentence_dic[item[0]] = item[1]
    short_sentence_list = []

    final_sentences = {}

    #it iterates once again through the files and lines
    for xml_file in glob.glob(indir + '/*mul.xml'):

        with open(xml_file, encoding="utf-8") as xmlfile:
            for _, sentence in ET.iterparse(xml_file, tag='s'):
                lemma_sentence2 = lemmatize_sent(sentence)
                hashed_sentence2 = hash(lemma_sentence2)
                #checks if the hash of the file is in the list of the most common sentences
                if hashed_sentence2 in short_sentence_dic and lemma_sentence2 not in final_sentences:
                    final_sentences[lemma_sentence2] = short_sentence_dic[hashed_sentence2]
                else:
                    pass
                sentence.clear()

    final_sentence_list_sorted = sorted(final_sentences.items(), key=lambda x: x[1])

    #the sentences and their occurrences are written to the file
    temp = ""
    for entry in reversed(final_sentence_list_sorted):
        temp += str(entry[0]) + " || " + str(entry[1]) + "\n"

    with open(outfile, 'w', encoding='utf-8') as output_file:
            output_file.write(temp)

def lemmatize_sent(sentence):
    """
    turns the raw text of the xml file into a lemmatized sentence
    """
    sent = ""
    for word in sentence.iterfind("w"):
        try:
            sent += word.attrib["lemma"] + " "
        except KeyError:
            sent += word.text
    return sent

def main():
    """
    Change filepath to the desired filepath
    """
    filepath = "SAC"
    outputfile = "output.txt"

    getfreqwords(filepath, outputfile)

if __name__ == '__main__':
    main()
