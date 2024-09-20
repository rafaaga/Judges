import java.util.Scanner;

public class Celebrities {

    public static void main(String[] args) {
        Scanner lectura = new Scanner(System.in);
        try {
          String expression = "";
            while (!(expression = lectura.nextLine()).equals("")) {
                System.out.println(expression);
            }
        } catch (Exception e) {
        }
    }
}
