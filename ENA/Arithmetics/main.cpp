#include <quadmath.h>
#include <iostream>
#include <cmath>
#include <interval.hpp>
#include <interpolation.hpp>
#include <vector>
#include <fstream>

using namespace std;

int floating_point(int num_count, char* argv[]){
    fstream input_file("Arithmetics/data.txt", ios::in);

    if (!input_file) {
        return 3;
    }

    vector<f128> x_numbers;
    vector<f128> y_numbers;

    string line;

    for(int i = 0; i < num_count; ++i) {
        if (input_file>>line) {
            f128 number = strtoflt128(line.c_str(), NULL);
            x_numbers.push_back(number);
        } else {
            cerr << "Error reading line " << i + 1 << endl;
            break;
        }
    }

    for(int i = 0; i < num_count; ++i) {
        if(input_file>>line) {
            f128 number = strtoflt128(line.c_str(), NULL);
            y_numbers.push_back(number);
        } else {
            cerr << "Error reading line " << i + 1 << endl;
            break;
        }
    }

    f128 x_val;
    input_file >> line;
    x_val = strtoflt128(line.c_str(), NULL);
    input_file.close();

    int st = check_conditions(x_numbers);
    if (st == 1) {
        return 1;
    } else if (st == 2) {
        return 2;
    }

    auto result = lagrange_interpolation(x_numbers, y_numbers, x_val);
    auto result2 = neville_interpolation(x_numbers, y_numbers, x_val);
    auto result3 = lagrange_interpolation_weighted(x_numbers, y_numbers, x_val);

    cout << "Lagrange Result: ";
    char buffer[128];
    quadmath_snprintf(buffer, sizeof(buffer), "%0.14Qe", result);
    cout << buffer << endl;

    cout << "Neville Result: ";
    quadmath_snprintf(buffer, sizeof(buffer), "%0.14Qe", result2);
    cout << buffer << endl;

    cout << "Lagrange polynomial coefficients: [\n";
    auto result4 = lagrange_coefficients(x_numbers, y_numbers);
    for (const auto& coeff : result4) {
        quadmath_snprintf(buffer, sizeof(buffer), "%0.14Qe", coeff);
        cout << "   " << buffer << ",\n" ;
    }
    cout << "]\n";

    //cout << "Lagrange Interpolation Weighted Result: ";
    //quadmath_snprintf(buffer, sizeof(buffer), "%0.36Qg", result3);
    //cout << buffer << endl;

    return 0;
}   



int floating_point_to_interval(int num_count, char* argv[]){
    fstream input_file("Arithmetics/data.txt", ios::in);
    if (!input_file) {
        return 3;
    }
    vector<Interval> x_numbers;
    vector<Interval> y_numbers;
    string line;

    for(int i = 0; i < num_count; ++i) {
        if (input_file>>line) {
            f128 number = strtoflt128(line.c_str(), NULL);
            x_numbers.push_back(string_to_interval(line));
        } else {
            cerr << "Error reading line " << i + 1 << endl;
            break;
        }
    }

    for(int i = 0; i < num_count; ++i) {
        if(input_file>>line) {
            f128 number = strtoflt128(line.c_str(), NULL);
            y_numbers.push_back(string_to_interval(line));
        } else {
            cerr << "Error reading line " << i + 1 << endl;
            break;
        }
    }
    
    input_file >> line;
    Interval x_val = string_to_interval(line);
    input_file.close();

    int st = check_conditions(x_numbers);
    if (st == 1) {
        return 1;
    } else if (st == 2) {
        return 2;
    }

    auto result  = lagrange_interpolation(x_numbers, y_numbers, x_val);
    auto result2  = neville_interpolation(x_numbers, y_numbers, x_val);
    auto result3  = lagrange_interpolation_weighted(x_numbers, y_numbers, x_val);
    
    cout << "Lagrange Result: " << result << endl;
    cout << "Neville Result: " << result2 << endl;

    cout << "Lagrange polynomial coefficients: [\n";
    auto result4 = lagrange_coefficients(x_numbers, y_numbers);
    for (const auto& coeff : result4) {
        cout << "   " << coeff << ",\n" ;
    }

    cout << "]\n";
    //cout << "Lagrange Interpolation Weighted Result: " << result3 << endl;
    

    return 0;
  
    
}



int interval_to_interval(int num_count, char* argv[]){
 fstream input_file("Arithmetics/data.txt", ios::in);
    if (!input_file) {
        return 3;
    }
    vector<Interval> x_numbers;
    vector<Interval> y_numbers;
    string a, b;

    for(int i = 0; i < num_count; ++i) {
        if (input_file>>a>>b) {
            f128 number1 = strtoflt128(a.c_str(), NULL);
            f128 number2 = strtoflt128(b.c_str(), NULL);
            Interval interval = Interval(number1, number2);

            x_numbers.push_back(interval);
        } else {
            cerr << "Error reading line " << i + 1 << endl;
            break;
        }
    }

    for(int i = 0; i < num_count; ++i) {
        if(input_file>>a>>b) {
            f128 number1 = strtoflt128(a.c_str(), NULL);
            f128 number2 = strtoflt128(b.c_str(), NULL);
            Interval interval = Interval(number1, number2);

            y_numbers.push_back(interval);
        } else {
            cerr << "Error reading line " << i + 1 << endl;
            break;
        }
    }
    
    input_file >> a >> b;
    
    f128 number1 = strtoflt128(a.c_str(), NULL);
    f128 number2 = strtoflt128(b.c_str(), NULL);
    Interval x_val = Interval(number1, number2);
    input_file.close();

    int st = check_conditions(x_numbers);
    if (st == 1) {
        return 1;
    } else if (st == 2) {
        return 2;
    }

    auto result = lagrange_interpolation(x_numbers, y_numbers, x_val);
    auto result2 = neville_interpolation(x_numbers, y_numbers, x_val);
    auto result3 = lagrange_interpolation_weighted(x_numbers, y_numbers, x_val);
    

    cout << "Lagrange Result: " << result << endl;
    cout << "Neville Result: " << result2 << endl;
    return 0;

    //cout << "Lagrange Interpolation Weighted Result: " << result3 << endl;
}





int main(int argc, char* argv[]) {

    //Interval x = string_to_interval("0.1");
    //cout << "Interval x: " << x << endl;



    if (argc < 2) {
        cerr << "Usage: " << argv[0] << " <interval>" << endl;
        return 1;
    }

    string cmd = argv[1];
    int num_count = atoi(argv[2]);

    if(cmd=="1")  {
        int status = floating_point(num_count, argv);
        if(status == 0){
            return 0;
        }else if(status == 1){
            cerr << "Error:" << endl;
            cerr << "Not enough points for interpolation" << endl;
            return 1;
        }else if(status == 2){
            cerr << "Error:" << endl;
            cerr << "Duplicated X values" << endl;
            return 2;
        }else if(status == 3){
            cerr << "Error:" << endl;
            cerr << "Error oppening file" << endl;
            return 3;
        }
    }else if (cmd=="2"){
        int status = floating_point_to_interval(num_count, argv);
        if(status == 0){
            return 0;
        }else if(status == 1){
            cerr << "Error:" << endl;
            cerr << "Not enough points for interpolation" << endl;
            return 1;
        }else if(status == 2){
            cerr << "Error:" << endl;
            cerr << "Duplicated X values" << endl;
            return 2;
        }else if(status == 3){
            cerr << "Error:" << endl;
            cerr << "Error oppening file" << endl;
            return 3;
        }
    }else if (cmd=="3"){
        int status = interval_to_interval(num_count, argv);
        if(status == 0){
            return 0;
        }else if(status == 1){
            cerr << "Error:" << endl;
            cerr << "Not enough points for interpolation" << endl;
            return 1;
        }else if(status == 2){
            cerr << "Error:" << endl;
            cerr << "Duplicated X values" << endl;
            return 2;
        }else if(status == 3){
            cerr << "Error:" << endl;
            cerr << "Error oppening file" << endl;
            return 3;
        }
    }else{
        cerr << "Invalid command. Use 1, 2, or 3." << endl;
        cerr.flush();
        return 4;
    }

    return 0;

}
