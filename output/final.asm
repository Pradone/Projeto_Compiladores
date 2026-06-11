section .data
x dw 0
y dw 0
z dw 0
a db 0
b db 0
ok db 0
msg db 255 dup(0)
t_0 dw 0
t_1 dw 0
t_2 dw 0
t_3 dw 0
t_4 dw 0
t_5 dw 0
t_6 dw 0
t_7 dw 0
t_8 dw 0
t_9 dw 0
str_0 db "Compilador funcionando",0
str_1 db "IF verdadeiro",0
str_2 db "IF falso",0
str_3 db "Negacao funcionando",0
str_4 db "Erro na negacao",0

section .text
global _start

_start:
    mov word ptr [x], 10
    mov word ptr [y], 20
    mov ax, word ptr [x]
    add ax, word ptr [y]
    mov word ptr [t_0], ax
    mov ax, word ptr [t_0]
    imul 2
    mov word ptr [t_1], ax
    mov ax, word ptr [t_1]
    mov word ptr [z], ax
    mov byte ptr [a], 1
    mov byte ptr [b], 0
    mov ax, word ptr [x]
    cmp ax, word ptr [y]
    jl t_2_true
    mov byte ptr [t_2], 0
    jmp t_2_fim
t_2_true:
    mov byte ptr [t_2], 1
t_2_fim:
    mov al, byte ptr [t_2]
    and al, byte ptr [a]
    mov byte ptr [t_3], al
    mov al, byte ptr [t_3]
    mov byte ptr [ok], al
    lea si, [str_0]
    lea di, [msg]
    ; copiar string de str_0 para msg
    ; WRITE msg
    ; WRITE z
    cmp byte ptr [ok], 0
    je L_0
    mov ax, word ptr [z]
    add ax, 5
    mov word ptr [t_4], ax
    mov ax, word ptr [t_4]
    mov word ptr [z], ax
    ; WRITE string str_1
    ; WRITE z
    jmp L_1
L_0:
    mov ax, word ptr [z]
    sub ax, 5
    mov word ptr [t_5], ax
    mov ax, word ptr [t_5]
    mov word ptr [z], ax
    ; WRITE string str_2
    ; WRITE z
L_1:
L_2:
    mov ax, word ptr [x]
    cmp ax, word ptr [y]
    jl t_6_true
    mov byte ptr [t_6], 0
    jmp t_6_fim
t_6_true:
    mov byte ptr [t_6], 1
t_6_fim:
    cmp byte ptr [t_6], 0
    je L_3
    mov ax, word ptr [x]
    add ax, 1
    mov word ptr [t_7], ax
    mov ax, word ptr [t_7]
    mov word ptr [x], ax
    ; WRITE x
    jmp L_2
L_3:
    mov al, byte ptr [b]
    or al, 0
    mov byte ptr [t_8], al
    mov al, byte ptr [t_8]
    xor al, 1
    mov byte ptr [t_9], al
    mov al, byte ptr [t_9]
    mov byte ptr [ok], al
    cmp byte ptr [ok], 0
    je L_4
    ; WRITE string str_3
    jmp L_5
L_4:
    ; WRITE string str_4
L_5:

; fim do programa
