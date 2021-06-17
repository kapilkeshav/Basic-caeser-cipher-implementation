# Basic-caeser-cipher-implementation
I have implemented the Caeser-Cipher using python. I tried to take the hash table approach for it and I made the hash tables using dictionaries.

The program basically has to has tables, one with alphabets as the key and other with the index of alphabets as the key. What happens is first my program checks and saves the index of the alphabet (like if a has index 0, program has a function that call the alphabet-key hash table and get the index). The it is sent to the hash function ((index+shift)%26)->encryption, (index-shift)%26->decryption) and then returns the encrypted text.

Hope you like it. You could contact me on twitter and linkedin:
*Twitter* - https://twitter.com/kapilkeshav__
*Linkedin* - https://www.linkedin.com/in/keshav-kapil-44a6491a5/
