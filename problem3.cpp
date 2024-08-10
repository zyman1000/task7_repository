#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int input();
int max(int* arr, int cn);
int main()
{
    const int cn = input();
    int heights[cn];
    for (int i = 0; i < cn; i++)
    {
        cin >> heights[i];
        if (heights[i] > pow(10, 9) || heights[i] < 0) //if the height is of invalid value, the program terminates
        {
            return 0;
        }
    }
    cout << max(heights, cn); //print the max height
}

int input()
{
    int n;
    do
    {
        cin >> n;
    }while(n < 1 || n > pow(10,5));
    return n;
}

int max(int* arr, int cn)
{
    int largest = 0; //assuming that the largest is the minimum possible value "0"
    for(int i = 0; i < cn; i++)
    {
        if(arr[i] > largest) //if an element is larger than the largest, it becomes the largest
            largest = arr[i];
    }
    return largest;
}
