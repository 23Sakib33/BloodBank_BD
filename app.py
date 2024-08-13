from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample data
donors = []
blood_requests = []
contact_info = {
    'email': 'info@bloodbankbangladesh.org',
    'phone': '+880 123 456 7890'
}

@app.route('/')
def home():
    return render_template('home.html', contact_info=contact_info)

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        name = request.form.get('name')
        blood_type = request.form.get('blood_type')
        contact_email = request.form.get('contact_email')
        if name and blood_type and contact_email:
            donors.append({'name': name, 'blood_type': blood_type, 'contact_email': contact_email})
            flash('Thank you for donating blood!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Please fill out all fields.', 'error')
    return render_template('donate.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        blood_type = request.form.get('blood_type')
        contact_email = request.form.get('contact_email')
        if name and blood_type and contact_email:
            blood_requests.append({'name': name, 'blood_type': blood_type, 'contact_email': contact_email})
            flash('Your blood request has been registered!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Please fill out all fields.', 'error')
    return render_template('register.html')

@app.route('/requests')
def show_requests():
    return render_template('requests.html', requests=blood_requests)

@app.route('/donors')
def show_donors():
    grouped_donors = {}
    for donor in donors:
        blood_type = donor['blood_type']
        if blood_type not in grouped_donors:
            grouped_donors[blood_type] = []
        grouped_donors[blood_type].append(donor)
    return render_template('donors.html', grouped_donors=grouped_donors)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        contact_name = request.form.get('name')
        contact_email = request.form.get('email')
        contact_message = request.form.get('message')
        if contact_name and contact_email and contact_message:
            # Instead of sending an email, just display a confirmation message
            flash('Your message has been received! We will get back to you shortly.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill out all fields.', 'error')
    return render_template('contact.html', contact_info=contact_info)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
