import java.util.Scanner;

public class IdentifyingTea {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            int tea, intentos = 0;
            int vector[];
            while (sc.hasNextInt()) {
                vector = new int[5];
                tea = sc.nextInt();
                for (int j = 0; j < 5; j++) {
                    vector[j] = sc.nextInt();
                    if (tea == vector[j]) {
                        intentos++;
                    }
                }
                System.out.println(intentos);
                intentos = 0;
            }
        } catch (Exception e) {
        }
    }
}
