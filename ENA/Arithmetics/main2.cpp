#include <iostream>
#include <cmath>      // std::nextafterl
#include <iomanip>    // std::setprecision
#include <string>     // std::string, std::stold
#include <cfenv>      // sterowanie zaokrągleniami
#include <mpfr.h>   // MPFR
#include <vector>
#include <tuple>
#include <fstream>

#include <interpolation.hpp>

#define PRECISION 63
#define OUTPUT_PRECISION 17

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

        bool operator==(const Interval& other) const {
            return lower_bound == other.lower() && upper_bound == other.upper();
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

void interval_to_string(Interval interval, string &left, string &right) {
     mpfr_t rop;
     mpfr_exp_t exponent;
     mpfr_init2(rop, PRECISION);
     char *str = NULL;
     char *buffer = new char[PRECISION + 3];
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
    cout << fixed << setprecision(OUTPUT_PRECISION);
    cout << scientific << "[" << left << ", " << right << "] " << "width: " << setprecision(3) << width(x) << endl;
    cout << fixed << setprecision(OUTPUT_PRECISION);
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

int mode_f80(char* argv[]) {
    
    fstream f80_file;
    f80_file.open("arithmetics/data.txt");
    
    if (!f80_file.is_open()) {
        return 3;
    }

    vector<f80> x_numbers;
    vector<f80> y_numbers;
    f80 xx;
    string line;

    for(int idx=0; idx < atoi(argv[2]); idx ++){
        if (f80_file >> line) {
            f80 number = stold(line);
            x_numbers.push_back(number);
        }
    }

    for(int idx=0; idx < atoi(argv[2]); idx ++){
        if (f80_file >> line) {
            f80 number = stold(line);
            y_numbers.push_back(number);
        }
    }

    f80_file >> line;
    xx = stold(line);

    f80_file.close();

    int st;

    f80 result = lagrange(x_numbers, y_numbers, xx, st);
    f80 result2 = neville(x_numbers, y_numbers, xx, st);
    vector<f80> result3 = coeffs(x_numbers, y_numbers, st);

    if(st == 0){
        cout << fixed << setprecision(OUTPUT_PRECISION);
        cout << "Lagrange Result: " << scientific << result << endl;
        cout << "Neville Result: " << scientific << result2 << endl;

        cout << "Lagrange polynomial coefficients: [\n";
        for (const auto& coeff : result3) {
            cout << "   " << coeff << ",\n";
        }
        cout << "]\n";
        return 0;

    }else{
        return st;
    }

}

int mode_f80_interval(char* argv[]) {
    fstream f80_file;
    f80_file.open("arithmetics/data.txt");
    
    if (!f80_file.is_open()) {
        return 3;
    }

    vector<Interval> x_numbers;
    vector<Interval> y_numbers;
    string line;


    for (int idx = 0; idx < atoi(argv[2]); idx++) {
        if (!(f80_file >> line)) {
            return 4;
        }
        try {
            x_numbers.emplace_back(line);
        } catch (const std::exception& e) {
            return 4;
        }
    }

    for (int idx = 0; idx < atoi(argv[2]); idx++) {
        if (!(f80_file >> line)) {
            return 4;
        }
        try {
            y_numbers.emplace_back(line);
        } catch (const std::exception& e) {
            return 4;
        }
    }


    f80_file >> line;
    Interval xx(line);
    f80_file.close();

    int st;

    Interval result = lagrange(x_numbers, y_numbers, xx, st);
    Interval result2 = neville(x_numbers, y_numbers, xx, st);
    vector<Interval> result3 = coeffs(x_numbers, y_numbers, st);

    if(st == 0){
        cout << "Lagrange Result: ";
        int_print(result);
        cout << "Neville Result: ";
        int_print(result2);

        cout << "Lagrange polynomial coefficients: [\n";
        for (const auto& coeff : result3) {
            int_print(coeff);
        }
        cout << "]\n";
        return 0;
    }else{
        return st;
    }
}

int mode_interval(char *argv[]){

   fstream f80_file;
    f80_file.open("arithmetics/data.txt");
    
    if (!f80_file.is_open()) {
        return 3;
    }

    vector<Interval> x_numbers;
    vector<Interval> y_numbers;
    string a, b;

    for(int idx=0; idx < atoi(argv[2]); idx ++){
        if (f80_file >> a >> b) {
            Interval number(a, b);
            x_numbers.push_back(number);
        }
    }

    for(int idx=0; idx < atoi(argv[2]); idx ++){
        if (f80_file >> a >> b) {
            Interval number(a, b);
            y_numbers.push_back(number);
        }
    }

    

    f80_file >> a >> b;
    Interval xx(a, b);
    f80_file.close();

    int st;

    Interval result = lagrange(x_numbers, y_numbers, xx, st);
    Interval result2 = neville(x_numbers, y_numbers, xx, st);
    vector<Interval> result3 = coeffs(x_numbers, y_numbers, st);

    if(st == 0){
        cout << "Lagrange Result: ";
        int_print(result);
        cout << "Neville Result: ";
        int_print(result2);

        cout << "Lagrange polynomial coefficients: [\n";
        for (const auto& coeff : result3) {
            int_print(coeff);
        }
        cout << "]\n";
        return 0;
    }else{
        return st;
    }



}




int main(int argc, char* argv[]) {

    try {
        string cmd = argv[1];

        if (cmd == "1"){
            int status = mode_f80(argv);
            if (status == 0) {
                return 0;
            } else if (status == 1) {
                cerr << "Error:" << endl;
                cerr << "Not enough points for interpolation" << endl;
                return 1;
            } else if (status == 2) {
                cerr << "Error:" << endl;
                cerr << "Duplicated X values" << endl;
                return 2;
            } else if (status == 3) {
                cerr << "Error:" << endl;
                cerr << "Error opening file" << endl;
                return 3;
            } else if(status == 4){
                cerr << "Error:" << endl;
                cerr << "Error reading file" << endl;
            }
        } else if (cmd == "2") {
            int status = mode_f80_interval(argv);
            if (status == 0) {
                return 0;
            } else if (status == 1) {
                cerr << "Error:" << endl;
                cerr << "Not enough points for interpolation" << endl;
                return 1;
            } else if (status == 2) {
                cerr << "Error:" << endl;
                cerr << "Duplicated X values" << endl;
                return 2;
            } else if (status == 3) {
                cerr << "Error:" << endl;
                cerr << "Error opening file" << endl;
                return 3;
            } else if(status == 4){
                cerr << "Error:" << endl;
                cerr << "Error reading file" << endl;
            }
        } else if (cmd == "3") {
            int status = mode_interval(argv);
            if (status == 0) {
                return 0;
            } else if (status == 1) {
                cerr << "Error:" << endl;
                cerr << "Not enough points for interpolation" << endl;
                return 1;
            } else if (status == 2) {
                cerr << "Error:" << endl;
                cerr << "Duplicated X values" << endl;
                return 2;
            } else if (status == 3) {
                cerr << "Error:" << endl;
                cerr << "Error opening file" << endl;
                return 3;
            } else if(status == 4){
                cerr << "Error:" << endl;
                cerr << "Error reading file" << endl;
            }
        } else {
            cerr << "Invalid command. Use '1', '2', or '3'." << endl;
            return 4;
        }
    } catch (const std::exception& e) {
        cerr << "Exception caught in main: " << e.what() << endl;
        return 5;  
    }  catch (...) {
        std::cerr << "Unknown exception caught!" << std::endl;
        return 6;
    }

}

//g++ -g -O0 -Wall -Wextra -Wpedantic -std=c++17 -mfpmath=387 -Iarithmetics/include -o ./arithmetics/main.exe ./arithmetics/main2.cpp -static -lmpfr -lgmp