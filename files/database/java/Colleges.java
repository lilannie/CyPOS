package CyPos;

import java.io.File;
import java.sql.*;
import java.util.Scanner;

public class Colleges {
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
			
			File fColleges = new File("colleges.txt");
			Scanner scanColleges = new Scanner(fColleges);
		
			
			String sql = "";
			while(true){
				if(scanColleges.hasNextLine()){
					sql = "INSERT INTO db309grp17.base_colleges (name) VALUES (\""
							+scanColleges.nextLine().trim()+"\");";
					stmt.executeUpdate(sql);
				}else {
					break;
				}
			}
			scanColleges.close();
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

