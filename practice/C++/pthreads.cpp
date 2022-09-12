#include <iostream>
#include <pthread.h>

using namespace std;

int average, minimum, maximum = 0;

int data[50];
int n = 0;

void *avg(void *arg)
{
    int i = 0, sum = 0;
    int *values;

    values = (int*)arg;

    for(i=0; i<n; i++)
    {
        sum = sum + values[i];
    }

    average = sum / (double)n;

    return NULL;
}

void *max(void *arg)
{
    int i = 0;
    int *values;

    values = (int*)arg;

    maximum = values[0];

    for(i=0; i<n; i++)
    {
        if(values[i] > maximum)
        {
            maximum = values[i];
        }
    }

    return NULL;
}

void *min(void *arg)
{
    int i = 0;
    int *values;

    values = (int*)arg;

    minimum = values[0];

    for(i=0; i<n; i++)
    {
        if(values[i] < minimum)
        {
            minimum = values[i];
        }
    }

    return NULL;
}


int main(void)
{
    pthread_t avg_thread, min_thread, max_thread;

	int x, counter = 0;
	cout << "enter number of items: ";
	cin >> n;
	cout << "";
	cout << "type in positive integers: ";
	while(counter < n)
	{
		cin >> x;
		data[counter] = x;
		counter += 1;
	}
	
    pthread_create(&avg_thread,NULL,avg, data);
    pthread_create(&min_thread,NULL,min, data);
    pthread_create(&max_thread,NULL,max, data);

    pthread_join(avg_thread,NULL);
    pthread_join(min_thread,NULL);
    pthread_join(max_thread,NULL);

    cout << "Average : " << average;
    cout << "\nMinimum : " << minimum;
    cout << "\nMaximum : " << maximum;
	cout << "\n";
	
	pthread_exit(NULL);

    return 0;
}
