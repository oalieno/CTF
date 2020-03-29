# VolgaCTF 2020 Qualifier : F-Hash

**category** : reverse

**points** : 250

**solves** : 43

## write-up

Run the executable. It takes a long time and fails to find the answer.  
Then I start to reverse the binary.  
Function 12A0 takes two parameter `a, b` and return `bitcount(a) + bitcount(b)`  
Function 13B0 is a recursion function and it is the main cause of the performance. There is a while loop that continues to execute `-=`. It is actually performing mod operations.

Rewrite the whole function using python and do the following two things.
1. Don't use recursion, cache the answer.
2. Turn the subtraction into modulus operation

Finally, replace the right value in gdb and continue running. The output will be the flag.  

# other write-ups and resources

* https://pastebin.com/Dj6wteXk
