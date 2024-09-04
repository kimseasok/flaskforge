import ast


class FieldModifier(ast.NodeTransformer):
    """
    AST Node Transformer for modifying class fields in Python code.

    This class modifies or adds fields within class definitions in the given AST.

    Args:
        new_field_code (str): The new field code to be inserted or used to replace existing fields.

    Example Usage:
        ```python
        import ast

        source_code = '''
        class Example:
            def __init__(self):
                self.old_field = 42
        '''

        new_field_code = '''
        self.new_field = 99
        '''

        # Create an instance of FieldModifier
        tree = ast.parse(source_code)
        modifier = FieldModifier(new_field_code)
        modified_tree = modifier.visit(tree)

        # Convert AST back to source code
        modified_source_code = ast.unparse(modified_tree)
        print(modified_source_code)
        ```

    TODO:
        - Handle cases where `new_field_code` contains multiple fields or statements.
        - Add error handling for parsing issues or invalid AST structures.
        - Support additional field types and complex field assignments.
    """

    def __init__(self, new_field_code: str):
        """
        Initializes the FieldModifier with the new field code.

        Args:
            new_field_code (str): The code of the new field to be inserted or used to replace existing fields.
        """
        # Parse the new field code into an AST node
        self.new_field = ast.parse(new_field_code).body[0]
        self.new_field_name = self.new_field.targets[0].id

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
        """
        Visit and modify class definitions. Updates or adds the field in the class body.

        Args:
            node (ast.ClassDef): The class definition node to be visited.

        Returns:
            ast.ClassDef: The modified class definition node with the new field.
        """
        # Extract existing fields and methods
        existing_fields = [n for n in node.body if isinstance(n, ast.Assign)]
        methods = [n for n in node.body if isinstance(n, ast.FunctionDef)]

        # Check if any existing field has the same name
        field_exists = False
        for existing_field in existing_fields:
            if (
                isinstance(existing_field.targets[0], ast.Name)
                and existing_field.targets[0].id == self.new_field_name
            ):
                # Replace the existing field
                node.body[node.body.index(existing_field)] = self.new_field
                field_exists = True
                break

        # Insert the new field before the first method if methods exist
        if not field_exists:
            if methods:
                first_method_index = node.body.index(methods[0])
                node.body.insert(first_method_index, self.new_field)
            else:
                # No methods present, append the new field
                node.body.append(self.new_field)

        return node
