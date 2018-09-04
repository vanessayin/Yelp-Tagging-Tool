#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

// Simply runs the bash command

int main() {
  system("python tagging.py");
  system("python research.py");
  return 0;
}
