#pragma once

#include <quadmath.h>   // dla __float128
#include <limits>
#include <iostream>
#include <string>
#include <cmath>

#ifndef INFINITY
#define INFINITY __builtin_inff()
#endif

using namespace std;

class Interval {
public:
    Interval(const __float128& lower, const __float128& upper)
        : lower_bound(lower), upper_bound(upper) {}

    __float128 lower() const { return lower_bound; }
    __float128 upper() const { return upper_bound; }

    void print() const {
        char buffer[128];
        quadmath_snprintf(buffer, sizeof(buffer), "%.36Qg", lower_bound);
        std::cout << "[" << buffer << ", ";

        quadmath_snprintf(buffer, sizeof(buffer), "%.36Qg", upper_bound);
        std::cout << buffer << "]" << std::endl;
    }

    Interval operator+(const Interval& other) const {
        return Interval(lower_bound + other.lower(), upper_bound + other.upper());
    }

    Interval operator-(const Interval& other) const {
        return Interval(lower_bound - other.upper(), upper_bound - other.lower());
    }

    Interval operator*(const Interval& other) const {
        __float128 l = std::min({lower_bound * other.lower(), lower_bound * other.upper(),
                               upper_bound * other.lower(), upper_bound * other.upper()});
        __float128 u = std::max({lower_bound * other.lower(), lower_bound * other.upper(),
                               upper_bound * other.lower(), upper_bound * other.upper()});
        return Interval(l, u);
    }

    Interval operator/(const Interval& other) const {
        if (other.lower() <= 0 && other.upper() >= 0) {
            throw std::invalid_argument("Nie można dzielić przez przedział, który zawiera 0.");
        }

        __float128 l = std::min({lower_bound / other.lower(), lower_bound / other.upper(),
                               upper_bound / other.lower(), upper_bound / other.upper()});
        __float128 u = std::max({lower_bound / other.lower(), lower_bound / other.upper(),
                               upper_bound / other.lower(), upper_bound / other.upper()});
        return Interval(l, u);
    }

private:
    __float128 lower_bound;
    __float128 upper_bound;
};

Interval string_to_interval(const std::string& str) {
    size_t pos = str.find(',');
    if (pos == std::string::npos) {
        throw std::invalid_argument("Niepoprawny format przedziału. Użyj formatu 'lower,upper'.");
    }

    

    __float128 lower = strtoflt128(str.substr(0, pos).c_str(), NULL);
    __float128 upper = strtoflt128(str.substr(pos + 1).c_str(), NULL);

    return Interval(lower, upper);
}