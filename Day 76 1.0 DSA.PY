import java.util.*;

public class ManageTasks {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        
        int N = sc.nextInt();
        int[] tasks = new int[N];

        
        for (int i = 0; i < N; i++) {
            tasks[i] = sc.nextInt();
        }

        
        int M = sc.nextInt();
        sc.close();

        
        if (M >= N) {
            System.out.println("List is empty");
            return;
        }

        
        for (int i = 0; i < N - M; i++) {
            System.out.print(tasks[i] + (i == N - M - 1 ? "" : " "));
        }
    }
}