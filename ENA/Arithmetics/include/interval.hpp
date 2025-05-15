#pragma once

#include <quadmath.h>   // dla f128
#include <limits>
#include <iostream>
#include <string>
#include <cmath>
#include <cfenv>

typedef __float128 f128;

#ifndef INFINITY
#define INFINITY __builtin_inff()
#endif

using namespace std;

class Interval {
public:
    Interval(const f128& lower, const f128& upper)
        : lower_bound(lower), upper_bound(upper) {}
    
    Interval(f128 value)
    : lower_bound(value), upper_bound(value) {}

    f128 lower() const { return lower_bound; }
    f128 upper() const { return upper_bound; }

    void print() const {
        char buffer[128];
        quadmath_snprintf(buffer, sizeof(buffer), "%.14Qe", lower_bound);
        std::cout << "[" << buffer << ", ";

        quadmath_snprintf(buffer, sizeof(buffer), "%.14Qe", upper_bound);
        std::cout << buffer << "]" << std::endl;
    }

    Interval operator+(const Interval& other) const {
        fesetround(FE_DOWNWARD);
        __float128 lo = lower_bound + other.lower();
        
        fesetround(FE_UPWARD);
        __float128 hi = upper_bound + other.upper();

        fesetround(FE_TONEAREST);
        return Interval(lo, hi);
    }

Interval operator-(const Interval& other) const {
    fesetround(FE_DOWNWARD);
    __float128 lo = lower_bound - other.upper();

    fesetround(FE_UPWARD);
    __float128 hi = upper_bound - other.lower();

    fesetround(FE_TONEAREST);
    return Interval(lo, hi);
}

    Interval operator*(const Interval& other) const {
        fesetround(FE_DOWNWARD);
        __float128 a = lower_bound * other.lower();
        __float128 b = lower_bound * other.upper();
        __float128 c = upper_bound * other.lower();
        __float128 d = upper_bound * other.upper();

        __float128 lo = fminq(fminq(a, b), fminq(c, d));

        fesetround(FE_UPWARD);
        a = lower_bound * other.lower();
        b = lower_bound * other.upper();
        c = upper_bound * other.lower();
        d = upper_bound * other.upper();

        __float128 hi = fmaxq(fmaxq(a, b), fmaxq(c, d));

        fesetround(FE_TONEAREST);
        return Interval(lo, hi);
    }

    Interval operator/(const Interval& other) const {
        if (other.lower() <= 0 && other.upper() >= 0) {
            throw std::invalid_argument("Nie można dzielić przez przedział zawierający zero.");
        }

        fesetround(FE_DOWNWARD);
        __float128 a = lower_bound / other.lower();
        __float128 b = lower_bound / other.upper();
        __float128 c = upper_bound / other.lower();
        __float128 d = upper_bound / other.upper();

        __float128 lo = fminq(fminq(a, b), fminq(c, d));

        fesetround(FE_UPWARD);
        a = lower_bound / other.lower();
        b = lower_bound / other.upper();
        c = upper_bound / other.lower();
        d = upper_bound / other.upper();

        __float128 hi = fmaxq(fmaxq(a, b), fmaxq(c, d));

        fesetround(FE_TONEAREST);
        return Interval(lo, hi);
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

    friend std::ostream& operator<<(std::ostream& os, const Interval& interval) {
        char buffer[128];
        quadmath_snprintf(buffer, sizeof(buffer), "%.14Qe", interval.lower_bound);
        os << "[" << "\n" << "    "<< buffer << ", " << "\n";
        quadmath_snprintf(buffer, sizeof(buffer), "%.14Qe", interval.upper_bound);
        os << "    " << buffer << "\n" << "]";
        return os;
    }

    Interval operator-() const {
        fesetround(FE_DOWNWARD);
        __float128 lo = -upper_bound;

        fesetround(FE_UPWARD);
        __float128 hi = -lower_bound;

        fesetround(FE_TONEAREST);
        return Interval(lo, hi);
    }
    

private:
    f128 lower_bound;
    f128 upper_bound;
};

string normalize_float_string(const string& str) {
    if (str.find('.') == string::npos) {
        return str + ".0"; // Jeśli nie ma kropki, dodajemy ".0"
    }
    return str;
}

bool is_representable(const string& str) {
    string input = normalize_float_string(str);
    f128 value = strtoflt128(input.c_str(), NULL); // Konwersja stringa na f128
    char buffer[128];
    quadmath_snprintf(buffer, sizeof(buffer), "%.40Qg", value);
    string back(buffer);
    
    string normalized_back = normalize_float_string(back);

    return input == normalized_back;
}

Interval string_to_interval(const string& str) {
   

    if(is_representable(str)){
        f128 value = strtoflt128(str.c_str(), NULL);
        return Interval(value, value);
    }

    fesetround(FE_DOWNWARD);
    f128 lower_bound = strtoflt128(str.c_str(), NULL);
    fesetround(FE_UPWARD);
    f128 upper_bound = strtoflt128(str.c_str(), NULL);
    fesetround(FE_TONEAREST);

    return Interval(lower_bound, upper_bound);
}
