
main.exe: euler.o main.o
	gfortran euler.o main.o -o main.exe

euler.o: euler.f90
	gfortran -Wall -Wextra -fdefault-real-8 -fdefault-double-8 -c euler.f90
main.o: main.f90
	gfortran -Wall -Wextra -fdefault-real-8 -fdefault-double-8 -c main.f90

