#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int difference(int rows, int columns); //takes the input, adds it to a grid and outputs the difference between the total wins of justice leage and the total wins of the villains
void winner(int x); //prints the winner based on the difference between the the wins of justice leage and the wins of the villains
int main()
{
    int r, c;
    cin >> r >> c;
    if (r < 1 || c < 1 || r > 100 || c > 100) //checks if the numbers are accepted
        return 0;
    winner(difference(r, c)); //calls difference, and the output is returned to function winner
}

int difference(int rows, int columns)
{
    int power_grid[2][rows][columns]; //the first dimentions refers to the team where index 0 is for justice leage and index 1 is for the villains
    
    //taking the input
    for (int i = 0; i < 2; i++)
    {
        for(int j = 0; j < rows; j++)
        {
            for(int k = 0; k < columns; k++)
            {
                cin >> power_grid[i][j][k];
                if (power_grid[i][j][k] > pow (10,9) || power_grid[i][j][k] < 1) //checks if the power is accepted
                    return 0;
            }
        }
    }
    //calculating the difference
    int justice = 0, evil = 0;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if (power_grid[0][i][j] > power_grid[1][i][j])
                justice++;
            else if (power_grid[0][i][j] < power_grid[1][i][j])
                evil++;
        }
    }
    return justice - evil;
}

void winner(int x)
{
    if (x > 0)
        cout << "Justice League";
    else if (x < 0)
        cout << "Villains";
    else
        cout << "Tie";
}

