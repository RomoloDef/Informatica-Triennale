CXX = g++
CXXFLAGS = -std=c++2b -O3 -Wall -Wextra

all: main

main: main.o network.o uav.o
	$(CXX) $(CXXFLAGS) -o $@ $^

main.o: main.cpp network.hpp uav.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

network.o: network.cpp network.hpp uav.hpp
	$(CXX) $(CXXFLAGS) -c network.cpp

uav.o: uav.cpp uav.hpp
	$(CXX) $(CXXFLAGS) -c uav.cpp

clean:
	rm -f *.o main results.txt
