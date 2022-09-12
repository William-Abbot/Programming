#include <Math.h>
#include <iostream>
#include <fstream>
#include <string>

#define PI 3.14159265f

using namespace std;

int main() 
{
        ofstream output;
        string outFileName = "sine.txt";
        output.open(outFileName.c_str());
        
        if(output.fail())
        {
                cout << "failed to open outputFile, terminating...\n";
		output.close();
                exit(EXIT_FAILURE);
        }
        
        float theta = 0.0;
        while (theta < 24*PI)
        {
                float result = sin(theta);
                theta = theta + (PI/8);
                cout << result << "\n";
                output << result << "\n";
        }
        output.close();
}