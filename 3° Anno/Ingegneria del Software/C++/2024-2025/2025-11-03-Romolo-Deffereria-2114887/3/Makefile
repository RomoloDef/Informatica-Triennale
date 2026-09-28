CXX = g++
CXXFLAGS = -std=c++17 -O3

OBJS = main.o MDP.o ParameterizedMDP.o Simulation.o

all: main

main: $(OBJS)
	$(CXX) $(CXXFLAGS) -o main $(OBJS)

main.o: main.cpp ParameterizedMDP.hpp Simulation.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

Simulation.o: Simulation.cpp Simulation.hpp MDP.hpp
	$(CXX) $(CXXFLAGS) -c Simulation.cpp

ParameterizedMDP.o: ParameterizedMDP.cpp ParameterizedMDP.hpp MDP.hpp
	$(CXX) $(CXXFLAGS) -c ParameterizedMDP.cpp

MDP.o: MDP.cpp MDP.hpp
	$(CXX) $(CXXFLAGS) -c MDP.cpp

clean:
	rm -f $(OBJS) main
