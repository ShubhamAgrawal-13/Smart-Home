package com.example.shubham.loginpi;

import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.os.AsyncTask;
import android.support.constraint.ConstraintLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class PIR extends AppCompatActivity {

    private Button pirOn;
    private Button pirOff;
    private Button backPir;
    private EditText editText;
    private TextView textView;
    ConstraintLayout layout;


    Socket myAppSocket = null;
    public static String wifiModuleIp = "";
    public static int wifiModulePort = 0;
    public static String  CMD = "0";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pir);

        pirOn = (Button)findViewById(R.id.pirOn);
        pirOff = (Button)findViewById(R.id.pirOFF);
        backPir = (Button)findViewById(R.id.backPir);
        textView=(TextView)findViewById(R.id.textViewCon);
        editText=(EditText)findViewById(R.id.editText1);
        layout=(ConstraintLayout)findViewById(R.id.BK);

        if(SecondActivity.flag==1)
        {
            layout.setBackground(Drawable.createFromPath("res/off.png"));
        }

        pirOn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                getIPandPort();
                CMD = "o";
                if(SecondActivity.flag==1)
                {
                        layout.setBackground(Drawable.createFromPath("res/onn.png"));
                }
                Soket_AsynTask cmd_on_security_system = new Soket_AsynTask();
                cmd_on_security_system.execute();
            }
        });

        pirOff.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                getIPandPort();
                CMD = "f";
                if(SecondActivity.flag==1)
                {
                    layout.setBackground(Drawable.createFromPath("res/off.png"));
                }
                Soket_AsynTask cmd_off_security_system = new Soket_AsynTask();
                cmd_off_security_system.execute();
            }
        });

        backPir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(PIR.this,SecondActivity.class);
                startActivity(intent);
                getIPandPort();
                SecondActivity.flag=0;
                CMD = "e";
                PIR.Soket_AsynTask cmd_off_security_system = new PIR.Soket_AsynTask();
                cmd_off_security_system.execute();
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
                InetAddress inetAddress = InetAddress.getByName(SecondActivity.wifiModuleIp);
                socket = new java.net.Socket(inetAddress,SecondActivity.wifiModulePort);
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
