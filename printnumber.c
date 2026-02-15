/*You are given an array of integers and its size.
Return the first number such that, from the digits of the first element up to that number, all digits 0–9 have appeared at least once; otherwise return */
int findNumber(int Size, int arr[]) {
    int find[10] = {0};  

    int allDigitsFound() {
        for (int i = 0; i < 10; i++) {
            if (find[i] == 0) return 0;  
        }
        return 1;  
    }

    for (int i = 0; i < Size; i++) {
        int num = arr[i];
        while (num > 0) {
            int d = num % 10;
            find[d] = 1;
            num /= 10;
        }
        if (allDigitsFound()) {
            return arr[i];  
        }
    }
    return -1;  
}
