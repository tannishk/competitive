

#include<bits/stdc++.h>
using namespace std;
int check(int a[],int n,int x)
{
    int l, r;
    /* Now fix the first element one by one and find the
       other two elements */
    for (int i = 0; i < n - 2; i++)
    {

        // To find the other two elements, start two index variables
        // from two corners of the array and move them toward each
        // other
        l = i + 1; // index of the first element in the remaining elements
        r = n-1; // index of the last element
        while (l < r)
        {
            if( a[i] + a[l] + a[r] == x)
            {
                return 1; //three numbers are found
            }
            else if (a[i] + a[l] + a[r] < x)
            {
                l++;
            }
            else 
            {
                r--;
            }
        }
    }

    
    return 0; // no three numbers are found

}
int main()
{

    int t;//testcases
    cin>>t;
    while(t--)
        {
            int n,x;//size of array n and the sum x
            cin>>n>>x;
            int a[n];
            for(int i=0;i<n;i++)
            {
                cin>>a[i]; //scanning the array elements
            }
            sort(a,a+n);  //sorting the array
            int ans=check(a,n,x); //call check function which return 1 if the there exist three 
                                //elements in A whose sum is exactly x, else 0.
            cout<<ans<<endl;
}
return 0;
}
