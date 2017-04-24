# PCL Uebung 4
### Notes

* Place all large files in _ex01/corpus_ or _ex02/dump_ or extend the _.gitignore_ file accordingly.
* Extend the requirements.txt file in ex01 or ex02 if using additional libraries, or use pip freeze to generate it automatically.

### Exercise 1

somebody somebody some some some somebody

### Exercise 2

To run the randomizer, one needs to have a bz2 compressed wikidump in dump/

```
$ cd ex02
$ mkdir -p dump
$ curl -o dump/dewiki-latest-pages-articles.xml.bz2 https://dumps.wikimedia.org/dewiki/latest/dewiki-latest-pages-articles.xml.bz2
$ pip3 install -r requirements.txt
$ python3 randomizer.py
```
Note: Although a slight increase in memory usage can be observed due to the overhead, it's growth should be smaller than linear growth.
![Memory Usage ex02](https://raw.githubusercontent.com/jvdassen/pcl-e4/master/assets/memory_usage_ex02.gif)


### Reflexion/Feedback

* Jan: Ich hatte noch nie mit grossen Datenmengen in Python gearbeitet. Das Implementieren einer skalierbaren Lösung in Python sowohl wie der vorgestellte Algorithmus waren neu für mich Der Zeitaufwand betrug etwa 6h.
