import glob
import lxml.etree as ET
import os

def getfreqwords(indir, outfile):

    filesize = 0
    hashed_sents = {}
    for xml_file in glob.glob(indir + '/*mul.xml'):

        with open(xml_file, encoding="utf-8") as xmlfile:
            filesize += os.path.getsize(xml_file)
            for _, sentence in ET.iterparse(xml_file, tag='s'):
                lemma_sentence = lemmatize_sent(sentence)
                hashed_sentence = hash(lemma_sentence)
                if hashed_sentence in hashed_sents:
                    hashed_sents[hashed_sentence] += 1
                elif hashed_sentence not in hashed_sents and len(sentence.findall("w")) > 5:
                    hashed_sents[hashed_sentence] = 1
                else:
                    pass
                sentence.clear()
    print(filesize)
    sentence_list = sorted(hashed_sents.items(), key=lambda x: x[1])
    hashed_sents.clear()

    short_sentence_list = sentence_list[-20:]
    sentence_list = []

    short_sentence_dic = {}
    for item in short_sentence_list:
        short_sentence_dic[item[0]] = item[1]
    short_sentence_list = []

    final_sentences = {}

    for xml_file in glob.glob(indir + '/*mul.xml'):

        with open(xml_file, encoding="utf-8") as xmlfile:
            filesize += os.path.getsize(xml_file)
            for _, sentence in ET.iterparse(xml_file, tag='s'):
                lemma_sentence2 = lemmatize_sent(sentence)
                hashed_sentence2 = hash(lemma_sentence2)
                if hashed_sentence2 in short_sentence_dic and lemma_sentence2 not in final_sentences:
                    final_sentences[lemma_sentence2] = short_sentence_dic[hashed_sentence2]
                else:
                    pass
                sentence.clear()


    final_sentence_list_sorted = sorted(final_sentences.items(), key=lambda x: x[1])

    with open(outfile, 'w', encoding='utf-8') as output_file:
        for entry in reversed(final_sentence_list_sorted):
            temp = ""
            temp += str(entry[0]) + " || " + str(entry[1]) + "\n"
            output_file.write(temp)

def lemmatize_sent(sentence):
    sent = ""
    for word in sentence.iterfind("w"):
        try:
            sent += word.attrib["lemma"] + " "
        except KeyError:
            sent += word.text
    return sent

def main():
    filepath = "/Users/luc/Documents/PCL II/Exercises/exercise4/SAC"
    outputfile = "output.txt"

    getfreqwords(filepath, outputfile)

if __name__ == '__main__':
    main()
