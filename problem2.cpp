#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int input();
int search (int* arr,int key, int cn);

int main()
{
    int target;
    const int cn = input();
    int list[cn];
    for (int i = 0; i < cn; i++)
    {
        cin >> list[i];
        if (list[i] > pow(10, 9))
        {
            return -1; //program terminates if an entered element is greater than 10^9
        }
    }
    cin >> target;
    cout << search(list, target, cn);
}

int search (int* arr, int key, int cn)
{
    //linear search
   for(int i = 0; i < cn; i++)
   {
        if (arr[i] == key)
            return i;
   }
    //if function does not exit before the loop ends, then the key is not found
   return -1;
}

int input()
{
    int n;
    do
    {
        cin >> n;
    }while(n < 1 || n > 100000);
    return n;
}
