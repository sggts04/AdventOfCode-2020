#include <bits/stdc++.h>
using namespace std;

void solve() {
    map<long long, long long> a;
    long long n;
    while(cin>>n) {
        a[n]++;
    }
    for(auto p: a) {
        if(a[2020 - p.first] > 0) {
            cout<<p.first * (2020 - p.first);
            return;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    long long t=1;
    //cin>>t;
    while(t--) {
        solve();
    }
    return 0;
}