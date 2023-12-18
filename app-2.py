import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd

st.markdown("<h1 style='text-align: center; '>CipherCraft</h1>", unsafe_allow_html=True)

# Add some custom CSS to adjust tab size and spacing
st.markdown(
    """
    <style>
        .st-bp {
            margin-right: 200px !important;
        }

        .stTabs {
            border-radius: 10px; /* Bords arrondis pour les onglets */
            margin: 10px 0; /* Marge autour des onglets */
        }

        .streamlit-tabs {
            margin-bottom: 20px;
        }

        .streamlit-tab-label {
            padding: 15px 20px;
            margin-right: 20px; /* Adjust the right margin between tabs */
        }

        .custom-button:hover {
            background-color: red !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Animation de Confirmation
def success_animation():
    st.success("Opération réussie! ✔️")

# Barre de Progression Visuelle
progress = st.progress(0.0)

# Function to display Vigenere table in Streamlit
def display_vigenere_table_streamlit(vigenere_table, string, keyword):
    vigenere_df = pd.DataFrame(vigenere_table)
    st.dataframe(vigenere_df)

# Then, when calling the function in your main code:
    display_vigenere_table_streamlit(vigenere_table, string, keyword)


    # Ajouter une classe CSS pour styliser la table
    st.markdown("""
        <style>
            .vigenere-table {
                border-collapse: collapse;
                width: 100%;
            }
            .vigenere-table th, .vigenere-table td {
                border: 1px solid black;
                padding: 8px;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # Afficher la table avec les colonnes et lignes mises en surbrillance
    st.table(vigenere_table.style.apply(lambda x: highlighted_column, axis=1).apply(lambda x: highlighted_row, axis=0).set_table_styles([{'selector': 'th', 'props': [('background-color', 'lightgray')]}]).set_precision(0))


# Function to plot Vigenere table using Plotly
def plot_vigenere_table_plotly(table, key):
    fig = make_subplots(rows=1, cols=1)

    fig.add_trace(
        go.Table(
            header=dict(values=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')),
            cells=dict(values=table.T)
        )
    )

    return fig

tab1, tab2, tab3 = st.tabs(["📚History","🌐Algorithm","🎮Game"])

with tab1:

    st.title("Vigenère Cipher History")

    st.header("Introduction")
    st.write("The Vigenère cipher is a polyalphabetic substitution cipher introduced by Blaise de Vigenère in the 16th century.")

    st.header("Background")
    st.subheader("Substitution Ciphers:")
    st.write("Substitution ciphers involve replacing each letter in the plaintext with another letter or symbol.")
    st.write("The Caesar cipher is a basic substitution cipher where each letter is shifted a fixed number of positions down the alphabet.")

    st.subheader("Polyalphabetic Substitution:")
    st.write("The Vigenère cipher is a polyalphabetic substitution cipher, using multiple substitution alphabets.")
    st.write("Unlike the Caesar cipher, it uses a keyword to determine the shift for each position in the text.")

    st.header("How It Works")
    st.subheader("Keyed Caesar Ciphers:")
    st.write("The Vigenère cipher is multiple Caesar ciphers in sequence, each with a different shift determined by the keyword.")

    st.subheader("Encrypting:")
    st.write("To encrypt a message, the sender selects a keyword and repeats it enough times to match the message's length.")
    st.write("Each letter in the message is shifted according to the corresponding letter in the keyword.")

    st.subheader("Decrypting:")
    st.write("To decrypt, the receiver uses the same keyword and shifts each letter in the opposite direction.")

    st.header("Historical Context")
    st.write("The Vigenère cipher is centuries old and was considered unbreakable for a long time.")
    st.write("It wasn't until the 19th century that cryptanalysts, such as Charles Babbage and Friedrich Kasiski, developed methods to break polyalphabetic ciphers like the Vigenère.")

    st.header("Cryptanalysis")
    st.write("The Vigenère cipher, while more secure than simple substitution ciphers, can still be broken.")
    st.write("The Kasiski examination and Friedman test are among the methods used for cryptanalysis.")

    st.write("Despite its vulnerability to modern cryptographic techniques, the Vigenère cipher remains an important historical cipher and a stepping stone in the development of more advanced cryptographic methods.")

with tab2 : 

    st.title("Vigenère Cipher Algorithm")

    st.header("Encryption:")
    st.subheader("Key Generation:")
    st.markdown("""
        1. Select a keyword, e.g., "KEY."
        2. Repeat the keyword to match the length of the plaintext.
           For example, if the plaintext is "HELLO," and the keyword is "KEY," repeat "KEY" to get "KEYKEY."
        3. The repeated keyword is the key used for encryption.
    """)

    st.subheader("Shifting:")
    st.markdown("""
        1. Assign numerical values to the letters (A=0, B=1, ..., Z=25).
        2. For each letter in the plaintext, find the corresponding letter in the key.
        3. Shift the plaintext letter by the numerical value of the key letter.
        Example: If the plaintext letter is "H" (numerical value 7) and the key letter is "K" (numerical value 10),
        the encrypted letter is (7 + 10) % 26 = 17, which corresponds to "R."
    """)

    st.subheader("Repeat:")
    st.markdown("""
        Continue this process for each letter in the plaintext.
    """)

    st.header("Decryption:")
    st.subheader("Key Generation:")
    st.markdown("""
        Use the same keyword used for encryption.
    """)

    st.subheader("Shifting:")
    st.markdown("""
        1. For each letter in the ciphertext, find the corresponding letter in the key.
        2. Shift the ciphertext letter backward by the numerical value of the key letter.
        Example: If the ciphertext letter is "R" (numerical value 17) and the key letter is "K" (numerical value 10),
        the decrypted letter is (17 - 10 + 26) % 26 = 7, which corresponds to "H."
    """)

    st.subheader("Repeat:")
    st.markdown("""
        Continue this process for each letter in the ciphertext.
    """)

    st.header("Example:")
    st.markdown("""
        **Plaintext:** "HELLO"
        
        **Keyword:** "KEY"
        
        **Key (repeated):** "KEYKEY"
        
        **Encryption:**
        - H + K = R
        - E + E = Q
        - L + Y = X
        - L + K = W
        - O + E = U
        
        **Ciphertext:** "RQXWU"
    """)

    st.subheader("Note:")
    st.markdown("""
        The Vigenère cipher is more secure than simple substitution ciphers like the Caesar cipher because the shift changes for each letter based on the keyword.
        However, it can still be vulnerable to cryptanalysis, especially if the keyword is short or if patterns exist in the plaintext.
        Methods like the Kasiski examination and Friedman test can be employed to break the Vigenère cipher.
    """)

with tab3:

    def generateKey(string, key):
        key = list(key)
        if len(string) == len(key):
            return(key)
        else:
            for i in range(len(string) - len(key)):
                key.append(key[i % len(key)])
        return("".join(key))

    def encryption(string, key):
        encrypt_text = []
        for i in range(len(string)):
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('A')
            encrypt_text.append(chr(x))
        return("".join(encrypt_text))

    def decryption(encrypt_text, key):
        orig_text = []
        for i in range(len(encrypt_text)):
            x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        return("".join(orig_text))

# Initialisez l'état de session pour stocker le texte dans le text_input et le mode du st.radio
if 'text_input_state' not in st.session_state:
    st.session_state.text_input_state = ""
if 'text_input_state_mode' not in st.session_state:
    st.session_state.text_input_state_mode = "🔒 Encryption"

st.title("Vigenere Cipher Game")

def generate_vigenere_table():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vigenere_table = np.array([list(alphabet)])
    for i in range(1, 26):
        row = np.roll(list(alphabet), i)
        vigenere_table = np.vstack([vigenere_table, row])
    return vigenere_table

def generateKey(string, key):
    key = list(key)
    expanded_key = ""
    for char in string:
        if char.isalpha():
            expanded_key += key[len(expanded_key) % len(key)]
        else:
            expanded_key += char
    return expanded_key


# Function to generate Vigenere table
def generate_vigenere_table():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vigenere_table = np.array([list(alphabet)])
    for i in range(1, 26):
        row = np.roll(list(alphabet), i)
        vigenere_table = np.vstack([vigenere_table, row])
    return vigenere_table

# Function to apply custom styles to Vigenere table
def custom_styles(value, text_upper, keyword_upper):
    styles_df = pd.DataFrame('', index=value.index, columns=value.columns)

    if text_upper in value.index:
        styles_df.loc[text_upper, :] = 'background-color: lightblue'

    if keyword_upper in value.columns:
        styles_df.loc[:, keyword_upper] = 'background-color: lightcoral'

    return styles_df

# Function to display Vigenere table
def display_vigenere_table_streamlit(vigenere_table, text, keyword):
    text_upper = text.upper()
    keyword_upper = keyword.upper()

    vigenere_df = pd.DataFrame(vigenere_table, columns=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    st.markdown("""
        <style>
            .vigenere-table {
                border-collapse: collapse;
                width: 100%;
            }
            .vigenere-table th, .vigenere-table td {
                border: 1px solid black;
                padding: 8px;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # Generate a DataFrame of styles
    styles_df = pd.DataFrame('', index=vigenere_df.index, columns=vigenere_df.columns)

    # Apply styles for the text column
    if text_upper in vigenere_df.index:
       styles_df.loc[text_upper, :] = 'background-color: lightblue'


    # Apply styles for the keyword row
    styles_df.loc[:, keyword_upper] = 'background-color: lightcoral'

    # Apply styles to the entire table
    styled_table = vigenere_df.style.applymap(lambda x: styles_df.get(x, '').get(x, ''), subset=pd.IndexSlice[vigenere_df.index, vigenere_df.columns])



    # Display the table
    st.dataframe(vigenere_df)


# User input
string = st.text_input("Enter the message:", key='text_input', value=st.session_state.text_input_state)
keyword = st.text_input("Enter the keyword:")

# Radio button for encryption and decryption
mode = st.radio("Choose mode:", ("🔒 Encryption", "🔓 Decryption", "🔍 Cryptanalysis"))

# Submit button
if st.button("Submit"):
    # Generate key, encrypt, and decrypt
    if string and keyword:
        key = generateKey(string, keyword)  # Utilisez generateKey au lieu de generate_key
        result_text = encryption(string, key)

        # Plot Vigenere table
        st.header("Vigenere Table:")
        vigenere_table = generate_vigenere_table()
        display_vigenere_table_streamlit(vigenere_table, string, keyword)

        # Display results
        st.header("Results:")
        st.write(f"Original message: {string}")
        st.write(f"Keyword: {keyword}")
        st.write(f"Generated Key: {key}")
        st.write(f"Encrypted message: {result_text}")

        # Update progress bar to 100%
        progress.progress(1.0)

# Update session state after processing inputs
st.session_state.text_input_state = string
st.session_state.text_input_state_mode = mode
