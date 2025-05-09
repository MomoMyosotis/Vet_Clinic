To do list:

create a f() → it initiate a SQL query → get all the univoque keys from all the tables
calls a function to make 3 arrays []
connect it to extentions.currently.dynamicpets\owners\illness()
make it be called from the rest of the code as normal
when  it hase to do a cycle like an action → f() SQL query →  looks for what table it’s from → fills  an obj with said data
do action ||  interaction → SQL query → save data in touched tables → commit changes
empty used space → NO obj dynamic arrays

add a impslist.C.dynamic_illness()
in impslist.ffile.initial_check() → should call SQL.connection.first_connect()
_______________
flow:

main.py → 	main()
		impslist.ffile.initial_check()
		impslist.ffile.cls()
		impslist.C.dynamic_pets()
		impslist.C.dynamic_owners()
		impslist.C.dynamic_illness()
						creates the arrays[]
		random number → cycle → choose if pet owner illness

if pet  →	
ffile.py	 →	pet_cycle() - choose random pet && choose random action from available
		optional → 	aggiorna la lista (es: if dead rm from list of available
		impslist.pet.pet_action()
does the action

_____________________________________________________________________


desired flow:

login → user || admin

main()
	check_data() → connette al db && controlla l’esistenza degli obj e dei file desiderati
	preparation()  → crea (if not exist) e riempie le tabelle e le liste dinamiche di primal key

if admin
	f_debug() → returns “all clear” msg if everything is fine else raise error
		→ print all the lists one at the time
				→ ask for confirm
					→ allows to plant a note in a ReadME file for debug
				→ proceed

	wndw() → opens GUI

clock()  → starts the apps clock
r_choice() → pics a n to choose if the action will be from a pet or an owner
cycle() → based on the obj picked → pet || owner
	r_choice() → to pick the random action it will do
	SQL query → picks the primary key chosen and extract all the related data from the db
		obj_create()  → fills a related obj with the related data from SQL
	action() → does the action
		consequences()	→ update tables with the new data es: status healthy
					→ update list[] es: dead? Rm || born? Add
			sdata() → save data
______________________________________

animations?
Pause?
How to C in py?