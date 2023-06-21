
class Tag:
    def __init__(self, tree):
        self.tree = tree


    def get_datatype(self):

        try:
            return str(self.tree.get('DataType'))
        except Exception as e:
            print(f"Error creating Tag: {e}")

    def get_name(self):

        try:
            return str(self.tree.get('Name'))
        except Exception as e:
            print(f"Error creating Tag: {e}")


    def get_tree(self):
        return str(self.tree)