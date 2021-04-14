#include <iostream>
using namespace std;

int main() {
	long long int t,n;
	cin>>t;
	while(t--){
	    cin>>n;
	    long long int x=n%4,y=n/4,a2=0,b3=0,c4=0,d5=0,e=0,f=0;
	    switch(x){
	        case 1: d5=1; break;
	        case 2: c4=2; break;
	        case 3: c4=2; b3=1; break;
	    }
	    if(y>0){
	        a2+=y*4;
	        f=(4-x)*4;
	    }
	    long long int sum=(a2*11)+(b3*15)+(c4*18)+(d5*20)+f;
	    cout<<sum<<endl;
	}
	return 0;
}
