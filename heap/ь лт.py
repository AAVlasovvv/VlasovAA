class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_node(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert_node(root.left, value)
    elif value > root.value:
        root.right = insert_node(root.right, value)

    return root


def create_binary_tree(values):
    root = None
    for value in values:
        root = insert_node(root, value)
    return root


def inorder_traversal(node):
    res = []
    if node is not None:
        inorder_traversal(node.left)
        res.append(int(node.value))
        
        print(node.value, end=" ")
        inorder_traversal(node.right)
    # print(res)
    
def geeeet(node):
    res = ''
    inorder_traversal(node)
    return print(res)

def output(node):
    # res = ''
    res = []
    inorder_traversal(node)
    # res1 = res.split()
    depth = 0
    counter = 0
    floor = []
    print(res)
    for i in range(len(res)):
        counter += 1
        if res[i]:
            floor.append(res[i])
        else:
            floor.append(None)
        if 2 ** depth == counter:
            counter %= (2 ** depth)
            depth += 1
            print(*floor)
            floor = []
            continue
        
    return ''
        
def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)




# Пример использования:
values = [ 4, 12, 2, 6, 10, 14, 9, 1, 24, 34]

# values.remove(min(values))
# root = create_binary_tree(values)
# inorder_traversal(root)
# geeeet(root)

# values.remove(min(values))
root = create_binary_tree(values)
inorder_traversal(root)
# output(root)

# values.append(5)
#
#
# # Создание бинарного дерева
# root = create_binary_tree(values)
#
# # Обход дерева в порядке возрастания
# inorder_traversal(root)
# # pre_order(root)