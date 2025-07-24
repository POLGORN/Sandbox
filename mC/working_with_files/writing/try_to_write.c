// Программа наученная читать теперь начнёт писать
// в отдельном файле
////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <stdlib.h>

int try_to_read() {
    FILE *file;
    char ch;

    file = fopen("input.txt", "r");
    if (file == NULL) {
        perror("!!!");
        return EXIT_FAILURE;
    }

    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }

    fclose(file);

    return EXIT_FAILURE;

}

void try_to_write(const char *filename, const char *text) { 
    // Открываем файл для записи
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Ошибка открытия файла");
        return;
    }

    // Записываем текс в файл
    fprintf(file, "%s", text);

    // Закрываем файл
    fclose(file);
}

int main() {
    int a = try_to_read();

    const char *filename = "output.txt";
    const char *text = "Hello World";

    try_to_write(filename, text);

    return 0;
}
////////////////////////////////////////////////////////////////
//
//
