from styleformer import Styleformer
import torch
sf = Styleformer(style = 3) 
#st.title('Active Voice to Passive Voice Converter')
#st.write("Please enter your sentence in active voice")
text = "John kicked the ball"
target_sentence = sf.transfer(text)
print(target_sentence)
