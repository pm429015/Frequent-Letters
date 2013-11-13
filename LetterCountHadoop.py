# Hadoop version
__author__ = 'pm429015'

from mrjob.job import MRJob


class MRLetterCount(MRJob):
    def map(self, _, line):
        # loop line based on letters
        for letter in line:
            yield (letter, 1)

    def combiner(self, key, counts):
        # group value according to key and counter
        # yield no key this time
        yield None, (key, sum(counts))

    def reducer(self, _, letter_count_pairs):
        # Just likes sequence code. sort the result and reverse
        # print top 10
        sdetail = sorted(letter_count_pairs, key=lambda x: x[1])
        sdetail.reverse()

        for index in range(10):
            print sdetail[index]

        yield None, None

    def steps(self):
        return ([
                    self.mr(mapper=self.map,
                            combiner=self.combiner,
                            reducer=self.reducer)
                ])


if __name__ == '__main__':
    MRLetterCount.run()