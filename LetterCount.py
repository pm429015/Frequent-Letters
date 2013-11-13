__author__ = 'pm429015'

class LetterCount:
    def __init__(self, url):
        # given a file url and select top frequent
        print 'letter count init'
        self.__url = url

    def readfile(self):
        # check file exist
        # iter file back
        try:
            print 'Reading File'
            with open(self.__url, 'r') as file:
                for line in file:
                    yield tuple(line)
        except:
            print 'Unknown File or something wrong here'

    def file_print(self):
        # call method readfile and yeild data back
        # break file by lines and print out
        file = self.readfile()
        for linedata in file:
            print linedata

    def method1_hash(self, top):
        # this is one approach that just jump into my mind
        # using python build-in dictionary
        # and use letters as key. loop all letters
        fileLength = 0
        hash_counter = {}
        file = self.readfile()
        for linedata in file:
            fileLength += 1
            for index in range(len(linedata) - 1): # -1 because '/n'
                # check if a letter is in the hash or not. if yes, add one, if not, create it
                if linedata[index] in hash_counter.keys():
                    hash_counter[linedata[index]] += 1
                else:
                    hash_counter[linedata[index]] = 1

        # However, python dict can't be sorted
        # change it to list and sort
        # reverse it
        sorted_list = [x for x in hash_counter.iteritems()]
        sorted_list.sort(key=lambda x: x[1]) # sort by value
        sorted_list.reverse()

        #print sorted_list[:self.__top]

        return sorted_list[:top], fileLength


if __name__ == '__main__':
    counter = LetterCount('./Full_frequent_words.txt')
    sortedList, fileLength = counter.method1_hash(10)
    print sortedList
