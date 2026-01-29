/*Problem:
The function/method **maximizeInteger** accepts four arguments - **M, arr1, N and arr2**.  
The integer M represents the size of the integer array arr1.  
The integer N represents the size of the integer array arr2.  
Both arrays contain only digits. The digits in the array arr1 represent an integer value X.  

The function/method **maximizeInteger** must maximize the value of X by replacing its digits with the digits in the array arr2.  
You must implement the function so that the program runs successfully.

Boundary Conditions:
- 1 <= M <= 1000  
- 1 <= N <= 1000  
- Each element in arr1 and arr2 is a digit (0–9).  
- Digits in arr2 can be used at most once.  
- Replacement must maximize the integer value represented by arr1.  

Input Format:
The first line contains M.  
The second line contains M integers (arr1).  
The third line contains N.  
The fourth line contains N integers (arr2).  

Output Format:
Print the modified arr1 after maximizing the integer value.  

Example Input/Output 1:
Input:
5  
1 0 3 5 6  
3  
1 9 7  

Output:
9 7 3 5 6  

Explanation:
- Replace 1 in arr1 with 9 → [9, 0, 3, 5, 6]  
- Replace 0 in arr1 with 7 → [9, 7, 3, 5, 6]  

Example Input/Output 2:
Input:
6  
8 9 1 2 6 2  
4  
4 4 4 4  

Output:
8 9 4 4 6 4  

Explanation:
- Replace 1 with 4 → [8, 9, 4, 2, 6, 2]  
- Replace 2 with 4 → [8, 9, 4, 4, 6, 2]  
- Replace last 2 with 4 → [8, 9, 4, 4, 6, 4]  */


#include <stdio.h>

void sort(int array[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (array[i] < array[j]) { // descending order
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
}

void maximize_array(int arr1[], int n, int arr2[], int m) {
    sort(arr2, m); 

    int j = 0;
    for (int i = 0; i < n && j < m; i++) {
        if (arr1[i] < arr2[j]) {
            arr1[i] = arr2[j];
            j++; 
        }
    }
}

