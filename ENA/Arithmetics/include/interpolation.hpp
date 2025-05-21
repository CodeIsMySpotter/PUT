#pragma once

#include <vector>
#include <tuple>
#include <set>


template<typename T>
int check_conditions(const std::vector<T>& x) {
    if (x.size() < 1) {
        return 1;  
    }
    for (size_t i = 0; i < x.size(); ++i) {
        for (size_t j = i + 1; j < x.size(); ++j) {
            if (x[i] == x[j]) {
                return 2;  
            }
        }
    }

    return 0;  
}

template<typename T>
std::vector<T> lagrange_coefficients(const std::vector<T>& x, const std::vector<T>& y) {
    size_t n = x.size();
    std::vector<T> result(n, T(0));

    for (size_t i = 0; i < n; ++i) {
        std::vector<T> li_coeffs = { T(1) }; 

        T denom = T(1);

        for (size_t j = 0; j < n; ++j) {
            if (i == j) continue;

            // li(x) *= (x - xj)
            std::vector<T> next(li_coeffs.size() + 1, T(0));

            for (size_t k = 0; k < li_coeffs.size(); ++k) {
                next[k]     -= li_coeffs[k] * x[j]; 
                next[k + 1] += li_coeffs[k];      
            }

            li_coeffs = next;
            denom *= (x[i] - x[j]); 
            
        }

        T scale = y[i] / denom;
        for (size_t k = 0; k < li_coeffs.size(); ++k)
            result[k] += li_coeffs[k] * scale;
    }

    return result;
}

template<typename T>
T lagrange_interpolation(const std::vector<T>& x, const std::vector<T>& y, T x_val) {
  
    T result = T(0);
    size_t n = x.size();
    for (size_t i = 0; i < n; ++i) {
        T term = y[i];
        for (size_t j = 0; j < n; ++j) {
            if (i != j) {
                T numerator = x_val - x[j];
                T denominator = x[i] - x[j];
                T fraction = numerator / denominator;
                
                term = term * fraction;
            }
        }
        result += term;
    }
    return result;
}

template<typename T>
T lagrange_interpolation_weighted(const std::vector<T>& x, const std::vector<T>& y, T x_val) {
   

    size_t n = x.size();
    std::vector<T> weights(n, T(1));

    // Oblicz wagi: w_i = 1 / Π_{j ≠ i} (x_i - x_j)
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j) {
            if (i != j)
                weights[i] = weights[i] * (x[i] - x[j]);
        }
        weights[i] = T(1) / weights[i];
    }

    // Oblicz licznik i mianownik sumy
    T numerator = T(0);
    T denominator = T(0);

    for (size_t i = 0; i < n; ++i) {
        T term = weights[i] / (x_val - x[i]);
        numerator += term * y[i];
        denominator += term;
    }

    T result = numerator / denominator;
    return result;
}


template<typename T>
T neville_interpolation(const std::vector<T>& x, const std::vector<T>& y, T x_val) {

    int n = static_cast<int>(x.size());
    std::vector<T> p = y;

    for (int i = 1; i < n; ++i) {
        for (int j = n - 1; j >= i; --j) {
            p[j] = ((x_val - x[j - i]) * p[j] - (x_val - x[j]) * p[j - 1]) / (x[j] - x[j - i]);
        }
    }

    return p[n - 1];
}
