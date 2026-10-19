CC ?= cc
CFLAGS ?= -O2 -Wall -Iinclude

libresize.a: src/resize.o src/clamp.o
	ar rcs $@ $^

clean:
	rm -f src/*.o libresize.a
