CXX = g++
CXXFLAGS = -std=c++2b -Wall -Wextra -O3

all: main

main: main.o Network.o Customer.o Supplier.o Server.o
	$(CXX) $(CXXFLAGS) -o main main.o Network.o Customer.o Supplier.o Server.o

main.o: main.cpp Network.hpp Customer.hpp Supplier.hpp Server.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

Network.o: Network.cpp Network.hpp Customer.hpp Supplier.hpp Server.hpp
	$(CXX) $(CXXFLAGS) -c Network.cpp

Customer.o: Customer.cpp Customer.hpp Network.hpp
	$(CXX) $(CXXFLAGS) -c Customer.cpp

Supplier.o: Supplier.cpp Supplier.hpp Network.hpp
	$(CXX) $(CXXFLAGS) -c Supplier.cpp

Server.o: Server.cpp Server.hpp Network.hpp
	$(CXX) $(CXXFLAGS) -c Server.cpp

clean:
	rm -f *.o main
