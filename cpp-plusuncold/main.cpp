#include <iostream>
#include <vector>
#include <cmath>
#include <sstream>
#include <limits>

#include "timer.h"

using namespace std;


bool isPrime(const unsigned long v) {
    if (v < 2) {
	return false;
    }
    if (v == 3) {
        return true;
    }
    if (v % 2 == 0) {
        return false;
    }
    if (v % 3 == 0) {
	return false;
    }

    unsigned long i = 5;
    while (i * i <= v) {
        if (v % i == 0 || v % (i + 2) == 0) {
	    return false;
        }
        i += 6;
    }
    return true;

    //for (unsigned long i = 2 ; i < v / 2 ; i++) {
    //if (i % (v / 100) == 0) cout << i << " ";
    //if (v % i == 0) return true;
    //}
    //return false;
}

int main() {

    unsigned long n0 = 0;
    unsigned long n1 = 1;
    unsigned long new_n;
    const unsigned long TARGET = 9000000000000000000;
    const unsigned int INT_MAX = numeric_limits<unsigned int>::max();
    vector<unsigned long> possibilities;
    int counter = 0;
    auto id = Timer::timerBegin();
    
    while (true) {
	counter++;
	new_n = n0 + n1;
	n0 = n1;
	n1 = new_n;

	if (n1 >= TARGET) {
	    break;
	}

	//cout << n1 << " ";
	possibilities.push_back(n1);

    }

    //auto time1 = Timer::timerEnd(id);
    //cout << "loops " << counter << " time " << time1 / 1000 << endl;
    //id = Timer::timerBegin();
    unsigned long val;
    
    // Check if value at satisfies square hex condition
    for (int i = possibilities.size() - 1 ; i >= 0 ; i--) {
	val = possibilities[i];
	if (!isPrime(val)) {
	    continue;
	}
	
	unsigned long value_squared = val * val;
	std::stringstream ss;
	ss << std::hex << value_squared;
	std::string res ( ss.str() );
	//std::cout << possibilities[i] << " " << value_squared << " " << res << " " << res.back() << "\n";
	if (res.back() == '9') {
	    auto time = Timer::timerEnd(id) / 1000;
	    std::cout << "plusuncold, C++, " << possibilities[i] << "," << time << ",\n";
	    exit(0);
	}
    }

    cout << endl; 
    return 0;
}
