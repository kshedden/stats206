HUGO=/home/kshedden/go/bin/hugo

%.html: %.md
	pandoc -t slidy -s $< -o $@
	mv $@ ../website/static/ks_slides
	cd ../website; $(HUGO)

