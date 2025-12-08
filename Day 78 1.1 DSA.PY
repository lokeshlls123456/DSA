import java.util.*; 
class Node { 
     int data; 
     Node next; 
     Node(int x) { 
         data = x; 
         next = null; 
     } 
    } 
public class Main { 
    static Node head1 = null, temp1 = null; 
    static Node head2 = null, temp2 = null; 
    public static void ins1(int x) { 
     Node nn = new Node(x); 
     if (head1 == null) { 
         head1 = temp1 = nn; 
     } else { 
         temp1.next = nn; 
         temp1 = nn; 
     } 
    } 
    public static void ins2(int x) { 
     Node nn = new Node(x); 
     if (head2 == null) { 
         head2 = temp2 = nn; 
     } else { 
         temp2.next = nn; 
         temp2 = nn; 
     } 
    } 
    public static void dis() { 
     temp1 = head1; 
     int p = 0; 
     while (temp1 != null) { 
         p = p * 10 + temp1.data; 
         temp1 = temp1.next; 
     } 
     temp2 = head2; 
     int q = 0; 
     while (temp2 != null) { 
         q = q * 10 + temp2.data; 
         temp2 = temp2.next; 
     } 
     int sum = p + q; 
     if (sum == 0) { 
         System.out.print("0"); 
         return; 
     } 
     Node head = null, temp = null; 
     while (sum > 0) { 
         int d = sum % 10; 
         Node nn = new Node(d); 
         nn.next = head; 
         head = nn; 
         sum /= 10; 
     } 
     temp = head; 
     while (temp != null) { 
         System.out.print(temp.data + " "); 
         temp = temp.next; 
     } 
    } 
    public static void main(String[] args) { 
     Scanner in = new Scanner(System.in); 
     int n1 = in.nextInt(); 
     for (int i = 0; i < n1; i++) { 
         ins1(in.nextInt()); 
     } 
     int n2 = in.nextInt(); 
for (int i = 0; i < n2; i++) { 
ins2(in.nextInt()); 
} 
dis(); 
} 
}