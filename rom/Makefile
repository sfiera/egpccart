.PHONY: all
all: gamepock-cart.zip pcb.png

.PHONY: gamepock-cart.zip
gamepock-cart.zip:
	rm -Rf gamepock-cart/ $@
	kicad-cli pcb export gerbers cart.kicad_pcb --output gamepock-cart
	kicad-cli pcb export drill cart.kicad_pcb --output gamepock-cart
	zip -r $@ gamepock-cart/

.PHONY: pcb.png
pcb.png: cart.kicad_pcb
	kicad-cli pcb render $< --output $@ --width 900 --height 750 --zoom 1.1 --side top --perspective
