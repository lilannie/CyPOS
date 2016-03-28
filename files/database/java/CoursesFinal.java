package CyPos;

import java.io.File;
import java.sql.*;
import java.util.Scanner;

public class CoursesFinal {
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
			
			File fnumber = new File("classNumber-corrected.txt");
			Scanner scanNum = new Scanner(fnumber);
			
			File fname = new File("className.txt");
			Scanner scanName = new Scanner(fname);
			
			File fdes = new File("classDescription.txt");
			Scanner scanDes = new Scanner(fdes);
			
			File fcredits = new File("credits.txt");
			Scanner scanCredits = new Scanner(fcredits);
			
			File fdepart = new File("classDepartmentID.txt");
			Scanner scanDepart = new Scanner(fdepart);
			
			File facronym = new File("classAcronym.txt");
			Scanner scanAcronym = new Scanner(facronym);
			
			String sql = "";
			while(true){
				if(scanNum.hasNextLine()){
					if(scanName.hasNextLine()){
						if(scanDes.hasNextLine()){
							if(scanCredits.hasNextLine()){
								if(scanDepart.hasNextLine()){
									if(scanAcronym.hasNextLine()){
										sql = "INSERT INTO db309grp17.base_courses (number, name, "
												+ "numCredits, department_id, acronym) VALUES "
												+ "(\""+scanNum.nextLine().trim()+"\", \""+scanName.nextLine().trim()
												+"\", \""+scanCredits.nextLine().trim()
												+"\", \""+scanDepart.nextLine().trim()+"\", \""+scanAcronym.nextLine().trim()
												+"\")";
										stmt.executeUpdate(sql);
									}else {
										break;
									}
								}else {
									break;
								}
							}else {
								break;
							}
							
						}else {
							break;
						}
					}else {
						break;
					}
				}else {
					break;
				}
			}
			
			scanNum.close();
			scanName.close();
			scanDes.close();
			scanCredits.close();
			scanDepart.close();
			scanAcronym.close();
			
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

