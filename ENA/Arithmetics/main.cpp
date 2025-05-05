#include <quadmath.h>
#include <iostream>
#include <cmath>

using namespace std;

// Funkcje nextafter dla __float128 (quadmath)
__float128 nextafter_up(__float128 x) {
    return nextafterq(x, INFINITY);
}

__float128 nextafter_down(__float128 x) {
    return nextafterq(x, -INFINITY);
}

void print_float128(__float128 x) {
    char buffer[128];
    quadmath_snprintf(buffer, sizeof(buffer), "%.36Qg", x); // Sformatowanie z dokładnością do 36 miejsc
    cout << buffer << endl;
}

string normalize_float_string(const string& str) {
    if (str.find('.') == string::npos) {
        return str + ".0"; // Jeśli nie ma kropki, dodajemy ".0"
    }
    return str;
}

bool is_representable(const string& str) {
    string input = normalize_float_string(str);
    __float128 value = strtoflt128(input.c_str(), NULL); // Konwersja stringa na __float128
    char buffer[128];
    quadmath_snprintf(buffer, sizeof(buffer), "%.40Qg", value);
    string back(buffer);
    
    string normalized_back = normalize_float_string(back);

    return input == normalized_back;
}


int main() {

    string str_value = "0.123456789123456789123456789123456789"; // Przykładowy string

    cout << "Is representable: " << (is_representable(str_value) ? "Yes" : "No") << endl;

    __float128 value = strtoflt128(str_value.c_str(), NULL); // Konwersja stringa na __float128
    cout << "Original value: ";
    print_float128(value);

    __float128 next_up = nextafter_up(value);
    cout << "Next value up: ";
    print_float128(next_up);
    
    __float128 next_down = nextafter_down(value);
    cout << "Next value down: ";
    print_float128(next_down);


    return 0;
}
