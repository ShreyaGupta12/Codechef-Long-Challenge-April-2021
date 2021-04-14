#include <iostream>
using namespace std;

int main() {
    int t,n,k,c,i;
    cin>>t;
    while(t--){
        cin>>n>>k;
        char s[1000000];
        cin>>s;
        c=0;
        for(i=0;i<n;i++){
            if (s[i]=='*') c++;
            else c=0;
            if (c>=k) break;
            }
            if (c>=k) cout<<"YES"<<endl;
            else cout<<"NO"<<endl;}
	return 0;
}
