# Generated from /home/wspeirs/src/php_linter_public/parser/PHPParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PHPParser import PHPParser
else:
    from PHPParser import PHPParser

# This class defines a complete generic visitor for a parse tree produced by PHPParser.

class PHPParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PHPParser#htmlDocument.
    def visitHtmlDocument(self, ctx:PHPParser.HtmlDocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#htmlElementOrPhpBlock.
    def visitHtmlElementOrPhpBlock(self, ctx:PHPParser.HtmlElementOrPhpBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#htmlElement.
    def visitHtmlElement(self, ctx:PHPParser.HtmlElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#scriptTextPart.
    def visitScriptTextPart(self, ctx:PHPParser.ScriptTextPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#phpBlock.
    def visitPhpBlock(self, ctx:PHPParser.PhpBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#importStatement.
    def visitImportStatement(self, ctx:PHPParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#topStatement.
    def visitTopStatement(self, ctx:PHPParser.TopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#useDeclaration.
    def visitUseDeclaration(self, ctx:PHPParser.UseDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#useDeclarationContentList.
    def visitUseDeclarationContentList(self, ctx:PHPParser.UseDeclarationContentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#useDeclarationContent.
    def visitUseDeclarationContent(self, ctx:PHPParser.UseDeclarationContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#namespaceDeclaration.
    def visitNamespaceDeclaration(self, ctx:PHPParser.NamespaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#namespaceStatement.
    def visitNamespaceStatement(self, ctx:PHPParser.NamespaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:PHPParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#classDeclaration.
    def visitClassDeclaration(self, ctx:PHPParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#classEntryType.
    def visitClassEntryType(self, ctx:PHPParser.ClassEntryTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#interfaceList.
    def visitInterfaceList(self, ctx:PHPParser.InterfaceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#typeParameterListInBrackets.
    def visitTypeParameterListInBrackets(self, ctx:PHPParser.TypeParameterListInBracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#typeParameterList.
    def visitTypeParameterList(self, ctx:PHPParser.TypeParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#typeParameterWithDefaultsList.
    def visitTypeParameterWithDefaultsList(self, ctx:PHPParser.TypeParameterWithDefaultsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#typeParameterDecl.
    def visitTypeParameterDecl(self, ctx:PHPParser.TypeParameterDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#typeParameterWithDefaultDecl.
    def visitTypeParameterWithDefaultDecl(self, ctx:PHPParser.TypeParameterWithDefaultDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#genericDynamicArgs.
    def visitGenericDynamicArgs(self, ctx:PHPParser.GenericDynamicArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#attributes.
    def visitAttributes(self, ctx:PHPParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#attributesGroup.
    def visitAttributesGroup(self, ctx:PHPParser.AttributesGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#attribute.
    def visitAttribute(self, ctx:PHPParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#attributeArgList.
    def visitAttributeArgList(self, ctx:PHPParser.AttributeArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#attributeNamedArgList.
    def visitAttributeNamedArgList(self, ctx:PHPParser.AttributeNamedArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#attributeNamedArg.
    def visitAttributeNamedArg(self, ctx:PHPParser.AttributeNamedArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#innerStatementList.
    def visitInnerStatementList(self, ctx:PHPParser.InnerStatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#innerStatement.
    def visitInnerStatement(self, ctx:PHPParser.InnerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#statement.
    def visitStatement(self, ctx:PHPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#emptyStatement.
    def visitEmptyStatement(self, ctx:PHPParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#nonEmptyStatement.
    def visitNonEmptyStatement(self, ctx:PHPParser.NonEmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#blockStatement.
    def visitBlockStatement(self, ctx:PHPParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#ifStatement.
    def visitIfStatement(self, ctx:PHPParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#elseIfStatement.
    def visitElseIfStatement(self, ctx:PHPParser.ElseIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#elseIfColonStatement.
    def visitElseIfColonStatement(self, ctx:PHPParser.ElseIfColonStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#elseStatement.
    def visitElseStatement(self, ctx:PHPParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#elseColonStatement.
    def visitElseColonStatement(self, ctx:PHPParser.ElseColonStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#whileStatement.
    def visitWhileStatement(self, ctx:PHPParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:PHPParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#forStatement.
    def visitForStatement(self, ctx:PHPParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#forInit.
    def visitForInit(self, ctx:PHPParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#forUpdate.
    def visitForUpdate(self, ctx:PHPParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#switchStatement.
    def visitSwitchStatement(self, ctx:PHPParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#switchBlock.
    def visitSwitchBlock(self, ctx:PHPParser.SwitchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#breakStatement.
    def visitBreakStatement(self, ctx:PHPParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#continueStatement.
    def visitContinueStatement(self, ctx:PHPParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#returnStatement.
    def visitReturnStatement(self, ctx:PHPParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#expressionStatement.
    def visitExpressionStatement(self, ctx:PHPParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#unsetStatement.
    def visitUnsetStatement(self, ctx:PHPParser.UnsetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#foreachStatement.
    def visitForeachStatement(self, ctx:PHPParser.ForeachStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#tryCatchFinally.
    def visitTryCatchFinally(self, ctx:PHPParser.TryCatchFinallyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#catchClause.
    def visitCatchClause(self, ctx:PHPParser.CatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#finallyStatement.
    def visitFinallyStatement(self, ctx:PHPParser.FinallyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#throwStatement.
    def visitThrowStatement(self, ctx:PHPParser.ThrowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#gotoStatement.
    def visitGotoStatement(self, ctx:PHPParser.GotoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#declareStatement.
    def visitDeclareStatement(self, ctx:PHPParser.DeclareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#inlineHtml.
    def visitInlineHtml(self, ctx:PHPParser.InlineHtmlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#declareList.
    def visitDeclareList(self, ctx:PHPParser.DeclareListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#formalParameterList.
    def visitFormalParameterList(self, ctx:PHPParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#formalParameter.
    def visitFormalParameter(self, ctx:PHPParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#typeHint.
    def visitTypeHint(self, ctx:PHPParser.TypeHintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#globalStatement.
    def visitGlobalStatement(self, ctx:PHPParser.GlobalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#globalVar.
    def visitGlobalVar(self, ctx:PHPParser.GlobalVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#echoStatement.
    def visitEchoStatement(self, ctx:PHPParser.EchoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#staticVariableStatement.
    def visitStaticVariableStatement(self, ctx:PHPParser.StaticVariableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#classStatement.
    def visitClassStatement(self, ctx:PHPParser.ClassStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#traitAdaptations.
    def visitTraitAdaptations(self, ctx:PHPParser.TraitAdaptationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#traitAdaptationStatement.
    def visitTraitAdaptationStatement(self, ctx:PHPParser.TraitAdaptationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#traitPrecedence.
    def visitTraitPrecedence(self, ctx:PHPParser.TraitPrecedenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#traitAlias.
    def visitTraitAlias(self, ctx:PHPParser.TraitAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#traitMethodReference.
    def visitTraitMethodReference(self, ctx:PHPParser.TraitMethodReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#baseCtorCall.
    def visitBaseCtorCall(self, ctx:PHPParser.BaseCtorCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#methodBody.
    def visitMethodBody(self, ctx:PHPParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#propertyModifiers.
    def visitPropertyModifiers(self, ctx:PHPParser.PropertyModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#memberModifiers.
    def visitMemberModifiers(self, ctx:PHPParser.MemberModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#variableInitializer.
    def visitVariableInitializer(self, ctx:PHPParser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#identifierInititalizer.
    def visitIdentifierInititalizer(self, ctx:PHPParser.IdentifierInititalizerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#globalConstantDeclaration.
    def visitGlobalConstantDeclaration(self, ctx:PHPParser.GlobalConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#expressionList.
    def visitExpressionList(self, ctx:PHPParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#parenthesis.
    def visitParenthesis(self, ctx:PHPParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#expression.
    def visitExpression(self, ctx:PHPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#andOrExpression.
    def visitAndOrExpression(self, ctx:PHPParser.AndOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:PHPParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#additionExpression.
    def visitAdditionExpression(self, ctx:PHPParser.AdditionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#multiplicationExpression.
    def visitMultiplicationExpression(self, ctx:PHPParser.MultiplicationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#CloneExpression.
    def visitCloneExpression(self, ctx:PHPParser.CloneExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#NewExpression.
    def visitNewExpression(self, ctx:PHPParser.NewExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#IndexerExpression.
    def visitIndexerExpression(self, ctx:PHPParser.IndexerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#CastExpression.
    def visitCastExpression(self, ctx:PHPParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#UnaryOperatorExpression.
    def visitUnaryOperatorExpression(self, ctx:PHPParser.UnaryOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#PrefixIncDecExpression.
    def visitPrefixIncDecExpression(self, ctx:PHPParser.PrefixIncDecExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#PostfixIncDecExpression.
    def visitPostfixIncDecExpression(self, ctx:PHPParser.PostfixIncDecExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:PHPParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#PrintExpression.
    def visitPrintExpression(self, ctx:PHPParser.PrintExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#ChainExpression.
    def visitChainExpression(self, ctx:PHPParser.ChainExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#ScalarExpression.
    def visitScalarExpression(self, ctx:PHPParser.ScalarExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#BackQuoteStringExpression.
    def visitBackQuoteStringExpression(self, ctx:PHPParser.BackQuoteStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#ParenthesisExpression.
    def visitParenthesisExpression(self, ctx:PHPParser.ParenthesisExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#ArrayCreationExpression.
    def visitArrayCreationExpression(self, ctx:PHPParser.ArrayCreationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#SpecialWordExpression.
    def visitSpecialWordExpression(self, ctx:PHPParser.SpecialWordExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#LambdaFunctionExpression.
    def visitLambdaFunctionExpression(self, ctx:PHPParser.LambdaFunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#newExpr.
    def visitNewExpr(self, ctx:PHPParser.NewExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:PHPParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#yieldExpression.
    def visitYieldExpression(self, ctx:PHPParser.YieldExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#arrayItemList.
    def visitArrayItemList(self, ctx:PHPParser.ArrayItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#arrayItem.
    def visitArrayItem(self, ctx:PHPParser.ArrayItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#lambdaFunctionUseVars.
    def visitLambdaFunctionUseVars(self, ctx:PHPParser.LambdaFunctionUseVarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#lambdaFunctionUseVar.
    def visitLambdaFunctionUseVar(self, ctx:PHPParser.LambdaFunctionUseVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#qualifiedStaticTypeRef.
    def visitQualifiedStaticTypeRef(self, ctx:PHPParser.QualifiedStaticTypeRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#typeRef.
    def visitTypeRef(self, ctx:PHPParser.TypeRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#indirectTypeRef.
    def visitIndirectTypeRef(self, ctx:PHPParser.IndirectTypeRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#qualifiedNamespaceName.
    def visitQualifiedNamespaceName(self, ctx:PHPParser.QualifiedNamespaceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#namespaceNameList.
    def visitNamespaceNameList(self, ctx:PHPParser.NamespaceNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#qualifiedNamespaceNameList.
    def visitQualifiedNamespaceNameList(self, ctx:PHPParser.QualifiedNamespaceNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#arguments.
    def visitArguments(self, ctx:PHPParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#actualArgument.
    def visitActualArgument(self, ctx:PHPParser.ActualArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#constantInititalizer.
    def visitConstantInititalizer(self, ctx:PHPParser.ConstantInititalizerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#constantArrayItemList.
    def visitConstantArrayItemList(self, ctx:PHPParser.ConstantArrayItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#constantArrayItem.
    def visitConstantArrayItem(self, ctx:PHPParser.ConstantArrayItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#constant.
    def visitConstant(self, ctx:PHPParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#literalConstant.
    def visitLiteralConstant(self, ctx:PHPParser.LiteralConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#numericConstant.
    def visitNumericConstant(self, ctx:PHPParser.NumericConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#classConstant.
    def visitClassConstant(self, ctx:PHPParser.ClassConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#stringConstant.
    def visitStringConstant(self, ctx:PHPParser.StringConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#string.
    def visitString(self, ctx:PHPParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#interpolatedStringPart.
    def visitInterpolatedStringPart(self, ctx:PHPParser.InterpolatedStringPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#chainList.
    def visitChainList(self, ctx:PHPParser.ChainListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#chain.
    def visitChain(self, ctx:PHPParser.ChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#memberAccess.
    def visitMemberAccess(self, ctx:PHPParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#functionCall.
    def visitFunctionCall(self, ctx:PHPParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#functionCallName.
    def visitFunctionCallName(self, ctx:PHPParser.FunctionCallNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#actualArguments.
    def visitActualArguments(self, ctx:PHPParser.ActualArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#chainBase.
    def visitChainBase(self, ctx:PHPParser.ChainBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#keyedFieldName.
    def visitKeyedFieldName(self, ctx:PHPParser.KeyedFieldNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#keyedSimpleFieldName.
    def visitKeyedSimpleFieldName(self, ctx:PHPParser.KeyedSimpleFieldNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#keyedVariable.
    def visitKeyedVariable(self, ctx:PHPParser.KeyedVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#squareCurlyExpression.
    def visitSquareCurlyExpression(self, ctx:PHPParser.SquareCurlyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#assignmentList.
    def visitAssignmentList(self, ctx:PHPParser.AssignmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#assignmentListElement.
    def visitAssignmentListElement(self, ctx:PHPParser.AssignmentListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#modifier.
    def visitModifier(self, ctx:PHPParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#identifier.
    def visitIdentifier(self, ctx:PHPParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#memberModifier.
    def visitMemberModifier(self, ctx:PHPParser.MemberModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#magicConstant.
    def visitMagicConstant(self, ctx:PHPParser.MagicConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#magicMethod.
    def visitMagicMethod(self, ctx:PHPParser.MagicMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#primitiveType.
    def visitPrimitiveType(self, ctx:PHPParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PHPParser#castOperation.
    def visitCastOperation(self, ctx:PHPParser.CastOperationContext):
        return self.visitChildren(ctx)



del PHPParser