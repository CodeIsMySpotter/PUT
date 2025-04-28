#include <iostream>
#include <boost/multiprecision/float128.hpp>
#include <interval.h>
#include <lagrange_interpolation.h>
#include <vector>

using namespace boost::multiprecision;
using namespace std;
int main() {
  vector<float128> x = {100, 121, 144}; 
  vector<float128> y = {10, 11, 12};  
  float128 x_val = 117; 


  cout << fixed << setprecision(20); // Ustawienie precyzji wyjścia
  // Obliczanie wartości Lagrange'a
  auto [result_lagrange, status_lagrange] = lagrange_interpolation(x, y, x_val);
  if (status_lagrange != 0) {
      cout << "Blad w obliczeniach Lagrange'a. Status: " << status_lagrange << endl;
  } else {
      cout << "Wartosc wielomianu Lagrange'a w punkcie " << x_val << " to: " << result_lagrange << endl;
  }

  // Obliczanie wartości Nevile'a
  auto [result_neville, status_neville] = neville_interpolation(x, y, x_val);
  if (status_neville != 0) {
      cout << "Blad w obliczeniach Nevile'a. Status: " << status_neville << endl;
  } else {
      cout << "Wartosc wielomianu Nevile'a w punkcie " << x_val << " to: " << result_neville << endl;
  }

  return 0;
}