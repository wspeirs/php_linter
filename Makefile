all: parser/PHPLexer.g4 parser/PHPParser.g4
	antlr4 -o $(PWD)/parser -listener -visitor -Dlanguage=Python3 -lib $(PWD)/parser $(PWD)/parser/PHPLexer.g4 $(PWD)/parser/PHPParser.g4
	sed 's/PHPLexer_Python/PHPLexer/g' -i parser/PHPLexer.py
	touch parser/__init__.py

clean:
	-rm parser/*.py
	-rm parser/*.tokens
