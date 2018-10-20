#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    /*
        do-while loop queries user for "Height" input between 0 and 23 inclusive.....
    */
    do
    {
       printf("Height: ");
       height = GetInt();
    }
    while (height > 23 || height < 0); 
   
   /*
        the "secret" is in the temporary variables "i and j" allowing for the "while" loops within the "for" loop....
        ....since the variables "i and j" are reset each use....they could technically be replaced by a single temp variable....
        ...finally, printing the first # before beginning the "Hash" loop solves the two hashes on top dilemma....
   */
       
    int h, i, j;
    
    for (h=0; h<height; h++)
    {
        j = h;
        while( height >= j + 2 )
        {
            printf(" ");
            j++;
        }
        i = h;
        printf("#");
        while( height + i >= height)
        {
            printf("#");
            i--;
        }
        printf("\n");
        
    }    
}