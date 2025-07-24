#include <stdio.h>
#include <string.h>


int main() {
    char my_string[] = "Hello";
    size_t string = strlen(my_string);
    printf("String length (%s) = %zu\n", my_string, string);
    return 0;
}
// String length (Hello) = 5
