import streamlit as st
import requests



def parseNB(file_name):
    if file_name.startswith('http'):
        response = requests.get(file_name).text.replace('true','True')
    else:
        with open(file_name) as f:
            response = f.read().replace('true','True')

    
    cells = eval(response)['cells']
    hierachy = [st.title,st.header,st.subheader]

    for cell in cells:
        if cell['cell_type'] == 'markdown':
            for line in cell['source']:
                
                if line.startswith('#'):
                    for i in range(len(hierachy),0,-1):
                        #st.write(i)
                        
                        if line.startswith('#'*i) :
                            hierachy[i-1](line[i:])
                            break
                else:
                    st.text(line)

        if cell['cell_type'] == 'code':
            text = ''.join(cell['source'])
            st.code(text,language='python')

        


