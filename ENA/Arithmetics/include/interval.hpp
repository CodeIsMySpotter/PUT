#pragma once

#include <quadmath.h>   // dla __float128
#include <limits>
#include <iostream>
#include <string>
#include <cmath>
#include <cfenv>

#ifndef INFINITY
#define INFINITY __builtin_inff()
#endif

using namespace std;

class Interval {
public:
    Interval(const __float128& lower, const __float128& upper)
        : lower_bound(lower), upper_bound(upper) {}
    
    Interval(__float128 value)
    : lower_bound(value), upper_bound(value) {}

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
        __float128 a = lower_bound * other.lower();
        __float128 b = lower_bound * other.upper();
        __float128 c = upper_bound * other.lower();
        __float128 d = upper_bound * other.upper();
    
        __float128 l = a;
        if (b < l) l = b;
        if (c < l) l = c;
        if (d < l) l = d;
    
        __float128 u = a;
        if (b > u) u = b;
        if (c > u) u = c;
        if (d > u) u = d;
    
        return Interval(l, u);
    }

    Interval operator/(const Interval& other) const {
        if (other.lower() <= 0 && other.upper() >= 0) {
            throw std::invalid_argument("Nie można dzielić przez przedział, który zawiera 0.");
        }
    
        __float128 a = lower_bound / other.lower();
        __float128 b = lower_bound / other.upper();
        __float128 c = upper_bound / other.lower();
        __float128 d = upper_bound / other.upper();
    
        __float128 l = a;
        if (b < l) l = b;
        if (c < l) l = c;
        if (d < l) l = d;
    
        __float128 u = a;
        if (b > u) u = b;
        if (c > u) u = c;
        if (d > u) u = d;
    
        return Interval(l, u);
    }
    
    Interval& operator+=(const Interval& other) {
        *this = *this + other;
        return *this;
    }
    
    Interval& operator-=(const Interval& other) {
        *this = *this - other;
        return *this;
    }
    
    Interval& operator*=(const Interval& other) {
        *this = *this * other;
        return *this;
    }
    
    Interval& operator/=(const Interval& other) {
        *this = *this / other;
        return *this;
    }

    bool operator==(const Interval& other) const {
        return lower_bound == other.lower_bound && upper_bound == other.upper_bound;
    }
    

private:
    __float128 lower_bound;
    __float128 upper_bound;
};

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

Interval string_to_interval(const string& str) {
    size_t comma_pos = str.find('.');
    if (comma_pos == string::npos) {
        throw std::invalid_argument("Niepoprawny format przedzialu. Oczekiwano formatu 'a,b'.");
    }


    if(is_representable(str)){
        __float128 value = strtoflt128(str.c_str(), NULL);
        return Interval(value, value);
    }

    int old_round = fegetround();
    fesetround(FE_DOWNWARD);
    __float128 lower_bound = strtoflt128(str.c_str(), NULL);
    fesetround(FE_UPWARD);
    __float128 upper_bound = strtoflt128(str.c_str(), NULL);
    fesetround(old_round);

    return Interval(lower_bound, upper_bound);
}
