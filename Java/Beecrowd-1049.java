import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            String vert, clas, diet;
            vert = sc.next();
            clas = sc.next();
            diet = sc.next();
            if ("vertebrado".equals(vert) && "ave".equals(clas) && "carnivoro".equals(diet) ) {
                System.out.println("aguia");
            }if ("vertebrado".equals(vert) && "ave".equals(clas) && "onivoro".equals(diet)) {
                System.out.println("pomba");
            }if ("vertebrado".equals(vert) && "mamifero".equals(clas) && "onivoro".equals(diet)) {
                System.out.println("homem");
            }if ("vertebrado".equals(vert) && "mamifero".equals(clas) && "herbivoro".equals(diet)) {
                System.out.println("vaca");
            }if ("invertebrado".equals(vert) && "inseto".equals(clas) && "hematofago".equals(diet)) {
                System.out.println("pulga");
            }if ("invertebrado".equals(vert) && "inseto".equals(clas) && "herbivoro".equals(diet)) {
                System.out.println("lagarta");
            }if ("invertebrado".equals(vert) && "anelideo".equals(clas) && "hematofago".equals(diet)) {
                System.out.println("sanguessuga");
            }if ("invertebrado".equals(vert) && "anelideo".equals(clas) && "onivoro".equals(diet)) {
                System.out.println("minhoca");
            }
        } catch (Exception e) {
        }
    }
    
}
