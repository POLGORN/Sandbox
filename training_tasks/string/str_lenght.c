#include <stdio.h>
#include <string.h>

int main() {
    char my_string[] = "Hello World";
    size_t length = strlen(my_string);
    printf("String length: %zu\n", length);
    return 0;
}
