// Человеку нужно что то прочитать или написать
// программа предлагает прочитать (R) или написать (W)
// человек вводит название файла для чтения
// или тоже самое но уже с текстом
// немного улучшим
////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <stdlib.h>


void reading_and_writing(const char *filename, const char *text, char action) {
    char ch;
    FILE *file = fopen(filename, "r+");
    
    if (file == NULL) {
        perror("!!!");
        return;
    }

    if (action == 'r') {
        while ((ch = fgetc(file)) != EOF) {
            putchar(ch);
        }
    } else {    
        fprintf(file, "%s", text);
    }

    fclose(file);
    return;
}

int main() {
    char action;
    const char *filename = "input.txt";
    const char *text = "1 2 3\n4 5 6\n7 8 9";

    printf("What action do u need? r/w: ");
    scanf("%c", &action);

    if (action == 'r' || action == 'w') {
        reading_and_writing(filename, text, action);
    } else {
        printf("Try again. Write only r(read) or w(write)\n");
    }

    return 0;
}
////////////////////////////////////////////////////////////////
//
//
