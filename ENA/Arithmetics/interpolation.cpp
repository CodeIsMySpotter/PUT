#include <boost/multiprecision/float128.hpp>
#include <iostream>
#include <vector>
#include <interpolation.h>
#include <interval.h>
#include <set>

using namespace boost::multiprecision;
using namespace std;

tuple<float128, int> lagrange_interpolation(const vector<float128>& x, const vector<float128>& y, float128 x_val) {
    int st = check_conditions(x);
    if (st == 1) {
        return make_tuple(0.0, 1);
    } else if (st == 2) {
        return make_tuple(0.0, 2);
    }

    float128 result = 0;
    size_t n = x.size();
    for (size_t i = 0; i < n; ++i) {
        float128 term = y[i];
        for (size_t j = 0; j < n; ++j) {
            if (i != j) {
                term *= (x_val - x[j]) / (x[i] - x[j]);
            }
        }
        result += term;
    }
    return make_tuple(result, 0);
}


tuple<float128, int> neville_interpolation(const vector<float128>& x, const vector<float128>& y, float128 x_val) {
    int st = check_conditions(x);
    if (st == 1) {
        return make_tuple(0.0, 1);
    } else if (st == 2) {
        return make_tuple(0.0, 2);
    }

    size_t n = x.size();
    vector<float128> p = y;

    for (size_t i = 1; i < n; ++i) {
        for (size_t j = n - 1; j >= i; --j) {
            p[j] = ((x_val - x[j - i]) * p[j] - (x_val - x[j]) * p[j - 1]) / (x[j] - x[j - i]);
        }
    }
    return make_tuple(p[n - 1], 0);
}

int check_conditions(const vector<float128>& x) {
    set<float128> unique_elements(x.begin(), x.end());
    if (unique_elements.size() != x.size()) {
        return 2;
    }

    if (x.size() < 1) {
        return 1;
    }

    return 0;
}