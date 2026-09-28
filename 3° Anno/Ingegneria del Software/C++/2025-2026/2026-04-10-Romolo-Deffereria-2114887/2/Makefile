CXX = g++
CXXFLAGS = -std=c++2b -Wall -Wextra -O3

all: main

main: main.o network.o uav.o
	$(CXX) $(CXXFLAGS) -o main main.o network.o uav.o

main.o: main.cpp network.hpp uav.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

network.o: network.cpp network.hpp uav.hpp
	$(CXX) $(CXXFLAGS) -c network.cpp

uav.o: uav.cpp uav.hpp network.hpp
	$(CXX) $(CXXFLAGS) -c uav.cpp

clean:
	rm -f *.o main
