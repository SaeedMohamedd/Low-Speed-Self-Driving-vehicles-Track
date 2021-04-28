#include<iostream>
#include"string.h"


int main(){

std::string s = "Saeed Mohamed Elsaid Bayome is publishing : 55";
std::string delimiter = ":";
size_t pos = 0;
std::string token;
while ((pos = s.find(delimiter)) != std::string::npos) {
    token = s.substr(0, pos);
    std::cout << token << std::endl;
    s.erase(0, pos + delimiter.length());
}
std::cout <<"the counter "<< s << std::endl;
    return 0;
}
