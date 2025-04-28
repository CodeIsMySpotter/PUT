#ifndef INTERVAL_H
#define INTERVAL_H

#include <boost/multiprecision/float128.hpp>
#include <iostream>
#include <string>

using namespace boost::multiprecision;
using namespace std;

class Interval {
public:
    Interval(const float128& lower, const float128& upper)
        : lower_bound(lower), upper_bound(upper) {}

    float128 lower() const { return lower_bound; }
    float128 upper() const { return upper_bound; }

    void print() const {
        std::cout << "[" << lower_bound << ", " << upper_bound << "]" << std::endl;
    }

    Interval operator+(const Interval& other) const {
        return Interval(lower_bound + other.lower(), upper_bound + other.upper());
    }

    Interval operator-(const Interval& other) const {
        return Interval(lower_bound - other.upper(), upper_bound - other.lower());
    }

    Interval operator*(const Interval& other) const {
        float128 l = std::min({lower_bound * other.lower(), lower_bound * other.upper(),
                               upper_bound * other.lower(), upper_bound * other.upper()});
        float128 u = std::max({lower_bound * other.lower(), lower_bound * other.upper(),
                               upper_bound * other.lower(), upper_bound * other.upper()});
        return Interval(l, u);
    }

    Interval operator/(const Interval& other) const {
        if (other.lower() <= 0 && other.upper() >= 0) {
            throw std::invalid_argument("Nie można dzielić przez przedział, który zawiera 0.");
        }

        float128 l = std::min({lower_bound / other.lower(), lower_bound / other.upper(),
                               upper_bound / other.lower(), upper_bound / other.upper()});
        float128 u = std::max({lower_bound / other.lower(), lower_bound / other.upper(),
                               upper_bound / other.lower(), upper_bound / other.upper()});
        return Interval(l, u);
    }

private:
    float128 lower_bound;
    float128 upper_bound;
};

#endif // INTERVAL_H
