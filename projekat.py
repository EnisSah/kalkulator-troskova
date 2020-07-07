import tkinter as tk
import sqlite3

HEIGHT = 600
WIDTH = 850



root = tk.Tk()
root.title('Kontrolor Troskova')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='4.png')
background_image = tk.PhotoImage(file='4.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
 
# Create frame
frame = tk.Frame(root, bd=5)
frame.place(relx=0.5, rely=0.25, relwidth =0.47, relheight=0.63, anchor='n' )



# Create sumbit functions for every month
def submit_januar():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()
	c.execute('INSERT INTO prihodi(Januar) VALUES (:Januar)',
		{
			'Januar' : januar_prihod.get(),
			})

	januar_prihod.delete(0,25)

	c.execute('INSERT INTO rashodi(Januar) VALUES (:Januar)',
		{
			'Januar' : januar_rashod.get(),
			})

	januar_rashod.delete(0,25)

	# if bilans_januar()>=0:
	# 	januar_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_januar()} RSD'))
	# 	januar_stanje.grid(row = 1, column = 4)
	# else:
	# 	januar_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_januar()} RSD'))
	# 	januar_stanje.grid(row = 1, column = 4)

	conn.commit()
	c.close()
	conn.close()

def bilans_januar():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(januar) FROM prihodi ')
	ukupan_prihod_januar = [int(i[0]) for i in c.fetchall()]

	c.execute('SELECT SUM(januar) FROM rashodi')
	ukupan_rashod_januar= [int(i[0]) for i in c.fetchall()]


	# print('Bilans za mesec Januar je:',sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar), '', 'RSD')
	return (sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar))
bilans_januar()




def submit_februar():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()
	c.execute('INSERT INTO prihodi(Februar) VALUES (:Februar)',
		{
			'Februar' : februar_prihod.get(),
			})


	februar_prihod.delete(0,25)

	c.execute('INSERT INTO rashodi(Februar) VALUES (:Februar)',
		{
			'Februar' : februar_rashod.get(),
			})

	februar_rashod.delete(0,25)

	conn.commit()
	c.close()
	conn.close()

def bilans_februar():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(februar) FROM prihodi ')
	ukupan_prihod_februar= [int(i[0]) for i in c.fetchall()]

	c.execute('SELECT SUM(februar) FROM rashodi')
	ukupan_rashod_februar= [int(i[0]) for i in c.fetchall()]

	# print('Bilans za mesec Januar je:',sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar), '', 'RSD')
	return(sum(ukupan_prihod_februar) - sum(ukupan_rashod_februar))
bilans_februar()




def submit_mart():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()
	c.execute('INSERT INTO prihodi(Mart) VALUES (:Mart)',
		{
			'Mart' : mart_prihod.get(),
			})

	mart_prihod.delete(0,25)

	c.execute('INSERT INTO rashodi(Mart) VALUES (:Mart)',
		{
			'Mart' : mart_rashod.get(),
			})

	mart_rashod.delete(0,25)

	conn.commit()
	c.close()
	conn.close()

def bilans_mart():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(mart) FROM prihodi ')
	ukupan_prihod_mart = [int(i[0]) for i in c.fetchall()]

	c.execute('SELECT SUM(mart) FROM rashodi')
	ukupan_rashod_mart= [int(i[0]) for i in c.fetchall()]

	# print('Bilans za mesec Januar je:',sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar), '', 'RSD')
	return(sum(ukupan_prihod_mart) - sum(ukupan_rashod_mart))
bilans_mart()


def submit_april():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()
	c.execute('INSERT INTO prihodi(April) VALUES (:April)',
		{
			'April' : april_prihod.get(),
			})

	april_prihod.delete(0,25)

	c.execute('INSERT INTO rashodi(April) VALUES (:April)',
		{
			'April' : april_rashod.get(),
			})

	april_rashod.delete(0,25)

	conn.commit()
	c.close()
	conn.close()

def bilans_april():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(April) FROM prihodi ')
	ukupan_prihod_april = [int(i[0]) for i in c.fetchall()]

	c.execute('SELECT SUM(April) FROM rashodi')
	ukupan_rashod_april= [int(i[0]) for i in c.fetchall()]

	# print('Bilans za mesec Januar je:',sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar), '', 'RSD')
	return(sum(ukupan_prihod_april) - sum(ukupan_rashod_april))
bilans_april()


def submit_maj():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()
	c.execute('INSERT INTO prihodi(Maj) VALUES (:Maj)',
		{
			'Maj' : maj_prihod.get(),
			})

	maj_prihod.delete(0,25)

	c.execute('INSERT INTO rashodi(Maj) VALUES (:Maj)',
		{
			'Maj' : maj_rashod.get(),
			})

	maj_rashod.delete(0,25)

	conn.commit()
	c.close()
	conn.close()

def bilans_maj():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(Maj) FROM prihodi ')
	ukupan_prihod_maj = [int(i[0]) for i in c.fetchall()]

	c.execute('SELECT SUM(Maj) FROM rashodi')
	ukupan_rashod_maj= [int(i[0]) for i in c.fetchall()]

	# print('Bilans za mesec Januar je:',sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar), '', 'RSD')
	return(sum(ukupan_prihod_maj) - sum(ukupan_rashod_maj))
bilans_maj()

def submit_jun():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()
	c.execute('INSERT INTO prihodi(Jun) VALUES (:Jun)',
		{
			'Jun' : jun_prihod.get(),
			})

	jun_prihod.delete(0,25)

	c.execute('INSERT INTO rashodi(Jun) VALUES (:Jun)',
		{
			'Jun' : jun_rashod.get(),
			})

	jun_rashod.delete(0,25)

	conn.commit()
	c.close()
	conn.close()

def bilans_jun():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(Jun) FROM prihodi ')
	ukupan_prihod_jun = [int(i[0]) for i in c.fetchall()]

	c.execute('SELECT SUM(Jun) FROM rashodi')
	ukupan_rashod_jun= [int(i[0]) for i in c.fetchall()]

	# print('Bilans za mesec Januar je:',sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar), '', 'RSD')
	return(sum(ukupan_prihod_jun) - sum(ukupan_rashod_jun))
bilans_jun()

def submit_jul():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()
	c.execute('INSERT INTO prihodi(Jul) VALUES (:Jul)',
		{
			'Jul' : jul_prihod.get(),
			})

	jul_prihod.delete(0,25)

	c.execute('INSERT INTO rashodi(Jul) VALUES (:Jul)',
		{
			'Jul' : jul_rashod.get(),
			})

	jul_rashod.delete(0,25)

	conn.commit()
	c.close()
	conn.close()

def bilans_jul():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(Jul) FROM prihodi ')
	ukupan_prihod_jul = [int(i[0]) for i in c.fetchall()]

	c.execute('SELECT SUM(Jul) FROM rashodi')
	ukupan_rashod_jul= [int(i[0]) for i in c.fetchall()]

	# print('Bilans za mesec Januar je:',sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar), '', 'RSD')
	return(sum(ukupan_prihod_jul) - sum(ukupan_rashod_jul))
bilans_jul()


def submit_avgust():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()
	c.execute('INSERT INTO prihodi(Avgust) VALUES (:Avgust)',
		{
			'Avgust' : avgust_prihod.get(),
			})

	avgust_prihod.delete(0,25)

	c.execute('INSERT INTO rashodi(Avgust) VALUES (:Avgust)',
		{
			'Avgust' : avgust_rashod.get(),
			})

	avgust_rashod.delete(0,25)

	conn.commit()
	c.close()
	conn.close()

def bilans_avgust():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(Avgust) FROM prihodi ')
	ukupan_prihod_avgust = [int(i[0]) for i in c.fetchall()]

	c.execute('SELECT SUM(Avgust) FROM rashodi')
	ukupan_rashod_avgust= [int(i[0]) for i in c.fetchall()]

	# print('Bilans za mesec Januar je:',sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar), '', 'RSD')
	return(sum(ukupan_prihod_avgust) - sum(ukupan_rashod_avgust))
bilans_avgust()

def submit_septembar():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()
	c.execute('INSERT INTO prihodi(Septembar) VALUES (:Septembar)',
		{
			'Septembar' : septembar_prihod.get(),
			})

	septembar_prihod.delete(0,25)

	c.execute('INSERT INTO rashodi(Septembar) VALUES (:Septembar)',
		{
			'Septembar' : septembar_rashod.get(),
			})

	septembar_rashod.delete(0,25)

	conn.commit()
	c.close()
	conn.close()

def bilans_septembar():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(Septembar) FROM prihodi ')
	ukupan_prihod_septembar = [int(i[0]) for i in c.fetchall()]

	c.execute('SELECT SUM(Septembar) FROM rashodi')
	ukupan_rashod_septembar= [int(i[0]) for i in c.fetchall()]

	# print('Bilans za mesec Januar je:',sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar), '', 'RSD')
	return(sum(ukupan_prihod_septembar) - sum(ukupan_rashod_septembar))
bilans_septembar()


def submit_oktobar():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()
	c.execute('INSERT INTO prihodi(Oktobar) VALUES (:Oktobar)',
		{
			'Oktobar' : oktobar_prihod.get(),
			})

	oktobar_prihod.delete(0,25)

	c.execute('INSERT INTO rashodi(Oktobar) VALUES (:Oktobar)',
		{
			'Oktobar' : oktobar_rashod.get(),
			})

	oktobar_rashod.delete(0,25)

	conn.commit()
	c.close()
	conn.close()

def bilans_oktobar():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(Oktobar) FROM prihodi ')
	ukupan_prihod_oktobar = [int(i[0]) for i in c.fetchall()]

	c.execute('SELECT SUM(Oktobar) FROM rashodi')
	ukupan_rashod_oktobar= [int(i[0]) for i in c.fetchall()]

	# print('Bilans za mesec Januar je:',sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar), '', 'RSD')
	return(sum(ukupan_prihod_oktobar) - sum(ukupan_rashod_oktobar))
bilans_oktobar()


def submit_novembar():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()
	c.execute('INSERT INTO prihodi(Novembar) VALUES (:Novembar)',
		{
			'Novembar' : novembar_prihod.get(),
			})

	novembar_prihod.delete(0,25)

	c.execute('INSERT INTO rashodi(Novembar) VALUES (:Novembar)',
		{
			'Novembar' : novembar_rashod.get(),
			})

	novembar_rashod.delete(0,25)

	conn.commit()
	c.close()
	conn.close()

def bilans_novembar():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(Novembar) FROM prihodi ')
	ukupan_prihod_novembar = [int(i[0]) for i in c.fetchall()]

	c.execute('SELECT SUM(Novembar) FROM rashodi')
	ukupan_rashod_novembar= [int(i[0]) for i in c.fetchall()]

	# print('Bilans za mesec Januar je:',sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar), '', 'RSD')
	return(sum(ukupan_prihod_novembar) - sum(ukupan_rashod_novembar))
bilans_novembar()

def submit_decembar():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()
	c.execute('INSERT INTO prihodi(Decembar) VALUES (:Decembar)',
		{
			'Decembar' : decembar_prihod.get(),
			})

	decembar_prihod.delete(0,25)

	c.execute('INSERT INTO rashodi(Decembar) VALUES (:Decembar)',
		{
			'Decembar' : decembar_rashod.get(),
			})

	decembar_rashod.delete(0,25)

	conn.commit()
	c.close()
	conn.close()

def bilans_decembar():
	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(Decembar) FROM prihodi ')
	ukupan_prihod_decembar = [int(i[0]) for i in c.fetchall()]

	c.execute('SELECT SUM(Decembar) FROM rashodi')
	ukupan_rashod_decembar= [int(i[0]) for i in c.fetchall()]

	# print('Bilans za mesec Januar je:',sum(ukupan_prihod_januar) - sum(ukupan_rashod_januar), '', 'RSD')
	return(sum(ukupan_prihod_decembar) - sum(ukupan_rashod_decembar))
bilans_decembar()









# Create month text
meseci_label = tk.Label(frame, text = 'Meseci')
meseci_label.grid(row = 0, column = 0)


# Create months text boxes
januar_label = tk.Label(frame, text = 'Januar', bg='#3333ff', width=15, bd = 4)
januar_label.grid(row = 1, column = 0)

februar = tk.Label(frame, text = 'Februar',bg='#4d94ff', width=15, bd = 4)
februar.grid(row = 2, column = 0)
mart = tk.Label(frame, text = 'Mart',bg='#009933', width=15, bd = 4)
mart.grid(row = 3, column = 0)
april = tk.Label(frame, text = 'April', bg='#00ff55', width=15, bd = 4)
april.grid(row = 4, column = 0)
maj = tk.Label(frame, text = 'Maj',bg='#cccc00', width=15, bd = 4)
maj.grid(row = 5, column = 0)
jun = tk.Label(frame, text = 'Jun',bg='#ffff00', width=15, bd = 4)
jun.grid(row = 6, column = 0)
jul = tk.Label(frame, text = 'Jul',bg='#ff8c1a', width=15, bd = 4)
jul.grid(row = 7, column = 0)
avgust = tk.Label(frame, text = 'Avgust',bg='#e67300', width=15, bd = 4)
avgust.grid(row = 8, column = 0)
september = tk.Label(frame, text = 'Septembar',bg='#ffb366', width=15, bd = 4)
september.grid(row = 9, column = 0)
oktobar = tk.Label(frame, text = 'Oktobar',bg='#ad1f8a', width=15, bd = 4)
oktobar.grid(row = 10, column = 0)
novembar = tk.Label(frame, text = 'Novembar', bg='#660fbd', width=15, bd = 4)
novembar.grid(row = 11, column = 0)
decembar = tk.Label(frame, text = 'Decembar',bg='#198cb3', width=15, bd = 4)
decembar.grid(row = 12, column = 0)



# Create text boxes for prihodi and rashodi

prihodi_label = tk.Label(frame, text = 'Prihodi')
prihodi_label.grid(row = 0, column = 1)

rashodi_label = tk.Label(frame, text = 'Rashodi')
rashodi_label.grid(row = 0, column = 2)





# Create entry buttons for prihodi and rashodi

januar_prihod = tk.Entry(frame, width = 10, bg='#ccffcc')
januar_prihod.grid(row = 1, column = 1)

januar_rashod = tk.Entry(frame, width = 10, bg='#ffcccc')
januar_rashod.grid(row = 1, column = 2)


februar_prihod = tk.Entry(frame, width = 10,bg='#ccffcc')
februar_prihod.grid(row = 2, column = 1)

februar_rashod = tk.Entry(frame, width = 10, bg='#ffcccc')
februar_rashod.grid(row = 2, column = 2)

mart_prihod = tk.Entry(frame, width = 10,bg='#ccffcc')
mart_prihod.grid(row = 3, column = 1)

mart_rashod = tk.Entry(frame, width = 10, bg='#ffcccc')
mart_rashod.grid(row = 3, column = 2)

april_prihod = tk.Entry(frame, width = 10,bg='#ccffcc')
april_prihod.grid(row = 4, column = 1)

april_rashod = tk.Entry(frame, width = 10, bg='#ffcccc')
april_rashod.grid(row = 4, column = 2)

maj_prihod = tk.Entry(frame, width = 10, bg='#ccffcc')
maj_prihod.grid(row = 5, column = 1)

maj_rashod = tk.Entry(frame, width = 10, bg='#ffcccc')
maj_rashod.grid(row = 5, column = 2)

jun_prihod = tk.Entry(frame, width = 10, bg='#ccffcc')
jun_prihod.grid(row = 6, column = 1)

jun_rashod = tk.Entry(frame, width = 10, bg='#ffcccc')
jun_rashod.grid(row = 6, column = 2)

jul_prihod = tk.Entry(frame, width = 10, bg='#ccffcc')
jul_prihod.grid(row = 7, column = 1)

jul_rashod = tk.Entry(frame, width = 10, bg='#ffcccc')
jul_rashod.grid(row = 7, column = 2)

avgust_prihod = tk.Entry(frame, width = 10, bg='#ccffcc')
avgust_prihod.grid(row = 8, column = 1)

avgust_rashod = tk.Entry(frame, width = 10, bg='#ffcccc')
avgust_rashod.grid(row = 8, column = 2)

septembar_prihod = tk.Entry(frame, width = 10, bg='#ccffcc')
septembar_prihod.grid(row = 9, column = 1)

septembar_rashod = tk.Entry(frame, width = 10, bg='#ffcccc')
septembar_rashod.grid(row = 9, column = 2)

oktobar_prihod = tk.Entry(frame, width = 10, bg='#ccffcc')
oktobar_prihod.grid(row = 10, column = 1)

oktobar_rashod = tk.Entry(frame, width = 10, bg='#ffcccc')
oktobar_rashod.grid(row = 10, column = 2)

novembar_prihod = tk.Entry(frame, width = 10, bg='#ccffcc')
novembar_prihod.grid(row = 11, column = 1)

novembar_rashod = tk.Entry(frame, width = 10, bg='#ffcccc')
novembar_rashod.grid(row = 11, column = 2)

decembar_prihod = tk.Entry(frame, width = 10, bg='#ccffcc')
decembar_prihod.grid(row = 12, column = 1)

decembar_rashod = tk.Entry(frame, width = 10, bg='#ffcccc')
decembar_rashod.grid(row = 12, column = 2)




# Create submit buttons for every month
submit_januar = tk.Button(frame, text = 'Dodati u bazu',command=submit_januar)
submit_januar.grid(row = 1, column = 3)

submit_februar = tk.Button(frame, text = 'Dodati u bazu',command=submit_februar)
submit_februar.grid(row = 2, column = 3)

submit_mart = tk.Button(frame, text = 'Dodati u bazu',command=submit_mart)
submit_mart.grid(row = 3, column = 3)

submit_april = tk.Button(frame, text = 'Dodati u bazu',command=submit_april)
submit_april.grid(row = 4, column = 3)

submit_maj = tk.Button(frame, text = 'Dodati u bazu',command=submit_maj)
submit_maj.grid(row = 5, column = 3)

submit_jun = tk.Button(frame, text = 'Dodati u bazu',command=submit_jun)
submit_jun.grid(row = 6, column = 3)

submit_jul = tk.Button(frame, text = 'Dodati u bazu',command=submit_jul)
submit_jul.grid(row = 7, column = 3)

submit_avgust = tk.Button(frame, text = 'Dodati u bazu',command=submit_avgust)
submit_avgust.grid(row = 8, column = 3)

submit_septembar = tk.Button(frame, text = 'Dodati u bazu',command=submit_septembar)
submit_septembar.grid(row = 9, column = 3)

submit_oktobar = tk.Button(frame, text = 'Dodati u bazu',command=submit_oktobar)
submit_oktobar.grid(row = 10, column = 3)

submit_novembar = tk.Button(frame, text = 'Dodati u bazu',command=submit_novembar)
submit_novembar.grid(row = 11, column = 3)

submit_decembar = tk.Button(frame, text = 'Dodati u bazu',command=submit_decembar)
submit_decembar.grid(row = 12, column = 3)


# Create balans text
prihodi_label = tk.Label(frame, text = 'Bilans')
prihodi_label.grid(row = 0, column = 4)


# Create bilans boxes 
# bilans_button_januar = tk.Button(frame, text = 'bilans januar', command = januar_st)
# bilans_button_januar.grid(row=1, column=4)

def januar_st():
	if bilans_januar()>=0:
		januar_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_januar()} RSD'))
		januar_stanje.grid(row = 1, column = 5)
	else:
		januar_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_januar()} RSD'))
		januar_stanje.grid(row = 1, column = 5)
januar_st()
bilans_button_januar = tk.Button(frame, text = 'bilans januar', command = januar_st, width=15)
bilans_button_januar.grid(row=1, column=4)

def februar_st():
	if bilans_februar()>=0:
		februar_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_februar()} RSD'))
		februar_stanje.grid(row = 2, column = 5)
	else:
		februar_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_februar()} RSD'))
		februar_stanje.grid(row = 2, column = 5)
februar_st()
bilans_button_februar = tk.Button(frame, text = 'bilans februar', command = februar_st,width=15)
bilans_button_februar.grid(row=2, column=4)

def mart_st():
	if bilans_mart()>=0:
		mart_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_mart()} RSD'))
		mart_stanje.grid(row = 3, column = 5)
	else:
		mart_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_mart()} RSD'))
		mart_stanje.grid(row = 3, column = 5)
mart_st()
bilans_button_mart = tk.Button(frame, text = 'bilans mart', command = mart_st,width=15)
bilans_button_mart.grid(row=3, column=4)

def april_st():
	if bilans_april()>=0:
		april_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_april()} RSD'))
		april_stanje.grid(row = 4, column = 5)
	else:
		april_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_april()} RSD'))
		april_stanje.grid(row = 4, column = 5)
april_st()
bilans_button_april = tk.Button(frame, text = 'bilans april', command = april_st,width=15)
bilans_button_april.grid(row=4, column=4)


def maj_st():
	if bilans_maj()>=0:
		maj_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_maj()} RSD'))
		maj_stanje.grid(row = 5, column = 5)
	else:
		maj_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_maj()} RSD'))
		maj_stanje.grid(row = 5, column = 5)
maj_st()
bilans_button_maj = tk.Button(frame, text = 'bilans maj', command = maj_st,width=15)
bilans_button_maj.grid(row=5, column=4)


def jun_st():
	if bilans_jun()>=0:
		jun_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_jun()} RSD'))
		jun_stanje.grid(row = 6, column = 5)
	else:
		jun_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_jun()} RSD'))
		jun_stanje.grid(row = 6, column = 5)
jun_st()
bilans_button_jun = tk.Button(frame, text = 'bilans jun', command = jun_st,width=15)
bilans_button_jun.grid(row=6, column=4)

def jul_st():
	if bilans_jul()>=0:
		jul_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_jul()} RSD'))
		jul_stanje.grid(row = 7, column = 5)
	else:
		jul_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_jul()} RSD'))
		jul_stanje.grid(row = 7, column = 5)
jul_st()
bilans_button_jul = tk.Button(frame, text = 'bilans jul', command = jul_st,width=15)
bilans_button_jul.grid(row=7, column=4)

def avgust_st():
	if bilans_avgust()>=0:
		avgust_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_avgust()} RSD'))
		avgust_stanje.grid(row = 8, column = 5)
	else:
		avgust_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_avgust()} RSD'))
		avgust_stanje.grid(row = 8, column = 5)
avgust_st()
bilans_button_avgust = tk.Button(frame, text = 'bilans avgust', command = avgust_st,width=15)
bilans_button_avgust.grid(row=8, column=4)

def septembar_st():
	if bilans_septembar()>=0:
		septembar_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_septembar()} RSD'))
		septembar_stanje.grid(row = 9, column = 5)
	else:
		septembar_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_septembar()} RSD'))
		septembar_stanje.grid(row = 9, column = 5)
septembar_st()
bilans_button_septembar = tk.Button(frame, text = 'bilans septembar', command = septembar_st,width=15)
bilans_button_septembar.grid(row=9, column=4)

def oktobar_st():
	if bilans_oktobar()>=0:
		oktobar_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_oktobar()} RSD'))
		oktobar_stanje.grid(row = 10, column = 5)
	else:
		oktobar_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_oktobar()} RSD'))
		oktobar_stanje.grid(row = 10, column = 5)
oktobar_st()
bilans_button_oktobar = tk.Button(frame, text = 'bilans oktobar', command = oktobar_st,width=15)
bilans_button_oktobar.grid(row=10, column=4)

def novembar_st():
	if bilans_novembar()>=0:
		novembar_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_novembar()} RSD'))
		novembar_stanje.grid(row = 11, column = 5)
	else:
		novembar_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_novembar()} RSD'))
		novembar_stanje.grid(row = 11, column = 5)
novembar_st()
bilans_button_novembar = tk.Button(frame, text = 'bilans novembar', command = novembar_st,width=15)
bilans_button_novembar.grid(row=11, column=4)

def decembar_st():
	if bilans_decembar()>=0:
		decembar_stanje = tk.Label(frame,fg='#00ff80' ,text= (f'{bilans_decembar()} RSD'))
		decembar_stanje.grid(row = 12, column = 5)
	else:
		decembar_stanje = tk.Label(frame,fg='#ff4000' ,text= (f'{bilans_decembar()} RSD'))
		decembar_stanje.grid(row = 12, column = 5)
decembar_st()
bilans_button_decembar = tk.Button(frame, text = 'bilans decembar', command = decembar_st,width=15)
bilans_button_decembar.grid(row=12, column=4)


stanje_po_mesecima = {
					1:bilans_januar(),
					2:bilans_februar(),
					3:bilans_mart(),
					4:bilans_april(),
					5:bilans_maj(),
					6:bilans_jun(),
					7:bilans_jul(),
					8:bilans_avgust(),
					9:bilans_septembar(),
					10:bilans_oktobar(),
					11:bilans_novembar(),
					12:bilans_decembar()
}


def prosecna_mesecna_potrosnja_prihod():
	brojac = 0
	for x in stanje_po_mesecima:
		if (stanje_po_mesecima[x])!=0:
			brojac +=1 
	# print(brojac)


	# return(bilans_januar()+bilans_februar()+bilans_mart()+
	# 	+bilans_april()+bilans_maj()+bilans_jun()+
	# 	+bilans_jul()+bilans_avgust()+ bilans_septembar()+bilans_oktobar()+
	# 	+bilans_novembar()+ bilans_decembar()//brojac)

	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(januar) +SUM (februar)+ SUM(mart)+SUM(april)+SUM(maj)+\
		SUM(jun)+SUM(jul)+SUM(avgust)+SUM(septembar)+SUM(novembar)+\
		SUM(oktobar)+SUM(decembar) FROM prihodi ')
	# return ((c.fetchall())
	ukupni_stanje = [int(i) for i in c.fetchone()] 
	return (sum(ukupni_stanje)//brojac)
print(prosecna_mesecna_potrosnja_prihod())

# Dve funkcija koje ce racunati prosecan mesecni prihod i prosecan mesecni rashod
def prosecna_mesecna_potrosnja_rashod():
	brojac = 0
	for x in stanje_po_mesecima:
		if (stanje_po_mesecima[x])!=0:
			brojac +=1 
	# print(brojac)


	# return(bilans_januar()+bilans_februar()+bilans_mart()+
	# 	+bilans_april()+bilans_maj()+bilans_jun()+
	# 	+bilans_jul()+bilans_avgust()+ bilans_septembar()+bilans_oktobar()+
	# 	+bilans_novembar()+ bilans_decembar()//brojac)

	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()

	c.execute('SELECT SUM(januar) +SUM (februar)+ SUM(mart)+SUM(april)+SUM(maj)+\
		SUM(jun)+SUM(jul)+SUM(avgust)+SUM(septembar)+SUM(novembar)+\
		SUM(oktobar)+SUM(decembar) FROM rashodi ')
	# return ((c.fetchall())
	ukupni_stanje = [int(i) for i in c.fetchone()] 
	return (sum(ukupni_stanje)//brojac)
# print(prosecna_mesecna_potrosnja_rashod())

#Funkcija koja ce racunati ustedjevinu kao razliku izmedju ukuphih prihoda i rashoda
def ustedjevina():

	conn = sqlite3.connect('expanse_tracker.db')
	c = conn.cursor()


	c.execute('SELECT SUM(januar) +SUM (februar)+ SUM(mart)+SUM(april)+SUM(maj)+\
		SUM(jun)+SUM(jul)+SUM(avgust)+SUM(septembar)+SUM(novembar)+\
		SUM(oktobar)+SUM(decembar) FROM prihodi ')
	ukupan_prihod = [int(i) for i in c.fetchone()] 

	c.execute('SELECT SUM(januar) +SUM (februar)+ SUM(mart)+SUM(april)+SUM(maj)+\
		SUM(jun)+SUM(jul)+SUM(avgust)+SUM(septembar)+SUM(novembar)+\
		SUM(oktobar)+SUM(decembar) FROM rashodi ')
	ukupan_rashod = [int(i) for i in c.fetchone()] 

	return (sum(ukupan_prihod)-(sum(ukupan_rashod)))






# Prosecni mesecni prihodi i rashodi Labels
prosecni_mesecni_prihodi = tk.Label(frame, text = 'Prosecni mesecni prihodi:')
prosecni_mesecni_prihodi.grid(row = 13, column=0)

prosecni_mesecni_prihodi_prikaz = tk.Label(frame, text = (f'{prosecna_mesecna_potrosnja_prihod()} RSD'))
prosecni_mesecni_prihodi_prikaz.grid(row=13, column = 1)

prosecni_mesecni_rashodi = tk.Label(frame, text = 'Prosecni mesecni rashodi:')
prosecni_mesecni_rashodi.grid(row = 14, column=0)

prosecni_mesecni_rashodi_prikaz = tk.Label(frame, text = (f'{prosecna_mesecna_potrosnja_rashod()} RSD'))
prosecni_mesecni_rashodi_prikaz.grid(row=14, column = 1)

ukupna_ustedjevina = tk.Label(frame, text='Ustedjevina (Σ prihod -  Σ rashod):')
ukupna_ustedjevina.grid(row=15, column=0)

ukupna_ustedjevina_prikaz = tk.Label(frame, text=(f'{ustedjevina()} RSD'))
ukupna_ustedjevina_prikaz.grid(row=15, column=1)





root.mainloop()