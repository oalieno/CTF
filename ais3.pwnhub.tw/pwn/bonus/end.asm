global _start

section .text
_start :
	xor rax,rax
	xor rbx,rbx
	xor rcx,rcx
	xor rdx,rdx
	xor rdi,rdi
	xor rsi,rsi
	xor r8,r8
	xor r9,r9
	xor r10,r10
	xor r11,r11
	xor r12,r12
	xor r13,r13
	xor r14,r14
	xor r15,r15
	xor rbp,rbp
	call _end
	mov rax,0x3c
	xor rdi,rdi
	xor rsi,rsi
	xor rdx,rdx
	syscall
_end :
	sub rsp,0x128
	mov rsi,rsp
	mov rdx,0x148
	syscall
	add rsp,0x128
	ret
	

