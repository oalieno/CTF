# pwnable.kr : leg

**points** : 2

## write-up

現學現賣一下 arm assembly

`r0` 是函式的回傳值

把 key1, key2, key3 的回傳值加起來就是答案

```
>>> key1 = 0x00008ce4
>>> key2 = 0x00008d08 + 4
>>> key3 = 0x00008d80
>>> key1 + key2 + key3
108400
```

# other write-ups and resources

