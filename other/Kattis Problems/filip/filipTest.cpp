#include<bits/stdc++.h>

using namespace std;


int reverseThree(string n);


int main() {

        string a;
        string b;
        cin >> a >> b;
        
        
        int x = reverseThree(a);
        int y = reverseThree(b);
        
        int result = std::max(x, y);
        
        cout << result << endl;
}

int reverseThree(string n) //reverses a 3-digit number
{
        int result = 0;
        int t = 1;
        for(int i=0;i<3;i++)
        {
                result = result + (n[i]-'0')*t;
                t*=10;
        }
	return result;
}