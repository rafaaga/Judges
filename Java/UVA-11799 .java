import java.util.Arrays;
import java.util.Scanner;

public class HorrorDash{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int vector[];
        int tamano;
        try {
            int caso = sc.nextInt();
            for (int j = 0; j < caso; j++) {
                tamano = sc.nextInt();
                vector = new int[tamano];
                for (int i = 0; i < tamano; i++) {
                    vector[i] = sc.nextInt();
                }
                Arrays.sort(vector);
                System.out.println("Case "+(j+1)+": "+vector[tamano - 1]);
            }
        } catch (Exception e) {
        }
    }
}
