import java.util.*;
class Main {
  public static void main(String[] args) {
    if(9 > 7){
    	System.out.println("Yay");
    }else{
    	System.out.println("Aww");
    }
    char something = (1 > 0) ? 'Y':'N';
    System.out.println(something);
    if(something == 'Y'){
    	System.out.println("Wohoo");
    }else{
    	System.out.println("Nope");
    }
    cat fluffy = new cat(5);
    fluffy.meow();
    System.out.println(fluffy.getAge());
    fluffy.status();
    for(int i = 0 ; i < 5; i++){
    	System.out.println("i is " + i);
    }
    ArrayList<Integer> temps = new ArrayList<Integer>();
    temps.add(54);
    temps.add(43);
    temps.add(25);
    System.out.println(temps);
	for(Integer temp:temps){
		System.out.println("It is "+temp+" today");
	}
    HashMap<String, Integer> prices = new HashMap<String, Integer>();
    prices.put("Computer", 679);
    prices.put("Phone",469);
    prices.put("4K TV",1099);
    System.out.println(prices);
    if(679 == prices.get("Computer")){
    	System.out.println("Yes");
    }else{
    	System.out.println("Awwn");
    }
    for(String item : prices.keySet()){
    	System.out.println("A new " + item + " costs $"+ prices.get(item));
    }
  }
}