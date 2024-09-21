import java.util.Scanner;

public class HelloKitty{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            String palabra, resultado = null;
            int repeat;
            palabra = sc.next();
            while (!(palabra.equals("."))) {
                resultado = "";
                repeat = sc.nextInt();
                for (int i = 0; i < repeat; i++) {
                    resultado += palabra;
                }
                for (int i = 0; i < palabra.length(); i++) {
                System.out.println(resultado);
                    resultado = resultado.substring(1,resultado.length())+resultado.substring(0,1);
                }
                palabra = sc.next();
            }
        } catch (Exception e) {
        }
    }
}
