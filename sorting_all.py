import random
import math
def random_array(arr,start,end,num):
    for i in range(num):
        arr.append(random.randint(start,end))
def asc_arr(arr,num):
    for i in range(num):
        arr.append(int(i))
def des_arr(arr,num):
    n=num-1
    for i in range(num):
        arr.append(int(n))
        n-=1
 
def merge_sort(arr):
   global count
   if len(arr)>1:
       mid = len(arr)//2
       lefthalf = arr[:mid]
       righthalf = arr[mid:]
       merge_sort(lefthalf)
       merge_sort(righthalf)
       i=0
       j=0
       k=0
       while i < len(lefthalf) and j < len(righthalf):
           count+=1
          
           if (lefthalf[i] < righthalf[j]):
               arr[k]=lefthalf[i]
               i=i+1
           else:
               arr[k]=righthalf[j]
               j=j+1
           k=k+1
       while (i<len(lefthalf)):
           count=count+1
           arr[k]=lefthalf[i]
           i=i+1
           k=k+1
       while (j<len(righthalf)):
           count=count+1
           arr[k]=righthalf[j]
           j=j+1
           k=k+1

def partition(arr,low,high):
    global count
    i = ( low-1 )
    pivot = arr[high]
    for j in range(low , high):
        if  arr[j] <= pivot:
            count+=1
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
def quick_Sort(arr,low,high):
    global count
    if low < high:
        count+=1
        pi = partition(arr,low,high)
        quick_Sort(arr, low, pi-1)
        quick_Sort(arr, pi+1, high)
       
        
def bubble_sort(arr):
    l=len(arr)
    global count
    for i in range(l):
        for j in range(l-1-i):
            count+=1
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
def selection_sort(arr):
    l=len(arr)
    global count
    for i in range(l):
        min=i
        for j in range(i+1,l):
            if(arr[j]<arr[min]):
                count+=1
                min=j
                arr[i],arr[min]=arr[min],arr[i]
                
def insertion_sort(arr):
        global count
        for i in range(1,len(arr)):
            current = arr[i]
            position = i
            while position>0 and arr[position-1]>current:
                count+=1
                arr[position]=arr[position-1]
                position = position-1
                arr[position]=current            
                
i=1
arr=[]
while(i!=0):
    print("\nPress 1 to perform Bubble Sort:\nPress 2 to perform Selection Sort:\nPress 3 to perform Insertion Sort:\nPress 4 to perform Merge Sort:\nPress 5 to perform Quick sort:\nPress 0 to exit:")
    i=int(input("\nEnter your choise: "))

    if(i==1):
        count=0
        print("Press 1 for best Case:\nPress 2 for average case:\nPress 3 for worst:")
        k=int(input("Enter your choise: "))
        if(k==1):
            num=int(input("\nEnter the no of element: "))
            asc_arr(arr,num)
            print("\nThe array is :")
            print(arr)
            bubble_sort(arr)
            p=num
        elif(k==2):
            num=int(input("Enter array size: "))
            start=int(input("Enter starting range: "))
            end=int(input("Enter ending range: "))
            random_array(arr,start,end,num)
            print("\nThe array is :")
            print(arr)
            bubble_sort(arr)
            p=num*num
        elif(k==3):
            num=int(input("\nEnter the no of element: "))
            des_arr(arr,num)
            print("\nThe array is :")
            print(arr)
            bubble_sort(arr)
            p=num*num
        else:
            print("Wrong Choise")
        
        print("\nArray sorted.")
        print("\nThe sorted array is: ")
        print(arr)
        print("Run time complexity = %d"%(count))
        print("Theoritical complexity = %d"%(p))
    
    elif(i==2):
        count=0
        print("Press 1 for best Case:\nPress 2 for average case:\nPress 3 for worst:")
        k=int(input("Enter your choise: "))
        if(k==1):
            num=int(input("\nEnter the no of element: "))
            asc_arr(arr,num)
            print("\nThe array is :")
            print(arr)
            insertion_sort(arr)
            p=num*num
            
        elif(k==2):
            num=int(input("Enter array size: "))
            start=int(input("Enter starting range: "))
            end=int(input("Enter ending range: "))
            random_array(arr,start,end,num)
            print("\nThe array is :")
            print(arr)
            insertion_sort(arr)
            p=num*num
        elif(k==3):
            num=int(input("\nEnter the no of element: "))
            des_arr(arr,num)
            print("\nThe array is :")
            print(arr)
            insertion_sort(arr)
            p=num*num
        else:
            print("Wrong Choise")
        
        print("\nArray sorted.")
        print("\nThe sorted array is: ")
        print(arr)
        print("Run time complexity = %d"%(count))
        print("Theoritical complexity = %d"%(p))
    
    elif(i==3):
        count=0
        print("Press 1 for best Case:\nPress 2 for average case:\nPress 3 for worst:")
        k=int(input("Enter your choise: "))
        if(k==1):
            num=int(input("\nEnter the no of element: "))
            asc_arr(arr,num)
            print("\nThe array is :")
            print(arr)
            insertion_sort(arr)
            p=num
            
        elif(k==2):
            num=int(input("Enter array size: "))
            start=int(input("Enter starting range: "))
            end=int(input("Enter ending range: "))
            random_array(arr,start,end,num)
            print("\nThe array is :")
            print(arr)
            insertion_sort(arr)
            p=num*num
        elif(k==3):
            num=int(input("\nEnter the no of element: "))
            des_arr(arr,num)
            print("\nThe array is :")
            print(arr)
            insertion_sort(arr)
            p=num*num
        else:
            print("Wrong Choise")
            
        print("\nArray sorted.")
        print("\nThe sorted array is: ")
        print(arr)
        print("Run time complexity = %d"%(count))
        print("Theoritical complexity = %d"%(p))
    
    elif(i==4):
        count=0
        num=int(input("Enter array size: "))
        start=int(input("Enter starting range: "))
        end=int(input("Enter ending range: "))
        random_array(arr,start,end,num)
        print("\nThe array is :")
        print(arr)
        merge_sort(arr)
        print("Array Sorted")
        print("\nThe sorted array is: ")
        print(arr)
        print("Run time complexity = %d"%(count))
        print("Theoritical complexity = ",num*(math.log2(num)))
    
    elif(i==5):
        count=0
        print("Press 1 for average Case:\nPress 2 for worst case:")
        k=int(input("Enter your choise: "))
        low=0
        high=len(arr)-1
        if(k==2):
            num=int(input("\nEnter the no of element: "))
            des_arr(arr,num)
            print("\nThe array is :")
            print(arr)
            quick_Sort(arr,low,high)
            p=num*num
            
        elif(k==1):
            num=int(input("Enter array size: "))
            start=int(input("Enter starting range: "))
            end=int(input("Enter ending range: "))
            random_array(arr,start,end,num)
            print("\nThe array is :")
            print(arr)
            quick_Sort(arr,low,high)
            p=num*(math.log2(num))
        else:
            print("Wrong Choise")
        
        print("Array Sorted")
        print("\nThe sorted array is: ")
        print(arr)
        print("Run time complexity = %d"%(count))
        print("Theoritical complexity = %d"%(p))
    
    elif(i==0):
        print("\n~*~ THANK YOU ~*~")
        
    else:
        print("\nWrong choise, Read the choise and enter suitable choise.")