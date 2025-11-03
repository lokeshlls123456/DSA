import java.util.*;

public class RedundantBrackets {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        
        int N = sc.nextInt();
        sc.nextLine(); 

        while (N-- > 0) {
            String expr = sc.nextLine();
            if (hasRedundantBrackets(expr)) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }

        sc.close();
    }

    
    public static boolean hasRedundantBrackets(String expr) {
        Stack<Character> stack = new Stack<>();

        for (char ch : expr.toCharArray()) {
            if (ch == ')') {
                boolean operatorFound = false;

                
                while (!stack.isEmpty() && stack.peek() != '(') {
                    char top = stack.pop();
                    if (top == '+' || top == '-' || top == '*' || top == '/') {
                        operatorFound = true;
                    }
                }

                
                if (!stack.isEmpty()) {
                    stack.pop();
                }

                
                if (!operatorFound) {
                    return true;
                }
            } else {
                stack.push(ch);
            }
        }

        return false;
    }
}