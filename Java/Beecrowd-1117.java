import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        try {
                float cont = 0;
                int c = 0;
                for (int i = 0; i < 1000; i++) {
                float a = sc.nextFloat();
                    if (a<0.0 || a>10.0) {
                        System.out.println("nota invalida"); 
                    }else{
                    cont +=a;
                    c +=1;
                    if (c==2) {
                    System.out.println("media = "+String.format("%.2f", cont/2));
                        break;
                    }
                    }
                }
        } catch (Exception e) {
        }
    }
}

