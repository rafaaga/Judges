import java.util.Scanner;

public class Mario {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            int t = sc.nextInt(), n, ar[], sub, baj;
            for (int i = 0; i < t; i++) {
                n = sc.nextInt();
                ar = new int[n];
                baj=sub=0;
                ar[0]= sc.nextInt();
                for (int j = 1; j < n; j++) {
                    ar[j]=sc.nextInt();
                    if (ar[j-1]>ar[j]) {
                        baj++;
                    }else if(ar[j-1]<ar[j]){
                        sub++;
                    }
                }
                System.out.println("Case "+(i+1)+": "+sub+" "+baj);
            }
        } catch (Exception e) {
        }
    }

}
