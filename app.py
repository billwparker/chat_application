import openai
import streamlit as st

if 'message_list' not in st.session_state:
  st.session_state.message_list = [
      {"role": "system", "content": "You are a helpful assistant."}
    ]      

class Conversaion:

  client = openai.OpenAI(
      base_url = 'http://localhost:11434/v1',
      api_key='ollama', # api_key is required, but unused for local models
  )
  
  def __init__(self):
    pass
        
  def message(self, question):
    
    q = {
      "role": "user",
      "content": question
    }
        
    st.session_state.message_list.append(q)
    
    response = self.client.chat.completions.create(
      model="mistral",
      messages=st.session_state.message_list
    )
    
    q = {
      "role": "assistant",
      "content": response.choices[0].message.content
    }
    
    st.session_state.message_list.append(q)
    
    return response.choices[0].message.content

  
if __name__ == "__main__":
  
  st.title('Chatbot')

  message = st.chat_message("assistant")
  message.write("Hello human!")

  conversation = Conversaion()
  
  prompt = st.chat_input("Ask a question")
  if prompt:
    
    with st.spinner('Thinking...'):
            
      answer = conversation.message(prompt)
            
      for l in st.session_state.message_list:
        
        print(l)
        
        if l['role'] == 'user':
          with st.chat_message("user"):
            st.write(l['content'])
        elif l['role'] == 'assistant':
          with st.chat_message("assistant"):
            st.write(l['content'])
          
