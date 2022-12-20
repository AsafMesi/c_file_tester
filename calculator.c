#include <stdio.h>

int main(void) {
  char operation;
  int num1, num2;


  while (1) {
      // Get the arithmetic operation
      printf("Enter the arithmetic operation (+, -, *) or enter 'E' to exit.\n");
      scanf(" %c", &operation);
      if (operation == 'E'){
          printf("Exiting\n");
          break;
      }

      // Get the operands
      printf("Enter the operands\n");
      scanf("%d %d", &num1, &num2);

      // Perform the requested operation
      switch (operation) {
          case '+':
              printf("%d + %d = %d\n", num1, num2, num1 + num2);
              break;
          case '-':
              printf("%d - %d = %d\n", num1, num2, num1 - num2);
              break;
          case '*':
              printf("%d * %d = %d\n", num1, num2, num1 * num2);
              break;
          default:
              printf("Invalid operator\n");
              break;
      }
  }

  return 0;
}
