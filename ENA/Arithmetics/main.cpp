//#include <quadmath.h>
#include <iostream>
#include <cmath>
#include <interval.hpp>
#include <interpolation.hpp>
#include <vector>
#include <fstream>
#include <iomanip>

using namespace std;

int floating_point(int num_count, char* argv[]){
    fstream input_file("Arithmetics/data.txt", ios::in);

    if (!input_file) {
        return 3;
    }

    vector<f80> x_numbers;
    vector<f80> y_numbers;

    string line;

    for(int i = 0; i < num_count; ++i) {
        if (input_file>>line) {
            f80 number = stold(line);
            x_numbers.push_back(number);
        } else {
            cerr << "Error reading line " << i + 1 << endl;
            break;
        }
    }

    for(int i = 0; i < num_count; ++i) {
        if(input_file>>line) {
            f80 number = stold(line);
            y_numbers.push_back(number);
        } else {
            cerr << "Error reading line " << i + 1 << endl;
            break;
        }
    }

    f80 x_val;
    input_file >> line;
    x_val = stold(line);
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

    cout << fixed << setprecision(20);
    cout << "Lagrange Result: " << scientific << result << endl;
    cout << "Neville Result: " << scientific << result2 << endl;


    cout << "Lagrange polynomial coefficients: [\n";
    auto result4 = lagrange_coefficients(x_numbers, y_numbers);
    for (const auto& coeff : result4) {
        
        cout << "   " << coeff << ",\n" ;
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
            f80 number = stold(line);
            x_numbers.push_back(string_to_interval(line));
        } else {
            cerr << "Error reading line " << i + 1 << endl;
            break;
        }
    }

    for(int i = 0; i < num_count; ++i) {
        if(input_file>>line) {
            f80 number = stold(line);
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
    
    
    cout << "Lagrange Result: " << result << endl;
    cout << "Neville Result: " << result2 << endl;

    cout << "Lagrange polynomial coefficients: [\n";
    auto result4 = lagrange_coefficients(x_numbers, y_numbers);
    for (const auto& coeff : result4) {
        cout << "   " << coeff << ",\n" ;
    }

    cout << "]\n";
    

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
            f80 number1 = stold(a);
            f80 number2 = stold(b);
            Interval interval = Interval(number1, number2);

            x_numbers.push_back(interval);
        } else {
            cerr << "Error reading line " << i + 1 << endl;
            break;
        }
    }

    for(int i = 0; i < num_count; ++i) {
        if(input_file>>a>>b) {
            f80 number1 = stold(a);
            f80 number2 = stold(b);
            Interval interval = Interval(number1, number2);

            y_numbers.push_back(interval);
        } else {
            cerr << "Error reading line " << i + 1 << endl;
            break;
        }
    }
    
    input_file >> a >> b;
    
    f80 number1 = stold(a);
    f80 number2 = stold(b);
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
