#include <iostream>
#include <cmath>      // std::nextafterl
#include <iomanip>    // std::setprecision
#include <string>     // std::string, std::stold
#include <cfenv>      // sterowanie zaokrągleniami
#include <mpfr.h>   // MPFR
#include <vector>
#include <tuple>

#include <interpolation.hpp>

#define PRECISION 63
#define OUTPUT_PRECISION 18

typedef long double f80;
using namespace std;







class Interval {
    public:
        Interval(string lower, string upper) {
            mpfr_t rop;
            mpfr_init2(rop, PRECISION);

            mpfr_set_str(rop, lower.c_str(), 10, MPFR_RNDD);
            lower_bound = mpfr_get_ld(rop, MPFR_RNDD);

            mpfr_set_str(rop, upper.c_str(), 10, MPFR_RNDU);
            upper_bound = mpfr_get_ld(rop, MPFR_RNDU);

            mpfr_clear(rop);
        }
        
        Interval(string value) {
            mpfr_t rop;
            mpfr_init2(rop, PRECISION);

            mpfr_set_str(rop, value.c_str(), 10, MPFR_RNDD);
            lower_bound = mpfr_get_ld(rop, MPFR_RNDD);

            mpfr_set_str(rop, value.c_str(), 10, MPFR_RNDU);
            upper_bound = mpfr_get_ld(rop, MPFR_RNDU);

            mpfr_clear(rop);
        }

        Interval(f80 lower, f80 upper) {
            lower_bound = lower;
            upper_bound = upper;
        }

        Interval(f80 value) {
            lower_bound = value;
            upper_bound = value;
        }

        f80 lower() const { return lower_bound; }
        f80 upper() const { return upper_bound; }

        Interval operator+(const Interval& other) const {
            fesetround(FE_DOWNWARD);
            f80 lo = lower_bound + other.lower();
            
            fesetround(FE_UPWARD);
            f80 hi = upper_bound + other.upper();

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
        f80 lower_bound;
        f80 upper_bound;
};

f80 width(const Interval &x) {
    f80 w1, w2;
    fesetround(FE_DOWNWARD);
    w1 = x.upper_bound - x.lower_bound;
    if (w1 < 0)
        w1 = -w1;

    fesetround(FE_UPWARD);
    w2 = x.upper_bound - x.lower_bound;
    if (w2 < 0)
        w2 = -w2;

    fesetround(FE_TONEAREST);
    return (w1 > w2) ? w1 : w2;
}

 inline void interval_to_string(Interval interval, string &left, string &right) {
     mpfr_t rop;
     mpfr_exp_t exponent;
     mpfr_init2(rop, PRECISION);
     char *str = NULL;
     char *buffer = new char(PRECISION + 3);
     mpfr_set_ld(rop, interval.lower_bound, MPFR_RNDD);
     mpfr_get_str(buffer, &exponent, 10, OUTPUT_PRECISION, rop, MPFR_RNDD);
     str = buffer;
 
     stringstream ss;
     int prec = 18; 
     ss.setf(std::ios_base::scientific);
     bool minus = (str[0] == '-');
     int splitpoint = minus ? 1 : 0;
     string sign = minus ? "-" : "";
 
     ss << std::setprecision(prec) << sign << str[splitpoint] << "."
             << &str[splitpoint + 1] << "e" << exponent - 1;
     left = ss.str();
     ss.str(std::string());
 
     mpfr_set_ld(rop, interval.upper_bound, MPFR_RNDU);
     mpfr_get_str(buffer, &exponent, 10, OUTPUT_PRECISION, rop, MPFR_RNDU);
     str = buffer;
     splitpoint = (str[0] == '-') ? 1 : 0;
     ss << std::setprecision(prec) << sign << str[splitpoint] << "."
             << &str[splitpoint + 1] << "e" << exponent - 1;
     right = ss.str();
     ss.clear();
 }
 


void int_print(Interval x) {
    string left, right;
    interval_to_string(x, left, right);
    cout << "[" << left << ", " << right << "]" << " width " << width(x) << endl;
}

Interval read(const string &sa) {
    Interval x(0);
    mpfr_t rop;
    mpfr_init2(rop, PRECISION);
    mpfr_set_str(rop, sa.c_str(), 10, MPFR_RNDD);
    f80 le = mpfr_get_ld(rop, MPFR_RNDD);

    mpfr_set_str(rop, sa.c_str(), 10, MPFR_RNDU);
    f80 re = mpfr_get_ld(rop, MPFR_RNDU);

    x.lower_bound = le;
    x.upper_bound = re;

    return x;
}

int mode_f80(){
    return 1;
}

int mode_f80_interval(){
    return 2;
}

int mode_interval(){
    return 3;
}



#pragma STDC FENV_ACCESS ON  

int main(int argc, char* argv[]) {

    vector<f80> x_numbers = {100, 121, 144};
    vector<f80> y_numbers = {10, 11, 12};
    f80 x_valf = 117;

    auto result_f = lagrange_interpolation(x_numbers, y_numbers, x_valf);
    auto result_f2 = neville_interpolation(x_numbers, y_numbers, x_valf);

    cout << fixed << setprecision(18);
    cout << "Lagrange Result: " << scientific << result_f << endl;
    cout << "Neville Result: " << scientific << result_f2 << endl;


    mpfr_set_default_prec(PRECISION);

    vector<Interval> x = {
        Interval("100"),
        Interval("121"),
        Interval("144"),
        
    };

    vector<Interval> y = {
        Interval("10"),
        Interval("11"),
        Interval("12"),
      
    };

    Interval x_val("117");

    auto result = lagrange_interpolation(x, y, x_val);
    auto result2 = neville_interpolation(x, y, x_val);
    int_print(result);
    int_print(result2);


    Interval xx(0.1, 1.1);
    int_print(xx);

    return 0;
}

//g++ -std=c++17 -mfpmath=387 -Iinclude -o main.exe main2.cpp -static -lmpfr -lgmp