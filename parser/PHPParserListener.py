# Generated from /home/wspeirs/src/php_linter_public/parser/PHPParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PHPParser import PHPParser
else:
    from PHPParser import PHPParser

# This class defines a complete listener for a parse tree produced by PHPParser.
class PHPParserListener(ParseTreeListener):

    # Enter a parse tree produced by PHPParser#htmlDocument.
    def enterHtmlDocument(self, ctx:PHPParser.HtmlDocumentContext):
        pass

    # Exit a parse tree produced by PHPParser#htmlDocument.
    def exitHtmlDocument(self, ctx:PHPParser.HtmlDocumentContext):
        pass


    # Enter a parse tree produced by PHPParser#htmlElementOrPhpBlock.
    def enterHtmlElementOrPhpBlock(self, ctx:PHPParser.HtmlElementOrPhpBlockContext):
        pass

    # Exit a parse tree produced by PHPParser#htmlElementOrPhpBlock.
    def exitHtmlElementOrPhpBlock(self, ctx:PHPParser.HtmlElementOrPhpBlockContext):
        pass


    # Enter a parse tree produced by PHPParser#htmlElement.
    def enterHtmlElement(self, ctx:PHPParser.HtmlElementContext):
        pass

    # Exit a parse tree produced by PHPParser#htmlElement.
    def exitHtmlElement(self, ctx:PHPParser.HtmlElementContext):
        pass


    # Enter a parse tree produced by PHPParser#scriptTextPart.
    def enterScriptTextPart(self, ctx:PHPParser.ScriptTextPartContext):
        pass

    # Exit a parse tree produced by PHPParser#scriptTextPart.
    def exitScriptTextPart(self, ctx:PHPParser.ScriptTextPartContext):
        pass


    # Enter a parse tree produced by PHPParser#phpBlock.
    def enterPhpBlock(self, ctx:PHPParser.PhpBlockContext):
        pass

    # Exit a parse tree produced by PHPParser#phpBlock.
    def exitPhpBlock(self, ctx:PHPParser.PhpBlockContext):
        pass


    # Enter a parse tree produced by PHPParser#importStatement.
    def enterImportStatement(self, ctx:PHPParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#importStatement.
    def exitImportStatement(self, ctx:PHPParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#topStatement.
    def enterTopStatement(self, ctx:PHPParser.TopStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#topStatement.
    def exitTopStatement(self, ctx:PHPParser.TopStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#useDeclaration.
    def enterUseDeclaration(self, ctx:PHPParser.UseDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#useDeclaration.
    def exitUseDeclaration(self, ctx:PHPParser.UseDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#useDeclarationContentList.
    def enterUseDeclarationContentList(self, ctx:PHPParser.UseDeclarationContentListContext):
        pass

    # Exit a parse tree produced by PHPParser#useDeclarationContentList.
    def exitUseDeclarationContentList(self, ctx:PHPParser.UseDeclarationContentListContext):
        pass


    # Enter a parse tree produced by PHPParser#useDeclarationContent.
    def enterUseDeclarationContent(self, ctx:PHPParser.UseDeclarationContentContext):
        pass

    # Exit a parse tree produced by PHPParser#useDeclarationContent.
    def exitUseDeclarationContent(self, ctx:PHPParser.UseDeclarationContentContext):
        pass


    # Enter a parse tree produced by PHPParser#namespaceDeclaration.
    def enterNamespaceDeclaration(self, ctx:PHPParser.NamespaceDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#namespaceDeclaration.
    def exitNamespaceDeclaration(self, ctx:PHPParser.NamespaceDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#namespaceStatement.
    def enterNamespaceStatement(self, ctx:PHPParser.NamespaceStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#namespaceStatement.
    def exitNamespaceStatement(self, ctx:PHPParser.NamespaceStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:PHPParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:PHPParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#classDeclaration.
    def enterClassDeclaration(self, ctx:PHPParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#classDeclaration.
    def exitClassDeclaration(self, ctx:PHPParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#classEntryType.
    def enterClassEntryType(self, ctx:PHPParser.ClassEntryTypeContext):
        pass

    # Exit a parse tree produced by PHPParser#classEntryType.
    def exitClassEntryType(self, ctx:PHPParser.ClassEntryTypeContext):
        pass


    # Enter a parse tree produced by PHPParser#interfaceList.
    def enterInterfaceList(self, ctx:PHPParser.InterfaceListContext):
        pass

    # Exit a parse tree produced by PHPParser#interfaceList.
    def exitInterfaceList(self, ctx:PHPParser.InterfaceListContext):
        pass


    # Enter a parse tree produced by PHPParser#typeParameterListInBrackets.
    def enterTypeParameterListInBrackets(self, ctx:PHPParser.TypeParameterListInBracketsContext):
        pass

    # Exit a parse tree produced by PHPParser#typeParameterListInBrackets.
    def exitTypeParameterListInBrackets(self, ctx:PHPParser.TypeParameterListInBracketsContext):
        pass


    # Enter a parse tree produced by PHPParser#typeParameterList.
    def enterTypeParameterList(self, ctx:PHPParser.TypeParameterListContext):
        pass

    # Exit a parse tree produced by PHPParser#typeParameterList.
    def exitTypeParameterList(self, ctx:PHPParser.TypeParameterListContext):
        pass


    # Enter a parse tree produced by PHPParser#typeParameterWithDefaultsList.
    def enterTypeParameterWithDefaultsList(self, ctx:PHPParser.TypeParameterWithDefaultsListContext):
        pass

    # Exit a parse tree produced by PHPParser#typeParameterWithDefaultsList.
    def exitTypeParameterWithDefaultsList(self, ctx:PHPParser.TypeParameterWithDefaultsListContext):
        pass


    # Enter a parse tree produced by PHPParser#typeParameterDecl.
    def enterTypeParameterDecl(self, ctx:PHPParser.TypeParameterDeclContext):
        pass

    # Exit a parse tree produced by PHPParser#typeParameterDecl.
    def exitTypeParameterDecl(self, ctx:PHPParser.TypeParameterDeclContext):
        pass


    # Enter a parse tree produced by PHPParser#typeParameterWithDefaultDecl.
    def enterTypeParameterWithDefaultDecl(self, ctx:PHPParser.TypeParameterWithDefaultDeclContext):
        pass

    # Exit a parse tree produced by PHPParser#typeParameterWithDefaultDecl.
    def exitTypeParameterWithDefaultDecl(self, ctx:PHPParser.TypeParameterWithDefaultDeclContext):
        pass


    # Enter a parse tree produced by PHPParser#genericDynamicArgs.
    def enterGenericDynamicArgs(self, ctx:PHPParser.GenericDynamicArgsContext):
        pass

    # Exit a parse tree produced by PHPParser#genericDynamicArgs.
    def exitGenericDynamicArgs(self, ctx:PHPParser.GenericDynamicArgsContext):
        pass


    # Enter a parse tree produced by PHPParser#attributes.
    def enterAttributes(self, ctx:PHPParser.AttributesContext):
        pass

    # Exit a parse tree produced by PHPParser#attributes.
    def exitAttributes(self, ctx:PHPParser.AttributesContext):
        pass


    # Enter a parse tree produced by PHPParser#attributesGroup.
    def enterAttributesGroup(self, ctx:PHPParser.AttributesGroupContext):
        pass

    # Exit a parse tree produced by PHPParser#attributesGroup.
    def exitAttributesGroup(self, ctx:PHPParser.AttributesGroupContext):
        pass


    # Enter a parse tree produced by PHPParser#attribute.
    def enterAttribute(self, ctx:PHPParser.AttributeContext):
        pass

    # Exit a parse tree produced by PHPParser#attribute.
    def exitAttribute(self, ctx:PHPParser.AttributeContext):
        pass


    # Enter a parse tree produced by PHPParser#attributeArgList.
    def enterAttributeArgList(self, ctx:PHPParser.AttributeArgListContext):
        pass

    # Exit a parse tree produced by PHPParser#attributeArgList.
    def exitAttributeArgList(self, ctx:PHPParser.AttributeArgListContext):
        pass


    # Enter a parse tree produced by PHPParser#attributeNamedArgList.
    def enterAttributeNamedArgList(self, ctx:PHPParser.AttributeNamedArgListContext):
        pass

    # Exit a parse tree produced by PHPParser#attributeNamedArgList.
    def exitAttributeNamedArgList(self, ctx:PHPParser.AttributeNamedArgListContext):
        pass


    # Enter a parse tree produced by PHPParser#attributeNamedArg.
    def enterAttributeNamedArg(self, ctx:PHPParser.AttributeNamedArgContext):
        pass

    # Exit a parse tree produced by PHPParser#attributeNamedArg.
    def exitAttributeNamedArg(self, ctx:PHPParser.AttributeNamedArgContext):
        pass


    # Enter a parse tree produced by PHPParser#innerStatementList.
    def enterInnerStatementList(self, ctx:PHPParser.InnerStatementListContext):
        pass

    # Exit a parse tree produced by PHPParser#innerStatementList.
    def exitInnerStatementList(self, ctx:PHPParser.InnerStatementListContext):
        pass


    # Enter a parse tree produced by PHPParser#innerStatement.
    def enterInnerStatement(self, ctx:PHPParser.InnerStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#innerStatement.
    def exitInnerStatement(self, ctx:PHPParser.InnerStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#statement.
    def enterStatement(self, ctx:PHPParser.StatementContext):
        pass

    # Exit a parse tree produced by PHPParser#statement.
    def exitStatement(self, ctx:PHPParser.StatementContext):
        pass


    # Enter a parse tree produced by PHPParser#emptyStatement.
    def enterEmptyStatement(self, ctx:PHPParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#emptyStatement.
    def exitEmptyStatement(self, ctx:PHPParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#nonEmptyStatement.
    def enterNonEmptyStatement(self, ctx:PHPParser.NonEmptyStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#nonEmptyStatement.
    def exitNonEmptyStatement(self, ctx:PHPParser.NonEmptyStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#blockStatement.
    def enterBlockStatement(self, ctx:PHPParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#blockStatement.
    def exitBlockStatement(self, ctx:PHPParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#ifStatement.
    def enterIfStatement(self, ctx:PHPParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#ifStatement.
    def exitIfStatement(self, ctx:PHPParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#elseIfStatement.
    def enterElseIfStatement(self, ctx:PHPParser.ElseIfStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#elseIfStatement.
    def exitElseIfStatement(self, ctx:PHPParser.ElseIfStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#elseIfColonStatement.
    def enterElseIfColonStatement(self, ctx:PHPParser.ElseIfColonStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#elseIfColonStatement.
    def exitElseIfColonStatement(self, ctx:PHPParser.ElseIfColonStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#elseStatement.
    def enterElseStatement(self, ctx:PHPParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#elseStatement.
    def exitElseStatement(self, ctx:PHPParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#elseColonStatement.
    def enterElseColonStatement(self, ctx:PHPParser.ElseColonStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#elseColonStatement.
    def exitElseColonStatement(self, ctx:PHPParser.ElseColonStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#whileStatement.
    def enterWhileStatement(self, ctx:PHPParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#whileStatement.
    def exitWhileStatement(self, ctx:PHPParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:PHPParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:PHPParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#forStatement.
    def enterForStatement(self, ctx:PHPParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#forStatement.
    def exitForStatement(self, ctx:PHPParser.ForStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#forInit.
    def enterForInit(self, ctx:PHPParser.ForInitContext):
        pass

    # Exit a parse tree produced by PHPParser#forInit.
    def exitForInit(self, ctx:PHPParser.ForInitContext):
        pass


    # Enter a parse tree produced by PHPParser#forUpdate.
    def enterForUpdate(self, ctx:PHPParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by PHPParser#forUpdate.
    def exitForUpdate(self, ctx:PHPParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by PHPParser#switchStatement.
    def enterSwitchStatement(self, ctx:PHPParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#switchStatement.
    def exitSwitchStatement(self, ctx:PHPParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#switchBlock.
    def enterSwitchBlock(self, ctx:PHPParser.SwitchBlockContext):
        pass

    # Exit a parse tree produced by PHPParser#switchBlock.
    def exitSwitchBlock(self, ctx:PHPParser.SwitchBlockContext):
        pass


    # Enter a parse tree produced by PHPParser#breakStatement.
    def enterBreakStatement(self, ctx:PHPParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#breakStatement.
    def exitBreakStatement(self, ctx:PHPParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#continueStatement.
    def enterContinueStatement(self, ctx:PHPParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#continueStatement.
    def exitContinueStatement(self, ctx:PHPParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#returnStatement.
    def enterReturnStatement(self, ctx:PHPParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#returnStatement.
    def exitReturnStatement(self, ctx:PHPParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#expressionStatement.
    def enterExpressionStatement(self, ctx:PHPParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#expressionStatement.
    def exitExpressionStatement(self, ctx:PHPParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#unsetStatement.
    def enterUnsetStatement(self, ctx:PHPParser.UnsetStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#unsetStatement.
    def exitUnsetStatement(self, ctx:PHPParser.UnsetStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#foreachStatement.
    def enterForeachStatement(self, ctx:PHPParser.ForeachStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#foreachStatement.
    def exitForeachStatement(self, ctx:PHPParser.ForeachStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#tryCatchFinally.
    def enterTryCatchFinally(self, ctx:PHPParser.TryCatchFinallyContext):
        pass

    # Exit a parse tree produced by PHPParser#tryCatchFinally.
    def exitTryCatchFinally(self, ctx:PHPParser.TryCatchFinallyContext):
        pass


    # Enter a parse tree produced by PHPParser#catchClause.
    def enterCatchClause(self, ctx:PHPParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by PHPParser#catchClause.
    def exitCatchClause(self, ctx:PHPParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by PHPParser#finallyStatement.
    def enterFinallyStatement(self, ctx:PHPParser.FinallyStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#finallyStatement.
    def exitFinallyStatement(self, ctx:PHPParser.FinallyStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#throwStatement.
    def enterThrowStatement(self, ctx:PHPParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#throwStatement.
    def exitThrowStatement(self, ctx:PHPParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#gotoStatement.
    def enterGotoStatement(self, ctx:PHPParser.GotoStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#gotoStatement.
    def exitGotoStatement(self, ctx:PHPParser.GotoStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#declareStatement.
    def enterDeclareStatement(self, ctx:PHPParser.DeclareStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#declareStatement.
    def exitDeclareStatement(self, ctx:PHPParser.DeclareStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#inlineHtml.
    def enterInlineHtml(self, ctx:PHPParser.InlineHtmlContext):
        pass

    # Exit a parse tree produced by PHPParser#inlineHtml.
    def exitInlineHtml(self, ctx:PHPParser.InlineHtmlContext):
        pass


    # Enter a parse tree produced by PHPParser#declareList.
    def enterDeclareList(self, ctx:PHPParser.DeclareListContext):
        pass

    # Exit a parse tree produced by PHPParser#declareList.
    def exitDeclareList(self, ctx:PHPParser.DeclareListContext):
        pass


    # Enter a parse tree produced by PHPParser#formalParameterList.
    def enterFormalParameterList(self, ctx:PHPParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by PHPParser#formalParameterList.
    def exitFormalParameterList(self, ctx:PHPParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by PHPParser#formalParameter.
    def enterFormalParameter(self, ctx:PHPParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by PHPParser#formalParameter.
    def exitFormalParameter(self, ctx:PHPParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by PHPParser#typeHint.
    def enterTypeHint(self, ctx:PHPParser.TypeHintContext):
        pass

    # Exit a parse tree produced by PHPParser#typeHint.
    def exitTypeHint(self, ctx:PHPParser.TypeHintContext):
        pass


    # Enter a parse tree produced by PHPParser#globalStatement.
    def enterGlobalStatement(self, ctx:PHPParser.GlobalStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#globalStatement.
    def exitGlobalStatement(self, ctx:PHPParser.GlobalStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#globalVar.
    def enterGlobalVar(self, ctx:PHPParser.GlobalVarContext):
        pass

    # Exit a parse tree produced by PHPParser#globalVar.
    def exitGlobalVar(self, ctx:PHPParser.GlobalVarContext):
        pass


    # Enter a parse tree produced by PHPParser#echoStatement.
    def enterEchoStatement(self, ctx:PHPParser.EchoStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#echoStatement.
    def exitEchoStatement(self, ctx:PHPParser.EchoStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#staticVariableStatement.
    def enterStaticVariableStatement(self, ctx:PHPParser.StaticVariableStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#staticVariableStatement.
    def exitStaticVariableStatement(self, ctx:PHPParser.StaticVariableStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#classStatement.
    def enterClassStatement(self, ctx:PHPParser.ClassStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#classStatement.
    def exitClassStatement(self, ctx:PHPParser.ClassStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#traitAdaptations.
    def enterTraitAdaptations(self, ctx:PHPParser.TraitAdaptationsContext):
        pass

    # Exit a parse tree produced by PHPParser#traitAdaptations.
    def exitTraitAdaptations(self, ctx:PHPParser.TraitAdaptationsContext):
        pass


    # Enter a parse tree produced by PHPParser#traitAdaptationStatement.
    def enterTraitAdaptationStatement(self, ctx:PHPParser.TraitAdaptationStatementContext):
        pass

    # Exit a parse tree produced by PHPParser#traitAdaptationStatement.
    def exitTraitAdaptationStatement(self, ctx:PHPParser.TraitAdaptationStatementContext):
        pass


    # Enter a parse tree produced by PHPParser#traitPrecedence.
    def enterTraitPrecedence(self, ctx:PHPParser.TraitPrecedenceContext):
        pass

    # Exit a parse tree produced by PHPParser#traitPrecedence.
    def exitTraitPrecedence(self, ctx:PHPParser.TraitPrecedenceContext):
        pass


    # Enter a parse tree produced by PHPParser#traitAlias.
    def enterTraitAlias(self, ctx:PHPParser.TraitAliasContext):
        pass

    # Exit a parse tree produced by PHPParser#traitAlias.
    def exitTraitAlias(self, ctx:PHPParser.TraitAliasContext):
        pass


    # Enter a parse tree produced by PHPParser#traitMethodReference.
    def enterTraitMethodReference(self, ctx:PHPParser.TraitMethodReferenceContext):
        pass

    # Exit a parse tree produced by PHPParser#traitMethodReference.
    def exitTraitMethodReference(self, ctx:PHPParser.TraitMethodReferenceContext):
        pass


    # Enter a parse tree produced by PHPParser#baseCtorCall.
    def enterBaseCtorCall(self, ctx:PHPParser.BaseCtorCallContext):
        pass

    # Exit a parse tree produced by PHPParser#baseCtorCall.
    def exitBaseCtorCall(self, ctx:PHPParser.BaseCtorCallContext):
        pass


    # Enter a parse tree produced by PHPParser#methodBody.
    def enterMethodBody(self, ctx:PHPParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by PHPParser#methodBody.
    def exitMethodBody(self, ctx:PHPParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by PHPParser#propertyModifiers.
    def enterPropertyModifiers(self, ctx:PHPParser.PropertyModifiersContext):
        pass

    # Exit a parse tree produced by PHPParser#propertyModifiers.
    def exitPropertyModifiers(self, ctx:PHPParser.PropertyModifiersContext):
        pass


    # Enter a parse tree produced by PHPParser#memberModifiers.
    def enterMemberModifiers(self, ctx:PHPParser.MemberModifiersContext):
        pass

    # Exit a parse tree produced by PHPParser#memberModifiers.
    def exitMemberModifiers(self, ctx:PHPParser.MemberModifiersContext):
        pass


    # Enter a parse tree produced by PHPParser#variableInitializer.
    def enterVariableInitializer(self, ctx:PHPParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by PHPParser#variableInitializer.
    def exitVariableInitializer(self, ctx:PHPParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by PHPParser#identifierInititalizer.
    def enterIdentifierInititalizer(self, ctx:PHPParser.IdentifierInititalizerContext):
        pass

    # Exit a parse tree produced by PHPParser#identifierInititalizer.
    def exitIdentifierInititalizer(self, ctx:PHPParser.IdentifierInititalizerContext):
        pass


    # Enter a parse tree produced by PHPParser#globalConstantDeclaration.
    def enterGlobalConstantDeclaration(self, ctx:PHPParser.GlobalConstantDeclarationContext):
        pass

    # Exit a parse tree produced by PHPParser#globalConstantDeclaration.
    def exitGlobalConstantDeclaration(self, ctx:PHPParser.GlobalConstantDeclarationContext):
        pass


    # Enter a parse tree produced by PHPParser#expressionList.
    def enterExpressionList(self, ctx:PHPParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by PHPParser#expressionList.
    def exitExpressionList(self, ctx:PHPParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by PHPParser#parenthesis.
    def enterParenthesis(self, ctx:PHPParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by PHPParser#parenthesis.
    def exitParenthesis(self, ctx:PHPParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by PHPParser#expression.
    def enterExpression(self, ctx:PHPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#expression.
    def exitExpression(self, ctx:PHPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#andOrExpression.
    def enterAndOrExpression(self, ctx:PHPParser.AndOrExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#andOrExpression.
    def exitAndOrExpression(self, ctx:PHPParser.AndOrExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#comparisonExpression.
    def enterComparisonExpression(self, ctx:PHPParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#comparisonExpression.
    def exitComparisonExpression(self, ctx:PHPParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#additionExpression.
    def enterAdditionExpression(self, ctx:PHPParser.AdditionExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#additionExpression.
    def exitAdditionExpression(self, ctx:PHPParser.AdditionExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#multiplicationExpression.
    def enterMultiplicationExpression(self, ctx:PHPParser.MultiplicationExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#multiplicationExpression.
    def exitMultiplicationExpression(self, ctx:PHPParser.MultiplicationExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#CloneExpression.
    def enterCloneExpression(self, ctx:PHPParser.CloneExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#CloneExpression.
    def exitCloneExpression(self, ctx:PHPParser.CloneExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#NewExpression.
    def enterNewExpression(self, ctx:PHPParser.NewExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#NewExpression.
    def exitNewExpression(self, ctx:PHPParser.NewExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#IndexerExpression.
    def enterIndexerExpression(self, ctx:PHPParser.IndexerExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#IndexerExpression.
    def exitIndexerExpression(self, ctx:PHPParser.IndexerExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#CastExpression.
    def enterCastExpression(self, ctx:PHPParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#CastExpression.
    def exitCastExpression(self, ctx:PHPParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#UnaryOperatorExpression.
    def enterUnaryOperatorExpression(self, ctx:PHPParser.UnaryOperatorExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#UnaryOperatorExpression.
    def exitUnaryOperatorExpression(self, ctx:PHPParser.UnaryOperatorExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#PrefixIncDecExpression.
    def enterPrefixIncDecExpression(self, ctx:PHPParser.PrefixIncDecExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#PrefixIncDecExpression.
    def exitPrefixIncDecExpression(self, ctx:PHPParser.PrefixIncDecExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#PostfixIncDecExpression.
    def enterPostfixIncDecExpression(self, ctx:PHPParser.PostfixIncDecExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#PostfixIncDecExpression.
    def exitPostfixIncDecExpression(self, ctx:PHPParser.PostfixIncDecExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx:PHPParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx:PHPParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#PrintExpression.
    def enterPrintExpression(self, ctx:PHPParser.PrintExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#PrintExpression.
    def exitPrintExpression(self, ctx:PHPParser.PrintExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#ChainExpression.
    def enterChainExpression(self, ctx:PHPParser.ChainExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#ChainExpression.
    def exitChainExpression(self, ctx:PHPParser.ChainExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#ScalarExpression.
    def enterScalarExpression(self, ctx:PHPParser.ScalarExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#ScalarExpression.
    def exitScalarExpression(self, ctx:PHPParser.ScalarExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#BackQuoteStringExpression.
    def enterBackQuoteStringExpression(self, ctx:PHPParser.BackQuoteStringExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#BackQuoteStringExpression.
    def exitBackQuoteStringExpression(self, ctx:PHPParser.BackQuoteStringExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#ParenthesisExpression.
    def enterParenthesisExpression(self, ctx:PHPParser.ParenthesisExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#ParenthesisExpression.
    def exitParenthesisExpression(self, ctx:PHPParser.ParenthesisExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#ArrayCreationExpression.
    def enterArrayCreationExpression(self, ctx:PHPParser.ArrayCreationExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#ArrayCreationExpression.
    def exitArrayCreationExpression(self, ctx:PHPParser.ArrayCreationExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#SpecialWordExpression.
    def enterSpecialWordExpression(self, ctx:PHPParser.SpecialWordExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#SpecialWordExpression.
    def exitSpecialWordExpression(self, ctx:PHPParser.SpecialWordExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#LambdaFunctionExpression.
    def enterLambdaFunctionExpression(self, ctx:PHPParser.LambdaFunctionExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#LambdaFunctionExpression.
    def exitLambdaFunctionExpression(self, ctx:PHPParser.LambdaFunctionExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#newExpr.
    def enterNewExpr(self, ctx:PHPParser.NewExprContext):
        pass

    # Exit a parse tree produced by PHPParser#newExpr.
    def exitNewExpr(self, ctx:PHPParser.NewExprContext):
        pass


    # Enter a parse tree produced by PHPParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:PHPParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by PHPParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:PHPParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by PHPParser#yieldExpression.
    def enterYieldExpression(self, ctx:PHPParser.YieldExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#yieldExpression.
    def exitYieldExpression(self, ctx:PHPParser.YieldExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#arrayItemList.
    def enterArrayItemList(self, ctx:PHPParser.ArrayItemListContext):
        pass

    # Exit a parse tree produced by PHPParser#arrayItemList.
    def exitArrayItemList(self, ctx:PHPParser.ArrayItemListContext):
        pass


    # Enter a parse tree produced by PHPParser#arrayItem.
    def enterArrayItem(self, ctx:PHPParser.ArrayItemContext):
        pass

    # Exit a parse tree produced by PHPParser#arrayItem.
    def exitArrayItem(self, ctx:PHPParser.ArrayItemContext):
        pass


    # Enter a parse tree produced by PHPParser#lambdaFunctionUseVars.
    def enterLambdaFunctionUseVars(self, ctx:PHPParser.LambdaFunctionUseVarsContext):
        pass

    # Exit a parse tree produced by PHPParser#lambdaFunctionUseVars.
    def exitLambdaFunctionUseVars(self, ctx:PHPParser.LambdaFunctionUseVarsContext):
        pass


    # Enter a parse tree produced by PHPParser#lambdaFunctionUseVar.
    def enterLambdaFunctionUseVar(self, ctx:PHPParser.LambdaFunctionUseVarContext):
        pass

    # Exit a parse tree produced by PHPParser#lambdaFunctionUseVar.
    def exitLambdaFunctionUseVar(self, ctx:PHPParser.LambdaFunctionUseVarContext):
        pass


    # Enter a parse tree produced by PHPParser#qualifiedStaticTypeRef.
    def enterQualifiedStaticTypeRef(self, ctx:PHPParser.QualifiedStaticTypeRefContext):
        pass

    # Exit a parse tree produced by PHPParser#qualifiedStaticTypeRef.
    def exitQualifiedStaticTypeRef(self, ctx:PHPParser.QualifiedStaticTypeRefContext):
        pass


    # Enter a parse tree produced by PHPParser#typeRef.
    def enterTypeRef(self, ctx:PHPParser.TypeRefContext):
        pass

    # Exit a parse tree produced by PHPParser#typeRef.
    def exitTypeRef(self, ctx:PHPParser.TypeRefContext):
        pass


    # Enter a parse tree produced by PHPParser#indirectTypeRef.
    def enterIndirectTypeRef(self, ctx:PHPParser.IndirectTypeRefContext):
        pass

    # Exit a parse tree produced by PHPParser#indirectTypeRef.
    def exitIndirectTypeRef(self, ctx:PHPParser.IndirectTypeRefContext):
        pass


    # Enter a parse tree produced by PHPParser#qualifiedNamespaceName.
    def enterQualifiedNamespaceName(self, ctx:PHPParser.QualifiedNamespaceNameContext):
        pass

    # Exit a parse tree produced by PHPParser#qualifiedNamespaceName.
    def exitQualifiedNamespaceName(self, ctx:PHPParser.QualifiedNamespaceNameContext):
        pass


    # Enter a parse tree produced by PHPParser#namespaceNameList.
    def enterNamespaceNameList(self, ctx:PHPParser.NamespaceNameListContext):
        pass

    # Exit a parse tree produced by PHPParser#namespaceNameList.
    def exitNamespaceNameList(self, ctx:PHPParser.NamespaceNameListContext):
        pass


    # Enter a parse tree produced by PHPParser#qualifiedNamespaceNameList.
    def enterQualifiedNamespaceNameList(self, ctx:PHPParser.QualifiedNamespaceNameListContext):
        pass

    # Exit a parse tree produced by PHPParser#qualifiedNamespaceNameList.
    def exitQualifiedNamespaceNameList(self, ctx:PHPParser.QualifiedNamespaceNameListContext):
        pass


    # Enter a parse tree produced by PHPParser#arguments.
    def enterArguments(self, ctx:PHPParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by PHPParser#arguments.
    def exitArguments(self, ctx:PHPParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by PHPParser#actualArgument.
    def enterActualArgument(self, ctx:PHPParser.ActualArgumentContext):
        pass

    # Exit a parse tree produced by PHPParser#actualArgument.
    def exitActualArgument(self, ctx:PHPParser.ActualArgumentContext):
        pass


    # Enter a parse tree produced by PHPParser#constantInititalizer.
    def enterConstantInititalizer(self, ctx:PHPParser.ConstantInititalizerContext):
        pass

    # Exit a parse tree produced by PHPParser#constantInititalizer.
    def exitConstantInititalizer(self, ctx:PHPParser.ConstantInititalizerContext):
        pass


    # Enter a parse tree produced by PHPParser#constantArrayItemList.
    def enterConstantArrayItemList(self, ctx:PHPParser.ConstantArrayItemListContext):
        pass

    # Exit a parse tree produced by PHPParser#constantArrayItemList.
    def exitConstantArrayItemList(self, ctx:PHPParser.ConstantArrayItemListContext):
        pass


    # Enter a parse tree produced by PHPParser#constantArrayItem.
    def enterConstantArrayItem(self, ctx:PHPParser.ConstantArrayItemContext):
        pass

    # Exit a parse tree produced by PHPParser#constantArrayItem.
    def exitConstantArrayItem(self, ctx:PHPParser.ConstantArrayItemContext):
        pass


    # Enter a parse tree produced by PHPParser#constant.
    def enterConstant(self, ctx:PHPParser.ConstantContext):
        pass

    # Exit a parse tree produced by PHPParser#constant.
    def exitConstant(self, ctx:PHPParser.ConstantContext):
        pass


    # Enter a parse tree produced by PHPParser#literalConstant.
    def enterLiteralConstant(self, ctx:PHPParser.LiteralConstantContext):
        pass

    # Exit a parse tree produced by PHPParser#literalConstant.
    def exitLiteralConstant(self, ctx:PHPParser.LiteralConstantContext):
        pass


    # Enter a parse tree produced by PHPParser#numericConstant.
    def enterNumericConstant(self, ctx:PHPParser.NumericConstantContext):
        pass

    # Exit a parse tree produced by PHPParser#numericConstant.
    def exitNumericConstant(self, ctx:PHPParser.NumericConstantContext):
        pass


    # Enter a parse tree produced by PHPParser#classConstant.
    def enterClassConstant(self, ctx:PHPParser.ClassConstantContext):
        pass

    # Exit a parse tree produced by PHPParser#classConstant.
    def exitClassConstant(self, ctx:PHPParser.ClassConstantContext):
        pass


    # Enter a parse tree produced by PHPParser#stringConstant.
    def enterStringConstant(self, ctx:PHPParser.StringConstantContext):
        pass

    # Exit a parse tree produced by PHPParser#stringConstant.
    def exitStringConstant(self, ctx:PHPParser.StringConstantContext):
        pass


    # Enter a parse tree produced by PHPParser#string.
    def enterString(self, ctx:PHPParser.StringContext):
        pass

    # Exit a parse tree produced by PHPParser#string.
    def exitString(self, ctx:PHPParser.StringContext):
        pass


    # Enter a parse tree produced by PHPParser#interpolatedStringPart.
    def enterInterpolatedStringPart(self, ctx:PHPParser.InterpolatedStringPartContext):
        pass

    # Exit a parse tree produced by PHPParser#interpolatedStringPart.
    def exitInterpolatedStringPart(self, ctx:PHPParser.InterpolatedStringPartContext):
        pass


    # Enter a parse tree produced by PHPParser#chainList.
    def enterChainList(self, ctx:PHPParser.ChainListContext):
        pass

    # Exit a parse tree produced by PHPParser#chainList.
    def exitChainList(self, ctx:PHPParser.ChainListContext):
        pass


    # Enter a parse tree produced by PHPParser#chain.
    def enterChain(self, ctx:PHPParser.ChainContext):
        pass

    # Exit a parse tree produced by PHPParser#chain.
    def exitChain(self, ctx:PHPParser.ChainContext):
        pass


    # Enter a parse tree produced by PHPParser#memberAccess.
    def enterMemberAccess(self, ctx:PHPParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by PHPParser#memberAccess.
    def exitMemberAccess(self, ctx:PHPParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by PHPParser#functionCall.
    def enterFunctionCall(self, ctx:PHPParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PHPParser#functionCall.
    def exitFunctionCall(self, ctx:PHPParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PHPParser#functionCallName.
    def enterFunctionCallName(self, ctx:PHPParser.FunctionCallNameContext):
        pass

    # Exit a parse tree produced by PHPParser#functionCallName.
    def exitFunctionCallName(self, ctx:PHPParser.FunctionCallNameContext):
        pass


    # Enter a parse tree produced by PHPParser#actualArguments.
    def enterActualArguments(self, ctx:PHPParser.ActualArgumentsContext):
        pass

    # Exit a parse tree produced by PHPParser#actualArguments.
    def exitActualArguments(self, ctx:PHPParser.ActualArgumentsContext):
        pass


    # Enter a parse tree produced by PHPParser#chainBase.
    def enterChainBase(self, ctx:PHPParser.ChainBaseContext):
        pass

    # Exit a parse tree produced by PHPParser#chainBase.
    def exitChainBase(self, ctx:PHPParser.ChainBaseContext):
        pass


    # Enter a parse tree produced by PHPParser#keyedFieldName.
    def enterKeyedFieldName(self, ctx:PHPParser.KeyedFieldNameContext):
        pass

    # Exit a parse tree produced by PHPParser#keyedFieldName.
    def exitKeyedFieldName(self, ctx:PHPParser.KeyedFieldNameContext):
        pass


    # Enter a parse tree produced by PHPParser#keyedSimpleFieldName.
    def enterKeyedSimpleFieldName(self, ctx:PHPParser.KeyedSimpleFieldNameContext):
        pass

    # Exit a parse tree produced by PHPParser#keyedSimpleFieldName.
    def exitKeyedSimpleFieldName(self, ctx:PHPParser.KeyedSimpleFieldNameContext):
        pass


    # Enter a parse tree produced by PHPParser#keyedVariable.
    def enterKeyedVariable(self, ctx:PHPParser.KeyedVariableContext):
        pass

    # Exit a parse tree produced by PHPParser#keyedVariable.
    def exitKeyedVariable(self, ctx:PHPParser.KeyedVariableContext):
        pass


    # Enter a parse tree produced by PHPParser#squareCurlyExpression.
    def enterSquareCurlyExpression(self, ctx:PHPParser.SquareCurlyExpressionContext):
        pass

    # Exit a parse tree produced by PHPParser#squareCurlyExpression.
    def exitSquareCurlyExpression(self, ctx:PHPParser.SquareCurlyExpressionContext):
        pass


    # Enter a parse tree produced by PHPParser#assignmentList.
    def enterAssignmentList(self, ctx:PHPParser.AssignmentListContext):
        pass

    # Exit a parse tree produced by PHPParser#assignmentList.
    def exitAssignmentList(self, ctx:PHPParser.AssignmentListContext):
        pass


    # Enter a parse tree produced by PHPParser#assignmentListElement.
    def enterAssignmentListElement(self, ctx:PHPParser.AssignmentListElementContext):
        pass

    # Exit a parse tree produced by PHPParser#assignmentListElement.
    def exitAssignmentListElement(self, ctx:PHPParser.AssignmentListElementContext):
        pass


    # Enter a parse tree produced by PHPParser#modifier.
    def enterModifier(self, ctx:PHPParser.ModifierContext):
        pass

    # Exit a parse tree produced by PHPParser#modifier.
    def exitModifier(self, ctx:PHPParser.ModifierContext):
        pass


    # Enter a parse tree produced by PHPParser#identifier.
    def enterIdentifier(self, ctx:PHPParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PHPParser#identifier.
    def exitIdentifier(self, ctx:PHPParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PHPParser#memberModifier.
    def enterMemberModifier(self, ctx:PHPParser.MemberModifierContext):
        pass

    # Exit a parse tree produced by PHPParser#memberModifier.
    def exitMemberModifier(self, ctx:PHPParser.MemberModifierContext):
        pass


    # Enter a parse tree produced by PHPParser#magicConstant.
    def enterMagicConstant(self, ctx:PHPParser.MagicConstantContext):
        pass

    # Exit a parse tree produced by PHPParser#magicConstant.
    def exitMagicConstant(self, ctx:PHPParser.MagicConstantContext):
        pass


    # Enter a parse tree produced by PHPParser#magicMethod.
    def enterMagicMethod(self, ctx:PHPParser.MagicMethodContext):
        pass

    # Exit a parse tree produced by PHPParser#magicMethod.
    def exitMagicMethod(self, ctx:PHPParser.MagicMethodContext):
        pass


    # Enter a parse tree produced by PHPParser#primitiveType.
    def enterPrimitiveType(self, ctx:PHPParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by PHPParser#primitiveType.
    def exitPrimitiveType(self, ctx:PHPParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by PHPParser#castOperation.
    def enterCastOperation(self, ctx:PHPParser.CastOperationContext):
        pass

    # Exit a parse tree produced by PHPParser#castOperation.
    def exitCastOperation(self, ctx:PHPParser.CastOperationContext):
        pass


