# Aero CTF 2020 : Magic I

**category** : crypto

**points** : 205

## write-up

XOR encryption

`key` is the sum of one column of a [magic square](https://en.wikipedia.org/wiki/Magic_square) of unknown dimension.

We are given the value of `key % x^2`, where `x` is the dimension.

After some computation, we got `key = x^2 * (x^2 - 1) / (2x) = (x^3 - x) / 2`

Assume `x` is even, and `x = 2y`, then `key = 4y^3 - y`, and `key % x^2 = key % 4y^2 = 4y^2 - y`.  
Plug in the value and find out that there is no integer solution.

Assume `x` is odd, and `x = 2y + 1`, then `key = 4y^3 + 6y^2 + 2y`, and `key % x^2 = 2y^2 + y`.  
Then use [Wolfram](https://www.wolframalpha.com/input/?i=2y%5E2+%2B+y+%3D+5405053190768240950975482839552589374748349681382030872360550121041249100085609471) to find the answer, which is `y = 51985830717457237488973954964904090788909` and then we can decrypt the flag.

# other write-ups and resources
