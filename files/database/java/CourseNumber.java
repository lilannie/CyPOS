package CyPos;

import java.io.File;
import java.sql.*;
import java.util.Scanner;

public class CourseNumber {
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
			
			File fCourses = new File("classNumber2.txt");
			Scanner scanCourses = new Scanner(fCourses);
			
			File fNumber= new File("classNumber-corrected.txt");
			Scanner scanNumber= new Scanner(fNumber);
			
			String sql = "";
			while(true){
				if(scanCourses.hasNextLine()){
					if(scanNumber.hasNextLine()){
						sql = "UPDATE db309grp17.base_courses SET number = '"+scanNumber.nextLine().trim()+"' WHERE acronym = '"
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
			scanNumber.close();
			System.out.println("Success");
		}catch (Exception e){
			System.out.println("Failure");
			System.out.println("SQLException: " + e.getMessage());
			System.out.println("SQLState: "+ e.getMessage());
		}finally {
			if (stmt != null) {
				stmt.close();
			}
		}
	}
}
