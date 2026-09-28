CXX = g++
CXXFLAGS = -std=c++2b -Wall -Wextra -O3

all: main

main: main.o Network.o UAV.o
	$(CXX) $(CXXFLAGS) -o main main.o Network.o UAV.o

main.o: main.cpp Network.hpp UAV.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

Network.o: Network.cpp Network.hpp UAV.hpp
	$(CXX) $(CXXFLAGS) -c Network.cpp

UAV.o: UAV.cpp UAV.hpp Network.hpp
	$(CXX) $(CXXFLAGS) -c UAV.cpp

clean:
	rm -f *.o main
