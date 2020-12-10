#include <bits/stdc++.h>
using namespace std;

void solve() {
    map<long long, long long> a;
    long long n;
    while(cin>>n) {
        a[n]++;
    }
    for(auto k: a) {
        if(k.second == 0) continue;
        long long s = 2020 - k.first;
        for(auto p: a) {
            if(p.second == 0) continue;
            if(a[s - p.first] > 0) {
                cout<<p.first*(s - p.first)*k.first<<endl;
            }
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