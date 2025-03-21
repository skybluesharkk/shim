#include <stdio.h>
#define MAX_NUMBER 10000

int sum(int n)          //셀프넘버가 아닌 수를 구하는 함수
{
    int sum = n;

    while(n>0)
    {
        sum += n%10;
        n/=10;
    }
    return sum;
}
int main(void)
{
    int arr[MAX_NUMBER+1], i, check;

    for(i=1; i<MAX_NUMBER+1; i++)
    {
        check = sum(i);
        if(check <MAX_NUMBER+1)       //셀프 넘버가 아닌 수 확인
            arr[check]=1;
    }

    for(i=1; i<MAX_NUMBER+1; i++)
    {
        if(arr[i]!=1)          //셀프 넘버 수 확인
            printf("%d\n", i);
    }
    return 0;
}