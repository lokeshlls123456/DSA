import java.util.*;

public class MaxDishPairSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        
        int n = sc.nextInt();
        int[] arr = new int[n];

        
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();


        if (n < 2) {
            System.out.println(0);
            return;
        }

        
        int firstMax = Integer.MIN_VALUE;
        int secondMax = Integer.MIN_VALUE;

        for (int num : arr) {
            if (num > firstMax) {
                secondMax = firstMax;
                firstMax = num;
            } else if (num > secondMax) {
                secondMax = num;
            }
        }

        
        System.out.println(firstMax + secondMax);
    }
}