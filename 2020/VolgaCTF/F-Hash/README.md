# VolgaCTF 2020 Qualifier : F-Hash

**category** : reverse

**points** : 250

**solves** : 43

## write-up

Run the executable. It takes a long time and fails to find the answer.  
Then I start to reverse the binary.  
Function 12A0 takes two parameter `a, b` and return `bitcount(a) + bitcount(b)`  
Function 13B0 is a recursion function and it is the main cause of the performance. There is a while loop that continues to execute `-=`. It is actually performing mod operations.  
Rewrite the whole function using python and replace the right value in gdb and continue running. And the output will be the flag.

# other write-ups and resources
