package com.github.wangxuxin.personalsmartcup;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.LinearLayout;
import lecho.lib.hellocharts.gesture.ZoomType;
import lecho.lib.hellocharts.model.Axis;
import lecho.lib.hellocharts.model.Line;
import lecho.lib.hellocharts.model.LineChartData;
import lecho.lib.hellocharts.model.PointValue;
import lecho.lib.hellocharts.view.LineChartView;

import java.util.ArrayList;

public class History2Activity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_history2);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        //if ("history".equals(type)) {
        LinearLayout llhistory = (LinearLayout) findViewById(R.id.llhistory);
        ArrayList<PointValue> values;
        ArrayList<Line> lines;
        LineChartView historyChart =(LineChartView)findViewById(R.id.history2Chart);
        values = new ArrayList<PointValue>();//折线上的点
        values.add(new PointValue(1,327));
        values.add(new PointValue(2,452));
        values.add(new PointValue(3,145));
        values.add(new PointValue(4,271));
            /*int i = 0;
            for (String str : cmd) {
                if (i == 0) {
                    i++;
                    continue;
                }
                String[] text = str.split(",");

                Log.d("wxxDebug", String.valueOf(Float.parseFloat(text[0])+Float.parseFloat(text[1])));
            }*/
        Line line = new Line(values).setColor(Color.BLUE);//声明线并设置颜色
        line.setCubic(true);//设置是平滑的还是直的
        lines = new ArrayList<Line>();
        lines.add(line);

        historyChart.setInteractive(true);//设置图表是可以交互的（拖拽，缩放等效果的前提）
        historyChart.setZoomType(ZoomType.HORIZONTAL_AND_VERTICAL);//设置缩放方向
        LineChartData data = new LineChartData();
        Axis axisX = new Axis();//x轴
        Axis axisY = new Axis();//y轴
        data.setAxisXBottom(axisX);
        data.setAxisYLeft(axisY);
        data.setLines(lines);
        historyChart.setLineChartData(data);//给图表设置数据

        FloatingActionButton fab2=(FloatingActionButton)findViewById(R.id.fab2);
        fab2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent();
                //intent.putExtra("type",type+"/"+l);
                intent.setClass(getApplicationContext(), HistoryActivity.class);
                startActivity(intent);
            }
        });
    }

}
