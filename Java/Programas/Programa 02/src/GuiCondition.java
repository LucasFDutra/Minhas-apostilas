import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GuiCondition extends JFrame{
    private JTextField textField1;
    private JTextField textField2;
    private JButton Button;
    private JLabel label1;
    private JPanel panel1;

    public GuiCondition(){
        add(panel1);
        setTitle("Teste de Condicionais");
        setSize(475, 113);

        Button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String a = textField1.getText();
                String b = textField2.getText();

                if (a.equals(b)){
                    label1.setText("'a' é igual à 'b'");
                }
                else{
                    label1.setText("'a' é diferente de 'b'");
                }
                label1.setVisible(true);
            }
        });
    }
}
