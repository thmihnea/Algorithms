#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <cmath>

/*
	Definim cartea nula in cazul in care intampinam
	erori atunci cand dorim sa cautam o carte
	in vector si nu o gasim.
*/
#define NULL_CARTE carte("", 0, 0, "");

/*
	Definim index-ul nul in cazul in care intampinam
	erori atunci cand nu gasim index-ul cartii
	respective.
*/
#define NULL_INDEX -1

/*
	Definim un numar foarte mare pentru a putea
	calcula diferentele intre pagini si ID-ul
	unei carti. Folosim aceasta definitie pentru
	evitarea utilizarii unui numar precum
	2.000.000.000 etc.
*/
#define HUGE 1e+300;

using namespace std;

/*
	Definim metodele/functiile prin care executam
	citirea si scrierea in fisiere.
*/
ifstream fin("intrare.txt");
ofstream fout("iesire.txt");

/*
	Structura carte responsabila pentru manipularea
	fiecarei carti in parte.
*/
struct carte {

	/*
		Campurile private ale cartii. Aici retinem informatii
		despre titlul cartii, numarul de pagini, ID-ul cartii si
		respectiv numele autorului.
		Le mentinem private intrucat arata urat daca apelam <carte>.titlu :)
		Singurul mod in care pot fi manipulate direct este prin
		reflection.
	*/
private:
	char titlu[32];
	int pagini;
	int id;
	char nume[32];

	/*
		Campurile publice ale cartii. Sunt constituite din
		metode care manipuleaza campurile private.
	*/
public:

	/*
		Constructorul cartii.
		Trebuie specificate argumentele:
		@param titlu[32] - titlul cartii
		@param pagini - numarul de pagini
		@param id - ID-ul cartii in biblioteca
		@param nume[32] - numele autorului
	*/
	carte(const char titlu[32], int pagini, int id, const char nume[32]) {
		strcpy(this->titlu, titlu);
		this->pagini = pagini;
		this->id = id;
		strcpy(this->nume, nume);
	}

	/*
		Metoda pentru a obtine titlul cartii.
	*/
	char* get_titlu() {
		return this->titlu;
	}

	/*
		Metoda pentru a obtine numarul de pagini
		din carte.
	*/
	int get_pagini() {
		return this->pagini;
	}

	/*
		Metoda pentru a obtine ID-ul cartii
		din biblioteca.
	*/
	int get_id() {
		return this->id;
	}

	/*
		Metoda pentru a obtine numele cartii.
		Utilizam un pointer pentru simplicitate.
	*/
	char* get_nume() {
		return this->nume;
	}

	/*
		Metoda pentru a verifica daca doua carti
		sunt egale (ca obiecte ale structurii carte).
	*/
	bool equals(carte c) {
		return ((strcmp(this->titlu, c.get_titlu()) == 0) && (strcmp(this->nume, c.get_nume()) == 0) && (this->id == c.get_id()) && (this->pagini == c.get_pagini()));
	}

	/*
		Metoda pentru a seta titlul
		unei carti daca dorim sa il editam.
	*/
	void set_titlu(const char titlu[32]) {
		strcpy(this->titlu, titlu);
	}

	/*
		Metoda pentru a seta numarul de pagini
		ale cartii daca dorim sa il editam.
	*/
	void set_pagini(int pagini) {
		this->pagini = pagini;
	}

	/*
		Metoda pentru a seta ID-ul unei carti
		daca dorim sa il editam.
	*/
	void set_id(int id) {
		this->id = id;
	}

	/*
		Metoda pentru a seta numele autorului
		unei carti.
	*/
	void set_nume(const char nume[32]) {
		strcpy(this->nume, nume);
	}
};

/*
	Structura responsabila pentru obiectul
	biblioteca din sursa.
*/
struct biblioteca {
	/*
		Campurile private ale bibliotecii.
		Folosim un vector de carti pentru a le tine in
		memorie si respectiv un int care se
		refera la numarul de carti aflate in
		biblioteca.
		(Se poate utiliza is vec.size())
	*/
private:
	vector<carte> carti;
	int size_biblioteca;
public:

	/*
		Constructorul bibliotecii.
		Simplist, doar initializeaza numarul
		de carti din biblioteca cu 0.
	*/
	biblioteca() {
		this->size_biblioteca = 0;
	}

	/*
		Metoda folosita pentru a returna
		vectorul care contine toate cartile
		din biblioteca.
	*/
	vector<carte> get_carti() {
		return this->carti;
	}

	/*
		Metoda folosita pentru a returna
		un vector care contine toate cartile
		scrise de un anumit autor.
		@param autor[32] - autorul dupa care
		initiem cautarea
	*/
	vector<carte> get_carti_by_autor(const char autor[32]) {
		vector<carte> carti_by_autor;
		int gasite = 0;
		for (int i = 0; i < this->size_biblioteca; i++)
			if (strcmp(this->carti[i].get_nume(), autor) == 0) {
				carti_by_autor.push_back(this->carti[i]);
				gasite++;
			}
		cout << "Au fost gasite " << gasite << " carti care au fost scrise de " << autor;
		cout << endl;
		return carti_by_autor;
	}

	/*
		Metoda folosita pentru a returna
		un vector care contine toate cartile
		care au un anumit numar de pagini.
		@param pagini - numarul de pagini dupa
		care initiem cautarea
	*/
	vector<carte> get_carti_by_pagini(int pagini) {
		vector<carte> carti_by_pagini;
		int gasite = 0;
		for (int i = 0; i < this->size_biblioteca; i++)
			if (this->carti[i].get_pagini() == pagini) {
				carti_by_pagini.push_back(this->carti[i]);
				gasite++;
			}
		if (gasite == 0) {
			cout << "Nu a fost gasita nicio carte cu " << pagini << " pagini." << endl;
			this->get_carte_with_closest_pages_to(pagini);
		}
		else {
			cout << "Au fost gasite " << gasite << " carti care au " << pagini << " pagini.";
			cout << endl;
		}
		return carti_by_pagini;
	}

	/*
		Metoda folosita pentru a returna
		cartea care are un anumit ID. Ne folosim
		de cautarea binara pentru o complexitate
		mai mica.

		@param id - ID-ul dupa care cautam
		@param leftbound - partea din stanga
		@param rightbound - partea din dreapta
	*/
	carte get_carte_by_id(int id, int leftbound, int rightbound) {
		if (leftbound > rightbound) {
			cout << "Nu a putut fi gasita o carte cu ID-ul " << id << "." << endl;
			this->get_carte_with_closest_id_to(id);
			return NULL_CARTE;
		}
		else {
			int middle = (leftbound + rightbound) / 2;
			if (this->carti[middle].get_id() == id)
				return this->carti[middle];
			if (id < this->carti[middle].get_id()) 
				return get_carte_by_id(id, leftbound, middle - 1);
			else 
				return get_carte_by_id(id, middle + 1, rightbound);
		}
	}

	/*
		Metoda utilizata pentru a returna
		cartea cu numarul de pagini cel mai apropiat
		de parametrul specificat.
	*/
	carte get_carte_with_closest_pages_to(int pagini) {
		int diferenta_minima = HUGE;
		int index = 0;
		for (int i = 0; i < this->size_biblioteca; i++) {
			int diferenta = abs(pagini - this->carti[i].get_pagini());
			if (diferenta < diferenta_minima) {
				diferenta_minima = diferenta;
				index = i;
			}
		}
		carte c = this->get_carte_by_index(index);
		cout << "Cartea cu un numar cel mai apropiat de pagini de " << pagini << " este:" << endl;
		cout << c.get_titlu() << ", scrisa de " << c.get_nume() << ", avand " << c.get_pagini() << " pagini.";
		return c;
	}

	/*
		Metoda utilizata pentru a returna
		cartea cu ID-ul cel mai apropiat de
		parametrul specificat.
	*/
	carte get_carte_with_closest_id_to(int id) {
		int diferenta_minima = HUGE;
		int index = 0;
		for (int i = 0; i < this->size_biblioteca; i++) {
			int diferenta = abs(this->carti[i].get_id() - id);
			if (diferenta < diferenta_minima) {
				diferenta_minima = diferenta;
				index = i;
			}
		}
		carte c = this->get_carte_by_index(index);
		cout << "Cartea cu cel mai apropiat ID este: ";
		cout << c.get_titlu() << ", scrisa de " << c.get_nume() << ", avand " << c.get_pagini() << " pagini.";
		return c;
	}

	/*
		Metoda utilizata pentru a returna o carte
		dupa un anumit index din vector.
	*/
	carte get_carte_by_index(int index) {
		return this->carti[index];
	}

	/*
		Metoda utilizata pentru a returna
		spatiul pe care il ocupa cartile
		in biblioteca (numarul de carti din
		biblioteca).
	*/
	int get_spatiu_biblioteca() {
		return this->size_biblioteca;
	}

	/*
		Metoda utilizata pentru a returna
		index-ul unei anumite carti din vector.
	*/
	int get_index(carte c) {
		for (int i = 0; i < this->size_biblioteca; i++) {
			if (this->carti[i].equals(c)) return i;
		}
		return NULL_INDEX;
	}

	/*
		Metoda folosita pentru a adauga
		o carte in vector.
		In acelasi timp, se incrementeaza
		spatiul/numarul de carti
		din biblioteca.
	*/
	void add_carte(carte c) {
		this->carti.push_back(c);
		this->size_biblioteca++;
	}

	/*
		Metoda folosita pentru a sterge
		o carte din vector.
		In acelasi timp, decrementam spatiul/
		numarul de carti din biblioteca.
	*/
	void remove_carte(carte c) {
		if (get_index(c) == NULL_INDEX) return;
		this->remove_carte_at(get_index(c));
	}

	/*
		Metoda utilizata pentru stergerea unei
		carti de la o anumita pozitie
		din biblioteca.
	*/
	void remove_carte_at(int index) {
		if (index > this->size_biblioteca) return;
		this->carti.erase(this->carti.begin() + index);
		this->size_biblioteca--;
	}
};
/*
	Functia main din programul
	nostru.
*/
int main() {
	/*
		Declaram biblioteca folosind
		constructorul creat in structura.
	*/
	biblioteca b = biblioteca();
	while (!(fin.eof)) {
		char s[512];
		fin.getline(s, 511);
	}
}
