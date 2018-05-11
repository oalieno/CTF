# pwnable.kr : uaf

**points** : 8

## write-up

這題是 use after free

delete 掉 man, woman 後沒有把 pointer 清成 0

功能 2 可以讀檔讀到新 new 出來的 heap 上

所以我們可以重新寫值在 man, woman pointer 指向的位置

man, woman 的 structure 長的像 ( 大小是 0x20 包括 header )

```
|            heap header            |
| vtable pointer |       age        |
|  name pointer  | next heap header |
```

vtabe 第一個是 `give_shell` 第二個是 `introduction`

那我們就產生 data 大小是 0x10 然後把 vtable pointer 蓋成 vtable pointer - 0x8 就可以了

流程是先把 data 檔案產生好

再 3) free 2) after 2) after 1) use

# other write-ups and resources

