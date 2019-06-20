
# Search


def linear_Search(arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    return linear_Search(arr, l+1, r, x)
def start_linear_Search():
    print('▐ Enter a list of integers : ',end = "")
    arr=[int(x) for x in input().split()]
    n = len(arr)
    x=eval(input('▐ Enter the search element : '))
    index = linear_Search(arr, 0, n-1, x)
    if index != -1:
        print("▐ Element", x,"is present at index %d" %(index))
    else:
        print("▐ Element",x,"is not present")

def binary_search_recursive(li, left, right, key):
  while True:
    if left > right:
      return -1
    mid = (left + right) // 2
    if li[mid] == key:
      return mid
    if li[mid] > key:
      right = mid - 1
    else:
      left = mid + 1
    return binary_search_recursive(li, left, right, key)

def start_binary_search():
    print('▐ Enter the list of integers : ')
    li=[int(x) for x in input().split()]
    left = 0
    right = len(li)
    li.sort()
    print('▐ The sorted list is : ',li)
    key=eval(input('▐ Enter the search element : '))
    for i in range(left,right):
        index = binary_search_recursive(li, left, right, key)
    print('▐ The element',key,'is found at',index,'position')

def fibo_search(a,x,n):
    f0=0
    f1=1
    f2=f0+f1
    while f2<n:
        f0=f1
        f1=f2
        f2=f0+f1
    offset=-1
    while f2>1:
        i=min(offset+f0,n-1)
        if a[i]<x:
            f2=f1
            f1=f0
            f0=f2-f1
            offset=i
        elif a[i]>x:
            f2=f0
            f1=f1-f0
            f0=f2-f1
        else:
            return i
    if f1 and a[offset]==x:
        return offset+1
    return -1
def start_fibo_search():
    print('▐ Enter the list of integers : ',end="")
    a=[int(x) for x in input().split()]
    a.sort()
    print('▐ The sorted list is : ',a)
    x=eval(input('▐ Enter the search element : '))
    n=len(a)
    pos=0
    pos=fibo_search(a,x,n)
    if pos>=0:
        print('▐ The element',x,'is found at',pos+1,'location')
    else:
        print('▐ The element',x,'is not found in the list')
    
#sorting techniques
def bubblesort(list):
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i]>list[i+1]:
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp
def start_bubblesort():    
    print('▐ Enter a list of integers : ',end="")
    list=[int(x) for x in input().split()]
    bubblesort(list)
    print('▐ The sorted list is : ',list)

def insertionsort(a):
    for i in range(1,len(a)):
        temp=a[i]
        pos=i
        while pos>0 and a[pos-1]>temp:
            a[pos]=a[pos-1]
            pos=pos-1
        a[pos]=temp
def start_insertionsort():
    print('▐ Enter a list of integers : ',end="")
    a=[int(x) for x in input().split()]
    insertionsort(a)
    print('▐ The sorted list is : ',a)

def selectionsort(a):
    for i in range(len(a)):
        least=i
        for k in range(i+1,len(a)):
            if a[k]<a[least]:
                least=k
        swap(a,least,i)
def swap(a,x,y):
    temp=a[x]
    a[x]=a[y]
    a[y]=temp
def start_selectionsort():
    print('▐ Enter a list of integers : ',end="")
    a=[int(x) for x in input().split()]
    selectionsort(a)
    print('▐ The sorted list is : ',a)

def quicksort(alist,low,high):
    if low<high:
        pivotpos=partition(alist,low,high)
        quicksort(alist,low,pivotpos-1)
        quicksort(alist,pivotpos+1,high)
def partition(alist,low,high):
    pivotvalue=alist[low]
    up=low+1
    down=high
    done=False
    while not done:
        if up<=down and alist[up]<pivotvalue:
            up=up+1
        if down>=up and alist[down]>pivotvalue:
            down=down-1
        if down<up:
            done=True
        else:
            temp=alist[up]
            alist[up]=alist[down]
            alist[down]=temp
    temp=alist[low]
    alist[low]=alist[down]
    alist[down]=temp
    return down
def start_quicksort():
    print('▐ Enter a list of integers : ',end="")
    alist=[int(x) for x in input().split()]
    low=0
    high=len(alist)-1
    quicksort(alist,low,high)
    print('▐ The sorted list is : ',alist)

def mergesort(a):
    if len(a)>1:
        mid=len(a)//2
        lefthalf=a[:mid]
        righthalf=a[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                a[k]=lefthalf[i]
                i+=1
            else:
                a[k]=righthalf[j]
                j+=1
            k+=1
        while i<len(lefthalf):
            a[k]=lefthalf[i]
            i+=1
            k+=1
        while j<len(righthalf):
            a[k]=righthalf[j]
            j+=1
            k+=1
def start_mergesort():
    print('▐ Enter a list of integers : ',end="")
    a=[int(x) for x in input().split()]
    mergesort(a)
    print('▐ The sorted list is : ',a)

#linear data structures/List
def createStack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print("▐ ▐ Pushed to stack",item)
def pop(stack):
    if isEmpty(stack):
        return "▐ ▐ stack overflow"
    return stack.pop()
def start_stack():
    top = 0
    mymax = 3
    stack=createStack()
    while True:
        print('▐ ▐ 1.Push')
        print('▐ ▐ 2.Pop')
        print('▐ ▐ 3.Display')
        print('▐ ▐ 4.Quit')
        ch=eval(input('▐ ▐ Enter choice : '))
        if ch==1:
            if top<mymax:
                item=eval(input('▐ ▐ Enter an item : '))
                push(stack,item)
                top+=1
            else:
                print("▐ ▐ Stack overflow")
        elif ch==2:
            print(pop(stack))
        elif ch==3:
            print(stack)
        else:
            break

def createQueue():
    queue=[]
    return queue
def isEmpty(queue):
    return len(queue)==0
def enqueue(queue,item):
    queue.append(item)
def dequeue(queue):
    if isEmpty(queue):
        return "▐ ▐ Queue is empty"
    item=queue[0]
    del queue[0]
    return item
def start_queue():
    front = 0
    rear = 0
    mymax = 3
    queue=createQueue()
    while True:
        print('▐ ▐ 1.Enqueue')
        print('▐ ▐ 2.Dequeue')
        print('▐ ▐ 3.Display')
        print('▐ ▐ 4.Quit')
        ch=eval(input('▐ ▐ Enter a choice : '))
        if ch==1:
            if rear<mymax:
                item=eval(input('▐ ▐ Enter an item : '))
                enqueue(queue,item)
                rear+=1
            else:
                print('▐ ▐ Queue is full')
        elif ch==2:
            print(dequeue(queue))
        elif ch==3:
            print(queue)
        else:
            break
#linear data structures/List/Application of Stack
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def infixToPostfix(infixexpr):
    prec={}
    prec["^"]= 4
    prec["*"]= 3
    prec["/"]= 3
    prec["+"]= 2
    prec["-"]= 2
    prec["("]= 1
    opStack=Stack()
    postfixList=[]
    tokenList=infixexpr.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token=='(':
            opStack.push(token)
        elif token==')':
            topToken=opStack.pop()
            while topToken !='(':
                postfixList.append(topToken)
                topToken=opStack.pop()
        else :
            while (not opStack.isEmpty())and(prec[opStack.peek()]>=prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
def start_infixToPostfix():
    infix = input("▐ ▐ ▐ Enter infix expression :")
    print(infixToPostfix(infix))

def postfixEval(postfixExpr):
    operandStack=Stack()
    tokenList=postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2=operandStack.pop()
            operand1=operandStack.pop()
            result=doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()
def doMath(op,op1,op2):
    if op=="*":
        return op1*op2
    elif op=='/':
        return op1/op2
    elif op=='+':
        return op1+op2
    elif op== '-':
        return op1-op2
def start_postfixEval():
    postfix = input("▐ ▐ ▐ Enter postfix expression:")
    print(postfixEval(postfix))
#

class Node:
    def __init__(self,data):
        print("▐ ▐ Node Created")
        self.data=data
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.ctr=0
    def insert_at_beg(self,new_data):
        new_node=Node(new_data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.ctr+=1
    def insert_at_end(self,new_data):
        new_node=Node(new_data)
        if self.head==None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        self.ctr+=1
        return
    def delete_at_beg(self):
        if self.head==None:
            print("▐ ▐ No nodes exist")
        else:
            print("▐ ▐ Node deleted",self.head.data)
            self.head=self.head.next
            self.ctr-=1
        return
    def delete_at_end(self):
        if self.head==None:
            print("▐ ▐ No node exists")
        elif self.ctr==1:
            self.ctr=0
            print("▐ ▐ Node deleted",self.head.data)
            self.head=None
        else:
            temp=self.head
            prev=self.head
            while temp.next is not None:
                prev=temp
                temp=temp.next
            print("▐ ▐ Node deleted",temp.data)
            prev.next=None
            self.ctr-=1
        return
    def insert_at_pos(self,pos,new_data):
        if pos==0:
            self.insert_at_beg(new_data)
        elif pos==self.ctr+1:
            self.insert_at_end(new_data)
        else:
            new_node=Node(new_data)
            temp=self.head
            i=1
            while i<pos-1:
                temp=temp.next
                i+=1
            new_node.next=temp.next
            temp.next=new_node
            self.ctr+=1
        return
    def delete_at_pos(self,pos):
        if self.head==None:
            print("▐ ▐ No node exists")
        else:
            if pos==0:
                self.delete_at_beg()
            elif pos==self.ctr:
                self.delete_at_end()
            else:
                temp=self.head
                prev=temp
                i=1
                while i<pos:
                    prev=temp
                    temp=temp.next
                    i+=1
                prev.next=temp.next
                print("▐ ▐ Node deleted",temp.data)
                temp.next=None
                self.ctr-=1
        return
    def traverse(self):
        print("▐ ▐ Traverse in forward direction")
        temp=self.head
        while temp is not None:
            print("▐ ▐ Data is",temp.data)
            temp=temp.next
def sll_menu():
    print("▐ ▐ ------------------")
    print("▐ ▐ Single Linked List")
    print("▐ ▐ ------------------")
    print("▐ ▐ 1.Insert at beginning")
    print("▐ ▐ 2.Insert at mid")
    print("▐ ▐ 3.Insert at end")
    print("▐ ▐ 4.Delete at beginning")
    print("▐ ▐ 5.Delete at mid")
    print("▐ ▐ 6.Delete at end")
    print("▐ ▐ 7.Traverse forward")
    print("▐ ▐ 8.Count the number of nodes")
    print("▐ ▐ 9.Quit")
    ch=eval(input("▐ ▐ Enter your choice : "))
    return ch
def start_sll():
    
    sll=SingleLinkedList()
    while True:
        ch=sll_menu()
        if ch==1:
            data=eval(input("▐ ▐ Enter a data element : "))
            sll.insert_at_beg(data)
        elif ch==2:
            pos=eval(input("▐ ▐ Enter the position : "))
            data=eval(input("▐ ▐ Enter a data element : "))
            sll.insert_at_pos(pos,data)
        elif ch==3:
            data=eval(input("▐ ▐ Enter a data element : "))
            sll.insert_at_end(data)
        elif ch==4:
            sll.delete_at_beg()
        elif ch==5:
            pos=eval(input("▐ ▐ Enter the position : "))
            sll.delete_at_pos(pos)
        elif ch==6:
            sll.delete_at_end()
        elif ch==7:
            sll.traverse()
        elif ch==8:
            print("▐ ▐ Total number of nodes : ",sll.ctr)
        else:
            break

class Node_dll:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
        self.ctr=0
    def insert_at_beg(self,data):
        new_node=Node_dll(data)
        if self.head==None:
            self.head=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
        self.ctr +=1
        return
    def insert_at_end(self,data):
        new_node=Node_dll(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            new_node.prev=temp
            temp.next=new_node
        self.ctr += 1
        return
    def insert_at_pos(self,data,pos):
        
        if pos==0:
            self.insert_at_beg(data)
        elif pos==self.ctr+1:
            self.insert_at_end(data)
        else:
            new_node=Node_dll(data)
            temp=self.head
            i=0
            while i<pos:
                temp=temp.next
                i +=1
            temp.next.prev=new_node
            new_node.next=temp.next
            new_node.prev=temp
            temp.next=new_node
        self.ctr+=1
        return
    def delete_at_beg(self):
        if self.head ==None:
            print("▐ ▐ No node exited")
        elif self.ctr==1:
            print("▐ ▐ ",self.head.data,"is delected")
            self.head=None
            self.ctr -=1
        else:
            print("▐ ▐ ",self.head.data,"is delected")
            self.head=self.head.next
            self.head.prev=None
        self.ctr-=1
        return
    def delete_at_end(self):
        if self.head==None:
            print("▐ ▐ No NOde exited")
        elif self.ctr == 1:
            #print("no node exicted")
            self.head=None
            self.ctr -=1
        else:
            temp=self.head
            while temp.next is not None:
                temp =temp.next
            print("▐ ▐ ",temp.prev.next.data,"is delected")
            temp.prev.next=None
        self.ctr -=1
        return
    def delete_at_pos(self,pos):
        if pos==0:
            self.delete_at_beg()
        elif pos==self.ctr:
            self.delete_at_end()
        else :
            temp=self.head
            i=0
            while i<pos:
                temp=temp.next
                i+=1
            print("▐ ▐ ",temp.data,"is delected")
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
        self.ctr -=1
        return
    def traversal(self):
        temp=self.head
        while temp.next is not None:
            print("▐ ▐ ",temp.data)
            temp=temp.next
        print(temp.data)
        return
def Menu_dll():
    print("▐ ▐ 1.insert at beg")
    print("▐ ▐ 2.insert at pos")
    print("▐ ▐ 3.insert at end")
    print("▐ ▐ 4.delect at beg")
    print("▐ ▐ 5.delect at pos")
    print("▐ ▐ 6.delect at end")
    print("▐ ▐ 7.Traversal")
    print("▐ ▐ 8.exit")
    ch=int(input("▐ ▐ Enter your choice:"))
    return ch
def start_dll():
    d=DLL()
    while True:
        ch=Menu_dll()
        if ch==1:
            data=int(input("▐ ▐ enter data:"))
            d.insert_at_beg(data)
        elif ch==2:
            pos=int(input("▐ ▐ enter position:"))
            data=int(input("▐ ▐ enter data"))
            d.insert_at_pos(data,pos)
        elif ch==3:
            data=int(input("▐ ▐ enter data:"))
            d.insert_at_end(data)
        elif ch==4:
            d.delete_at_beg()
        elif ch==5:
            pos=int(input("▐ ▐ enter position:"))
            d.delete_at_pos(pos)
        elif ch==6:
            d.delete_at_end()
        elif ch==7:
            d.traversal()
        else:
            break
class Node_cll:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.ctr=0
    def insert_at_beg(self,new_data):
        new_node=Node_cll(new_data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.ctr +=1
    def insert_at_end(self,new_data):
        new_node=Node_cll(new_data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
        self.ctr +=1
        
    def insert_at_pos(self,new_data,pos):
        new_node=Node_cll(new_data)
        if pos==1:
            self.insert_at_beg(new_data)
        elif pos==self.ctr+1:
            self.insert_at_end(new_data)
        else:
            temp=self.head
            i=1
            while i<pos-1:
                temp=temp.next
            new_node.next=temp.next.next
            temp.next=new_node
            self.ctr +=1
    def del_at_beg(self):
        if self.head==None:
            print("▐ ▐ No none exist")
        elif self.ctr==1:
            self.head=None
            self.ctr -=1
        else:
            self.head=self.head.next
            self.ctr -=1
    def del_at_end(self):
        if self.head==None:
            print("▐ ▐ No none exist")
        elif self.ctr==1:
            self.head=None
            self.ctr -=1
        else:
            temp=self.head
            while temp.next is not None:
                prev=temp
                temp=temp.next
            prev.next=None
            self.ctr -=1
    def del_at_pos(self,pos):
        if pos==1:
            self.del_at_beg()
        elif pos==self.ctr:
            self.del_at_end()
        else:
            i=1
            temp=self.head
            while i<pos:
                prev=temp
                temp=temp.next
            prev.next=temp.next
            self.ctr -=1
    def travers(self):
        temp=self.head
        while temp.next is not None:
            print(temp.data)
            temp=temp.next
        print("▐ ▐ ",temp.data)
def start_cll():
    c=CLL
    while True:
        print("▐ ▐ 1.insert at beg")
        print("▐ ▐ 2.insert at mid")
        print("▐ ▐ 3.insert at end")
        print("▐ ▐ 4.del at beg")
        print("▐ ▐ 5.del at mid")
        print("▐ ▐ 6.del at end")
        print("▐ ▐ 7.display")
        print("▐ ▐ 8.exit")
        ch=int(input("▐ ▐ enter your choice:"))
        if ch==1:
            new_data=eval(input("▐ ▐ enter data:"))
            c.insert_at_beg(new_data)
        elif ch==2:
            new_data=eval(input("▐ ▐ enter data:"))
            pos=eval(input("▐ ▐ enter position:"))
            c.insert_at_pos(new_data,pos)
        elif ch==3:
            new_data=eval(input("▐ ▐ enter data:"))
            c.insert_at_end(new_data)
        elif ch==4:
            c.del_at_beg()
        elif ch==5:
            pos=eval(input("▐ ▐ enter position:"))
            c.del_at_pos(pos)
        elif ch==6:
            c.del_at_end()
        elif ch==7:
            c.travers()
        elif ch==8:
            break
        else:
            print("▐ ▐ Enter correct choice")
        
class Node_Q:
  def __init__(self,data):
    self.data=data
    self.next=None

class Queue:
  def __init__(self):
    self.front=None
    self.ctr=0
    self.rear=None
  def Enqueue(self,data):
    node=Node_Q(data)
    if self.front==None:
      self.front=node
      self.rear=node
    else:
      self.rear.next=node
      self.rear=node
    print("▐ ▐ Node enqueued to queue",data)
    self.ctr+=1
    return
  def Dequeue(self):
    if self.front==None:
      print("▐ ▐ No Nodes exist")
    else:
      print("▐ ▐ Dequeued from queue",self.front.data)
      self.front=self.front.next
      self.ctr-=1
    return
  def Traverse(self):
    if self.front==None:
      print("▐ ▐ No Nodes exist")
      return
    temp=self.front
    while temp is not None:
      print(temp.data)
      temp=temp.next

def Menu_Q():
  print("▐ ▐ 1.Enqueue\n▐ ▐ 2.Dequeue\n▐ ▐ 3.Traverse\n▐ ▐ 4.Number of nodes\n▐ ▐ 5.Exit")
  ch=int(input("▐ ▐ Enter choice:"))
  return ch
def start_Q():    
    s=Queue()
    while True:
      ch=Menu_Q()
      if ch==1:
        data=input("▐ ▐ Enter data:")
        s.Enqueue(data)
      elif ch==2:
        s.Dequeue()
      elif ch==3:
        s.Traverse()
      elif ch==4:
       print("▐ ▐ Number of nodes",s.ctr)
      else:
        print('▐ ▐ Quit')
        break

class Node_Stack:
  def __init__(self,data):
    self.data=data
    self.next=None

class Stack:
  def __init__(self):
    self.head=None
    self.ctr=0
    self.top=None
  def Push(self,data):
    node=Node_Stack(data)
    if self.head==None:
      self.head=node
      self.top=node
    else:
      self.top.next=node
      self.top=node
    print("▐ ▐ Node pushed to stack",data)
    self.ctr+=1
    return
  def Pop(self):
    if self.head==None:
      print("▐ ▐ Stack Underflow")
    elif self.head==self.top:
      print("▐ ▐ Deleted from Stack",self.head.data)
      self.head=self.top=None
      self.ctr-=1
    else:
      print("▐ ▐ Deleted from Stack",self.top.data)
      temp=self.head
      while temp.next is not self.top:
        temp=temp.next
      temp.next=None
      self.top=temp
      self.ctr-=1
    return
  def Traverse(self):
    if self.head==None:
      print("▐ ▐ No Nodes exist")
      return
    temp=self.head
    while temp is not None:
      print("▐ ▐ ",temp.data)
      temp=temp.next

def Menu_Stack():
  print("▐ ▐ 1.Push\n▐ ▐ 2.Pop\n▐ ▐ 3.Traverse\n▐ ▐ 4.Number of nodes\n▐ ▐ 5.Exit")
  ch=int(input("▐ ▐ Enter choice:"))
  return ch
def start_Stack():
    
    s=Stack()
    while True:
      ch=Menu_Stack()
      if ch==1:
        data=input("▐ ▐ Enter data:")
        s.Push(data)
      elif ch==2:
        s.Pop()
      elif ch==3:
        s.Traverse()
      elif ch==4:
        print("▐ ▐ Number of nodes",s.ctr)
      else:
        print('▐ ▐ Quit')
        break

class Node_BST:
    def __init__(self,data):
        self.lc=None
        self.data=data
        self.rc = None
class BST:
    def __init__(self):
        self.ctr=0
        self.root=None
    def creation(self,data):
        new_node=Node_BST(data)
        if self.root==None:
                self.root=new_node
        else:
            temp=self.root
            while True:
                if temp.data > new_node.data and temp.lc==None:
                    temp.lc=new_node
                    break
                elif temp.data < new_node.data and temp.rc==None:
                    temp.rc=new_node
                    break
                elif temp.data> new_node.data:
                    temp=temp.lc
                elif temp.data < new_node.data:
                    temp=temp.rc
            self.ctr +=1
    def post(self,root):
        if root.lc != None:
            self.post(root.lc)
        if root.rc != None:
            self.post(root.rc)
        print("▐ ",root.data)
    def inoder(self,root):
        if root.lc != None:
            self.inoder(root.lc)
        print("▐ ",root.data)
        if root.rc != None:
            self.inoder(root.rc)
    def pre(self,root):
        print("▐ ",root.data)
        if root.lc != None:
            self.pre(root.lc)
        if root.rc != None:
            self.pre(root.rc)
        
    def leaf(self,root):
        if root.lc != None:
            self.leaf(root.lc)
        if root.rc != None:
            self.leaf(root.rc)
        if root.lc==None and root.rc==None:
            print("▐ ",root.data)
    def height(self,root):
        if root==None:
            return -1
        else :
            return 1+max(self.height(root.lc),self.height(root.rc))
def start_BST():        
    b=BST()
    while True:
        print("▐ 1.create tree")
        print("▐ 2.leaf node")
        print("▐ 3.post order")
        print("▐ 4.in order")
        print("▐ 5.pre order")
        print("▐ 6.height")
        print("▐ 7.break")
        ch=int(input("▐ enter your choice:"))
        if ch==1:
            n=int(input("▐ Enter no.of node:"))
            for i in range(n):
                data=int(input("▐ enter data:"))
                b.creation(data)
        if ch==3:
            b.post(b.root)
        if ch==2:
            print("▐ leaf node are:")
            b.leaf(b.root)
        if ch==4:
            b.inoder(b.root)
        if ch==5:
            b.pre(b.root)
        if ch==6:
            print("▐ height=",b.height(b.root))
    
class Vertex:
    def __init__(self, data) :
        self.data = data
        self.nxtVertex = None
        self.AdjHead = None
        self.trvState = None
        
class AdjNode :
    def __init__(self) :
        self.reference = None
        self.nxt = None
        
class Graph :
    def __init__(self) :
        self.root = None
        self.vertexCtr = 0    
    def create(self) :        
        print('▐ Enter the Vertex List : ')
        vertexLst = input().split()
        print("▐ ",vertexLst)
        for i in range(len(vertexLst)) :
            new_node = Vertex(vertexLst[i])
            if self.root == None :
                self.root = new_node
            else :
                temp = self.root
                while temp.nxtVertex is not None :
                    temp = temp.nxtVertex
                temp.nxtVertex = new_node
        # Creation of AdjacetList
        temp = self.root        
        while temp is not None :
            print('▐ Enter the Adjacency List of Vertex(',temp.data,')')
            adjLst = input('▐ Enter Here (In Ascending order : ) : ').split()
            for i in range(len(adjLst)) :
                refPtr = self.getReference(adjLst[i])
                new_node = AdjNode()
                new_node.reference = refPtr
                if temp.AdjHead == None :
                    temp.AdjHead = new_node
                else :
                    temp1 = temp.AdjHead
                    while temp1.nxt is not None :
                        temp1 = temp1.nxt
                    temp1.nxt = new_node
            temp = temp.nxtVertex
    def getReference(self, nodeData) :
        temp = self.root
        while temp is not None :
            if temp.data == nodeData :
                
                return temp
            temp = temp.nxtVertex
    def LinearSearch(self, Lst, Key) :
        for i in range(len(Lst)) :
            if Lst[i] == Key :
                return True
        return False
    def DFT(self) :
        Path = []
        S = []
        V = self.root
        S.append(V)
        while len(S) is not 0 :
            V = S.pop()
            if  self.LinearSearch(Path, V.data) == False :
                Path.append(V.data)
                temp = V.AdjHead
                while temp is not None :
                    S.append(temp.reference)
                    temp = temp.nxt
        return Path
    def BFT(self) :
        Path = []
        S = []
        V = self.root
        S.append(V)
        while len(S) is not 0 :
            V = S.pop(0)
            if  self.LinearSearch(Path, V.data) == False :
                Path.append(V.data)
                temp = V.AdjHead
                while temp is not None :
                    S.append(temp.reference)
                    temp = temp.nxt
        return Path
def start_GraphTraversals():    
    print("▐ ######---Graph---#####")
    G = Graph()
    G.create()
    print('▐ Graph Traversals :')
    print('▐ 1. DFT')
    print('▐ 2. BFT')

    while True :
        ch = int(input('▐ Enter Choice : '))
        if ch == 1 :
            print(G.DFT())
        elif ch == 2 :
            print(G.BFT())
        else:
            print("▐ Exit")
            break    


def menu():
    print("1.searching techniques")
    print("2.sorting techniques")
    print("3.linear data structures")
    print("4.non-linear data structures")
    print("5. quit")
    ch = int(input("Enter your choices:"))
    return ch


print("""
    
       .-"^`\                                              /`^"-.
  .'   ___\                                          /___   `.
 /    /.---.                                         .---.\    !
|    //     '-.  _______________________________    .-'     !!    |
|   ;|         \/------------------------------- //         |;   |
\   ||       |\_) ______      _                  (_/|       ||   /
 \  | \  . \ ;  | |  _  \    | |                || ; / .  / |  /
  '\_\ !\ \ \ \ | | | | |__ _| |_ __ _          ||/ / / // /_/'
        !\ \ \ \| | | | / _` | __/ _` |         |/ / / //
         `'-\_\_\ | |/ / (_| | || (_| |         /_/_/-'`
                | |___/ \__,_|\__\__,_|         \ 
                |                                \ 
                |  _____ _                   _    \                   
                | /  ___| |                 | |    \___________________                 
                | \ `--.| |_ _ __ _   _  ___| |_ _   _ _ __ ___  ___   |
                |  `--. \ __| '__| | | |/ __| __| | | | '__/ _ \/ __|  |
                |/\__/ / |_| |  | |_| | (__| |_| |_| | | |  __/\__ \   | 
                |\____/ \__|_|   \__,_|\___|\__|\__,_|_|  \___||___/   | 
                |______________________________________________________|                                  
""")
while True:
    c = 0
    ch = menu()
    if ch == 1:
        while c != 4:
            print("▐=>### searching techniques ###")
            print("▐ 1.Linear search")
            print("▐ 2.Binary search")
            print("▐ 3.Fibonacci search")
            print("▐ 4.exit from searching techniques")
            c = int(input("▐ Enter your choices:"))
            if c == 1:
                print("▐-=:Linear search")
                start_linear_Search()
            elif c == 2:
                print("▐-=:Binary search")
                start_binary_search()
            elif c == 3:
                print("▐-=:Fibonacci search")
                start_fibo_search()
            print("|")
    elif ch == 2:
        c = 0
        while c != 6:
            print("▐=>### sorting techniques ###")
            print("▐ 1.Bubble sort")
            print("▐ 2.Insertion sort")
            print("▐ 3.Selection sort")
            print("▐ 4.Quick sort")
            print("▐ 5.Merge sort")
            print("▐ 6.exit from sorting techniques")
            c = int(input("▐ Enter your choices:"))
            if c == 1:
                print("▐-=:Bubble sort")
                start_bubblesort()
            elif c == 2:
                print("▐-=:Insertion sort")
                start_insertionsort()
            elif c == 3:
                print("▐-=:Selection sort")
                start_selectionsort()
            elif c == 4:
                print("▐-=:Quick sort")
                start_quicksort()
            elif c == 5:
                print("▐-=:Merge sort")
                start_mergesort()
            print("/")

    elif ch == 3:
        c = 0
        while c != 3:
            print("▐=>### linear data structures ###")
            print("▐ 1.List")
            print("▐ 2.Linked Lists")
            print("▐ 3.exit from linear data structures")
            c = int(input("▐ Enter your choices:"))
            if c == 1:
                c = 0
                while c != 4:
                    print("▐ ▐=>### linear data structures/List  ###")
                    print("▐ ▐ 1.Stack")
                    print("▐ ▐ 2.Queue")
                    print("▐ ▐ 3.Application of Stack")
                    print("▐ ▐ 4.exit from List")
                    c = int(input("▐ ▐ Enter your choices:"))
                    if c == 1:
                        print("▐ ▐-=:Stack")
                        start_stack()
                    elif c == 2:
                        print("▐ ▐-=:Queue")
                        start_queue()
                    elif c == 3:

                        c = 0
                        while c != 3:
                            print("▐ ▐ ▐=>### linear data structures/List/Application of Stack  ###")
                            print("▐ ▐ ▐ 1.infix expression to postfix expression")
                            print("▐ ▐ ▐ 2.evaluation of postfix expression")
                            print("▐ ▐ ▐ 3.exit from Application of Stack")
                            c = int(input("▐ ▐ ▐ Enter your choices:"))
                            if c == 1:
                                print("▐ ▐ ▐-=:infix expression to postfix expression")
                                start_infixToPostfix()
                            elif c == 2:
                                print("▐ ▐ ▐-=:evaluation of postfix expression")
                                start_postfixEval()
                        print("▐ ▐  ")
                print("▐ ")

            elif c == 2:
                c = 0
                while c!=5:
                    print("▐ ▐=>### linear data structures/Linked Lists  ###")
                    print("▐ ▐ 1.Single Linked List")
                    print("▐ ▐ 2.Double Linked List")
                    print("▐ ▐ 3.Circular Single Linked List")
                    print("▐ ▐ 4.Application Single Linked List")
                    print("▐ ▐ 5.exit from Linked Lists")
                    c = int(input("▐ ▐ Enter your choices:"))
                    if c == 1:
                        print("▐ ▐-=:Single Linked List")
                        start_sll()
                    elif c == 2:
                        print("▐ ▐-=:Double Linked List")
                        start_dll()
                    elif c == 3:
                        print("▐ ▐-=:Circular Single Linked List")
                        start_cll()
                    elif c == 4:
                        c = 0
                        while c != 3:
                            print("▐ ▐ ▐=>### linear data structures/Linked Lists/Application Single Linked List  ###")
                            print("▐ ▐ ▐ 1.Queue Using Linked List")
                            print("▐ ▐ ▐ 2.Stack Using Linked List")
                            print("▐ ▐ ▐ 3.exit from Application Single Linked List")
                            c = int(input("▐ ▐ ▐ Enter your choices:"))
                            if c == 1:
                                print("▐ ▐ ▐-=:Queue Using Linked List")
                                start_Q()
                            elif c == 2:
                                print("▐ ▐ ▐-=:Stack Using Linked List")
                                start_Stack()
                            print("▐ ▐ ")
                    print("▐ ")
        print("| ")
    elif ch == 4:
        c= 0
        while c != 3:
            print("▐=>### non-linear data structures ###")
            print("▐ 1.Trees ==> Binary Search Tree")
            print("▐ 2.Graph ==> Graph Traversals")
            print("▐ 3.exit from non-linear data structures")
            c = int(input("▐ Enter your choices:"))
            if c == 1:
                print("▐-=:Binary Search Tree")
                start_BST()
            elif c == 2:
                print("▐-=:Graph Traversals")
                start_GraphTraversals()
            print("|")
            
    elif ch == 5:
        break
            
            
