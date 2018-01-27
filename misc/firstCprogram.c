int main(void) {
    /* variable definition: */
   int age;
   int birth;
   int current_year;
   printf("Type in your age: ");
   scanf("%d", &age);
   if(age <= 40){
       printf("You are young \n");
   }else{
       printf("You are old \n");
   }
   return 0;
}