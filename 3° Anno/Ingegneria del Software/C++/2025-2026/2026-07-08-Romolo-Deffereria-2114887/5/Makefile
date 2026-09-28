CXX = g++
CXXFLAGS = -std=c++2b -O3 -Wall -Wextra

all: main

main: main.o network.o server.o customer.o
	$(CXX) $(CXXFLAGS) -o $@ $^

main.o: main.cpp network.hpp server.hpp customer.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

network.o: network.cpp network.hpp server.hpp customer.hpp
	$(CXX) $(CXXFLAGS) -c network.cpp

server.o: server.cpp server.hpp
	$(CXX) $(CXXFLAGS) -c server.cpp

customer.o: customer.cpp customer.hpp
	$(CXX) $(CXXFLAGS) -c customer.cpp

clean:
	rm -f *.o main results.txt
