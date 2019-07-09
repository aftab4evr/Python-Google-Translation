from googletrans import Translator  
translator = Translator() 
strText="This is a  Traslation Using Google Traslation by Python code"
translated = translator.translate(strText,dest='ha') #It will traslate to Hausa language 
print(" Source Language:" + translated.src) 
print(" Translated string:" + translated.text
