class cat extends Animal{ 
	int age;
	public cat(int ctage){
		age = ctage;
		// System.out.println("Hi");
	}
	public void meow() {
		System.out.println("Meow");
	}
	public int getAge() {
		return age;
	}
	public static void main(String[] args) {
		System.out.println("Hi");	
	}
}