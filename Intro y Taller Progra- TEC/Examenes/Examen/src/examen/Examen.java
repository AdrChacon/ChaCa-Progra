
package examen;
import java.util.Scanner;

public class Examen {
    Scanner entrada = new Scanner(System.in);
    
    public Examen(){}
    
    public void contar(){
    System.out.println("Ingrese numero:");
    int num = entrada.nextInt();
    int result = num;
    int contador = 0;
    if (num == 0){System.out.println("0 tiene 1 digito");}
    else{
        while(result != 0){
            result = result / 10;
            contador = contador + 1;}
        System.out.println(num + " tiene " + contador + " digitos");
        }
    }
    
    public void crearLista(){
        System.out.println("Ingrese largo de array");
        int Largo = entrada.nextInt();
        int[] lista = new int[Largo];
        for(int i= 0; i < Largo; i++){
            lista[i] = entrada.nextInt();
        }
    }
    
    public void ordenar(){
        crearLista();
        int contador = 0;
        int[] listaresult = new int[Largo];
        for (int x = 0; x > Largo; x++){
            for(int y; y>Largo; y++){
                if(lista[x]>lista[y]){
                    contador = contador + 1;
                }
                else{}
            }
            listaresult[contador] = lista[x];
            contador = 0;
        }
        System.out.println("El resultado de ordenar" + lista + " es " + listaresult);
    }
    public static void main(String[] args) {
        Examen puntos = new Examen();
        puntos.contar();
        puntos.ordenar();
    }
    
}
