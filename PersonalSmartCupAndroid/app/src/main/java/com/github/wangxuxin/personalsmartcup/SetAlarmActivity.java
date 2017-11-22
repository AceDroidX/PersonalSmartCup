package com.github.wangxuxin.personalsmartcup;

import android.content.Context;
import android.content.Intent;
import android.media.AudioManager;
import android.media.MediaPlayer;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.*;
import android.os.Parcelable;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.util.Timer;
import java.util.TimerTask;

public class SetAlarmActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_set_alarm);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        final EditText minEdit = (EditText) findViewById(R.id.minEdit);
        final EditText secEdit = (EditText) findViewById(R.id.secEdit);
        Button setButton = (Button) findViewById(R.id.setButton);
        Button cancelButton = (Button) findViewById(R.id.cancelButton);
        setButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int time = Integer.parseInt(minEdit.getText().toString()) * 60 + Integer.parseInt(secEdit.getText().toString());
                timer.schedule(task, time*1000);
            }
        });
        cancelButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                timer.cancel();
                Intent intent = new Intent();
                //intent.putExtra("type",type+"/"+l);
                intent.setClass(getApplicationContext(), AlarmActivity.class);
                startActivity(intent);
            }
        });
//启动定时器
    }

    private final Handler handler = new Handler() {
        public void handleMessage(Message msg) {
            super.handleMessage(msg);
            if (msg.what == 1) {
                //todo something....
                Uri alert = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_ALARM);
                MediaPlayer player = new MediaPlayer();
                try {
                    player.setDataSource(getApplicationContext(), alert);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                final AudioManager audioManager = (AudioManager) getApplication().getSystemService(Context.AUDIO_SERVICE);
                if (audioManager.getStreamVolume(AudioManager.STREAM_ALARM) != 0) {
                    player.setAudioStreamType(AudioManager.STREAM_ALARM);
                    player.setLooping(false);
                    try {
                        player.prepare();
                    } catch (Exception e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                    player.start();
                }
            }
        }
    };


    private Timer timer = new Timer(true);

    //任务
    private TimerTask task = new TimerTask() {
        public void run() {
            Message msg = new Message();
            msg.what = 1;
            handler.sendMessage(msg);
        }
    };
}
