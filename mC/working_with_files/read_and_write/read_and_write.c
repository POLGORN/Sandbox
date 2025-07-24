// Программа наученная читать теперь начнёт писать
// функции теперь типа void и вся конкретика лежит в main()
// пусть он создаст файл запишет в неё строку прочитает её же и выведет обратно
////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <stdlib.h>

void try_to_read(const char *file_to_read) {
    char ch;
    FILE *file = fopen(file_to_read, "r");

    if (file == NULL) {
        perror("!!!: file do not exist");
        return;
    } 

    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }

    fclose(file);
}

void try_to_write(const char *file_to_write, const char *text) {
    FILE *file = fopen(file_to_write, "w");
    
    if (file == NULL) {
        perror("!!!: file does not open");
        return;
    }

    fprintf(file, "%s", text);
    fclose(file);
}

int main() {
    const char *file_to_write = "in&out.txt";
    const char *text = "1 2 3\n4 5 6\n7 8 9";
    const char *file_to_read = "in&out.txt";
    
    try_to_write(file_to_write, text);
    try_to_read(file_to_read);

    return 0;
}
////////////////////////////////////////////////////////////////
//
//
