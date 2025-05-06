#include <quadmath.h>
#include <iostream>
#include <cmath>
#include <interval.hpp>
#include <interpolation.hpp>
#include <vector>

using namespace std;


int main() {

    vector<Interval> X = {
        string_to_interval("1.0"),
        string_to_interval("2.0"),
        string_to_interval("3.0"),
        string_to_interval("4.0"),
    };
    vector<Interval> Y = {
        string_to_interval("1.0"),
        string_to_interval("2.0"),
        string_to_interval("3.0"),
        string_to_interval("4.0"),
    };
    Interval x = string_to_interval("5.0");

    auto [RESULT, ERROR] = lagrange_interpolation<Interval>(X, Y, x);
    cout << "Wynik: ";
    RESULT.print();


    return 0;
}
