import java.util.Scanner;

public class AreaOfCircle {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("شعاع دایره را وارد کنید: ");
        double radius = input.nextDouble();

        double area = 3.14 * radius * radius;

        System.out.println("مساحت دایره = " + area);
    }
}




import java.util.Scanner;

public class PerimeterOfRectangle {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter length: ");
        double length = input.nextDouble();
        System.out.print("Enter width: ");
        double width = input.nextDouble();

        double perimeter = 2 * (length + width);
        System.out.println("Perimeter of Rectangle = " + perimeter);
    }
}

import java.util.Scanner;

public class SwapNumbers {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter first number: ");
        int a = input.nextInt();
        System.out.print("Enter second number: ");
        int b = input.nextInt();

         a=b;
         b=a;

        System.out.println("After swapping: a = " + a + ", b = " + b);
    }
}

import java.util.Scanner;

public class SimpleInterest {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter Principal: ");
        double p = input.nextDouble();
        System.out.print("Enter Rate of Interest: ");
        double r = input.nextDouble();
        System.out.print("Enter Time (in years): ");
        double t = input.nextDouble();

        double si = (p * r * t) / 100;
        System.out.println("Simple Interest = " + si);
    }
}

import java.util.Scanner;

public class EvenOdd {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = input.nextInt();

        if (num % 2 == 0)
            System.out.println(num + " is Even.");
        else
            System.out.println(num + " is Odd.");
    }
}

import java.util.Scanner;

public class SumNaturalNumbers {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter n: ");
        int n = input.nextInt();

        int sum = (n * (n + 1)) / 2; // formula
        System.out.println("Sum of first " + n + " natural numbers = " + sum);
    }
}

import java.util.Scanner;

public class CelsiusToFahrenheit {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter temperature in Celsius: ");
        double c = input.nextDouble();

        double f = (c * 9/5) + 32;
        System.out.println("Temperature in Fahrenheit = " + f);
    }
}


import java.util.Scanner;

public class MaxOfTwo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter first number: ");
        int a = input.nextInt();
        System.out.print("Enter second number: ");
        int b = input.nextInt();

        if (a > b)
            System.out.println("Maximum = " + a);
        else
            System.out.println("Maximum = " + b);
    }
}

import java.util.Scanner;

public class LeapYear {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a year: ");
        int year = input.nextInt();

        if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))
            System.out.println(year + " is a Leap Year.");
        else
            System.out.println(year + " is NOT a Leap Year.");
    }
}


import java.util.Scanner;

public class ReverseNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = input.nextInt();
        int rev = 0;

        while (num != 0) {
            int digit = num % 10;
            rev = rev * 10 + digit;
            num /= 10;
        }

        System.out.println("Reversed Number = " + rev);
    }
}
