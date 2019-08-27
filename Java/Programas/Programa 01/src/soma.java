import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class soma extends JFrame{
    private JTextField textField1;
    private JTextField textField2;
    private JButton button1;
    private JPanel panel1;
    private JLabel label1;

    public soma(){
        add(panel1);
        setTitle("Soma");
        setSize(561, 124);

        button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                float a = Float.parseFloat(textField1.getText());
                float b = Float.parseFloat(textField2.getText());
                label1.setText(Float.toString(a+b));
                label1.setVisible(true);
            }
        });
    }
}
