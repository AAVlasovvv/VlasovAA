class Box:
    def __init__(self, cat):
        self.cat = cat
        self.previouscat = None
        self.nextcat = None
        
    
    
        # def append(self, newcat):
        #     newbox = Box(newcat)
        


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
            
    def getnext(self, catIndex):
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:
            if boxIndex == catIndex:
                lastbox = lastbox.nextcat
                return lastbox.cat
            boxIndex = boxIndex + 1
            lastbox = lastbox.nextcat
            
    def getprev(self, catIndex):
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:
            if boxIndex == catIndex:
                lastbox = lastbox.previouscat
                return lastbox.cat
            boxIndex = boxIndex + 1
            lastbox = lastbox.nextcat
    
    
    def addToPlace(self, newcatIndex, newcat):
        newbox = Box(newcat)
        box = self.head
        boxIndex = 0
        previous_box = box.previouscat
        
        if newcatIndex == 0:
            self.head = newbox
            newbox.nextcat = box
            box.previouscat = newbox
            return
            
        if newcatIndex > len(List):
            print('kurva bubr, learn to count!!!')
            return
        
        if newcatIndex < 0:
            print('Kurwa, pierdolę ci usta, pomyśl co wkładasz, kurwa bóbr!!!') #Извиняюсь за ненормативную лексикку...
            return
        
        while boxIndex <= newcatIndex:
            if boxIndex == newcatIndex:
                previous_box.nextcat = newbox
                newbox.previouscat = previous_box
                box.previouscat = newbox
                newbox.nextcat = box
                
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
        s = s[:-1]
        return s
    
    def __len__(self):
        lastbox = self.head
        boxIndex = 0
        while lastbox is not None:
            lastbox = lastbox.nextcat
            boxIndex = boxIndex + 1
            
        return boxIndex
    
    def delete_an_item_by_index(self, catIndex):
        
        box = self.head
        boxIndex = 0
        previous_box = box.previouscat
        next_box = box.nextcat
        
        if catIndex == 0:
            self.head = box.nextcat
            box.cat = None
            return
        
        if catIndex > len(List):
            print('kurva bobr, learn to count!!!')
            return
        
        if catIndex < 0:
            print(
                'Kurwa, pierdolę ci usta, pomyśl co wkładasz, kurwa bóbr!!!')  # Извиняюсь за ненормативную лексикку...
            return
        
        while boxIndex <= catIndex:
            if boxIndex == catIndex:
                previous_box.nextcat = next_box
                next_box.previouscat = previous_box
                box.cat = None
                
                return
            boxIndex = boxIndex + 1
            box = box.nextcat
            previous_box = box.previouscat
            next_box = box.nextcat
        
        
    


print('Введите коробки через пробел.')
List = LinkedList()
P_List = list(map(str, input().split()))

for i in range(len(P_List)):
    List.addToEnd(P_List[i])
    
    


print(List.get(4))
List.delete_an_item_by_index(0)
print(str(List))
List.addToPlace(0, 'капибара')
print(str(List))
print(len(List))


    

