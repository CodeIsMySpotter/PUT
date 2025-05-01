# pragma once

#include <boost/multiprecision/float128.hpp>

using namespace boost::multiprecision;
using namespace std;


// Can we somehowa make these function generic? to suport the interval type?
// Or maybe we should just use the interval type in the function signatures?


int check_conditions(const vector<float128>& x);
tuple<float128, int> lagrange_interpolation(const vector<float128>& x, const vector<float128>& y, float128 x_val);
tuple<float128, int> neville_interpolation(const vector<float128>& x, const vector<float128>& y, float128 x_val);