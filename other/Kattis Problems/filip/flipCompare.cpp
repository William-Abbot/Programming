#include <stdio.h>      /* printf */
#include <math.h>       /* remainder */
#include <iostream>
using namespace std;


int reverseThree(int n);


int main ()
{
        string a;
        string b;
        cin >> a >> b;
        
        
        int x = reverseThree(stoi(a));
        int y = reverseThree(stoi(b));
        
        int result = std::max(x, y);
        
        cout << result << endl;
}

int reverseThree(int n) //reverses a 3-digit number
{
	int result = 1;
	for (int i =2; i > -1; i--){
		result += (n%10)*(pow(10, i));
		n /= 10;
	}
	return result;
}
