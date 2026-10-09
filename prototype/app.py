from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

market_name = "Kasanga Market"
traders = [
    {
        "id": 1,
        "name": "Amina Kato",
        "stall": "A12",
        "section": "Fresh Produce",
        "due_per_month": 50000,
        "paid": 45000,
        "status": "Outstanding",
        "last_payment": "2026-09-15"
    },
    {
        "id": 2,
        "name": "Juma Ssekandi",
        "stall": "B07",
        "section": "Food Stalls",
        "due_per_month": 60000,
        "paid": 60000,
        "status": "Paid",
        "last_payment": "2026-09-18"
    },
    {
        "id": 3,
        "name": "Sarah Nampala",
        "stall": "C04",
        "section": "Retail",
        "due_per_month": 40000,
        "paid": 20000,
        "status": "Outstanding",
        "last_payment": "2026-09-05"
    }
]

@app.route('/')
def index():
    expected_total = sum(t['due_per_month'] for t in traders)
    paid_total = sum(t['paid'] for t in traders)
    leakage_total = expected_total - paid_total
    outstanding = sum(1 for t in traders if t['status'] == 'Outstanding')
    return render_template(
        'index.html',
        market_name=market_name,
        traders=traders,
        expected_total=expected_total,
        paid_total=paid_total,
        leakage_total=leakage_total,
        outstanding=outstanding
    )

@app.route('/register', methods=['POST'])
def register_trader():
    trader = {
        'id': len(traders) + 1,
        'name': request.form['name'],
        'stall': request.form['stall'],
        'section': request.form['section'],
        'due_per_month': int(request.form['due_per_month']),
        'paid': int(request.form['paid']),
        'status': 'Paid' if int(request.form['paid']) >= int(request.form['due_per_month']) else 'Outstanding',
        'last_payment': request.form['last_payment']
    }
    traders.append(trader)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
