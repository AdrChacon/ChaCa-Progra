package multiples;
import java.util.Scanner;

public class Multiples {
    public Multiples(){
    }
    public void table(){
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese un numero");
        int Numero = entrada.nextInt();
        for (int valor = 1; valor < 11; valor++){
            System.out.println(Numero + "x" + valor + "=" + Numero*valor);
        }
    }
    
    public static void main(String[] args) {
        Multiples Tabla = new Multiples();
        Tabla.table();
    }
    
}
