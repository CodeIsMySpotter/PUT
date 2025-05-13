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

template <typename T>
T evaluate_polynomial(const std::vector<T>& coefficients, T x) {
    T result = 0;
    T power_of_x = 1;

    for (const T& coeff : coefficients) {
        result += coeff * power_of_x;
        power_of_x *= x;
    }

    return result;
}

template<typename T>
std::vector<T> poly_multiply_scalar(const std::vector<T>& poly, T scalar) {
    std::vector<T> result(poly.size());
    for (size_t i = 0; i < poly.size(); ++i) {
        result[i] = poly[i] * scalar;
    }
    return result;
}

template<typename T>
std::vector<T> poly_multiply(const std::vector<T>& a, const std::vector<T>& b) {
    std::vector<T> result(a.size() + b.size() - 1, T(0));
    for (size_t i = 0; i < a.size(); ++i) {
        for (size_t j = 0; j < b.size(); ++j) {
            result[i + j] += a[i] * b[j];
        }
    }
    return result;
}

template<typename T>
std::vector<T> poly_add(const std::vector<T>& a, const std::vector<T>& b) {
    size_t n = std::max(a.size(), b.size());
    std::vector<T> result(n, T(0));
    for (size_t i = 0; i < a.size(); ++i) {
        result[i] += a[i];
    }
    for (size_t i = 0; i < b.size(); ++i) {
        result[i] += b[i];
    }
    return result;
}

template<typename T>
std::tuple<std::vector<T>, int> lagrange_polynomial(const std::vector<T>& x, const std::vector<T>& y) {
    int st = check_conditions(x);
    if (st != 0) {
        return std::make_tuple(std::vector<T>(), st);
    }

    size_t n = x.size();
    std::vector<T> result(n, T(0));  

    for (size_t i = 0; i < n; ++i) {
        std::vector<T> li = { T(1) };
        T denom = T(1);
        for (size_t j = 0; j < n; ++j) {
            if (i != j) {
                li = poly_multiply(li, { -x[j], T(1) }); 
                denom *= (x[i] - x[j]);
            }
        }
        li = poly_multiply_scalar(li, y[i] / denom);
        result = poly_add(result, li);
    }

    return std::make_tuple(result, 0);
}


template<typename T>
std::tuple<T, int> lagrange_interpolation(const std::vector<T>& x, const std::vector<T>& y, T x_val) {
    int st = check_conditions(x);
    if (st == 1) {
        return std::make_tuple(T(0), 1);
    } else if (st == 2) {
        return std::make_tuple(T(0), 2);
    }

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
    return std::make_tuple(result, 0);
}

template<typename T>
std::tuple<T, int> lagrange_interpolation_weighted(const std::vector<T>& x, const std::vector<T>& y, T x_val) {
    int st = check_conditions(x);
    if (st == 1) return {T(0), 1};
    if (st == 2) return {T(0), 2};

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
    return {result, 0};
}


template<typename T>
std::tuple<T, int> neville_interpolation(const std::vector<T>& x, const std::vector<T>& y, T x_val) {
    int st = check_conditions(x);
    if (st == 1) {
        return std::make_tuple(T(0), 1);
    } else if (st == 2) {
        return std::make_tuple(T(0), 2);
    }

    int n = static_cast<int>(x.size());
    std::vector<T> p = y;

    for (int i = 1; i < n; ++i) {
        for (int j = n - 1; j >= i; --j) {
            p[j] = ((x_val - x[j - i]) * p[j] - (x_val - x[j]) * p[j - 1]) / (x[j] - x[j - i]);
        }
    }

    return std::make_tuple(p[n - 1], 0);
}
