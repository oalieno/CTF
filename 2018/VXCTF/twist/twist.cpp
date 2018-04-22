#include <bits/stdc++.h>

using namespace std;

struct Random {
	mt19937_64 rng;
	uint64_t state;
	int count;
	Random(uint64_t seed) : rng(seed), state(0), count(0) {
		cout << "[*] Your key is: " << seed << endl;
	}
	uint64_t getNumber() {
		if (count == 0)
			state = rng();
		uint64_t res = state & (0xFF << (8 * (3 - count)));
		res >> (8 * (3 - count));
		count++;
		if (count > 3) count = 0;
		return res;
	}
};

int main(int argc, const char **argv) {
	if (argc < 2){
		cerr << "[*] Usage: " << argv[0] << " filename1 filename2 ..." << endl;
		return 1; 
	}
	random_device dev;
	Random stream(dev());
	for (int i = 1; i < argc; i++){
		string f(argv[i]);
		ifstream in(f, ios::binary);
		string s;
		char c;
		while (in.get(c)) {
			s += c;
		}
		valarray<uint64_t> plain(s.size());
		copy(s.begin(),s.end(),begin(plain));
		ofstream out(f + ".out", ios::binary);
		for (auto x : plain) {
			x ^= stream.getNumber();
			out.write(reinterpret_cast<const char*>(&x), sizeof x);
		}
	}
}
