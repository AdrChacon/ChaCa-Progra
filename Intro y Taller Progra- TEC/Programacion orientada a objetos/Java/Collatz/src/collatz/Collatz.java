package collatz;
import java.util.Scanner;

public class Collatz {
    Scanner entrada = new Scanner(System.in);
    public Collatz(){
    }
    public void conjecture(){
        String sequence = "";
        System.out.println("Ingrese el valor de n");
        int Inicio = entrada.nextInt();
        System.out.println("n: " + Inicio);
        sequence = sequence + Inicio;
        while(Inicio != 1){
            if (Inicio%2 == 0){
                Inicio = Inicio / 2;
                sequence = sequence + " " + Inicio;
            }
            else{
                Inicio = Inicio * 3 + 1;
                sequence = sequence + " " + Inicio;
            }
        }
        System.out.println(sequence);
    }
    public void Imprimir(){
        System.out.println("Ingrese el valor de n");
        int Inicio = entrada.nextInt();
        String sequence = "";
        System.out.println("n: " + Inicio);
        for(int n = 0; n < Inicio; n++){
            sequence = sequence + "*";
        }
        System.out.println(Inicio +" "+ sequence);
        sequence = "";
        while(Inicio != 1){
            if (Inicio%2 == 0){
                Inicio = Inicio / 2;
                for(int n = 0; n < Inicio; n++){
                    sequence = sequence + "*";
                }
                System.out.println(Inicio +" "+ sequence);
                sequence = "";
            }
            else{
                Inicio = Inicio * 3 + 1;
                for(int n = 0; n < Inicio; n++){
                    sequence = sequence + "*";
                }
                System.out.println(Inicio +" "+ sequence);
                sequence = "";
            }
        }
    }
    
    public static void main(String[] args) {
        Collatz serie = new Collatz();
        serie.conjecture();
        serie.Imprimir();
    }
    
}
