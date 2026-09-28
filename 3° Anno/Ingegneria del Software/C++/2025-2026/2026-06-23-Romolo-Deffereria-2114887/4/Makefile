CXX = g++
CXXFLAGS = -std=c++2b -O3 -Wall -Wextra

all: main

main: main.o network.o server.o customer.o supplier.o
	$(CXX) $(CXXFLAGS) -o $@ $^

main.o: main.cpp engine.hpp common.hpp network.hpp server.hpp customer.hpp supplier.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

network.o: network.cpp network.hpp engine.hpp server.hpp customer.hpp supplier.hpp
	$(CXX) $(CXXFLAGS) -c network.cpp

server.o: server.cpp server.hpp network.hpp engine.hpp
	$(CXX) $(CXXFLAGS) -c server.cpp

customer.o: customer.cpp customer.hpp network.hpp engine.hpp
	$(CXX) $(CXXFLAGS) -c customer.cpp

supplier.o: supplier.cpp supplier.hpp network.hpp engine.hpp
	$(CXX) $(CXXFLAGS) -c supplier.cpp

clean:
	rm -f *.o main results.txt
