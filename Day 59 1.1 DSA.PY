import java.util.Scanner;

public class FixUnbalancedParentheses {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        
        int T = sc.nextInt();
        sc.nextLine(); 

        while (T-- > 0) {
            String S = sc.nextLine();
            System.out.println(minAddToMakeValid(S));
        }

        sc.close();
    }

    
    public static int minAddToMakeValid(String s) {
        int balance = 0; 
        int additions = 0; 

        for (char c : s.toCharArray()) {
            if (c == '(') {
                balance++;
            } else {
                if (balance > 0) {
                    balance--; 
                } else {
                    additions++; 
                }
            }
        }

     
        return additions + balance;
    }
}