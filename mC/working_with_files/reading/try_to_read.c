// Программа которая берет данные из файла
// обрабатывает и выводит данные
////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file;
    char ch;

    // Открываем файл в режиме чтения
    file = fopen("input.txt", "r");
    if (file == NULL) {
        perror("User-Error");
        return EXIT_FAILURE;
    }

    // Читаем файл посимвольно и выводим на экран
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }

    // Закрываем файл
    fclose(file);
    
    return EXIT_SUCCESS;
}
////////////////////////////////////////////////////////////////
//
//
