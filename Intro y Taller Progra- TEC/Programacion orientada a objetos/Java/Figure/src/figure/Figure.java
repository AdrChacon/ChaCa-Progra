package figure;
import java.util.Scanner;
public class Figure {
    String triangulo = "";
    public Figure(){}
    public void Triangle(){
    Scanner entrada = new Scanner(System.in);
    int Height = entrada.nextInt();
    int[] Times = new int[Height];
    for(int valor : Times){
        triangulo = triangulo + "*";
        System.out.println(triangulo);}}
    public static void main(String[] args) {
        Figure Triangulo = new Figure();
        System.out.println("Ingrese la altura del triangulo");
        Triangulo.Triangle();}
    
}
