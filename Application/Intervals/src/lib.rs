use rug::{Float, Assign};
use rug::ops::Pow;

// Testy w Rust są oznaczane atrybutem #[test]
#[test]
fn test_dodawanie_f128() {
    // Ustawiamy precyzję na 113 bitów (jak w f128)
    let prec = 113;
    
    // Tworzymy dwie liczby zmiennoprzecinkowe
    let a = Float::with_val(prec, 1.23456789);
    let b = Float::with_val(prec, 3.14159265);
    
    // Wykonujemy dodawanie
    let wynik = a + b;
    
    // Sprawdzamy, czy wynik jest bliski oczekiwanej wartości
    let oczekiwany = Float::with_val(prec, 4.37616054);
    assert!(Float::abs(&wynik - &oczekiwany) < Float::with_val(prec, 1e-10));
}

#[test]
fn test_mnozenie_f128() {
    let prec = 113;
    
    let a = Float::with_val(prec, 2.5);
    let b = Float::with_val(prec, 3.0);
    
    let wynik = a * b;
    
    let oczekiwany = Float::with_val(prec, 7.5);
    assert_eq!(wynik, oczekiwany);
}

#[test]
fn test_konwersja_string_na_float() {
    let prec = 113;
    let mut float = Float::new(prec);
    
    // Parsowanie stringa
    let string = "123.456789";
    let parsed = Float::parse(string).expect("Nieprawidłowy format liczby");
    float.assign(parsed);
    
    // Sprawdzamy, czy skonwertowana wartość jest poprawna
    let oczekiwany = Float::with_val(prec, 123.456789);
    assert!(Float::abs(&float - &oczekiwany) < Float::with_val(prec, 1e-10));
}

#[test]
fn test_potegowanie_f128() {
    let prec = 113;
    
    let podstawa = Float::with_val(prec, 2.0);
    let wynik = podstawa.pow(3); // 2^3
    
    let oczekiwany = Float::with_val(prec, 8.0);
    assert_eq!(wynik, oczekiwany);
}

#[test]
#[should_panic(expected = "Nieprawidłowy format liczby")]
fn test_nieprawidlowy_string() {
    let prec = 113;
    let mut float = Float::new(prec);
    
    // Próba parsowania nieprawidłowego stringa
    let string = "abc.def";
    let parsed = Float::parse(string).expect("Nieprawidłowy format liczby");
    float.assign(parsed);
}