package CyPos;

import java.io.File;
import java.sql.*;
import java.util.Scanner;

public class Majors {
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
			
			File fMajors = new File("Majors.txt");
			Scanner scanMajors = new Scanner(fMajors);
			
			File fDepartments = new File("MajorsDepartments.txt");
			Scanner scanDepartments = new Scanner(fDepartments);
			
			String sql = "";
			while(true){
				if(scanMajors.hasNextLine()){
					if(scanDepartments.hasNextLine()){
						sql = "INSERT INTO db309grp17.base_majors (name, department_id) VALUES (\""+scanMajors.nextLine().trim()+
								"\", (SELECT id FROM db309grp17.base_departments WHERE acronym='"+scanDepartments.nextLine().trim()+
								"'));";
						stmt.executeUpdate(sql);
					}else {
						break;
					}
				}else {
					break;
				}
			}
			scanMajors.close();
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
