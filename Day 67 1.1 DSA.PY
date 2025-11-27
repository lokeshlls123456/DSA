import java.util.Scanner;

public class MagicalShoes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int[] A = new int[N];

        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
        }

        int count = 0;
        for (int i = 0; i < N; i++) {
            if (A[i] % 3 == 0) {
                count++;
            }
        }

        System.out.println(count);
    }
}