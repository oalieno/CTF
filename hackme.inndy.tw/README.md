# hackme.inndy.tw

## ROP2

Use the syscall gadget on the code section, but there is `leave` after syscall  
Apply stack migration technique (carefully manipulate `ebp`) to read "/bin/sh" and `syscall 0xb` (`sys_execve`)
