// 直接插入排序
// TODO
#include <type_traits>
void insertSort(Element A[], int n) {
    for(int i = 2; i<n; i++) {
        A[0] = A[i];
        if(A[i-1] > A[i]) {
            for(int j = i - 1; A[j] > A[0];  j--) {
                A[j+1] = A[j];
            }
            A[j+1] = A[0]; // 插入正确数值
        }
    }
}


// TODO
// 折半插入排序
void binaryInsertSort(Element A[], int n) {
    int i, j, mid, low, high;
    for(i = 2; i<n; i++) {
        low = 1, high = i - 1; // 初始化数据
        A[0] = A[i];
        while(low <= high) {
            mid = (low + high) / 2;
            if(A[0] < A[mid]) right = mid - 1;
            else left = mid + 1; //包含了=》当查找到相同的数字时，还要继续向后查找，保证了排序的稳定性，即排序前后的
                                 //相对位置没有改变
        } 
        for(j = i-1; j >= low; j--) {
            A[j+1] = A[j];
        }
        A[low] = A[0];
    }
}



// 希尔排序
void sewoSort(Element A[], int n) {

}


// TODO
// 快速排序
int partition(Element A[], int low, int high) {
    int privot = A[low]; //初始化
    while(low <= high) {
        while(low <= high && A[high] >= privot)  high--; //因为开始的时候先将A[low]位置先存储到了privot，
                                                         //这里先比较A[high]，如果找到比privot小的数，就
                                                         //存放在A[low]
        A[high] = A[low]; // 通过上述循环找到比privot大的数，将大的数放到右表
        while(low <= high && A[low] <= privot) low++;
        
        A[low] = A[high];//通过上述循环找到比privot小的数，将小的数放到左表
    }
    A[low] = privot; // or A[high] = privot
    return low; // or return high;
}

void quickSort(Element A[], int low, int high) {
    if(low < high) {
        int partitionNum = partition(A, low, high);
        quickSort(A, low, partitionNum - 1);
        quickSort(A, partitionNum + 1, high);
    }
}

// 选择排序

void selectSort(Element A[], int n) {
    int i, j, min;
    for(i = 0, i<n-1; i++) {
        min = i; //记录每一趟最小数的位置
        for(j = i+1; j<n; j++) {
            if(A[min] > A[j]) {
                min = j;
            }
            if(min != i) std::swap(A[min], A[i]);
        }
    }
    if()
}

