package sequence;
import java.util.Scanner;
public class Sequence {
    public Sequence(){
    }
    public void serie(){
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese numero");
        int Inicio = entrada.nextInt() + 1;
        System.out.println("Ingrese numero");
        int Final = entrada.nextInt();
        int result = 0;
        while(Inicio < Final){
            result = result + Inicio;
            Inicio = Inicio + 1;}
        System.out.println(result);
    }
    
    public static void main(String[] args) {
        Sequence Serie = new Sequence();
        System.out.println("Calculo de todos los numeros entre los valores ingresados");
        Serie.serie();
    }
    
}
