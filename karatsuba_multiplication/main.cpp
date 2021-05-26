#include <iostream>
#include <math.h>

using namespace std;

int digitsNum(int number);
int multiply(int num1, int num2);

int main() {
    int256_t x = 0, x_len = 0;
    int y = 0, y_len = 0;
    int a = 0, b = 0, c = 0, d = 0;

    cout << "Enter x" << endl;
    cin >> x;
    cout << "Enter y" << endl;
    cin >> y;
    cout << multiply(x, y) << endl;
    return 0;
}
/*
 * returns the number of digits of a number
 */
int digitsNum(int number)
{
    if (number==0) return 1;
    return log10(number) + 1;
}

/*
 * The core multiplication function take two number x and y and returns the multiplication recursevely
 */
int multiply(int x, int y)
{
    /*
     * x_len is x's number of digits, the same is for y
     * a is x's most significant part (MSP) and b is the least part
     * c is x's most significant part (MSP) and d is the least part
     * if either of the x or y is one digit then a or c respectively should be zero (see else if)
     *
     * Concept: x = 10^n/2 a + b   a is to the power of b's number of digits
     *          y = 10^n/2 c + d   c is to the power of d's number of digits
     *       so n should be b's number of digits + d's number of digits, see line 84
     * xy = 10^n ac + 10^n/2 (ad + bc) + bd
     * but, (a+b)(c+d) = ac + ad + bc + bd
     * then ad+bc = (a+b)(c+d) - ac - bd , see line 85
     */
    int x_len = 0, y_len = 0;
    int a = 0, b = 0, c = 0, d = 0;
    x_len = digitsNum(x);
    y_len = digitsNum(y);

    if(x_len==1 && y_len==1) return x*y;//base case
    else if(x_len==1)
    {
        int y_divider = (int) pow(10, y_len/2);
        a = 0;
        b = x;
        c = y / y_divider;
        d = y % y_divider;
    }
    else if(y_len==1)
    {
        int x_divider = (int) pow(10, x_len/2);
        a = x / x_divider;
        b = x % x_divider;
        c = 0;
        d = y;
    }
    else
    {
        int x_divider = (int) pow(10, x_len/2);
        int y_divider = (int) pow(10, y_len/2);
        a = x / x_divider;
        b = x % x_divider;
        c = y / y_divider;
        d = y % y_divider;
    }

    int ac = multiply(a, c);
    int bd = multiply(b, d);
    int ad_bc =  multiply(a+b, c+d) - ac - bd;

    int n = digitsNum(b) + digitsNum(d);
    return  pow(10, n) * ac + pow(10, (int)n/2) * ad_bc + bd;;

}