#include <stdio.h>

int is_bit_set(unsigned char value, int position) {
    return (value & (1 << position)) != 0;
}

unsigned char set_bit(unsigned char value, int position) {
    return value | (1 << position);
}

unsigned char clear_bit(unsigned char value, int position) {
    return value & ~(1 << position);
}

void print_bits(unsigned char value) {
    for (int i = 7; i >= 0; i--) {
        printf("%d", (value >> i) & 1);
    }
    printf("\n");
}

int main(void) {
    unsigned char value = 0b01001001;  // 0100 1001 (73)
    printf("Current value = ");
    print_bits(value);
	

    // 1. is_set_bit >> 비트가 1로 설정되어 있는지 확인
    if (is_bit_set(value, 3)) {
        printf("4th bit is set!\n");
    } else {
        printf("4th bit is not set.\n");
    }

    // 2. set_bit >> 설정되어 있지 않은 비트 켜기   
    value = set_bit(value, 2);
    printf("Value after being set:");
    print_bits(value);

    // 3. clear_bit >> 설정된 비트 끄기
    value = clear_bit(value, 6);
    printf("Value after being cleared:");
    print_bits(value);

    return 0;
}

