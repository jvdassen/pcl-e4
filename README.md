# PCL Uebung 4
### Notes

* Place all large files in _ex01/corpus_ or _ex02/dump_ or extend the _.gitignore_ file accordingly.
* Extend the requirements.txt file in ex01 or ex02 if using additional libraries, or use pip freeze to generate it automatically.

### Exercise 2

To run the randomizer, one needs to have a bz2 compressed wikidump in dump/

```
$ cd ex02
$ mkdir -p dump
$ curl -o dump/dewiki-latest-pages-articles.xml.bz2 https://dumps.wikimedia.org/dewiki/latest/dewiki-latest-pages-articles.xml.bz2
$ pip3 install -r requirements.txt
$ python3 randomizer.py
```

