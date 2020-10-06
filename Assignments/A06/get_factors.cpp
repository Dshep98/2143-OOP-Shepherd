#include <iostream>
#include<fstream> 
using namespace std;
//Function: Prime number function
//input: it takes in a value to determine if its prime
//output: returns true for prime, false for not prime
bool prime(int num)
{
  int i;
  for(i=2; i< num; i++)
  {
    if(num % i==0)
    {
      return false;
    } 
  }
  return true;
}  


int main()
{ //How to determine if a number is prime or not
  int num; int i;int count=1;bool result;
  //The lines declare input and output of the file.
	ifstream infile;
	ofstream outfile;
	infile.open("num.txt");
	outfile.open("output.txt");
	outfile << "Name:Dominique Shepherd\n\n";
 //Reads in values from a file until the end of a line
  while(infile >> num)
  {  //result takes in the first integer to see if its prime or not.
    result=prime(num);
    if (result==true)// if result returns true it prints prime.
    {
      outfile << "Number "<< count << ": "<< "prime\n";
    }
    if(result==false)//if result returns false it prints the factors
    {
      outfile << "Number "<< count << ": " << num << "-Factors: ";
      for(i=2; i<= num/2; i++)//the loop starts at 2 since 1 is neither prime nor composite
      {
        if(num % i==0)//this runs if remainder of num divided by i equals zero.
        {
          outfile<< " " << i<< ",";// prints out the factors of number being read from file
        } 
      }
      outfile << "\n";
    }
    count++;//this just updates the number its on in the file
 }

  return 0;
}

