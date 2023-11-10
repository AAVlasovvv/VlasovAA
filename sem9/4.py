class Box:
    def __init__(self, cat=None, nextcat = None, previouscat = None):
        
        self.cat = cat
        self.nextcat = nextcat
        self.previouscat = previouscat


class LinkedList:
    def __init__(self):
        self.head = None


    def contains(self, cat):
        lastbox = self.head
        while (lastbox):
            if cat == lastbox.cat:
                return True
            else:
                lastbox = lastbox.nextcat
        return False


    def addToEnd(self, newcat):
        newbox = Box(newcat)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while (lastbox.nextcat):
            lastbox = lastbox.nextcat
        lastbox.nextcat = newbox
        newbox.previouscat = lastbox


    def get(self, catIndex):
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:
            if boxIndex == catIndex:
                return lastbox.cat
            boxIndex = boxIndex + 1
            lastbox = lastbox.nextcat
    
    
    def addToPlace(self, newcatIndex, newcat):
        box = self.head
        previous_box = box.previouscat
        boxIndex = 0
        while boxIndex <= newcatIndex:
            if boxIndex == newcatIndex:
                previous_box.nextcat = newcat
                box.previouscat = newcat
                return
            boxIndex = boxIndex + 1
            box = box.nextcat
            previous_box = box.previouscat
            
    def __str__(self):
        s = ''
        box = self.head
        
        while (box != None):
            s += box.cat
            s += ' '
            box = box.nextcat
        s = s[:-2]
        return s
    
    


print('Введите коробки каждый в новой строчке.')
List = LinkedList()
P_List = list(map(str, input().split()))
for i in range(len(P_List)):
    List.addToEnd(P_List[i])
    
print(List)
# print(vectors)
print(str(List.addToPlace(6, 'ghhg')))

    

