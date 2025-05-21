#pragma once

#include <quadmath.h>   // dla f128
#include <limits>
#include <iostream>
#include <string>
#include <cmath>
#include <cfenv>
#include <iomanip>

typedef __float128 f128;
typedef long double f80;

#ifndef INFINITY
#define INFINITY __builtin_inff()
#endif

using namespace std;

class Interval {
public:
    Interval(const f80& lower, const f80& upper)
        : lower_bound(lower), upper_bound(upper) {}
    
    Interval(f80 value)
    : lower_bound(value), upper_bound(value) {}

    f80 lower() const { return lower_bound; }
    f80 upper() const { return upper_bound; }



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
    f80 lo = lower_bound - other.upper();

    fesetround(FE_UPWARD);
    f80 hi = upper_bound - other.lower();

    fesetround(FE_TONEAREST);
    return Interval(lo, hi);
}

    Interval operator*(const Interval& other) const {
        fesetround(FE_DOWNWARD);
        f80 a = lower_bound * other.lower();
        f80 b = lower_bound * other.upper();
        f80 c = upper_bound * other.lower();
        f80 d = upper_bound * other.upper();

        f80 lo = min(min(a, b), min(c, d));

        fesetround(FE_UPWARD);
        a = lower_bound * other.lower();
        b = lower_bound * other.upper();
        c = upper_bound * other.lower();
        d = upper_bound * other.upper();

        f80 hi = max(max(a, b), max(c, d));

        fesetround(FE_TONEAREST);
        return Interval(lo, hi);
    }

    Interval operator/(const Interval& other) const {
        if (other.lower() <= 0 && other.upper() >= 0) {
            throw std::invalid_argument("Nie można dzielić przez przedział zawierający zero.");
        }

        fesetround(FE_DOWNWARD);
        f80 a = lower_bound / other.lower();
        f80 b = lower_bound / other.upper();
        f80 c = upper_bound / other.lower();
        f80 d = upper_bound / other.upper();

        f80 lo = min(min(a, b), min(c, d));

        fesetround(FE_UPWARD);
        a = lower_bound / other.lower();
        b = lower_bound / other.upper();
        c = upper_bound / other.lower();
        d = upper_bound / other.upper();

        f80 hi = max(max(a, b), max(c, d));

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
        std::ostringstream oss_lower, oss_upper;
        oss_lower << std::setprecision(20) << std::scientific << interval.lower_bound;
        oss_upper << std::setprecision(20) << std::scientific << interval.upper_bound;
        f80 diff = interval.upper_bound - interval.lower_bound;

        os << "[\n"
        << "    " << oss_lower.str() << ", \n"
        << "    " << oss_upper.str() << "\n"
        << "    width: " << std::setprecision(20) << std::scientific << diff << "\n"
        << "]\n";
        return os;
    }


    Interval operator-() const {
        fesetround(FE_DOWNWARD);
        f80 lo = -upper_bound;

        fesetround(FE_UPWARD);
        f80 hi = -lower_bound;

        fesetround(FE_TONEAREST);
        return Interval(lo, hi);
    }
    

private:
    f80 lower_bound;
    f80 upper_bound;
};

string normalize_float_string(const string& str) {
    if (str.find('.') == string::npos) {
        return str + ".0"; // Jeśli nie ma kropki, dodajemy ".0"
    }
    return str;
}

bool is_representable(const std::string& str) {
    std::string input = normalize_float_string(str);

    long double value = std::stold(input);

    char buffer[128];  // <-- deklaracja bufora o odpowiednim rozmiarze
    std::snprintf(buffer, sizeof(buffer), "%.40Le", value);

    std::string back(buffer);
    std::string normalized_back = normalize_float_string(back);

    return input == normalized_back;
}

Interval string_to_interval(const string& str) {
   

    if(is_representable(str)){
        f80 value = stold(str);
        return Interval(value, value);
    }

    fesetround(FE_DOWNWARD);
    f80 lower_bound = stold(str);
    fesetround(FE_UPWARD);
    f80 upper_bound = stold(str);
    fesetround(FE_TONEAREST);

    return Interval(lower_bound, upper_bound);
}
