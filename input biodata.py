import sys 
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit,QFormLayout,QCheckBox,QRadioButton
 
def biodata():
    #inisialisasi pyqt
    app = QApplication(sys.argv)
    c = QWidget()
    
    #menyiapkan label, menempelkan label ke window
    #setText dan posisi
    label= QLabel()
    label.setStyleSheet("background-color: #A4C1DA; color:red; font-size: 25px; font:bold;")
    label.setText("Input biodata")
    
    #membuat dua kolom, kolom kiri berisi label dan kanan berisi inputan
    lab=QFormLayout()
    lab.addRow(label)
    
    #membuat kotak dengan menggunakan QLineEdit dimana kita dapat menginputkan suatu text dikotak label
    lab.addRow("Name",QLineEdit())
    lab.addRow("Address",QLineEdit())
    lab.addRow("",QLineEdit())
    
    #menggunakan QCheckBox untuk membuat ChexBox
    lab.addRow("Hobby",QCheckBox("makan"))
    lab.addRow("",QCheckBox("Tidur"))
    lab.addRow("",QCheckBox("Main"))
    
    #menggunakan QRadioButton untuk membuat RadioButton
    lab.addRow("Status",QRadioButton("pelajar"))
    lab.addRow("",QRadioButton("pegawai"))
    lab.addRow("",QRadioButton("Wiraswasta"))
    c.setLayout(lab)
    
    #menentukan ukuran window,title dan menampilkan
    c.setGeometry(50,50,500,400)
    c.setWindowTitle("PyQt5 ")
    c.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    biodata()
