class Box:
  def __init__ (self, cat = None, nextcat = None):
    self.cat = cat
    self.nextcat = None
    # self.previouscat = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def contains (self, cat):
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
        
    def get(self, catIndex):
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:
          if boxIndex == catIndex:
              return lastbox.cat
          boxIndex = boxIndex + 1
          lastbox = lastbox.nextcat
    
    def __str__(self):
        s = ''
        box = self.head
        
        while (box != None):
            s += box.cat
            s += ' '
            box = box.nextcat
        s = s[:-1]
        return s
    

box1 = Box(1, 2)
box2 = Box(2, 3)
box3 = Box(3, 4)
box4 = Box(4, None)

List = LinkedList()
P_List = list(map(str, input().split()))
print(P_List)

