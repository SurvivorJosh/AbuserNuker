#include <iostream>
#include <math.h>
#include <thread>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <string.h>
#include <cstring>
#include <fstream>


using namespace std;
void getUsers() {
    ifstream input("Scrape/members.txt");
    ifstream guild("data/guild.txt");
    ifstream token("data/token.txt");
    string str;
    string gu;
    string to;
    while(!input.eof())
    {
        input>>str;
        guild>>gu;
        token>>to;

    }
}

int main()
{
    char op;
    cout << "MassBan[y]: ";
    cin >> op;

    if (op == 'y') {
        getUsers();
    }


    return 0;
}
