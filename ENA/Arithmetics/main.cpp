#include <quadmath.h>
#include <iostream>
#include <cmath>
#include <interval.hpp>

using namespace std;


int main() {

    string str_value = "0.1"; // Przykładowy string

    Interval interval = string_to_interval(str_value);
    interval.print();

   


    return 0;
}
