package asd;

import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        Operaciones oper = new Operaciones();
        System.out.println("Menú");
        System.out.println("1- Sumar");
        System.out.println("2- Restar");
        System.out.println("3- Multiplicar");
        System.out.println("4- Dividir");
        Scanner entrada = new Scanner(System.in);
        int opcion = entrada.nextInt();
        System.out.println("Ingrese el valor 1:");
        int valor1 = entrada.nextInt();
        System.out.println("Ingrese el valor 2");
        int valor2 = entrada.nextInt();
        double resultado = 0;
        switch(opcion){
            case 1: 
                resultado = oper.suma(valor1, valor2);
                break;
            case 2:
                resultado = oper.resta(valor1, valor2);
                break;
            case 3:
                resultado = oper.multiplicacion(valor1, valor2);
                break;
            case 4:
                resultado = oper.division(valor1, valor2);
                break;
            default:
                System.out.println();
                   
        }
        System.out.println(resultado);
    }
}
