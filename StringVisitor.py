from parser.PHPParserVisitor import PHPParserVisitor


class StringVisitor(PHPParserVisitor):
    def __init__(self):
        pass

    def visitChildren(self, node):
        result = []

        for child in node.getChildren():
            childResult = child.accept(self)
            result.append(childResult)

        if len(result) == 1 and isinstance(result, list):
            return result[0]
        else:
            return result

    def visitTerminal(self, node):
        return node.getText()