#include<iostream>
#include<cmath>
#include<chrono>
using namespace std ;


int main(){
/////// Q1.
/***********
int num ;
cout<<"enter your favorite number"<<endl;
cin>>num;
if(num == 24)
cout<<"Amazing !! thatis my favourite number too !"<<endl;
else
cout<<"No really!!"<<num<<" is my favorite number!"<<endl;
********/

/////Q2.
/*******************
int n, reverse=0, rem;    
cout<<"Enter an integer: ";    
cin>>n;    
  while(n!=0)    
  {    
     rem=n%10;
   //  cout<<rem<<endl;      
     reverse=reverse*10+rem;    
     n/=10;    
  }    
 cout<<"Reversed Number: "<<reverse<<endl;   

 */////////////////////


 /////////Q3.
 /************************
 int arr[5];
 int* ptr;
 ptr=arr ;
 cout<<"Enter elements:";
 for(int i=0;i<5;i++)
 {
     cin>>arr[i];
 }
 cout<<"You entered"<<endl;
  for(int i=0;i<5;i++)
 {

     cout<<ptr[i]<<endl;
 }

*/////////////////////


//Q4.


/***************************
 int size ;
 cout<<"Enter total number of elements(1 to 100):";
 cin>>size;
int arr[size];
 int larggest=0;
 for(int i=0;i<size;i++)
 {
      cout<<"Enter number "<<i<<": ";
       cin>>arr[i];
 }

  for(int i=0;i<size;i++)
 {

    if(larggest<arr[i])
    larggest=arr[i];
    
 }
 cout<<"Largest element = "<<larggest<<endl;
 *********************/

////Q5..

/*******************
 int size ;
 cout<<"Enter the number of data: ";
 cin>>size;
int arr[size];
 double average=0;
 int sum =0;
 for(int i=0;i<size;i++)
 {
      cout<<"Enter number : ";
       cin>>arr[i];
 }

  for(int i=0;i<size;i++)
 {

    sum+=arr[i];
    
 }
 average=sum/size;
 cout<<"Avrage = "<<average<<endl;
 ********************************************/

///////Q6...
/*********************
int a,b;
cout<<"enter first number : ";
cin>>a;
cout<<"enter second number : ";
cin>>b;
class Add{
    private:
    int num1,num2;
    public:
Add(int n1,int n2){
   num1=n1;
   num2=n2;
   cout<<"number initalized"<<endl;
   cout<<"the addition result on: "<<num1+num2<<endl;
}
};
Add add(a,b);
************************************/
///////Q7.

int a,b,c,d;
cout<<" first number : "<<endl;
cout<<"enter the real part: ";
cin>>a;
cout<<"Rnter the imaginary part: ";
cin>>b;
cout<<" second number : "<<endl;
cout<<"enter the real part: ";
cin>>c;
cout<<"Rnter the imaginary part: ";
cin>>d;
class Number{


public:
int real_part;
int img_part ;
Number(int r,int i){
    real_part=r;
    img_part=i;
}
int add_numbers_parts(int r1,int r2){
    return r1 +r2 ;
}
};
Number n1(a,b);
Number n2(c,d);

cout<<"the sum of the real parts is "<<n1.add_numbers_parts(n1.real_part,n2.real_part)<<endl;
cout<<"the sum of the imainary parts is "<<n1.add_numbers_parts(n1.img_part,n2.img_part)<<endl;
cout<<endl;
cout<<"the sum of the real parts is "<<n1.real_part+n2.real_part<<endl;
cout<<"the sum of the imainary parts is "<<n1.img_part+n2.img_part<<endl;

    return 0;
}
