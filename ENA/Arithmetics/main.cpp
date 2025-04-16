#include <iostream>
#include <boost/multiprecision/float128.hpp>

int main() {
    using boost::multiprecision::float128;

    float128 a = 0.1;
    float128 b = 0.2;

    std::cout << std::fixed << std::setprecision(35);
    std::cout << "Wynik (float128): " << a + b << std::endl;

    double c = 0.1;
    double d = 0.2;
    std::cout << "Wynik (double): " << c + d << std::endl;

    return 0;
}


// g++ main.cpp -O2 -I/mingw64/include -lquadmath -o main
