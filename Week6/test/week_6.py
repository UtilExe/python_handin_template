from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import requests


class NotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TextComparer():
    #1.1
    def __init__(self, url_list):
        self.url_list = url_list
        self.index = 0

    #1.2
    def download(self, url, filename):
        """
        store the file on disk and raise NotFoundException when url returns 404
        """
        response = requests.get(url)

        if response.status_code == 404:
            raise NotFoundException("404, URL was not found")
        else:
            with open(filename, 'wb') as write_object:
                write_object.write(response.content)
                return response
    #1.3
    def multi_download(self):
        """
        use threads to download files parallel
        """
        with ThreadPoolExecutor(max_workers=6) as ex:
            for key in self.url_list:
                # key == URL
                # self.url_list[key] == filename
                                              # retrieves the specific value (filename) of every key element
                ex.submit(self.download, key, self.url_list[key])

                # attempt that doesnt work:
                #ex.map(self.download, key, self.url_list[key])

    # 1.4
    def __iter__(self):
        return self

    # 1.5
    def __next__(self):
        if self.index >= len(self.url_list.values()):
            raise StopIteration
        else:
            self.index += 1
            return list(self.url_list.values())[self.index]

    # 1.6
    def urllist_generator(self):
        for url in self.url_list.keys():  # this is the urls
            yield url

    # 1.7
    def avg_vowels(self, text):
        """
        a rough estimate on readability returns average number of vowels in the words of the text
        """

        vowels = ['a', 'e', 'i', 'o', 'u', 'Y', 'A', 'E', 'I', 'O', 'U', 'Y']
        vowel_count = 0
        word_count = 0

        #print("im hit")

        with open(text) as file_object:
            for line in file_object:
                # split gets the full word, instead of only a character
                for word in line.split(" "):
                    word_count += 1
                    for char in word:
                        if char in vowels:
                            vowel_count += 1

        return vowel_count / word_count
    
    # 1.8
    def hardest_read(self):
        """
        reads all text from files in filenames and returns the filename of the text with the highest vowel score 
        (use all the cpu cores on the computer for this work.)
        """

        tasks = {}
        result_data = {}

        with ProcessPoolExecutor(max_workers=6) as executor:
            for url in self.url_list.keys():
                # self.url_list[url] gives the filename, like '11-0.txt'
                tasks[self.url_list[url]] = executor.submit(self.avg_vowels,self.url_list[url])

        # tasks[task].result() gives the result value (avg_vowels)
        # tasks stores the Filename

        for task in tasks:
            result_data[task] = tasks[task].result()
        
        # result_data is a dictionary, with: value = filename. key = avg_vowel data. 
        return max(result_data, key=lambda x: result_data[x])    #could also have used .get to retrieve the future

books = {
  #  "https://www.gutenberg.org/files/asdsadaassdas": "Pride And Prejudice.txt",
    "https://www.gutenberg.org/files/11/11-0.txt": "Alice's Adventures in Wonderland.txt",
    "http://www.gutenberg.org/cache/epub/16328/pg16328.txt": "Beowulf.txt",
    "https://www.gutenberg.org/files/1661/1661-0.txt": "The Adventures of Sherlock Holmes.txt",
    "https://www.gutenberg.org/files/1952/1952-0.txt": "The Yellow Wallpaper.txt",
    "https://www.gutenberg.org/files/98/98-0.txt": "A Tale of Two Cities.txt",
    "https://www.gutenberg.org/files/2701/2701-0.txt": "Moby Dick.txt",
    "https://www.gutenberg.org/files/84/84-0.txt": "Frankenstein; Or, The Modern Prometheus.txt",
    "http://www.gutenberg.org/cache/epub/5200/pg5200.txt": "Metamorphosis.txt",
    "http://www.gutenberg.org/cache/epub/1497/pg1497.txt": "The Republic.txt"
}

text1 = TextComparer(books)
#text1.multi_download()

# For task 1.4 and 1.5:
my_iterator = iter(text1)

try:
    element1 = next(my_iterator)
    element2 = next(my_iterator)

    #element11 = next(my_iterator)

    print(element1)
    print(element2)

except StopIteration as e:
    print(type(e))

# 1.6 - Returns a generator:
#print([x for x in text1.urllist_generator()])

# 1.7:
#print(text1.avg_vowels('11-0.txt'))

# 1.8:
print(text1.hardest_read())