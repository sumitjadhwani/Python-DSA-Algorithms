from tree import TreeNode

class CompanyTreeHierarchy(TreeNode):
    def __init__(self, obj):
        super().__init__(data=None)
        self.name = obj['name']
        self.designation = obj['designation']

    def print_tree(self, hierarchy):
        level = self.get_level()
        prefix = ' ' * level * 2
        if level != 0:
            prefix=prefix+'|__'
        nodes = self.child

        if hierarchy == 'name':
            print(prefix+self.name)
            for child in nodes:
                child.print_tree('name')

        if hierarchy == 'designation':
            print(prefix+self.designation)
            for child in nodes:
                child.print_tree('designation')

        if hierarchy == 'both':
            print(prefix+self.name+' ('+self.designation+')')
            for child in nodes:
                child.print_tree('both')
        
    def print_level_tree(self, max_level, hierarchy = "name"):
        level = self.get_level()
        prefix = ' ' * level * 2

        if level <= max_level:
            prefix = ' ' * level * 2
            if level != 0:
                prefix=prefix+'|__'
            nodes = self.child

            if hierarchy == 'name':
                print(prefix+self.name)
                for child in nodes:
                    child.print_level_tree(max_level)
    
def build_management_tree():
    ceo = CompanyTreeHierarchy({'name':'Abhay','designation':'CEO'})
    cto = CompanyTreeHierarchy({'name':'Sumit','designation':'CTO'})

    infra = CompanyTreeHierarchy({'name':'Gels','designation':'Infra Head'})
    cloud = CompanyTreeHierarchy({'name':'Dhawal','designation':'Cloud Manager'})
    app = CompanyTreeHierarchy({'name':'Abhijit','designation':'App Manager'})

    app_head = CompanyTreeHierarchy({'name':'Aamir','designation':'Application Head'})

    hr = CompanyTreeHierarchy({'name':'Chitnis','designation':'HR Head'})
    recrutiment = CompanyTreeHierarchy({'name':'Peter','designation':'Recruitment Manager'})
    policy = CompanyTreeHierarchy({'name':'Waqas','designation':'Policy Manager'})

    ceo.add_child(cto)
    ceo.add_child(hr)

    cto.add_child(infra)
    cto.add_child(app_head)

    infra.add_child(cloud)
    infra.add_child(app)

    hr.add_child(recrutiment)
    hr.add_child(policy)

    return ceo


if __name__ == '__main__':
    
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
    root_node.print_level_tree(2)


    
