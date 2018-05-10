import javalang

def parse_code(code_list):
    '''parses the code from a list of source code strings to fetch all the
    classes in the module
    '''

    type_decls = {}

    for text in code_list:
        tree = javalang.parse.parse(text)

        # grab any kind of reference type declaration, which inludes classes,
        # interfaces, and enums
        for path, node in tree.filter(javalang.tree.TypeDeclaration):
            # make sure there are no duplicates
            if node.name not in type_decls.keys():
                type_decls[node.name] = node

    return type_decls.values()
