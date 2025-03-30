#include <stdio.h>
#include <math.h>
#include <quadmath.h>

int main() {
    __float128 x = 0.1Q;
    double y = 0.1;

    printf("double              %.36g\n", y);
    printf("double nextafter    %.36g\n", nextafter(y, 1.0));
    
    char x_str[128];
    quadmath_snprintf(x_str, sizeof(x_str), "%.36Qg", x);
    printf("__float128      x = %s\n", x_str);

    // Najbliższa większa liczba maszynowa
    __float128 next = nextafterq(x, 1.0Q);
    quadmath_snprintf(x_str, sizeof(x_str), "%.36Qg", next);
    printf("Next float128     = %s\n", x_str);

    // Najbliższa mniejsza liczba maszynowa
    __float128 prev = nextafterq(x, 0.0Q);
    quadmath_snprintf(x_str, sizeof(x_str), "%.36Qg", prev);
    printf("Previous float128 = %s\n", x_str);

    return 0;
}
