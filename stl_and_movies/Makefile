all: hello_there
	

hello_there: clean main.o 
	g++ -g main.o -o hello_there  -std=c++0x

main.o: main.cpp
	g++ -g -c main.cpp -std=c++0x

clean:
	rm -rf *.o