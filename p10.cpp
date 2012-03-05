/*The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 *
 * Find the sum of all the primes below two million.
 */
#include <stdlib.h>
#include <iostream>
#include <map>
using namespace std;


template<typename T = int, typename M = map<T, T> > class prime_iterator 
{
public:
  prime_iterator() : current(2), skips() { skips[4] = 2; }
  T operator*() { return current; }
  prime_iterator &operator++() {
    typename M::iterator i;
    while ((i = skips.find(++current)) != skips.end()) {
      T skip = i->second, next = current + skip;
      skips.erase(i);
      for (typename M::iterator j = skips.find(next);
	   j != skips.end(); j = skips.find(next += skip)) {}
      skips[next] = skip;
    }
    skips[current * current] = current;
    return *this;
  }
private:
  T current;
  M skips;
};

int main(int argc,char** argv)
{
  int sum=0;
  int bound=atoi(argv[1]);
  prime_iterator<int> primes;
  for(;*primes<bound;++primes){
    int val=*primes;
    cout<<val<<"~";
    sum+=*primes;
  }
  cout<<endl<<sum<<endl;
}
