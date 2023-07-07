from flask import Flask, render_template, request
import pywhatkit as kit

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        group_id = request.form['group_id']
        message = request.form['message']
        hour = int(request.form['hour'])
        minute = int(request.form['minute'])

        try:
            kit.sendwhatmsg_to_group(group_id, message, hour, minute)
            return "WhatsApp message sent successfully."
        except Exception as e:
            return f"An exception occurred while sending the WhatsApp message: {str(e)}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
