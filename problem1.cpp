#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    do
    {
        cin >> n;
    } while (n < 1 || n > 100);
    for (int i = 0; i < n; i++)
    {
        for(int j = 0; j <= i; j++)
            cout << "*";
        cout << endl;
    } 
    return 0;
}

