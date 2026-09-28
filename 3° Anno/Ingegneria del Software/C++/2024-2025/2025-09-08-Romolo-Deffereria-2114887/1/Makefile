CXX = g++
CXXFLAGS = -std=c++17 -O3

OBJS = main.o UAV.o Simulation.o

all: main

main: $(OBJS)
	$(CXX) $(CXXFLAGS) -o main $(OBJS)

main.o: main.cpp Simulation.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

Simulation.o: Simulation.cpp Simulation.hpp UAV.hpp
	$(CXX) $(CXXFLAGS) -c Simulation.cpp

UAV.o: UAV.cpp UAV.hpp
	$(CXX) $(CXXFLAGS) -c UAV.cpp

clean:
	rm -f $(OBJS) main
