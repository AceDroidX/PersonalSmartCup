package com.github.wangxuxin.personalsmartcup;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView stateText=(TextView)findViewById(R.id.stateText);
        final TCPSocket MainSocket = new TCPSocket(MainActivity.this,"main");
        if(MainSocket.isConnected()){
            stateText.setText("已连接");
        }else {
            stateText.setText("未连接");
        }


        Button historyButton = (Button)findViewById(R.id.historyButton);
        historyButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(MainSocket.isConnected()){
                    Intent intent = new Intent();
                    //intent.putExtra("type",type+"/"+l);
                    intent.setClass(getApplicationContext(), HistoryActivity.class);
                    startActivity(intent);
                }else {
                    Toast.makeText(getApplicationContext(), "未连接！",
                            Toast.LENGTH_LONG).show();
                }
            }
        });

        Button aboutButton = (Button) findViewById(R.id.aboutMain);
        aboutButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent();
                //intent.putExtra("type",type+"/"+l);
                intent.setClass(MainActivity.this, AboutActivity.class);
                startActivity(intent);
            }
        });
    }
}
