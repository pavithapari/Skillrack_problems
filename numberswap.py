"""Problem:  
--------  
The function/method swapDigitsSameSum accepts two arguments ptr1 and ptr2 representing the addresses of two integer values X and Y. The number of digits in X and Y are always not equal.  

The function/method swapDigitsSameSum must modify the given two integer values based on the following condition.  

1. The function must remove the first D digits from the largest integer.  
2. The removed digits must be prepended to the smallest integer between the given two integers.  
3. D is the absolute difference between the number of digits in X and Y.  

Boundary Conditions:  
--------------------  
The number of digits in X and Y are always not equal.  

Input Format:  
-------------  
The first line contains two integers X and Y.  

Output Format:  
--------------  
The first line contains the modified values of X and Y.  

Example:  
--------  
Input:  
254 6573  

Output:  
6254 573  

Input:  
5056 23  

Output:  
56 5023  

Input:  
23 5056  

Output:  
5023 56  """

void swapDigitsSameSum(int *ptr1, int *ptr2)
{
    int c1 = digcount(*ptr1);
    int c2 = digcount(*ptr2);
    int diff = abs(c1 - c2);

    int max = *ptr1;
    int min = *ptr2;
    int maxIsPtr1 = 1;  

    if (*ptr2 > *ptr1) {
        max = *ptr2;
        min = *ptr1;
        maxIsPtr1 = 0;
    }

    int divi = 1;
    for (int i = 0; i < digcount(max) - diff; i++) {
        divi *= 10;
    }

    int firstD = max / divi;
    int remaining = max % divi;

    int multiplier = 1;
    int temp = min;
    while (temp > 0) {
        multiplier *= 10;
        temp /= 10;
    }

    min = firstD * multiplier + min;

    if (maxIsPtr1) {
        *ptr1 = remaining;
        *ptr2 = min;
    } else {
        *ptr2 = remaining;
        *ptr1 = min;
    }
}

