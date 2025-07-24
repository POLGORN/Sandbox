// S of the triangle
////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <stdlib.h>

int main () {

    int xA, yA, xB, yB, xC, yC;
    float S;

    // Координаты вершины А
    printf("Input coordinates of vertex A:\n");
    printf("xA = ");
    scanf("%d", &xA);
    printf("yA = ");
    scanf("%d", &yA);

    // Координаты вершины B
    printf("Input coordinates of vertex B:\n");
    printf("xB = ");
    scanf("%d", &xB);
    printf("yB = ");
    scanf("%d", &yB);
    
    // Координаты вершины C
    printf("Input coordinates of vertex C:\n");
    printf("xC = ");
    scanf("%d", &xC);
    printf("yC = ");
    scanf("%d", &yC);

    S = abs((xC - xA)*(yB - yC) - (xC - xB)*(yA - yC))/2;

    if (S == 0) {
        printf("Error: Its not triangle");
        return 1;
    }

    printf("S of the triangle = %g", S);
    return 0;
}
