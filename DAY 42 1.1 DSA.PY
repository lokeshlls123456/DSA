import java.util.*;

public class TwoStacks {
    static class DualStack {
        int[] arr;
        int size;
        int top1, top2;

        public DualStack(int n) {
            size = n;
            arr = new int[n];
            top1 = -1;
            top2 = n;
        }

        public void push1(int x) {
            if (top1 < top2 - 1) {
                arr[++top1] = x;
            }
        }

        public void push2(int x) {
            if (top1 < top2 - 1) {
                arr[--top2] = x;
            }
        }

        public void pop1() {
            if (top1 >= 0) {
                System.out.println(arr[top1--]);
            }
        }

        public void pop2() {
            if (top2 < size) {
                System.out.println(arr[top2++]);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        DualStack stack = new DualStack(n);

        while (true) {
            int cmd = sc.nextInt();
            if (cmd == -1) break;

            switch (cmd) {
                case 1: 
                    int x1 = sc.nextInt();
                    stack.push1(x1);
                    break;
                case 2: 
                    int x2 = sc.nextInt();
                    stack.push2(x2);
                    break;
                case 3: 
                    stack.pop1();
                    break;
                case 4: 
                    stack.pop2();
                    break;
            }
        }
    }
}