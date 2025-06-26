clean:
	rm -rf $(shell find . | grep pycache)

run: 
	flask run