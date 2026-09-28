CXX = g++
CXXFLAGS = -std=c++17 -O3

OBJS = main.o Customer.o

all: main

main: $(OBJS)
	$(CXX) $(CXXFLAGS) -o main $(OBJS)

main.o: main.cpp Customer.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

Customer.o: Customer.cpp Customer.hpp
	$(CXX) $(CXXFLAGS) -c Customer.cpp

clean:
	rm -f $(OBJS) main
