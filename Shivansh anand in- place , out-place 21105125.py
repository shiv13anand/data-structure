#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('WHAT IS THE DIFFERENCE BETWEEN IN PLACE AND OUT PLACE');get_ipython().run_line_magic('pinfo', 'PLACE')
#IN PLACE
1.A IN PLACE ALGORITHM MAY REQUIRE A SMALL AMOUNT OF EXTRA MEMORY FOR ITS OPERATION.HOWEVER ,THE AMOUNT OF MEMORY REQUIRED MUST NOT BE DEPENDENT ON INPUT SIZE AND SHOULD BE CONSTANT 
2.USUALLY,AN ALGORITHM IS BASED ON THE EXPLICT STORAGE ALLOCATED BY THE ALGORITHM.HOWEVER,CALLING A RECURSIVE ALGORITHM AS IN-PLACE IS HIGHLY DETABLE SINCE EXTRA SPACE IS BEING USED BY THE CALL STACK.ALTHOUGH THE SPACE REQUIRED BY THE CALL STACK TECHNICALLY TAKES THE RECURSIVE ALGORITHM OUT OF THE IN-PLACE ALGORITHMS CATEGORY,THE ALGORITHMS REQUIRING ONLY O(LOG(N)) ADDITIONAL SPACE IS CONSIDERED TO BE IN - PLACE
3.IN-PLACE ALGORITHMS ARE USUALLY USED IN AN EMBEDDED SYSTEM THAT RUNS IN LIMITED MEMORY.THEY REDUCE THE SPACE REQUIREMENTS TO A GREAT EXTENT , THE ALGORITHM TIME COMPLEXITY INCREASES IN SOME CASES
4. EXAMPLES ARE- 1.BUBBLE SORT 2.HEAP SORT 3.INSERTION SORT 3.QUICK SORT 4.SELECTION SORT 

#OUT-PLACE
1. AN ALGORITHM THAT NOT IN -PLACE IS CALLED OUT -PLACE . UNLIKE AN IN-PLACE ALGORITHM,THE EXTRA SPACE USED BY OUT-OF-PLACE ALGORITHM DEPENDS ON THE INPUT SIZE
2. THE MERGING CAN BE DONE IN-PLACE , BUT IT INCREASES THE TIME COMPLEXITY OF THE SORTING ROUTINE
3. THE STANDARD MERGE SORT ALGORITHM IS AN EXAMPLE OF OUT OF PLACE ALGORITHM AS IT REQUIRES O(N) EXTRA SPACE FOR MERGING
4.EXAMPLES :- RADIX SORT AND MERGE SORT
    
get_ipython().set_next_input('Q.2 IMPLEMENTATION OF IN PLACE AND OUT PLACE IN INSERTION SORT');get_ipython().run_line_magic('pinfo', 'SORT')

1.Insertion Sort Using In-Place Algorithm

#include <iostream>
using namespace std;
(/Creating, Insertion, Sort, void, function)
void insertion_sort_IP(int arr[],int n){
    //Initialising variables i and j
    int i=0,j=i+1;
    while(j<=n-1){
        int temp=arr[j];
        while(i>=0){
            if(arr[i]>temp){
                arr[i+1]=arr[i];
                i--;
            }
            if(i==-1){arr[0]=temp;break;}
            if(arr[i]<=temp){arr[i+1]=temp;break;}
        }
        j++;
        i=j-1;
    }
    return;
}

2.Insertion Sort Using Out-Place Algorithm

void insertion_sort_OP(int arr[],int si,int ei){
    //si=starting index
    //ei=ending index
    if(si==ei){return;}
    int j=si+1;
    int temp=arr[j];
    while(si>=0){
        if(arr[si]>temp){
            arr[si+1]=arr[si];
            si--;
        }
        if(si==-1){arr[0]=temp;break;}
        if(arr[si]<=temp){arr[si+1]=temp;break;}
    }
    insertion_sort_OP(arr,si+1,ei);
}
(/Function, to, print, array)
void pfun(int arr[],int n){
    for(int i=0;i<n;i++){cout<<arr[i]<<" ";}
}
int main(){
    int n;
    //Taking Input array
    cout<<"ENTER NUMBER OF ELEMENTS IN THE ARRAY: ";
    cin>>n;
    int arr[n],arr2[n];//Two array with same size and elements
    cout<<"ENTER ELEMENTS OF ARRAY SEPERATED BY SPACE: ";
    for(int i=0;i<n;i++){cin>>arr[i];}
    //copying arr to arr2
    for(int i=0;i<n;i++){arr2[i]=arr[i];}
    cout<<endl;
    cout<<"ARRAY BEFORE SORTING : ";pfun(arr,n);
    //Calling insertion sort using in-place algorithm.
    insertion_sort_IP(arr,n);
    cout<<endl;
    cout<<"ARRAY AFTER SORTING USING IN-PLACE ALGORITHM : ";
    //printing the array
    pfun(arr,n);
    cout<<endl;
    //calling insertiong sort using out-place algorithm.
    insertion_sort_OP(arr2,0,n-1);"AS IT USES AN EXTRA MEMORY BASED ON INPUT SIZE"
    cout<<"ARRAY AFTER SORTING USING OUT-PLACE ALGORITHM : ";
    //printing the array
    pfun(arr,n);
    cout<<endl;

}
   
get_ipython().set_next_input('Q.3 WHAT ARE PRACTICAL APPLICATIONS OF IN-PLACE AND OUT-PLACE');get_ipython().run_line_magic('pinfo', 'PLACE')
#IN - PLACE
1.For exapmle if we want to reverse an array then its in-place algorithm will be swaping the first and last element of array until we reach the 
  middle of array,
2.In many cases, the space requirements of an algorithm can be drastically cut by using a randomized algorithm.
3. For example, say we wish to know if two vertices in a graph of n vertices are in the same connected component of the graph. There is no known simple, deterministic, in-place algorithm to determine this, but if we simply start at one vertex and perform a random walk of about 20n3 steps, the chance that we will stumble across the other vertex provided that it is in the same component is very high
4. Similarly, there are simple randomized in-place algorithms for primality testing such as the Miller–Rabin primality test
5.there are also simple in-place randomized factoring algorithms such as Pollards rho algorithm. See RL and BPL for more discussion of this phenomenon.

#OUT-PLACE 
1.If we want to solve the same problem using out-place algorithm we have to create one extra array of same size and copy elements of original array from back to the front of new array,this 
 algorith increases the space complexity to O(n) as we have creaed an extra array.
2.merge sort is an example of out of place.
3.Now a days, using out-of-place sorting is a much better option because most of the computers offers decent amount of RAM. So even if this method of sorting uses extra memory, the program can still get executed.
then out of place algorithm can be used in editing the spreadsheet,browsing internet and performing day to day life easy tasks
4.we assume a person sing in a choir and when there’s free time I sort of pathologically sort the music. The choir members are assigned numbers so as to keep track of our personal performance “notes”, reminderts of the conductor’s nuances. I sort the music for a while, but soon it becomes a nuisance to hold the stack of books or thumb through to the right spot into which I then have to slip in the new entry. Thus I start a new stack, 
  and then…you guessed it. I merge sort the three or four piles into one group.


