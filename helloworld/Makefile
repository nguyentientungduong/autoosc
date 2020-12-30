chello:
	gcc -g -o chello chello.c

clean:
	rm chello
install:
	mkdir -p $(DESTDIR)/usr/bin
	install -m 0755 chello $(DESTDIR)/usr/bin/chello
