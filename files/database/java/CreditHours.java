package CyPos;

import java.io.File;
import java.sql.*;
import java.util.Scanner;

public class CreditHours {
	public static void main(String[] args) throws SQLException {
		Connection connect = null;
		Statement stmt = null;
		try{
			Class.forName("com.mysql.jdbc.Driver");
			String username = "dbu309grp17";
			String password = "AugtUmP22JP";
			String dbServer = "jdbc:mysql://mysql.cs.iastate.edu";
			connect = DriverManager.getConnection(dbServer, username, password);
			stmt = connect.createStatement();
			
			File fCourses = new File("classNumber.txt");
			Scanner scanCourses = new Scanner(fCourses);
			
			File fCredits = new File("credits.txt");
			Scanner scanCredits = new Scanner(fCredits);
			
			String sql = "";
			
			
			while(true){
				if(scanCourses.hasNextLine()){
					if(scanCredits.hasNextLine()){
						sql = "UPDATE db309grp17.courses_courses SET numCredits = '"+scanCredits.nextLine().trim()+"' WHERE number = '"
								+scanCourses.nextLine().trim()+"';";
						stmt.executeUpdate(sql);
					}else {
						break;
					}
				}else {
					break;
				}
			}
			
			scanCourses.close();
			scanCredits.close();
			
			
			
		}catch (Exception e){
			System.out.println("Failure");
			System.out.println("SQLException: " + e.getMessage());
			System.out.println("SQLState: "+ e.getMessage());
		}finally {
			System.out.println("Success");
			if (stmt != null) {
				stmt.close();
			}
		}
	}
}
