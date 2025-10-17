import java.util.Scanner;

public class solution
{
    public static void main(String[]args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] readings = new int[n];
        for (int i = 0; i < n; i++) {
            readings[i] = scanner.nextInt();
        }
        for (int i = n - 1; i >= 0; i--)
        {
            System.out.print(readings[i]);
            if (i != 0) 
            {
                System.out.print(" ");
            }
        }
    }
}