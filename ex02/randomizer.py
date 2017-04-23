#!/usr/bin/python

'''
The randomizer module can be used to split a set of articles into to files.
A number of random k articles will be written into a file, the remaining into
the other output file provided.
'''
from bz2file import BZ2File
from lxml import etree
import random
import sys
import os
try:
    import psutil
    psutil_available = True
except Exception as e:
    psutil_available = False


def get_titles(infile, testfile, trainfile, k):
    counter = 0
    reservoir = [None] * 5

    with BZ2File(infile) as xml_dump:
        xml_parser = etree.iterparse(xml_dump, events=('end',))

        for events, elem in xml_parser:
            if elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}title':

                if counter < k:
                    reservoir[counter] = elem.text
                    # print(reservoir)
                else:
                    m = random.randint(0, counter)
                    if m < k:
                        # If a word is about to be replaced in the reservoir
                        # write it to the trainfile and replace it in the reservoir
                        with open(trainfile, 'a') as trainfile_out:
                            trainfile_out.write(reservoir[m] + '\n')
                            trainfile_out.close()
                        reservoir[m] = elem.text



                counter = counter + 1
            # Only print the Memory usage on systems where psutil is installed
            if psutil_available:
                sys.stdout.write(str(counter) +' articles processed, Using approx. '
                                + str(memusage()) + ' MB of memory currently\r')
                sys.stdout.flush()
            else:
                sys.stdout.write(str(counter) +' articles processed\r')
                sys.stdout.flush()

            # Uncomment these lines if you want to see the two resulting files
            # after evaluating only 100000 elements.
            if counter > 100000:
                break;

            elem.clear()

        # after all articles were evaluated, we can write everything that is in
        # the reservoir to the testfile.
        with open(testfile, 'a') as testfile_out:
            for article in reservoir:
                if article != None:
                    testfile_out.write(article + '\n')
            testfile_out.close()


def main():
    ''' Function used for testing and demonstrating.'''

    archive_filename = 'dump/dewiki-latest-pages-articles.xml.bz2'
    test_filename = 'k_random_titles.txt'
    train_filename = 'remaining_titles.txt'

    get_titles(archive_filename, test_filename, train_filename, 5)

def memusage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss/1024/1024

if __name__ == '__main__':
    # Run the "demo" only if the randomizer module is run directly and not imported
    # as a module
    main()