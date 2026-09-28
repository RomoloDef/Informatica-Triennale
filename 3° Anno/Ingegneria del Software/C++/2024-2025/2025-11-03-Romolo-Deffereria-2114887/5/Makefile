CXX = g++
CXXFLAGS = -std=c++17 -O3

OBJS = main.o Customer.o Server.o Simulation.o

all: main

main: $(OBJS)
	$(CXX) $(CXXFLAGS) -o main $(OBJS)

main.o: main.cpp Simulation.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

Simulation.o: Simulation.cpp Simulation.hpp Customer.hpp Server.hpp
	$(CXX) $(CXXFLAGS) -c Simulation.cpp

Customer.o: Customer.cpp Customer.hpp
	$(CXX) $(CXXFLAGS) -c Customer.cpp

Server.o: Server.cpp Server.hpp
	$(CXX) $(CXXFLAGS) -c Server.cpp

clean:
	rm -f $(OBJS) main
