package com.example.shubham.loginpi;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class DoorActivity extends AppCompatActivity {

    ImageButton imageButton;
    Button btnExit;
    EditText editText;
    boolean flag=true;
    Socket myAppSocket = null;
    public static String wifiModuleIp = "";
    public static int wifiModulePort = 12346;
    public static String  CMD = "0";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_door);

        imageButton = (ImageButton)findViewById(R.id.imageButton);
        btnExit = (Button)findViewById(R.id.btnExit);
        editText=(EditText)findViewById(R.id.editText);


        imageButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v)
            {
                if(flag)
                {
                    CMD="o";
                    flag=false;
                    getIPandPort();
                    imageButton.setImageResource(R.drawable.unlock3);
                    Soket_AsynTask t1 = new Soket_AsynTask();
                    t1.execute();
                }
                else
                {
                    CMD="f";
                    flag=true;
                    getIPandPort();
                    imageButton.setImageResource(R.drawable.lock3);
                    Soket_AsynTask t2  =new Soket_AsynTask();
                    t2.execute();
                }
            }

        });

        btnExit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v)
            {
                CMD = "e";
                getIPandPort();
                Intent intent = new Intent(DoorActivity.this,SecondActivity.class);
                startActivity(intent);
                Soket_AsynTask t = new Soket_AsynTask();
                t.execute();
                finish();
            }
        });

    }

    public void getIPandPort()
    {
        String iPandPort = editText.getText().toString();
        Log.d("MYTEST","IP String: "+iPandPort);
        String temp[]= iPandPort.split(":");
        wifiModuleIp = temp[0];
        wifiModulePort = Integer.valueOf(temp[1]);
        Log.d("MY TEST","IP: "+wifiModuleIp);
        Log.d("MY TEST","PORT: "+wifiModulePort);

    }
    public class Soket_AsynTask extends AsyncTask<Void,Void,Void>
    {
        Socket socket;

        @Override
        protected  Void doInBackground(Void... params)
        {
            try
            {
                getIPandPort();
                InetAddress inetAddress = InetAddress.getByName(SecondActivity.wifiModuleIp);
                socket = new java.net.Socket(inetAddress,wifiModulePort);
                DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
                dataOutputStream.writeBytes(CMD);
                dataOutputStream.close();
                socket.close();
            }
            catch (UnknownHostException e)
            {
                e.printStackTrace();
            }
            catch(IOException e)
            {
                e.printStackTrace();
            }
            return null;
        }
    }

}
