class order{
  int price;
  String order;
  public order(String ordr, int pric){
    order = ordr;
    price = pric;
  }
  public String returnOrder(){
    return order;
  }
  public int returnPrice(){
    return price;
  }
  public static void main(String[] args) {
    System.out.println("You have made an order");
  }
}
