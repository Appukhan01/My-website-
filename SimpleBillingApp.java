import java.util.Scanner;

// Billing System for HM Store
// Developer: Appu Khan

public class SimpleBillingApp {
    public static void main(String[] args) {
        System.out.println("--- HM STORE BILLING SYSTEM ---");
        System.out.println("1. Mobile - ₹15000");
        System.out.println("2. Charger - ₹500");
        System.out.println("-------------------------------");
        
        // Example Bill Calculation
        int mobilePrice = 15000;
        int chargerPrice = 500;
        
        // Customer bought 1 Mobile and 2 Chargers
        int total = mobilePrice + (chargerPrice * 2);
        
        System.out.println("Generating Bill...");
        System.out.println("Total Amount to Pay: ₹" + total);
        System.out.println("Thank you for visiting!");
    }
}

