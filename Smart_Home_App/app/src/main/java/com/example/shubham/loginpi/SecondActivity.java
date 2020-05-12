package com.example.shubham.loginpi;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AlertDialog;
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
import java.net.SocketAddress;
import java.net.UnknownHostException;

public class SecondActivity extends AppCompatActivity {


    private Button btnExit;
    private Button btnPir;
    private Button btnLed;
    private Button btnFan;
    private Button curtain;
    private Button sled;
    private Button scurtain;

    static int flag=0;

    private EditText editText;
    private TextView textView;
    Socket myAppSocket = null;
    public static String wifiModuleIp = "";
    public static int wifiModulePort = 0;
    public static String  CMD = "0";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);


        btnExit= (Button)findViewById(R.id.btnExit);
        btnPir = (Button)findViewById(R.id.btnPir);
        btnLed= (Button)findViewById(R.id.btnLed);
        curtain= (Button)findViewById(R.id.curtain);
        btnFan= (Button)findViewById(R.id.btnFan);
        sled=(Button)findViewById(R.id.sled);
        scurtain=(Button)findViewById(R.id.scurtain);

        editText=(EditText)findViewById(R.id.editText);



        btnExit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                getIPandPort();
                CMD = "a";
                Soket_AsynTask cmd_exit_security_system = new Soket_AsynTask();
                cmd_exit_security_system.execute();
                final AlertDialog.Builder builder = new AlertDialog.Builder(SecondActivity.this);
                builder.setTitle("Exit");
                builder.setMessage("Do you want to exit ??");
                builder.setPositiveButton("Yes. Exit now!", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {
                        finish();
                    }
                });
                builder.setNegativeButton("Not now", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i)
                    {
                        dialogInterface.dismiss();
                    }
                });

                AlertDialog dialog = builder.create();
                dialog.show();
                finish();
            }
        });

        btnPir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(SecondActivity.this,PIR.class);
                startActivity(intent);
                getIPandPort();
                CMD = "p";
                Soket_AsynTask cmd_exit_security_system = new Soket_AsynTask();
                cmd_exit_security_system.execute();
            }
        });

        btnLed.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(SecondActivity.this,PIR.class);
                startActivity(intent);
                getIPandPort();
                CMD = "l";
                flag=1;
                Soket_AsynTask cmd_exit_security_system = new Soket_AsynTask();
                cmd_exit_security_system.execute();
            }
        });

        btnFan.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(SecondActivity.this,PIR.class);
                startActivity(intent);
                getIPandPort();
                CMD = "m";
                Soket_AsynTask cmd_exit_security_system = new Soket_AsynTask();
                cmd_exit_security_system.execute();
            }
        });

        curtain.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(SecondActivity.this,PIR.class);
                startActivity(intent);
                getIPandPort();
                CMD = "c";
                Soket_AsynTask curtain_security_system = new Soket_AsynTask();
                curtain_security_system.execute();
            }
        });

        scurtain.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(SecondActivity.this,DoorActivity.class);
                startActivity(intent);
                getIPandPort();
                CMD = "r";
                Soket_AsynTask scurtain_security_system = new Soket_AsynTask();
                scurtain_security_system.execute();
            }
        });

        sled.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(SecondActivity.this,PIR.class);
                startActivity(intent);
                getIPandPort();
                CMD = "q";
                Soket_AsynTask sled_security_system = new Soket_AsynTask();
                sled_security_system.execute();
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
