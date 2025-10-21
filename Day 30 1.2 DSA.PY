import java.util.*; 
public class Main { 
    static class Node { 
     int data; 
     Node next; 
     Node(int d) { data = d; } 
    } 
  
    static Node head, tail; 
  
    static void insert(int val) { 
     Node nn = new Node(val); 
     if (head == null) head = tail = nn; 
     else { tail.next = nn; tail = nn; } 
    } 
  
    static Node reverse(Node h) { 
     Node prev = null, curr = h; 
     while (curr != null) { 
         Node next = curr.next; 
         curr.next = prev; 
         prev = curr; 
         curr = next; 
     } 
     return prev; 
    } 
  
    static boolean isPalindrome(Node h) { 
     if (h == null || h.next == null) return true; 
     Node slow = h, fast = h; 
     while (fast != null && fast.next != null) { 
         slow = slow.next; fast = fast.next.next; 
     } 
     Node second = reverse(slow), first = h; 
     while (second != null) { 
         if (first.data != second.data) return false; 
         first = first.next; second = second.next; 
     } 
     return true; 
    } 
  
    public static void main(String[] args) { 
     Scanner sc = new Scanner(System.in); 
int n = sc.nextInt(); 
while (n-- > 0) insert(sc.nextInt()); 
System.out.println(isPalindrome(head) ? "Yes" : "No"); 
} 
}