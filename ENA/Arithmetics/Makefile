# Kompilator
CXX = g++
# Flagi kompilatora
CXXFLAGS = -O2 -Iinclude -ID:\IT\SCOOP\apps\msys2\current\mingw64\include
# Flagi linkera
LDFLAGS = -lquadmath
# Wszystkie pliki cpp
SRC = $(wildcard *.cpp)
# Nazwa pliku wynikowego
OUT = main

# Domyślne polecenie
all: $(OUT)

# Jak budować main
$(OUT): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(OUT) $(LDFLAGS)

# Czyszczenie plików
clean:
	rm -f $(OUT)
