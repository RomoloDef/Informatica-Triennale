CXX = g++
CXXFLAGS = -std=c++2b -O3 -Wall -Wextra

all: main

main: main.o customer.o supplier.o network.o server.o db.o
	$(CXX) $(CXXFLAGS) -o $@ $^

main.o: main.cpp engine.hpp common.hpp network.hpp server.hpp db.hpp customer.hpp supplier.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

customer.o: customer.cpp customer.hpp engine.hpp common.hpp
	$(CXX) $(CXXFLAGS) -c customer.cpp

supplier.o: supplier.cpp supplier.hpp engine.hpp common.hpp
	$(CXX) $(CXXFLAGS) -c supplier.cpp

network.o: network.cpp network.hpp engine.hpp common.hpp
	$(CXX) $(CXXFLAGS) -c network.cpp

server.o: server.cpp server.hpp engine.hpp common.hpp
	$(CXX) $(CXXFLAGS) -c server.cpp

db.o: db.cpp db.hpp engine.hpp common.hpp
	$(CXX) $(CXXFLAGS) -c db.cpp

clean:
	rm -f *.o main results.txt
