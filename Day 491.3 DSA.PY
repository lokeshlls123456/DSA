import java.util.*;

public class PostfixEvaluator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        
        String expression = sc.nextLine();
        sc.close();

        
        System.out.println(evaluatePostfix(expression));
    }

    
    public static int evaluatePostfix(String expr) {
        Stack<Integer> stack = new Stack<>();

        
        String[] tokens = expr.split("\\s+");

        for (String token : tokens) {
            if (isOperator(token)) {
                
                int b = stack.pop();
                int a = stack.pop();

                
                int result = applyOperator(a, b, token.charAt(0));
                stack.push(result);
            } else {
                
                stack.push(Integer.parseInt(token));
            }
        }

        
        return stack.pop();
    }

    
    private static boolean isOperator(String token) {
        return token.equals("+") || token.equals("-") || 
               token.equals("*") || token.equals("/");
    }

    
    private static int applyOperator(int a, int b, char operator) {
        switch (operator) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/': return a / b; 
            default: throw new IllegalArgumentException("Invalid operator: " + operator);
        }
    }
}