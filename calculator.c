#include <stdio.h>
#include <stdlib.h>

int main() {
    // Open Google in the default web browser
    system("xdg-open https://www.google.com");  // On Linux

    // For Windows, you can use:
    // system("start https://www.google.com");

    return 0;
}
