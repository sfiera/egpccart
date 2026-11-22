KICAD_CLI ?= docker run --platform linux/amd64 -v $(CURDIR):/src -w /src -u root kicad/kicad:10.0 kicad-cli

.PHONY: all
all: gamepock-cart.zip pcb.png

.PHONY: gamepock-cart.zip
gamepock-cart.zip:
	rm -Rf gamepock-cart/ $@
	$(KICAD_CLI) pcb export gerbers cart.kicad_pcb --output gamepock-cart
	$(KICAD_CLI) pcb export drill cart.kicad_pcb --output gamepock-cart
	zip -r $@ gamepock-cart/

.PHONY: pcb.png
pcb.png: cart.kicad_pcb
	$(KICAD_CLI) pcb render $< --output $@ --width 900 --height 750 --zoom 1.1 --side top --perspective

.PHONY: clean
clean:
	rm -Rf gamepock-cart gamepock-cart.zip
