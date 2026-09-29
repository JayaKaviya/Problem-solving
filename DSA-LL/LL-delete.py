class Node: 
    def __init__(self,data): 
        self.data=data 
        self.head=None 

class LinkedList: 
    def __init__(self): 
        self.head=None
    
    # adding at the front
    def push(self,data): 
       new_node=Node(data) 
       new_node.next=self.head 
       self.head=new_node  

    def deletef(self): 
        self.head=self.head.next  

    def deletel(self): 
        temp=self.head 

        while(temp.next): 
            prev=temp
            temp=temp.next 
        
        prev.next=None 

    #delete based on position 

    def deletep(self,pos): 
        temp=self.head 
        prev=self.head  

        for i in range(0,pos): 
            if i==0 and pos==1: 
                self.head=self.head.next 
                return 0 
            elif(i==pos-1 and temp) : 
                prev.next=temp.next

            else: 
                prev=temp  
                if prev==None:  #position greater than no. of nodes
                    break
                temp=temp.next
            
        

    def print(self): 
        temp=self.head 
        while(temp): 
            print(temp.data) 
            temp=temp.next 
        
l=LinkedList() 
l.push(30)
l.push(20) 
l.push(10) 
l.push(40) 
l.push(60) 
l.push(80)
l.print()   
l.deletef() 
print("delete at first")
l.print()
 

l.deletel() 
print("delete at last")
l.print() 

l.deletep(3) 
print("delete at given position")
l.print()
