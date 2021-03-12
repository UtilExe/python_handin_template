from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import requests


class NotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TextComparer():
    def __init__(self, url_list):
        self.url_list = url_list
        self.index = 0

    def download(self, url, filename):
        response = requests.get(url)

        if response.status_code == 404:
            raise NotFoundException("404, URL was not found")
        else:
            with open(filename, 'wb') as write_object:
                write_object.write(response.content)
                return response

    def multi_download(self):
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
        for url in self.url_list.values():
            yield url


books = {
    "https://www.gutenberg.org/files/asdsadaassdas": "Pride And Prejudice.txt",
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
text1.multi_download()

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
