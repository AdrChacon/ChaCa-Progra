package suma;
import java.util.Scanner;
public class Suma {
    public Suma(){
    }
    public void SumarValores(){
    int result = 0;
    int ValorIngresado = 0;
    Scanner entrada = new Scanner(System.in);
    boolean NoCero = true;
    while(NoCero){
        ValorIngresado = entrada.nextInt();
        result = result + ValorIngresado;
        if (ValorIngresado == 0){
                NoCero = false;
        }}
    System.out.println(result);
    }
    public static void main(String[] args) {
        Suma Valores = new Suma();
        System.out.println("Ingrese los valores que desea sumar.");
        System.out.println("Cuando quiera ver el resultado, ingrese 0.");
        Valores.SumarValores();
    }
    
}
