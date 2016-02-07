# hex-words_finder


#### Wow. Such software.

It's not realy supposed to be useful, I am just practicing trying to make my code look nice and cozy. The code itself is rather simple, however.

This program takes an English lexicon on input, filters it and tries to transform words into the "hex" equivalent.  For example, [the notorious #BADA55 RGB color.](http://i.imgur.com/72Qn6ow.jpg)

You can find one of pregenerated results in the file "output.txt" in this repository. There are a couple of interesting words, such 0xAC1D1C, 0xBA0BAB, 0xCABA1A, 0xDEFACE, 0xF001ED and many others.


### Substitution Rules:
1. O is substituted with 0.
2. G is substituted with 9.
3. I and L are substituted with 1, however there should be no BOTH L and I in the same word.
4. S is substituted with 5.

Yep, that's it.


### Requirements:
* Python 3
