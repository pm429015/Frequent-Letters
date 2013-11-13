import math
from LetterCount import LetterCount

__author__ = 'pm429015'
# please visit below website for algorithm details
# http://hareenlaks.blogspot.com/2011/06/fp-tree-example-how-to-identify.html

class Node:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode      #needs to be updated
        self.child = {}

    def countAdd(self, numOccur):
        self.count += numOccur

    def has_key(self, key):
        if self.child.has_key(key):
            return True
        else:
            return False

class FPtree:
    def __init__(self, url, min):
        self.__minSupport = min
        self.__sorter = LetterCount(url)
        self.__header = {}
        self.__fptree = None

    def growTree(self, data=None):
        # read data and call sort function to sort it
        # After finish this, we are at the step 4
        # flag is used to build conditional tree
        if data is None:
            sortList, lenght = self.__sorter.method1_hash(24)
            # store data back to frequency list and calcuate min support
            self.__minSupport = math.ceil(lenght * self.__minSupport)
        else:
            sortList = self.__sortedRead(data)

        if len(sortList) == 0:
            return None, None
        header = {}
        for i in range(len(sortList)):
            if sortList[i][1] >= self.__minSupport:
                #self.__header[sortList[i][0]] = [sortList[i][1], None]
                header[sortList[i][0]] = [sortList[i][1], None]

        # create root node
        root = Node('root', 1, None)

        # read data second time
        if data is None:
            file = self.__sorter.readfile()
        else:
            file = self.__originalRead(data)

        for linedata in file: # by line
            if data is None:
                count = 1
            else:
                count = file[linedata]
            tempdict = {}
            for letter in linedata: # by letter
                if header.has_key(letter):
                    # give counters for the temp dict
                    tempdict[letter] = header[letter][0]
                    # reorder the letter
            sortletter = [v[0] for v in sorted(tempdict.items(), key=lambda p: p[1], reverse=True)]
            self.__growing(sortletter, root, header, count)

        # Step 6 done

        if data is None:
            self.__header = header
            self.__fptree = root
        else:
            return root, header

    def __sortedRead(self, data):
        temp = {}
        for trans in data:
            for item in trans:
                temp[item] = temp.get(item, 0) + data[trans]
        sorted_list = [x for x in temp.iteritems()]

        return sorted_list

    def __originalRead(self, data):
        return data


    def __growing(self, letters, tree, header, count):
        # recursive grown tree
        if len(letters) != 0:
            if tree.has_key(letters[0]):
                tree.child[letters[0]].countAdd(1)
            else:
                tree.child[letters[0]] = Node(letters[0], count, tree)
                #update header
                if header[letters[0]][1] == None: # if this is new node, header will link to it
                    header[letters[0]][1] = tree.child[letters[0]]
                else:# otherwise, new node link to header's node, and header link to the new node
                    tree.child[letters[0]].nodeLink = header[letters[0]][1]
                    header[letters[0]][1] = tree.child[letters[0]]
            self.__growing(letters[1::], tree.child[letters[0]], header, count)

    def printHeader(self):
        print self.__header

    def __nodeToroot(self, node, prefixPath): #ascends from leaf node to root
        if node.parent != None:
            prefixPath.append(node.name)
            self.__nodeToroot(node.parent, prefixPath)

    def __findPath(self, Node):
        # node comes from header table
        # return the full path
        path = {}
        while Node != None:
            prefixPath = []
            self.__nodeToroot(Node, prefixPath)
            if len(prefixPath) > 1:
                path[frozenset(prefixPath[1:])] = Node.count
            Node = Node.nodeLink
        return path

    def minTree(self,  prex = None, freqList = None, header=None):
        # recursive find the pattern until all headers are gone
        # use set store items and avoid duplicate
        if header == None:
            prex = set([])
            freqList = []
            self.minTree(prex, freqList, header= self.__header)
            return freqList
        else:
            # sort according to low to high frequence
            sortHeader = [v[0] for v in sorted(header.items(), key=lambda x: x[1])]
            for letter in sortHeader: # sorted letters
                # copy the temp set, add new letter and store back to frequent list
                conditFreq = prex.copy()
                conditFreq.add(letter)
                freqList.append(conditFreq)
                condPattBases = self.__findPath(header[letter][1])
                tree, smallheader = self.growTree(data=condPattBases)
                # if smallheader has letters, we build the tree again
                if smallheader is not None:
                    self.minTree( conditFreq, freqList, header=smallheader)

if __name__ == '__main__':
    # Support that you are interesting to know letter patterns. Take min support as 5%
    fptree = FPtree('./Full_frequent_words.txt', 0.05)
    fptree.growTree()
    result= fptree.minTree()
    for set in result:
        if len(set) > 1:
            print set