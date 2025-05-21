#include <iostream>
#include <cmath>      // std::nextafterl
#include <iomanip>    // std::setprecision
#include <string>     // std::string, std::stold
#include <cfenv>      // sterowanie zaokrągleniami

#include <vector>
#include <tuple>

#include <interpolation.hpp>
#include <interval.hpp>

typedef long double f80;
using namespace std;

#pragma STDC FENV_ACCESS ON  // umożliwia dostęp do trybów zaokrągleń

int main() {

    cout << sizeof(f80) << endl;
    vector<Interval> X = {string_to_interval("1"), string_to_interval("2"), string_to_interval("3")};
    vector<Interval> Y = {string_to_interval("1"), string_to_interval("2"), string_to_interval("3")};
    Interval x = string_to_interval("1.1");

    auto y = lagrange_interpolation(X, Y, x);
    auto y2 = neville_interpolation(X, Y, x);

    cout << fixed << setprecision(20);
    cout << "Lagrange: " << y << endl;

    cout << "Neville: " << y2 << endl;

    vector<f80> x_vals = {1.0, 2.0, 3.0};
    vector<f80> y_vals = {1.0, 2.0, 3.0};
    f80 x_val = 1.1;
    f80 lagrange_result = lagrange_interpolation(x_vals, y_vals, x_val);
    f80 neville_result = neville_interpolation(x_vals, y_vals, x_val);
    cout << "   " << lagrange_result << endl;
    cout << "   " << neville_result << endl;
    

    return 0;
}