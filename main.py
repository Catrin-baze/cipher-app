import streamlit as st
import random
import pyperclip
from tools.FileReader import FileReader
from cipher import Cipher

def encrypt(key, files):
    c = Cipher(key)
    for file in files:
            #self.consoler.echoText("正在加密：" + file)
            reader = FileReader(file)
            text = reader.read()
            encoding = reader.encoding
            result = c.encrypt(files)
            return  result

def decrypt(key, files):
    c = Cipher(key)
    for file in files:
            reader = FileReader(file)
            text = reader.read()
            encoding = reader.encoding
            result = c.decrypt(files)
            return result


if __name__ == '__main__':
    st.title('文件加解密 App')
    uploaded_file = st.file_uploader("请选择一个文本文件：")
    if uploaded_file is not None:
        fs = []
        # To read file as string:
        string_data = uploaded_file.read().decode("utf-8")
        st.write('文本内容如下：')
        st.write(string_data)
        files = string_data
        if files.strip():
            files = files.split("|")
            for file in files:
                if file.strip() != "":
                    fs.append(file)
        genre = st.radio('select',
         ('encrypt', 'decrypt'))
        if genre=='encrypt':
            length = st.slider('随机生成n位密钥', 0, 20, 1)
            key = ""
            for i in range(length):
                key += chr(random.randint(33, 125))
            st.write('密钥：')
            st.write(key)
            #if st.button('Copy Key'):
            #    pyperclip.copy(key)
            r=encrypt(key,string_data)
            st.download_button(
            label="Download data as txt",
            data=r,
            file_name='result.txt',
            mime='text/csv',
           )
        else:
            key = st.text_input('输入密钥', 'x')
            r = decrypt(key, string_data)
            st.download_button(
                label="Download data as txt",
                data=r,
                file_name='result.txt',
                mime='text/csv',
            )
