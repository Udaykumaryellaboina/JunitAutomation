# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:49:45 2024

@author: LENOVO
"""
from cryptography.fernet import Fernet
import re

# Generate a secret key (keep it safe!)
secret_key = Fernet.generate_key()
print("Secret Key:", secret_key)

# Initialize the Fernet instance with the secret key
fernet = Fernet(secret_key)

# Define Java keywords
java_keywords = [
    "abstract", "continue", "for", "new", "switch",
    "assert", "default", "goto", "package", "synchronized",
    "boolean", "do", "if", "private", "this",
    "break", "double", "implements", "protected", "throw",
    "byte", "else", "import", "public", "throws",
    "case", "enum", "instanceof", "return", "transient",
    "catch", "extends", "int", "short", "try",
    "char", "final", "interface", "static", "void",
    "class", "finally", "long", "strictfp", "volatile",
    "const", "float", "native", "super", "while",
    "import", "static", "final", "public", "private",
    "protected", "default", "synchronized", "volatile",
    "transient", "strictfp", "native", "abstract",
    "@Override", "@SuppressWarnings", "@Deprecated",
    "System.out.println", "System.out.print",
    "JFrame", "JPanel", "JButton", "JLabel", "JTextField",
    "JTextArea", "JScrollPane", "JComboBox", "JList",
    "JMenu", "JMenuBar", "JMenuItem", "JCheckBox",
    "JRadioButton", "JSlider", "JSpinner", "JTabbedPane",
    "JTable", "JTree", "JFileChooser", "JDialog",
    "JOptionPane", "ActionListener", "MouseListener",
    "MouseMotionListener", "KeyListener", "FocusListener",
    "WindowListener", "ComponentListener", "ContainerListener",
    "Runnable", "Thread", "Timer", "TimerTask","import javax.swing.*;","import java.lang.;", "import java.util.;", "import java.io.;", "import java.net.;",
    "import java.nio.;", "import java.nio.file.;", "import java.nio.channels.*;", 
    "import java.util.concurrent.;", "import java.util.function.;", "import java.util.stream.*;",
    "import java.math.;", "import java.text.;", "import java.util.regex.;", "import java.sql.;",
    "import javax.swing.;", "import javax.servlet.;", "import javax.xml.*;", 
    "import javax.persistence.;", "import org.springframework.;", "import org.apache.commons.*;","@Override", "@Deprecated", "@SuppressWarnings", "@SafeVarargs", "@FunctionalInterface",
    "@Entity", "@Table", "@Id", "@Column", "@GeneratedValue", "@Transient", "@Autowired",
    "@RequestMapping", "@PathVariable", "@RequestParam", "@Service", "@Component",
    "@Controller", "@RestController", "@Configuration", "@Bean", "@PostConstruct",
    "@PreDestroy", "@Transactional", "@Aspect", "@Pointcut", "@Before", "@After",
    "@Around", "@AfterReturning", "@AfterThrowing", "@Transactional","File", "FileInputStream", "FileOutputStream", "FileReader", "FileWriter",
    "BufferedReader", "BufferedWriter", "PrintWriter", "InputStream", "OutputStream",
    "Reader", "Writer", "PrintStream", "DataInputStream", "DataOutputStream",
    "ObjectInputStream", "ObjectOutputStream", "PipedInputStream", "PipedOutputStream",
    "PipedReader", "PipedWriter", "CharArrayReader", "CharArrayWriter", "StringReader",
    "StringWriter", "StreamTokenizer", "RandomAccessFile", "LineNumberReader"
]


# Define Java keywords and syntax
encrypted_words_dict = {}
def encrypt_java_code(java_code):
    encrypted_code = []
    for line in java_code.splitlines():
        words = re.findall(r'\b\w+\b', line)
        for word in words:
            if word not in java_keywords:
                encrypted_word = "".join(chr(ord(c) + 3) for c in word)
                encrypted_words_dict[word] = encrypted_words_dict.get(word, encrypted_word)
                line = line.replace(word, encrypted_word)
        encrypted_code.append(line)
    return "\n".join(encrypted_code)
