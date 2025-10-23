import java.util.*;

class TicketBookingSystem {
    private String[] queue;
    private int front, rear, size, capacity;

    public TicketBookingSystem(int capacity) {
        this.capacity = capacity;
        queue = new String[capacity];
        front = 0;
        rear = -1;
        size = 0;
    }

    public void enqueue(String customer) {
        if (size == capacity) {
            System.out.println("Queue is full. Cannot add " + customer);
            return;
        }
        rear = (rear + 1) % capacity;
        queue[rear] = customer;
        size++;
    }

    public void dequeue() {
        if (size == 0) {
            System.out.println("Served Customer: Queue is empty. No customer to serve.");
            return;
        }
        System.out.println("Served Customer: " + queue[front]);
        front = (front + 1) % capacity;
        size--;
    }

    public void display() {
        if (size == 0) {
            System.out.println("Queue is empty.");
            return;
        }
        System.out.print("Current Queue: ");
        for (int i = 0; i < size; i++) {
            System.out.print(queue[(front + i) % capacity] + " ");
        }
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int capacity = sc.nextInt();
        int operations = sc.nextInt();
        sc.nextLine();
        TicketBookingSystem system = new TicketBookingSystem(capacity);

        for (int i = 0; i < operations; i++) {
            String input = sc.nextLine();
            if (input.startsWith("ENQUEUE")) {
                String customer = input.split(" ")[1];
                system.enqueue(customer);
            } else if (input.equals("DEQUEUE")) {
                system.dequeue(); 
            } else if (input.equals("DISPLAY")) {
                system.display();
            }
        }
    }
}