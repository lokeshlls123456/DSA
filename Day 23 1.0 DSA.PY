import java.util.*;

public class InsertProductID {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] productIds = new int[n];
        
        for (int i = 0; i < n; i++) {
            productIds[i] = sc.nextInt();
        }
    
        int newProductId = sc.nextInt();
        sc.close();

        int[] updated = new int[n + 1];
        boolean inserted = false;
        int j = 0;

        for (int i = 0; i < n; i++) {
            if (!inserted && newProductId <= productIds[i]) {
                updated[j++] = newProductId;
                inserted = true;
            }
            updated[j++] = productIds[i];
        }

        if (!inserted) {
            updated[j] = newProductId;
        }

        for (int i = 0; i < updated.length; i++) {
            System.out.print(updated[i] + (i == updated.length - 1 ? "" : " "));
        }
    }
}