import javalang

class DepGraph:
    """Computes and stores the class dependencies throughout a module
    into a directed graph. Each class is a node, and an edge from class A into
    another class B means that class A depends on class B
    """

    def __init__(self, package_types):
        '''initialize the class dependency graph'''
        self.type_deps = {}
        self.package_types = package_types

        self._compute_package_names()
        self._compute_deps()

    def _compute_package_names(self):
        '''computes a set of all the type names defined in the package'''
        self.package_names = set()
        type_params = set()

        # filter out type parameters
        for type_decl in self.package_types:
            for path, node in type_decl.filter(javalang.tree.TypeParameter):
                type_params.add(node.name)

        for type_decl in self.package_types:
            for path, node in type_decl.filter(javalang.tree.TypeDeclaration):
                if node.name not in type_params:
                    self.package_names.add(node.name)

    def _compute_deps_of(self, class_decl):
        '''computes the set of all types a class uses/depends on'''
        type_set = set()
        type_params = set()

        # filter out type parameters
        for path, node in class_decl.filter(javalang.tree.TypeParameter):
            type_params.add(node.name)

        # grab all the types used in the class
        for path, node in class_decl.filter(javalang.tree.Type):
            # set up a flag for various filters
            include = True

            # don't allow type parameters
            if node.name in type_params:
                include = False

            # don't use any types not in the module, or this will artificially
            # increase the computed coupling
            if node.name not in self.package_names:
                include = False

            # don't include itself
            if node.name == class_decl.name:
                include = False

            if include:
                type_set.add(node.name)

        return type_set

    def _compute_deps(self):
        '''calculates the dependencies between the classes in the module'''
        for type_decl in self.package_types:
            self.type_deps[type_decl.name] = self._compute_deps_of(type_decl)

    def get_deps_of(self, class_name):
        '''returns the classes which are depended on by the given class'''
        if class_name in self.type_deps:
            return self.type_deps[class_name]
        else:
            raise KeyError('Class "%s" not found in module.' % class_name)

    def get_efferent(self, class_name):
        '''returns the efferent coupling of a class, which is the number of
        classes in the module the given class depends on
        '''

        return len(self.get_deps_of(class_name))

    def get_afferent(self, class_name):
        '''returns the afferent coupling of a class, which is the number of
        classes in the module that depend on the given class
        '''
        num = 0

        for type_decl in self.package_types:
            # don't compute the dependencies for self
            if type_decl.name == class_name:
                continue

            type_deps_of = self.get_deps_of(type_decl.name)
            if class_name in type_deps_of:
                num += 1

        return num

    def get_total_coupling(self, class_name):
        '''returns the total coupling of the class, which is:
            C_T = C_E / (C_E + C_A)'''
        eff = self.get_efferent(class_name)
        aff = self.get_afferent(class_name)

        # include a small smoothing constant to handle division by zero
        # higher values are worse
        return float(eff + 0.01) / (eff + aff + 0.01)

    def get_all_coupling(self):
        '''returns the coupling of all classes in the module'''
        results = {}
        for type_decl in self.package_types:
            results[type_decl.name] = self.get_total_coupling(type_decl.name)

        return results

    def print_deps(self):
        '''displays a table of each class in the module and its dependencies.
        Not really useful for anything except for simple debugging
        '''
        print '%-25s Dependencies' % 'Class'
        print '='*80
        for type, deps in self.type_deps.iteritems():
            print '%-25s' % type,
            print ', '.join([dep for dep in deps])

    def toJSON(self):
        '''converts the dependency graph to a JSON'''
        obj = {}
        for type, deps in self.type_deps.iteritems():
            obj[type] = list(deps)
        return obj
