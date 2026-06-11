section .data
x dw 0
y dw 0
t_0 db 0

section .text
global _start

_start:
    mov word ptr [x], 10
    mov word ptr [y], 20
    mov ax, word ptr [x]
    cmp ax, word ptr [y]
    jl t_0_true
    mov byte ptr [t_0], 0
    jmp t_0_fim
t_0_true:
    mov byte ptr [t_0], 1
t_0_fim:
    cmp byte ptr [t_0], 0
    je L_0
    ; WRITE x
    jmp L_1
L_0:
    ; WRITE y
L_1:

; fim do programa
