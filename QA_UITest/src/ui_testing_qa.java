import java.util.ArrayList;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.edge.EdgeOptions;


public class ui_testing_qa {

	public static void main(String[] args) {
//		set the webdriver prop
		System.setProperty("webdriver.edge.driver", "D:\\Selenium\\edgedriver_win64\\msedgedriver.exe");
		
        WebDriver driver = new EdgeDriver();
		driver.manage().window().maximize();

		driver.get("http://127.0.0.1:5000/wordsearch");
		
//		get title from the form page
//		test on the title (interface)
		String at2 = driver.getTitle();
		System.out.println("Actual Title : " + at2);
		String et2 = "Matrix Form";
		System.out.println("Expected Title : " + et2);
		if(at2.equalsIgnoreCase(et2)) {
			System.out.println("Expected Title Match with Actual Title\n\n");
		}
		else {
			System.out.println("Expected Title Not Match with Actual Title\n\n");
		};
		
//		input on the form
		driver.findElement(By.name("matrix[0][0]")).sendKeys("A");
		driver.findElement(By.name("matrix[0][1]")).sendKeys("D");
		driver.findElement(By.name("matrix[0][2]")).sendKeys("A");
		driver.findElement(By.name("matrix[0][3]")).sendKeys("H");
		
		driver.findElement(By.name("matrix[1][0]")).sendKeys("E");
		driver.findElement(By.name("matrix[1][1]")).sendKeys("C");
		driver.findElement(By.name("matrix[1][2]")).sendKeys("A");
		driver.findElement(By.name("matrix[1][3]")).sendKeys("A");
		
		driver.findElement(By.name("matrix[2][0]")).sendKeys("B");
		driver.findElement(By.name("matrix[2][1]")).sendKeys("K");
		driver.findElement(By.name("matrix[2][2]")).sendKeys("Z");
		driver.findElement(By.name("matrix[2][3]")).sendKeys("U");
		
		driver.findElement(By.name("word")).sendKeys("CCG", Keys.ENTER);
		
		WebElement t = driver.findElement(By.xpath("//*[@id='matrix_table']/tbody"));
        // count rows with size() method
        List<WebElement> rws = t.findElements(By.tagName("tr"));
        int rws_cnt = rws.size();
        //iterate rows of table
        for (int i = 0;i < rws_cnt; i++) {
        // count columns with size() method
        List<WebElement> cols = rws.get(i).findElements(By.tagName("td"));
        int cols_cnt = cols.size();
        //iterate cols of table
        	for (int j = 0;j < cols_cnt; j++) {
        // get cell text with getText()
        String c = cols.get(j).getText();
        	System.out.println("The cell value is: " + c);
        	}
        }
        
//        check the input value
        String[][] expectedMatrix = {{"A", "D", "A", "H"}, {"E", "C", "A", "A"}, {"B", "K", "Z", "U"}};
     // Retrieve the contents of the table
        WebElement table = driver.findElement(By.xpath("//*[@id='matrix_table']/tbody"));
        List<WebElement> rows = table.findElements(By.tagName("tr"));

        // Check that the contents of the table match the expected values
        for (int i = 0; i < rows.size(); i++) {
            List<WebElement> cols = rows.get(i).findElements(By.tagName("td"));
            for (int j = 0; j < cols.size(); j++) {
                String actualValue = cols.get(j).getText();
                String expectedValue = expectedMatrix[i][j];
                if (!actualValue.equals(expectedValue)) {
                    System.out.println("Error: actual value " + actualValue + " does not match expected value " + expectedValue);
                }
                
                else {
                	System.out.println("letter in matrix ["+i+"]["+j+"] are the exact same as the input");
                }
            }
        }

//		check the title on result page
//		test on the title (interface)
		String at = driver.getTitle();
		System.out.println("\n\nActual Title : " + at);
		String et = "Matrix Result";
		System.out.println("Expected Title : " + et);
		if(at.equalsIgnoreCase(et)) {
			System.out.println("Expected Title Match with Actual Title");
		}
		else {
			System.out.println("Expected Title Not Match with Actual Title");
		}
		
//		check on the output on the result page
		String at1 = driver.findElement(By.id("keyword")).getText();
		System.out.println(at1);
		System.out.println("\n\nActual text : " + at1);
		String et1 = "Keyword : CCG";
		System.out.println("Expected text : " + et1);
		if(at1.equalsIgnoreCase(et1)) {
			System.out.println("Expected Keyword Match with Actual Title");
		}
		else {
			System.out.println("Expected Keyword Not Match with Actual Title");
		}
		
		
		driver.close();
	}

}
