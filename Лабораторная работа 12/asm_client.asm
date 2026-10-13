section .data
    ; sockaddr_in: IPv4, адрес 127.0.0.1, порт 8080
    sock_addr:
        dw 2
        dw 0x901F
        dd 0x0100007F
        dq 0
    sock_addr_len equ $ - sock_addr

    msg db "Hello from clean NASM assembly code!", 10
    msg_len equ $ - msg

section .text
global _start

_start:
    ; socket(AF_INET, SOCK_STREAM, 0)
    mov rax, 41
    mov rdi, 2
    mov rsi, 1
    xor rdx, rdx
    syscall

    ; Проверка результата socket()
    test rax, rax
    js exit_error

    ; Сохраняем файловый дескриптор
    mov r12, rax

    ; connect(fd, &sock_addr, 16)
    mov rax, 42
    mov rdi, r12
    mov rsi, sock_addr
    mov rdx, sock_addr_len
    syscall

    ; При ошибке закрываем сокет
    test rax, rax
    js close_error

    ; write(fd, msg, msg_len)
    mov rax, 1
    mov rdi, r12
    mov rsi, msg
    mov rdx, msg_len
    syscall

    ; close(fd)
    mov rax, 3
    mov rdi, r12
    syscall

    ; exit(0)
    mov rax, 60
    xor rdi, rdi
    syscall

close_error:
    mov rax, 3
    mov rdi, r12
    syscall

exit_error:
    mov rax, 60
    mov rdi, 1
    syscall
