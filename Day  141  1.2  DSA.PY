import java.util.*;

public class Main {

    static class Activity {
        int start, end;

        Activity(int s, int e) {
            start = s;
            end = e;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        Activity[] activities = new Activity[n];

        for (int i = 0; i < n; i++) {
            int s = sc.nextInt();
            int e = sc.nextInt();
            activities[i] = new Activity(s, e);
        }

        
        Arrays.sort(activities, (a, b) -> a.end - b.end);

        int count = 0;
        int lastEnd = Integer.MIN_VALUE;

        
        for (Activity act : activities) {
            if (act.start >= lastEnd) {
                count++;
                lastEnd = act.end;
            }
        }

        System.out.println(count);

        sc.close();
    }
}