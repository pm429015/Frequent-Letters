.. -*- mode: rst -*-

About
=====

Thanks `Sift Science`_ that give me a chance to play around with `1000 Most Common Words`_ dataset. I really have a lot of fun. 

After reviewed the `1000 Most Common Words`_ list, there were three questions just came to my mind, so I decided to crunch it a little bit more:

1. What is the 10 most frequent letters in this list ?

2. How to solve the first question if the list size is very hug, like 1TB ?

3. Is there any frequent letters pattern occurs in this words? 

Please go through each section for detail.

Have Fun !!

.. _`1000 Most Common Words`: http://www.giwersworld.org/computers/linux/common-words.phtml

.. _`Sift Science`: https://siftscience.com/

1. What is the 10 most frequent letters in this list ?
========================================================

Actually, this is the question that post on the company website. Since there are only 24 letters in English, I believe the easiest and fastest way to solve this problem is hash (dict in python). Please let me know if you have any better idea. 

Usage::

	python LetterCount.py

Output::

-(‘E’, 730)
-(’T’, 425) 
-(‘R’, 399)
-(‘A’, 394)
-(‘O’, 384)
-(’N’, 383)
-(‘I’, 364)
-(’S’, 352)
-(‘L’, 281)
-(‘D’, 238)]



2. How to solve the first question if the list size is very hug, like 1TB ?
==============================================================

Big data is a hot topic in these few years, so always keep in mind how to scale up your approach is a good habit. I am still a newbie of Hadoop and NoSQL, but I would still like to share my approach with you. 

Install::

Please install Mrjob (a python Hadoop framework) in order to run the code.

Usage::

	python LetterCountHadoop.py Full_frequent_words.txt

Output::

Same as Question 1.

3. Is there any frequent letters pattern occurs in this words ?
==============================================================

Recently, I saw a TV show calls `Wheel bloopers`_ . This is a interesting word guessing puzzle, but I am not good at this game, so I was thinking about implementing a algorithm to solve this problem. After crunching the common words list, I think if I can list the most frequent letter patterns in the list, I believe I will have more hints to solve the word puzzle. 

So the question becomes: how to find the frequent letter patterns ? Well, the answer become clear. The answer is “FP tree” !! The explanation of FP tree can be found `here`_ . 

Usage::
	
	python treeFP.py

Output::
In this example, if I take minimum support as 5%, I will get a lot of frequent patterns. 

Let’s play a game:

1. PA_T_C_LA_ ?
	
2. WE_ _ERN ?

3. W_A_E_E_ ?



.. _`Wheel bloopers`: http://www.youtube.com/results?search_query=Wheel%20bloopers

.. _`here`: http://hareenlaks.blogspot.com/2011/06/fp-tree-example-how-to-identify.html

Reference
============
Thanks `FP tree example`_

.. _`FP tree example` : http://hareenlaks.blogspot.com/2011/06/fp-tree-example-how-to-identify.html


