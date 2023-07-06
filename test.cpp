#include <iostream>
#include <vector>

using namespace std;

void changee(vector<int> a) {
    a[0] = 1;
}

int main() {
    vector<int> a{2,3,4};
    changee(a);
    std::cout << a[0] << std::endl;
    return 0;
}
