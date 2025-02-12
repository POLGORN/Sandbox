#include <stdio.h>
#include <math.h>

int main() {
    double p, q, r, d;
    int n;
    n = scanf("%lf %lf %lf", &p, &q, &r);
    if (n != 3) {
        printf("Error: Freak\n");
        return 1;
    }
    return 0;
}
