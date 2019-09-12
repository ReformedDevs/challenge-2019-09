# challenge-2019-09

## September 2019

### Background

The Reformed Devs on Slack began doing monthly code challenges a couple of months ago. We decided to begin hosting the challenges in the official TRD namespace for June 2019. You can see the previous challenges below:

* [April 2019](https://github.com/plusuncold/longest-word-test)
* [May 2019](https://github.com/plusuncold/rainfall-calc-challenge)
* [June 2019](https://github.com/ReformedDevs/challenge-2019-06)
* [July 2019](https://github.com/ReformedDevs/challenge-2019-07)

### The Challenge

#### Problem

Find the largest prime number in the Fibonacci sequence under 9,000,000,000,000,000,000 who's square, as hexidecimal, ends on 0x9.

#### Output

Use a .sh file to output:
`Author, Language, Result, Time, Notes`

Author should be your Github account name.
Result should be an integer (no `.0`)
Time should be in milliseconds.
Notes do not need to be filled in, that's up to you. Usually people include things like single/multi thread or the algorithm used.

##### Example

The the sequence of Fibonacci numbers under 2000 is

`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597`

Of the above, `3, 5, 13, 89, 233, 1597` are prime.

The square of these primes, as hexidecimal are

`0x9, 0x19, 0xa9, 0x1ef1, 0xd411, 0x26ea89`.

Since 1597's hexidecimal square (`0x26ea89`) ends in `0x9` this is the answer.
​
The output for this, if it was found in Python would be

`github_username, Python, 1597, 30, any notes about the implementation used`

#### Scoring

This will be a time challenge, so users will be scored based on the execution time of their solution in milliseconds.

### Leaderboard

Author | Language | Results | Time | Notes
--- | --- | --- | --- | ---
cco3 | Go | 433494437 | 0.00015279999999999997 | 
pard68 | Python 3 | 433494437 | 0.0004149263999977393 |  the yeetiest
pard68 | Rust | 433494437 | 0.1266396 |  Miller-rabin
zombeej | Node | 433494437 | 0.7538570000000001 |  blarg
plusuncold | C++ | 433494437 | 710.6 | 