#include <iostream>
using namespace std;
typedef long long int ll;

ll min(ll a,ll b){
    if(a<b) return a;
    return b;
}
int main() {
	ll t;
	cin>>t;
	while(t--){
	    ll n,m,k;
	    cin>>n>>m>>k;
	    double matrix[n+1][m+1];
	    for(ll i=0;i<=n;i++){
	        for(ll j=0;j<=m;j++){
	        if(i==0 || j==0) matrix[i][j]=0;
	        else cin>>matrix[i][j];}
	    }
	for(ll i=0;i<=n;i++){
	    double pre=0;
	    for(ll j=0;j<=m;j++){
	        matrix[i][j]+=pre;
	        pre=matrix[i][j];
	    }
	}
	for(ll j=0;j<=m;j++){
	    double pre=0;
	    for(ll i=0;i<=n;i++){
	        matrix[i][j]+=pre;
	        pre= matrix[i][j];
	    }
	}
	ll zz=min(n,m);
	ll ans=0;
	for(ll len=1;len<=zz;len++){
	    for(ll i=len;i<=n;i++){
	        for(ll j=len;j<=m;j++){
	            if((matrix[i][j]+matrix[i-len][j-len]-matrix[i][j-len]-matrix[i-len][j])/(len*len)>=k) ans++;
	        }
	    }
	}
	cout<<ans<<endl;}
	return 0;
}
