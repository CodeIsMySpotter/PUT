#ifndef WIDGET_H  
#define WIDGET_H

#define MAX_ID_LENGTH 100  // Maksymalna długość identyfikatora

typedef struct WidgetComponent WidgetComponent;

// Struktura przechowująca dane projektowe widgetu
typedef struct {
  int width, height;      // Szerokość i wysokość
  int border_radius;      // Promień zaokrąglenia krawędzi
  int color;              // Kolor

  int icon;               // Ikona (np. indeks lub identyfikator)

  int hovered;            // Stan najechania (hover)
  int active;             // Stan aktywności
  int on_click;           // Akcja po kliknięciu (np. identyfikator funkcji)
} DesignData;

// Struktura przechowująca dane systemowe widgetu
typedef struct {
  WidgetComponent** children;  // Wskaźnik na tablicę dzieci (WidgetComponent)
  char id[MAX_ID_LENGTH];      // Identyfikator widgetu
} SystemData;

// Struktura reprezentująca komponent widgetu
typedef struct {
  DesignData design_data;  // Dane projektowe
  SystemData system_data;  // Dane systemowe
} WidgetComponent;

#endif // WIDGET_H