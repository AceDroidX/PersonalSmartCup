package com.github.wangxuxin.personalsmartcup;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

/**
 * A login screen that offers login via email/password.
 */
public class LoginActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        //------------------------------------------------------------------
        //------------------------------------------------------------------
        //------------------------------------------------------------------
        SharedPreferences locklistSP = getSharedPreferences("lock", 0);
        final String lockip = locklistSP.getString("ip", null);

        final EditText ipEdit = (EditText) findViewById(R.id.ipEdit);

        if (!(lockip == null)) {
            ipEdit.setText(lockip);
        }
        //------------------------------------------------------------------
        //------------------------------------------------------------------
        //------------------------------------------------------------------

        Button addButton = (Button) findViewById(R.id.addButton);
        Button aboutButton = (Button) findViewById(R.id.aboutButton);
        addButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if ("".equals(ipEdit.getText().toString())) {
                    Toast.makeText(getApplicationContext(), "IP地址不能为空",
                            Toast.LENGTH_LONG).show();
                    return;
                }

                final TCPSocket password = new TCPSocket(LoginActivity.this);
                password.connect(ipEdit.getText().toString(), 23333, "verify", 5000);
            }
        });

        //------------------------------------------------------------------
        //------------------------------------------------------------------
        //------------------------------------------------------------------
        aboutButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent();
                //intent.putExtra("type",type+"/"+l);
                intent.setClass(LoginActivity.this, AboutActivity.class);
                startActivity(intent);
            }
        });
    }
}

