import java.util.*;

public class Main {

    
    public static int totalRevenue(int n) {
        if (n == 0) {
            return 0;  
        }
        return n + totalRevenue(n - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        System.out.println(totalRevenue(n));
    }
}