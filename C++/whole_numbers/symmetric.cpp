#include <iostream>
int main()
{
    int number;
    bool ok = true;
    std::cin>>number;
    char text[4];
    std::sprintf(text,"%d",number);
    for (int i=0;i<4;i++)
    {
        if (text[i] != text[4-i-1])
        {
            ok = false;
        }
    }
    int result = (ok==true) ? 1: 37;
    std::cout << result <<'\n';
    return 0;

}