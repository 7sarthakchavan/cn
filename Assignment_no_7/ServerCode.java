import java.io.*;
import java.net.*;

public class ServerCode
{
ServerSocket ss;
Socket socket;
BufferedReader sock_in,kdb_in;
PrintWriter sock_out;
String str;
    public ServerCode()
    {
    try{
        ss=new ServerSocket(8080);
        System.out.println("Server is listening port 8080");
        socket=ss.accept();
        System.out.println("Connection established...");
        kdb_in=new BufferedReader(new InputStreamReader(System.in));
        sock_in=new BufferedReader(new InputStreamReader(socket.getInputStream()));
        sock_out=new PrintWriter(socket.getOutputStream());
        while(true)
        {
        System.out.println("Msg from client");
        str=sock_in.readLine();

        System.out.println(str);
   
        System.out.println("Enter the msg");
        str=kdb_in.readLine();
        sock_out.println(str);
        sock_out.flush();
        if(str.equals("bye"))
        break;
        }
    }catch (Exception e) { }
    }
public static void main(String arg[])
{
    new ServerCode();
}
}