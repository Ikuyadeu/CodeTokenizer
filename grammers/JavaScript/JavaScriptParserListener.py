# Generated from JavaScriptParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JavaScriptParser import JavaScriptParser
else:
    from JavaScriptParser import JavaScriptParser

# This class defines a complete listener for a parse tree produced by JavaScriptParser.
class JavaScriptParserListener(ParseTreeListener):

    # Enter a parse tree produced by JavaScriptParser#program.
    def enterProgram(self, ctx:JavaScriptParser.ProgramContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#program.
    def exitProgram(self, ctx:JavaScriptParser.ProgramContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#sourceElement.
    def enterSourceElement(self, ctx:JavaScriptParser.SourceElementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#sourceElement.
    def exitSourceElement(self, ctx:JavaScriptParser.SourceElementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#statement.
    def enterStatement(self, ctx:JavaScriptParser.StatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#statement.
    def exitStatement(self, ctx:JavaScriptParser.StatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#block.
    def enterBlock(self, ctx:JavaScriptParser.BlockContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#block.
    def exitBlock(self, ctx:JavaScriptParser.BlockContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#statementList.
    def enterStatementList(self, ctx:JavaScriptParser.StatementListContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#statementList.
    def exitStatementList(self, ctx:JavaScriptParser.StatementListContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#variableStatement.
    def enterVariableStatement(self, ctx:JavaScriptParser.VariableStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#variableStatement.
    def exitVariableStatement(self, ctx:JavaScriptParser.VariableStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#variableDeclarationList.
    def enterVariableDeclarationList(self, ctx:JavaScriptParser.VariableDeclarationListContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#variableDeclarationList.
    def exitVariableDeclarationList(self, ctx:JavaScriptParser.VariableDeclarationListContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:JavaScriptParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:JavaScriptParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#emptyStatement.
    def enterEmptyStatement(self, ctx:JavaScriptParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#emptyStatement.
    def exitEmptyStatement(self, ctx:JavaScriptParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#expressionStatement.
    def enterExpressionStatement(self, ctx:JavaScriptParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#expressionStatement.
    def exitExpressionStatement(self, ctx:JavaScriptParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ifStatement.
    def enterIfStatement(self, ctx:JavaScriptParser.IfStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ifStatement.
    def exitIfStatement(self, ctx:JavaScriptParser.IfStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#DoStatement.
    def enterDoStatement(self, ctx:JavaScriptParser.DoStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#DoStatement.
    def exitDoStatement(self, ctx:JavaScriptParser.DoStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#WhileStatement.
    def enterWhileStatement(self, ctx:JavaScriptParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#WhileStatement.
    def exitWhileStatement(self, ctx:JavaScriptParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ForStatement.
    def enterForStatement(self, ctx:JavaScriptParser.ForStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ForStatement.
    def exitForStatement(self, ctx:JavaScriptParser.ForStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ForVarStatement.
    def enterForVarStatement(self, ctx:JavaScriptParser.ForVarStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ForVarStatement.
    def exitForVarStatement(self, ctx:JavaScriptParser.ForVarStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ForInStatement.
    def enterForInStatement(self, ctx:JavaScriptParser.ForInStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ForInStatement.
    def exitForInStatement(self, ctx:JavaScriptParser.ForInStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ForVarInStatement.
    def enterForVarInStatement(self, ctx:JavaScriptParser.ForVarInStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ForVarInStatement.
    def exitForVarInStatement(self, ctx:JavaScriptParser.ForVarInStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#varModifier.
    def enterVarModifier(self, ctx:JavaScriptParser.VarModifierContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#varModifier.
    def exitVarModifier(self, ctx:JavaScriptParser.VarModifierContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#continueStatement.
    def enterContinueStatement(self, ctx:JavaScriptParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#continueStatement.
    def exitContinueStatement(self, ctx:JavaScriptParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#breakStatement.
    def enterBreakStatement(self, ctx:JavaScriptParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#breakStatement.
    def exitBreakStatement(self, ctx:JavaScriptParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#returnStatement.
    def enterReturnStatement(self, ctx:JavaScriptParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#returnStatement.
    def exitReturnStatement(self, ctx:JavaScriptParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#withStatement.
    def enterWithStatement(self, ctx:JavaScriptParser.WithStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#withStatement.
    def exitWithStatement(self, ctx:JavaScriptParser.WithStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#switchStatement.
    def enterSwitchStatement(self, ctx:JavaScriptParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#switchStatement.
    def exitSwitchStatement(self, ctx:JavaScriptParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#caseBlock.
    def enterCaseBlock(self, ctx:JavaScriptParser.CaseBlockContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#caseBlock.
    def exitCaseBlock(self, ctx:JavaScriptParser.CaseBlockContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#caseClauses.
    def enterCaseClauses(self, ctx:JavaScriptParser.CaseClausesContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#caseClauses.
    def exitCaseClauses(self, ctx:JavaScriptParser.CaseClausesContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#caseClause.
    def enterCaseClause(self, ctx:JavaScriptParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#caseClause.
    def exitCaseClause(self, ctx:JavaScriptParser.CaseClauseContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#defaultClause.
    def enterDefaultClause(self, ctx:JavaScriptParser.DefaultClauseContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#defaultClause.
    def exitDefaultClause(self, ctx:JavaScriptParser.DefaultClauseContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#labelledStatement.
    def enterLabelledStatement(self, ctx:JavaScriptParser.LabelledStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#labelledStatement.
    def exitLabelledStatement(self, ctx:JavaScriptParser.LabelledStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#throwStatement.
    def enterThrowStatement(self, ctx:JavaScriptParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#throwStatement.
    def exitThrowStatement(self, ctx:JavaScriptParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#tryStatement.
    def enterTryStatement(self, ctx:JavaScriptParser.TryStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#tryStatement.
    def exitTryStatement(self, ctx:JavaScriptParser.TryStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#catchProduction.
    def enterCatchProduction(self, ctx:JavaScriptParser.CatchProductionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#catchProduction.
    def exitCatchProduction(self, ctx:JavaScriptParser.CatchProductionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#finallyProduction.
    def enterFinallyProduction(self, ctx:JavaScriptParser.FinallyProductionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#finallyProduction.
    def exitFinallyProduction(self, ctx:JavaScriptParser.FinallyProductionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#debuggerStatement.
    def enterDebuggerStatement(self, ctx:JavaScriptParser.DebuggerStatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#debuggerStatement.
    def exitDebuggerStatement(self, ctx:JavaScriptParser.DebuggerStatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:JavaScriptParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:JavaScriptParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#classDeclaration.
    def enterClassDeclaration(self, ctx:JavaScriptParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#classDeclaration.
    def exitClassDeclaration(self, ctx:JavaScriptParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#classTail.
    def enterClassTail(self, ctx:JavaScriptParser.ClassTailContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#classTail.
    def exitClassTail(self, ctx:JavaScriptParser.ClassTailContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#classElement.
    def enterClassElement(self, ctx:JavaScriptParser.ClassElementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#classElement.
    def exitClassElement(self, ctx:JavaScriptParser.ClassElementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#methodDefinition.
    def enterMethodDefinition(self, ctx:JavaScriptParser.MethodDefinitionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#methodDefinition.
    def exitMethodDefinition(self, ctx:JavaScriptParser.MethodDefinitionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#generatorMethod.
    def enterGeneratorMethod(self, ctx:JavaScriptParser.GeneratorMethodContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#generatorMethod.
    def exitGeneratorMethod(self, ctx:JavaScriptParser.GeneratorMethodContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#formalParameterList.
    def enterFormalParameterList(self, ctx:JavaScriptParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#formalParameterList.
    def exitFormalParameterList(self, ctx:JavaScriptParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#formalParameterArg.
    def enterFormalParameterArg(self, ctx:JavaScriptParser.FormalParameterArgContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#formalParameterArg.
    def exitFormalParameterArg(self, ctx:JavaScriptParser.FormalParameterArgContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#lastFormalParameterArg.
    def enterLastFormalParameterArg(self, ctx:JavaScriptParser.LastFormalParameterArgContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#lastFormalParameterArg.
    def exitLastFormalParameterArg(self, ctx:JavaScriptParser.LastFormalParameterArgContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#functionBody.
    def enterFunctionBody(self, ctx:JavaScriptParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#functionBody.
    def exitFunctionBody(self, ctx:JavaScriptParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#sourceElements.
    def enterSourceElements(self, ctx:JavaScriptParser.SourceElementsContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#sourceElements.
    def exitSourceElements(self, ctx:JavaScriptParser.SourceElementsContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:JavaScriptParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:JavaScriptParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#elementList.
    def enterElementList(self, ctx:JavaScriptParser.ElementListContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#elementList.
    def exitElementList(self, ctx:JavaScriptParser.ElementListContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#lastElement.
    def enterLastElement(self, ctx:JavaScriptParser.LastElementContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#lastElement.
    def exitLastElement(self, ctx:JavaScriptParser.LastElementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#objectLiteral.
    def enterObjectLiteral(self, ctx:JavaScriptParser.ObjectLiteralContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#objectLiteral.
    def exitObjectLiteral(self, ctx:JavaScriptParser.ObjectLiteralContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PropertyExpressionAssignment.
    def enterPropertyExpressionAssignment(self, ctx:JavaScriptParser.PropertyExpressionAssignmentContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#PropertyExpressionAssignment.
    def exitPropertyExpressionAssignment(self, ctx:JavaScriptParser.PropertyExpressionAssignmentContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ComputedPropertyExpressionAssignment.
    def enterComputedPropertyExpressionAssignment(self, ctx:JavaScriptParser.ComputedPropertyExpressionAssignmentContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ComputedPropertyExpressionAssignment.
    def exitComputedPropertyExpressionAssignment(self, ctx:JavaScriptParser.ComputedPropertyExpressionAssignmentContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PropertyGetter.
    def enterPropertyGetter(self, ctx:JavaScriptParser.PropertyGetterContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#PropertyGetter.
    def exitPropertyGetter(self, ctx:JavaScriptParser.PropertyGetterContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PropertySetter.
    def enterPropertySetter(self, ctx:JavaScriptParser.PropertySetterContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#PropertySetter.
    def exitPropertySetter(self, ctx:JavaScriptParser.PropertySetterContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#MethodProperty.
    def enterMethodProperty(self, ctx:JavaScriptParser.MethodPropertyContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#MethodProperty.
    def exitMethodProperty(self, ctx:JavaScriptParser.MethodPropertyContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PropertyShorthand.
    def enterPropertyShorthand(self, ctx:JavaScriptParser.PropertyShorthandContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#PropertyShorthand.
    def exitPropertyShorthand(self, ctx:JavaScriptParser.PropertyShorthandContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#propertyName.
    def enterPropertyName(self, ctx:JavaScriptParser.PropertyNameContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#propertyName.
    def exitPropertyName(self, ctx:JavaScriptParser.PropertyNameContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#arguments.
    def enterArguments(self, ctx:JavaScriptParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#arguments.
    def exitArguments(self, ctx:JavaScriptParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#lastArgument.
    def enterLastArgument(self, ctx:JavaScriptParser.LastArgumentContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#lastArgument.
    def exitLastArgument(self, ctx:JavaScriptParser.LastArgumentContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#expressionSequence.
    def enterExpressionSequence(self, ctx:JavaScriptParser.ExpressionSequenceContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#expressionSequence.
    def exitExpressionSequence(self, ctx:JavaScriptParser.ExpressionSequenceContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#TemplateStringExpression.
    def enterTemplateStringExpression(self, ctx:JavaScriptParser.TemplateStringExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#TemplateStringExpression.
    def exitTemplateStringExpression(self, ctx:JavaScriptParser.TemplateStringExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#TernaryExpression.
    def enterTernaryExpression(self, ctx:JavaScriptParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#TernaryExpression.
    def exitTernaryExpression(self, ctx:JavaScriptParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#LogicalAndExpression.
    def enterLogicalAndExpression(self, ctx:JavaScriptParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#LogicalAndExpression.
    def exitLogicalAndExpression(self, ctx:JavaScriptParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PreIncrementExpression.
    def enterPreIncrementExpression(self, ctx:JavaScriptParser.PreIncrementExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#PreIncrementExpression.
    def exitPreIncrementExpression(self, ctx:JavaScriptParser.PreIncrementExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ObjectLiteralExpression.
    def enterObjectLiteralExpression(self, ctx:JavaScriptParser.ObjectLiteralExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ObjectLiteralExpression.
    def exitObjectLiteralExpression(self, ctx:JavaScriptParser.ObjectLiteralExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#InExpression.
    def enterInExpression(self, ctx:JavaScriptParser.InExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#InExpression.
    def exitInExpression(self, ctx:JavaScriptParser.InExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#LogicalOrExpression.
    def enterLogicalOrExpression(self, ctx:JavaScriptParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#LogicalOrExpression.
    def exitLogicalOrExpression(self, ctx:JavaScriptParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#NotExpression.
    def enterNotExpression(self, ctx:JavaScriptParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#NotExpression.
    def exitNotExpression(self, ctx:JavaScriptParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PreDecreaseExpression.
    def enterPreDecreaseExpression(self, ctx:JavaScriptParser.PreDecreaseExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#PreDecreaseExpression.
    def exitPreDecreaseExpression(self, ctx:JavaScriptParser.PreDecreaseExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ArgumentsExpression.
    def enterArgumentsExpression(self, ctx:JavaScriptParser.ArgumentsExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ArgumentsExpression.
    def exitArgumentsExpression(self, ctx:JavaScriptParser.ArgumentsExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ThisExpression.
    def enterThisExpression(self, ctx:JavaScriptParser.ThisExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ThisExpression.
    def exitThisExpression(self, ctx:JavaScriptParser.ThisExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#FunctionExpression.
    def enterFunctionExpression(self, ctx:JavaScriptParser.FunctionExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#FunctionExpression.
    def exitFunctionExpression(self, ctx:JavaScriptParser.FunctionExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#UnaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx:JavaScriptParser.UnaryMinusExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#UnaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx:JavaScriptParser.UnaryMinusExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx:JavaScriptParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx:JavaScriptParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PostDecreaseExpression.
    def enterPostDecreaseExpression(self, ctx:JavaScriptParser.PostDecreaseExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#PostDecreaseExpression.
    def exitPostDecreaseExpression(self, ctx:JavaScriptParser.PostDecreaseExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#TypeofExpression.
    def enterTypeofExpression(self, ctx:JavaScriptParser.TypeofExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#TypeofExpression.
    def exitTypeofExpression(self, ctx:JavaScriptParser.TypeofExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#InstanceofExpression.
    def enterInstanceofExpression(self, ctx:JavaScriptParser.InstanceofExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#InstanceofExpression.
    def exitInstanceofExpression(self, ctx:JavaScriptParser.InstanceofExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#UnaryPlusExpression.
    def enterUnaryPlusExpression(self, ctx:JavaScriptParser.UnaryPlusExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#UnaryPlusExpression.
    def exitUnaryPlusExpression(self, ctx:JavaScriptParser.UnaryPlusExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#DeleteExpression.
    def enterDeleteExpression(self, ctx:JavaScriptParser.DeleteExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#DeleteExpression.
    def exitDeleteExpression(self, ctx:JavaScriptParser.DeleteExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ArrowFunctionExpression.
    def enterArrowFunctionExpression(self, ctx:JavaScriptParser.ArrowFunctionExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ArrowFunctionExpression.
    def exitArrowFunctionExpression(self, ctx:JavaScriptParser.ArrowFunctionExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#EqualityExpression.
    def enterEqualityExpression(self, ctx:JavaScriptParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#EqualityExpression.
    def exitEqualityExpression(self, ctx:JavaScriptParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#BitXOrExpression.
    def enterBitXOrExpression(self, ctx:JavaScriptParser.BitXOrExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#BitXOrExpression.
    def exitBitXOrExpression(self, ctx:JavaScriptParser.BitXOrExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#SuperExpression.
    def enterSuperExpression(self, ctx:JavaScriptParser.SuperExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#SuperExpression.
    def exitSuperExpression(self, ctx:JavaScriptParser.SuperExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#MultiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:JavaScriptParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#MultiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:JavaScriptParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#BitShiftExpression.
    def enterBitShiftExpression(self, ctx:JavaScriptParser.BitShiftExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#BitShiftExpression.
    def exitBitShiftExpression(self, ctx:JavaScriptParser.BitShiftExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:JavaScriptParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:JavaScriptParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#AdditiveExpression.
    def enterAdditiveExpression(self, ctx:JavaScriptParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#AdditiveExpression.
    def exitAdditiveExpression(self, ctx:JavaScriptParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#RelationalExpression.
    def enterRelationalExpression(self, ctx:JavaScriptParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#RelationalExpression.
    def exitRelationalExpression(self, ctx:JavaScriptParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PostIncrementExpression.
    def enterPostIncrementExpression(self, ctx:JavaScriptParser.PostIncrementExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#PostIncrementExpression.
    def exitPostIncrementExpression(self, ctx:JavaScriptParser.PostIncrementExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#BitNotExpression.
    def enterBitNotExpression(self, ctx:JavaScriptParser.BitNotExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#BitNotExpression.
    def exitBitNotExpression(self, ctx:JavaScriptParser.BitNotExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#NewExpression.
    def enterNewExpression(self, ctx:JavaScriptParser.NewExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#NewExpression.
    def exitNewExpression(self, ctx:JavaScriptParser.NewExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#LiteralExpression.
    def enterLiteralExpression(self, ctx:JavaScriptParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#LiteralExpression.
    def exitLiteralExpression(self, ctx:JavaScriptParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ArrayLiteralExpression.
    def enterArrayLiteralExpression(self, ctx:JavaScriptParser.ArrayLiteralExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ArrayLiteralExpression.
    def exitArrayLiteralExpression(self, ctx:JavaScriptParser.ArrayLiteralExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#MemberDotExpression.
    def enterMemberDotExpression(self, ctx:JavaScriptParser.MemberDotExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#MemberDotExpression.
    def exitMemberDotExpression(self, ctx:JavaScriptParser.MemberDotExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ClassExpression.
    def enterClassExpression(self, ctx:JavaScriptParser.ClassExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#ClassExpression.
    def exitClassExpression(self, ctx:JavaScriptParser.ClassExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#MemberIndexExpression.
    def enterMemberIndexExpression(self, ctx:JavaScriptParser.MemberIndexExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#MemberIndexExpression.
    def exitMemberIndexExpression(self, ctx:JavaScriptParser.MemberIndexExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#IdentifierExpression.
    def enterIdentifierExpression(self, ctx:JavaScriptParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#IdentifierExpression.
    def exitIdentifierExpression(self, ctx:JavaScriptParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#BitAndExpression.
    def enterBitAndExpression(self, ctx:JavaScriptParser.BitAndExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#BitAndExpression.
    def exitBitAndExpression(self, ctx:JavaScriptParser.BitAndExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#BitOrExpression.
    def enterBitOrExpression(self, ctx:JavaScriptParser.BitOrExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#BitOrExpression.
    def exitBitOrExpression(self, ctx:JavaScriptParser.BitOrExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#AssignmentOperatorExpression.
    def enterAssignmentOperatorExpression(self, ctx:JavaScriptParser.AssignmentOperatorExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#AssignmentOperatorExpression.
    def exitAssignmentOperatorExpression(self, ctx:JavaScriptParser.AssignmentOperatorExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#VoidExpression.
    def enterVoidExpression(self, ctx:JavaScriptParser.VoidExpressionContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#VoidExpression.
    def exitVoidExpression(self, ctx:JavaScriptParser.VoidExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#arrowFunctionParameters.
    def enterArrowFunctionParameters(self, ctx:JavaScriptParser.ArrowFunctionParametersContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#arrowFunctionParameters.
    def exitArrowFunctionParameters(self, ctx:JavaScriptParser.ArrowFunctionParametersContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#arrowFunctionBody.
    def enterArrowFunctionBody(self, ctx:JavaScriptParser.ArrowFunctionBodyContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#arrowFunctionBody.
    def exitArrowFunctionBody(self, ctx:JavaScriptParser.ArrowFunctionBodyContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:JavaScriptParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:JavaScriptParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#literal.
    def enterLiteral(self, ctx:JavaScriptParser.LiteralContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#literal.
    def exitLiteral(self, ctx:JavaScriptParser.LiteralContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#numericLiteral.
    def enterNumericLiteral(self, ctx:JavaScriptParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#numericLiteral.
    def exitNumericLiteral(self, ctx:JavaScriptParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#identifierName.
    def enterIdentifierName(self, ctx:JavaScriptParser.IdentifierNameContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#identifierName.
    def exitIdentifierName(self, ctx:JavaScriptParser.IdentifierNameContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#reservedWord.
    def enterReservedWord(self, ctx:JavaScriptParser.ReservedWordContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#reservedWord.
    def exitReservedWord(self, ctx:JavaScriptParser.ReservedWordContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#keyword.
    def enterKeyword(self, ctx:JavaScriptParser.KeywordContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#keyword.
    def exitKeyword(self, ctx:JavaScriptParser.KeywordContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#getter.
    def enterGetter(self, ctx:JavaScriptParser.GetterContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#getter.
    def exitGetter(self, ctx:JavaScriptParser.GetterContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#setter.
    def enterSetter(self, ctx:JavaScriptParser.SetterContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#setter.
    def exitSetter(self, ctx:JavaScriptParser.SetterContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#eos.
    def enterEos(self, ctx:JavaScriptParser.EosContext):
        pass

    # Exit a parse tree produced by JavaScriptParser#eos.
    def exitEos(self, ctx:JavaScriptParser.EosContext):
        pass


