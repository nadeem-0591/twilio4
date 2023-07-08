from flask import Flask, render_template, request
import time
import pyautogui

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        group_id = request.form['group_id']
        message = request.form['message']

        try:
            send_whatsapp_message(group_id, message)
            return "WhatsApp message sent successfully."
        except Exception as e:
            return f"An exception occurred while sending the WhatsApp message: {str(e)}"

    return render_template('index.html')

def send_whatsapp_message(group_id, message):
    time.sleep(5)  
    pyautogui.hotkey('ctrl', 't')  
    pyautogui.typewrite(f'https://web.whatsapp.com/accept?code={group_id}\n')  
    time.sleep(10)  
    pyautogui.typewrite(message) 
    pyautogui.press('enter')  

if __name__ == '__main__':
    app.run()
