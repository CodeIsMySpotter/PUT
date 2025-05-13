#include <quadmath.h>
#include <iostream>
#include <cmath>
#include <interval.hpp>
#include <interpolation.hpp>
#include <vector>
#include <fstream>

using namespace std;

void floating_point(int num_count, char* argv[]){
    fstream input_file("Arithmetics/data.txt", ios::in);

    if (!input_file) {
        cout << "Error opening file." << endl;
        return;
    }

    vector<f128> x_numbers;
    vector<f128> y_numbers;

    string line;

    for(int i = 0; i < num_count; ++i) {
        if (input_file>>line) {
            f128 number = strtoflt128(line.c_str(), NULL);
            x_numbers.push_back(number);
        } else {
            cout << "Error reading line " << i + 1 << endl;
            break;
        }
    }

    for(int i = 0; i < num_count; ++i) {
        if(input_file>>line) {
            f128 number = strtoflt128(line.c_str(), NULL);
            y_numbers.push_back(number);
        } else {
            cout << "Error reading line " << i + 1 << endl;
            break;
        }
    }

    f128 x_val;
    input_file >> line;
    x_val = strtoflt128(line.c_str(), NULL);
    input_file.close();

    auto [result, status] = lagrange_interpolation(x_numbers, y_numbers, x_val);
    auto [result2, status2] = neville_interpolation(x_numbers, y_numbers, x_val);
    auto [result3, status3] = lagrange_interpolation_weighted(x_numbers, y_numbers, x_val);

    cout << "Lagrange Interpolation Result: ";
    char buffer[128];
    quadmath_snprintf(buffer, sizeof(buffer), "%0.36Qg", result);
    cout << buffer << endl;

    cout << "Neville Interpolation Result: ";
    quadmath_snprintf(buffer, sizeof(buffer), "%0.36Qg", result2);
    cout << buffer << endl;

    cout << "Lagrange Interpolation Weighted Result: ";
    quadmath_snprintf(buffer, sizeof(buffer), "%0.36Qg", result3);
    cout << buffer << endl;

    
}   



void floating_point_to_interval(int num_count, char* argv[]){
    fstream input_file("Arithmetics/data.txt", ios::in);
    if (!input_file) {
        cout << "Error opening file." << endl;
        return;
    }
    vector<Interval> x_numbers;
    vector<Interval> y_numbers;
    string line;

    for(int i = 0; i < num_count; ++i) {
        if (input_file>>line) {
            f128 number = strtoflt128(line.c_str(), NULL);
            x_numbers.push_back(string_to_interval(line));
        } else {
            cout << "Error reading line " << i + 1 << endl;
            break;
        }
    }

    for(int i = 0; i < num_count; ++i) {
        if(input_file>>line) {
            f128 number = strtoflt128(line.c_str(), NULL);
            y_numbers.push_back(string_to_interval(line));
        } else {
            cout << "Error reading line " << i + 1 << endl;
            break;
        }
    }
    
    input_file >> line;
    Interval x_val = string_to_interval(line);
    input_file.close();

    auto [result, status] = lagrange_interpolation(x_numbers, y_numbers, x_val);
    auto [result2, status2] = neville_interpolation(x_numbers, y_numbers, x_val);
    auto [result3, status3] = lagrange_interpolation_weighted(x_numbers, y_numbers, x_val);
    
    cout << "Lagrange Interpolation Result: " << result << endl;
    cout << "Neville Interpolation Result: " << result2 << endl;
    cout << "Lagrange Interpolation Weighted Result: " << result3 << endl;
    


  
    
}



void interval_to_interval(int num_count, char* argv[]){
 fstream input_file("Arithmetics/data.txt", ios::in);
    if (!input_file) {
        cout << "Error opening file." << endl;
        return;
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
            cout << "Error reading line " << i + 1 << endl;
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
            cout << "Error reading line " << i + 1 << endl;
            break;
        }
    }
    
    input_file >> a >> b;
    
    f128 number1 = strtoflt128(a.c_str(), NULL);
    f128 number2 = strtoflt128(b.c_str(), NULL);
    Interval x_val = Interval(number1, number2);
    input_file.close();

    auto [result, status] = lagrange_interpolation(x_numbers, y_numbers, x_val);
    auto [result2, status2] = neville_interpolation(x_numbers, y_numbers, x_val);
    auto [result3, status3] = lagrange_interpolation_weighted(x_numbers, y_numbers, x_val);
    
    cout << "Lagrange Interpolation Result: " << result << endl;
    cout << "Neville Interpolation Result: " << result2 << endl;
    cout << "Lagrange Interpolation Weighted Result: " << result3 << endl;
}





int main(int argc, char* argv[]) {

    //Interval x = string_to_interval("0.1");
    //cout << "Interval x: " << x << endl;



    if (argc < 2) {
        cout << "Usage: " << argv[0] << " <interval>" << endl;
        return 1;
    }

    string cmd = argv[1];
    int num_count = atoi(argv[2]);

    if(cmd=="1")  {
        floating_point(num_count, argv);
    }else if (cmd=="2"){
        floating_point_to_interval(num_count, argv);
    }else if (cmd=="3"){
        interval_to_interval(num_count, argv);
    }else{
        cout << "Invalid command. Use 1, 2, or 3." << endl;
        return 1;
    }

    return 0;

}
