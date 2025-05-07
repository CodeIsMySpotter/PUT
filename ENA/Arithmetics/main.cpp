#include <quadmath.h>
#include <iostream>
#include <cmath>
#include <interval.hpp>
#include <interpolation.hpp>
#include <vector>

using namespace std;

void floating_point(int num_count){
    std::vector<__float128> X;
    for (int i = 0; i < num_count; ++i) {
        int num = strtoflt128(argv[3 + i]);
        X.push_back(num);
    }

    std::vector<__float128> Y;
    for (int i = 0; i < num_count; ++i) {
        int num = strtoflt128(argv[3 + num_count + i]);
        Y.push_back(num);
    }

    __float128 x_val = strtoflt128(argv[3 + 2 * num_count]);
    __float128 result = neville_interpolation(X, Y, x_val);
    
    char buffer[128];
    quadmath_snprintf(buffer, sizeof(buffer), "%.36Qg", result);
    std::cout << buffer << std::endl;
}

void floating_point_to_interval(){

}

void interval_to_interval(){

}





int main(int argc, char* argv[]) {
    if (argc < 2) {
        cout << "Usage: " << argv[0] << " <interval>" << endl;
        return 1;
    }

    string cmd = argv[1];
    string num_count = atoi(argv[2]);

    if(cmd=="1")  {
        floating_point(num_count);
    }else if (cmd=="2"){
        floating_point_to_interval();
    }else if (cmd=="3"){
        interval_to_interval();
    }else{
        cout << "Invalid command. Use 1, 2, or 3." << endl;
        return 1;
    }

    return 0;

}
