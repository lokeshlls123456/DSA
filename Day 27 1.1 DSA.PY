import java.util.Scanner;

public class PalindromeLinkedList {

  
    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
        }
    }

   
    static Node reverse(Node head) {
        Node prev = null;
        while (head != null) {
            Node nextNode = head.next;
            head.next = prev;
            prev = head;
            head = nextNode;
        }
        return prev;
    }

   
    static boolean isPalindrome(Node head) {
        if (head == null || head.next == null) {
            return true;
        }

        
        Node slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

       
        Node secondHalf = reverse(slow);

       
        Node firstHalf = head;
        Node temp = secondHalf; 

        while (temp != null) {
            if (firstHalf.data != temp.data) {
                return false;
            }
            firstHalf = firstHalf.next;
            temp = temp.next;
        }

        return true;
    }

   
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

      
        int n = sc.nextInt();

        
        Node head = null, tail = null;
        for (int i = 0; i < n; i++) {
            int value = sc.nextInt();
            Node newNode = new Node(value);
            if (head == null) {
                head = tail = newNode;
            } else {
                tail.next = newNode;
                tail = newNode;
            }
        }

     
        if (isPalindrome(head)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        sc.close();
    }
}