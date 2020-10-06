nclude <iostream>
#include<fstream> 
using namespace std;
  


int main()
{ //How to determine if a number is prime or not
//with prime initally set as true.
  int num; int i; bool prime=true;int count=1;
  //The lines declare input and output of the file.
		ifstream infile;
		ofstream outfile;
		infile.open("num.txt");
		outfile.open("output.txt");
		outfile << "Name:Dominique Shepherd\n\n";
 
	//reads until the end of the file
  while(infile >> num)
  {  
    //prints the number its on and its factors
    outfile << "Number "<< count << ": " << num << "-Factors: ";
    //the loop here starts at 2 since 1 is neither a prime or composite and from there it keeps
    //going until its either determined as prime or not
    for(i=2; i<= num/2; i++)
    {
      if(num % i==0)// if the remainder is 0 prime becomes false and it prints out all the factors of a number
      {
        prime=false;
        outfile << " " <<i << ",";
      } 
    }
    outfile << '\n';
    if (prime)// this operates if prime stays true 
    {
      outfile << "Prime\n";
    }
      
    count++;//updates the counter to know what number were in
 }

  return 0;
}
