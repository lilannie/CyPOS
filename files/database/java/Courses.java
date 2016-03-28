package CyPos;

import java.io.File;
import java.sql.*;
import java.util.Scanner;

public class Courses {
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
			
			File fDepartments = new File("MajorsDepartments.txt");
			Scanner scanDepartments = new Scanner(fDepartments);
			int counter = 1;
			
			String sql = "";
			while(true){
				if(scanDepartments.hasNextLine()){
					sql = "UPDATE db309grp17.Courses SET db309grp17.Courses.departmentID = "+counter+" WHERE db309grp17.Courses.number "
							+ "LIKE '"+scanDepartments.nextLine()+"%'";
					stmt.executeUpdate(sql);
					counter++;
				}else {
					break;
				}
			}
			scanDepartments.close();
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


