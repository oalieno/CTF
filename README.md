# CTF

CTF writeups and exploit code by OAlienO

Don't take DIFFICULTY so seriously

## CRYPTO

| YEAR |       CTF        |        PROBLEM        |                KEYWORDS                | DIFFICULTY |
| :--: | :--------------: | :-------------------: | :------------------------------------: | :--------: |
| 2018 |  ASIS CTF QUALS  |     Uncle Sam         |         Schmidt-Samoa Cryptosystem     |     B      |
| 2018 |  ASIS CTF QUALS  |   The Early School    |                  xor                   |     D      |
| 2018 |      VXCTF       |    Mersenne had a fun time twisting |  mt19937_64, xor cipher  |     C      |
| 2018 |      VXCTF       |     Multiprime RSA    |        RSA, binary search              |     B      |
| 2018 |      VXCTF       | Groundbreaking Conjecture |    RSA, known high bits of p       |     B      |
| 2018 |      VXCTF       |        Taunt          |        RSA, coppersmith method         |     B      |
| 2018 |      VXCTF       |    Classical Medley   |    affine cipher, permutation cipher   |     D      |
| 2018 |     UIUCTF       |        xoracle        |               xor cipher               |     B      |
| 2018 |     UIUCTF       |        Hastad         | Håstad's Broadcast Attack, short message |    D     |
| 2018 |       0CTF       |         zer0C4        | RC4, Related Key attack                |    SSS     |
| 2018 |       0CTF       |        zer0SPN        | SPN, Linear and Differential Cryptanalysis |    SSS     |
| 2018 |       0CTF       |         zer0TC        | SPN, Linear and Differential Cryptanalysis |    SSS     |
| 2018 |     VolgaCTF     |       Forbidden       |                AES GCM                 |     A      |
| 2018 |     VolgaCTF     |        Nonsense       |                  DSA                   |     B      |
| 2018 |      N1CTF       |       baby N1ES       |            Feistel Network             |     C      |
| 2018 |      N1CTF       |        easy fs        |       Håstad's Broadcast Attack        |     B      |
| 2018 |      N1CTF       |      rsa padding      | Franklin-Reiter Related Message Attack |     C      |
| 2018 |   AceBear CTF    |   Hello fibonacci?    |                  Math                  |     C      |
| 2018 |   AceBear CTF    |     random to win     |                  Math                  |     B      |
| 2018 |   AceBear CTF    |      CNVService       |              AES CBC 變形              |     A      |
| 2018 |     TAMUCTF      |    Enigma Too Far     |                 Enigma                 |     D      |
| 2018 |     TAMUCTF      |      Image That       |                AES ECB                 |     D      |
| 2018 |     TAMUCTF      |      readyXORnot      |               xor cipher               |     D      |
| 2018 |     TAMUCTF      |       XORbytes        |               xor cipher               |     D      |
| 2017 |     UIUCTF       |        PapaRSA        | Coppersmith's Method, Known Most Bits  |     B      |
| 2017 |     UIUCTF       |        BabyRSA        |               short message            |     D      |
| 2017 | HITCON CTF QUALS |     secret server     |            AES CBC, padding            |     B      |
| 2017 | HITCON CTF QUALS | secret server revenge |            AES CBC, padding            |     A      |
| 2017 | SECCON CTF QUALS |      Vigenere3d       |            Vigenere Cipher             |     D      |
| 2017 | SECCON CTF QUALS |       Ps and Qs       |           RSA, common factor           |     C      |
| 2017 | SECCON CTF QUALS |     SHA-1 is dead     |             SHA1 Collision             |     D      |
| 2017 | SECCON CTF QUALS |      Very smooth      |              Williams p+1              |     C      |
| 2017 |  AIS3 pre exam   |        crypto1        |               xor cipher               |     D      |
| 2017 |  AIS3 pre exam   |        crypto4        |             SHA1 collision             |     C      |
| 2017 |  ASIS CTF FINAL  |     Simple Crypto     |               xor cipher               |     D      |
| 2017 |  ASIS CTF FINAL  |    Handicraft RSA     |            RSA, Pollard p-1            |     C      |
| 2017 |  CSAW CTF QUALS  |      Another Xor      |               xor cipher               |     C      |
| 2017 |  CSAW CTF QUALS  |      Almost Xor       |               xor cipher               |     B      |
| 2017 |  CSAW CTF QUALS  |       BabyCrypt       |        AES ECB, byte at a time         |     C      |
| 2017 |    DCTF QUALS    |      forgotmykey      |               xor cipher               |     C      |
| 2016 |       HCTF       | Crypto So Interesting |       rsa backdoor, wiener attack      |     C      |
| 2016 |    0CTF QUALS    |         RSA?          |               Rabin 變形               |     B      |
| 2015 | HITCON CTF QUALS |        rsabin         |               Rabin 變形               |     A      |
| 2014 | HITCON CTF QUALS |         rsaha         | Franklin-Reiter Related Message Attack |     C      |
|  OJ  |   jarvisoj.com   |      Medium RSA       |                  RSA                   |     D      |
|  OJ  |   jarvisoj.com   |       hard RSA        |                 Rabin                  |     C      |
|  OJ  |   jarvisoj.com   |     very hard RSA     |          RSA, common modulus           |     C      |
|  OJ  |   jarvisoj.com   |  Extremely hard RSA   |           RSA, short message           |     C      |

## PWN

| YEAR |       CTF        |  PROBLEM   |        KEYWORDS         | DIFFICULTY |
| :--: | :--------------: | :--------: | :---------------------: | :--------: |
| 2018 |     VXCTF        | Ken Wong's sanity check |  stack overflow |   D   |
| 2018 |     VolgaCTF     |   Ping2    |     stack overflow      |     D      |
| 2018 |   AceBear CTF    | easy heap  | out of bound read write |     C      |
| 2018 |  EOF CTF QUALS   |  writeme   |                         |     D      |
| 2018 |  EOF CTF QUALS   | magicheap2 |     fastbin attack      |     B      |
| 2018 |  EOF CTF FINAL   |   secsh    |      stack overflow     |     D      |
| 2017 |  AIS3 pre exam   |    pwn1    |                         |     D      |
| 2017 |    AIS3 FINAL    |    pwn1    |     open read write     |     C      |
| 2015 | HITCON CTF QUALS |  readable  |     stack migration     |     A      |

## REVERSE

| YEAR |           CTF            |  PROBLEM   | KEYWORDS | DIFFICULTY |
| :--: | :----------------------: | :--------: | :------: | :--------: |
| 2018 |          UIUCTF          |  triptych  |          |     C      |
| 2018 |        0CTF QUALS        |    udp     |  socket  |     A      |
| 2018 |         VolgaCTF         |   CrackMe  |  dot net, AES brute force | C |
| 2018 | CODEGATE CTF Preliminary | RedVelvet  |   angr   |     D      |
| 2018 | CODEGATE CTF Preliminary |    Boom    |   rust   |     B      |
| 2018 |      EOF CTF QUALS       |   simple   | windows  |     C      |
| 2018 |      EOF CTF QUALS       | singlehell |          |     C      |
| 2018 |      EOF CTF QUALS       | helloworld |   klee   |     C      |

## WEB

| YEAR |       CTF        |    PROBLEM     |      KEYWORDS       | DIFFICULTY |
| :--: | :--------------: | :------------: | :-----------------: | :--------: |
| 2017 |    0CTF QUALS    |  simplesqlin   | sql injection, waf  |     C      |
| 2017 |    AIS3 FINAL    |      web1      |     robots.txt      |     D      |
| 2017 |  ASIS CTF FINAL  |    Dig Dug     |     dig domain      |     C      |
| 2017 |  ASIS CTF FINAL  |    Mathilda    |         LFI         |     C      |
| 2017 | SECCON CTF QUALS |     SqlSRF     | sql injection, ssrf |     B      |
| 2017 | SECCON CTF QUALS | automatic door |         php         |     B      |

## PPC

| YEAR |  CTF  | PROBLEM  |   KEYWORDS   | DIFFICULTY |
| :--: | :---: | :------: | :----------: | :--------: |
| 2018 | ASIS CTF QUALS | Neighbour | perfect power | C |
| 2018 | ASIS CTF QUALS | Shapiro | chinese remainder theorem | B |
| 2018 | N1CTF | losetome | anti reversi |     B      |
| 2018 | N1CTF | mathGame |   3D cube    |     S      |

