import java.util.*;
class main{
  public static void main(String[] args) {
    System.out.println("Hello");
    order sandwich = new order("Sandwich",32);
    System.out.println("Your order was $"+sandwich.returnPrice());
    System.out.println("You ordered: "+sandwich.returnOrder());
  }
}
