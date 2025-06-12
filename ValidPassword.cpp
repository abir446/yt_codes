#include<bits/stdc++.h>
using namespace std;


int isValidPassword(string str)
{
    if(str.size() < 4)
        return 0;
    if(isdigit(str[0]))
        return 0;

    int hasCapital = 0, hasDigit = 0;

    for (int i = 0; i < str.size(); i++)
    {
        if(str[i] == ' ' || str[i] == '/')
            return 0;
        if (isupper(str[i]))
            hasCapital++;
        if(isdigit(str[i]))
            hasDigit++;
    }

    if(hasDigit && hasCapital)
        return 1;
    else
        return 0;
}

int main() {
    string password;

  
    getline(cin, password);

    cout<<isValidPassword(password);

    return 0; 
}
