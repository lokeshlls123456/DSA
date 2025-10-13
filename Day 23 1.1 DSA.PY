import java.util.*;

public class SecondLargestCount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();

        if (n == 1) {
            System.out.println(0);
            return;
        }

        int largest = arr[0];
        for (int num : arr) {
            if (num > largest) largest = num;
        }

        int secondLargest = Integer.MIN_VALUE;
        for (int num : arr) {
            if (num < largest && num > secondLargest) {
                secondLargest = num;
            }
        }

        if (secondLargest == Integer.MIN_VALUE) {
            System.out.println(0);
            return;
        }

        int count = 0;
        for (int num : arr) {
            if (num == secondLargest) count++;
        }

        System.out.println(count);
    }
}