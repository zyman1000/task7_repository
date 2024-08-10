#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;
int main() {
    string name;
    int i = 0;
    getline(cin, name);
    for(char test : name)
    {
        if (test != '\0')
            i++;
    }
    if(i <= 100 && i > 0)
        cout << "Hello, " << name << "!" << endl;
    return 0;
}
