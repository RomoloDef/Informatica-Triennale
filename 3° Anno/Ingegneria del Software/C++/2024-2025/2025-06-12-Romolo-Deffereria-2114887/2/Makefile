CXX = g++
CXXFLAGS = -std=c++17 -O3

OBJS = main.o Vehicle.o SmartVehicle.o Simulation.o

all: main

main: $(OBJS)
	$(CXX) $(CXXFLAGS) -o main $(OBJS)

main.o: main.cpp Simulation.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

Simulation.o: Simulation.cpp Simulation.hpp Vehicle.hpp SmartVehicle.hpp
	$(CXX) $(CXXFLAGS) -c Simulation.cpp

SmartVehicle.o: SmartVehicle.cpp SmartVehicle.hpp Vehicle.hpp
	$(CXX) $(CXXFLAGS) -c SmartVehicle.cpp

Vehicle.o: Vehicle.cpp Vehicle.hpp
	$(CXX) $(CXXFLAGS) -c Vehicle.cpp

clean:
	rm -f $(OBJS) main
