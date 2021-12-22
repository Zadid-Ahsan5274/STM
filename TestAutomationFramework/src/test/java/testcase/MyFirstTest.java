package testcase;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import io.github.bonigarcia.wdm.WebDriverManager;

public class MyFirstTest {

	public static void main(String[] args) {
		WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("https://classic.crmpro.com/");
        System.out.println("URL opened successfully");
        driver.findElement(By.name("username")).sendKeys("naveenk");
        driver.findElement(By.name("password")).sendKeys("test@123");
        driver.findElement(By.xpath("//input[@value='Login']")).click();
	}

}
