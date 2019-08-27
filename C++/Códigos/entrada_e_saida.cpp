#include <iostream>
using namespace std;
int main(){
  int a = 0;
  int b = 5;
  std::cout << "iniciando o loop while" << '\n';

  while (1) {
    std::cout << "Valor de a é: " << a <<'\n';
    a++;
    if (a==b){
      break;
    }
  }

  std::cout << "Iniciando o loop for" << '\n';
  a = 0;
  for(;;){
    std::cout << "Valor de a é: " << a << '\n';
    a++;
    if (a==b){
      break;
    }
  }
}
