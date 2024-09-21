import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        try {
            float num, sum =0;
            int cont = 0;
                for (int i = 1; i <=6; i++) {
                    num = sc.nextFloat();
                    if (num>0) {
                        cont+=1;
                        sum +=num;
                    }
                }
                    System.out.println(cont+" valores positivos");
                    System.out.println(String.format("%.1f",sum/cont).replace(',', '.'));
        } catch (Exception e) {
        }
    }
    
}