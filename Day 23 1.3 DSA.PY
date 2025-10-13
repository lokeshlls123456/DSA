import java.util.*;

public class ConsecutiveMarks {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        
        int n = sc.nextInt();
        int[] arr = new int[n];

        
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();

        
        if (n == 1) {
            System.out.println(1);
            return;
        }

        
        Set<Integer> set = new HashSet<>();
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;

        for (int num : arr) {
            if (set.contains(num)) {
                System.out.println(0); 
                return;
            }
            set.add(num);
            min = Math.min(min, num);
            max = Math.max(max, num);
        }

        
        if (max - min + 1 == n) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}