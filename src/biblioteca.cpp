#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <string>
#include <stdlib.h>

#define NULL_CARTE carte("", 0, 0, "");
#define NULL_INDEX -1
#define HUGE 1e+300;

using namespace std;

struct carte {

private:
	string titlu, nume;
	int pagini, id;

public:

	carte(string titlu, int pagini, int id, string nume) {
		this->titlu = titlu;
		this->pagini = pagini;
		this->id = id;
		this->nume = nume;
	}

	string get_titlu() {
		return this->titlu;
	}

	int get_pagini() {
		return this->pagini;
	}

	int get_id() {
		return this->id;
	}

	string get_nume() {
		return this->nume;
	}

	bool equals(carte c) {
		return ((this->titlu == c.get_titlu())
			&& (this->nume == c.get_nume())
			&& (this->id == c.get_id())
			&& (this->pagini == c.get_pagini()));
	}

	void set_titlu(string titlu) {
		this->titlu = titlu;
	}

	void set_pagini(int pagini) {
		this->pagini = pagini;
	}

	void set_id(int id) {
		this->id = id;
	}

	void set_nume(string nume) {
		this->nume = nume;
	}
};

struct biblioteca {
private:
	vector<carte> carti;
	int size_biblioteca;
public:

	biblioteca() {
		this->size_biblioteca = 0;
	}

	vector<carte> get_carti() {
		return this->carti;
	}

	vector<carte> get_carti_by_autor(string autor) {
		vector<carte> carti_by_autor;
		int gasite = 0;
		for (int i = 0; i < this->size_biblioteca; i++)
			if (this->carti[i].get_nume() == autor) {
				carti_by_autor.push_back(this->carti[i]);
				gasite++;
			}
		cout << "Au fost gasite " << gasite << " carti care au fost scrise de " << autor;
		cout << endl;
		return carti_by_autor;
	}

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
			cout << endl;
			cout << "Au fost gasite " << gasite << " carti care au " << pagini << " pagini." << endl;
		}
		return carti_by_pagini;
	}

	carte get_carte_by_id(unsigned int id) {
		for (int i = 0; i < this->carti.size(); i++) {
			carte c = this->carti[i];
			if (c.get_id() == id) {
				return c;
				break;
			}
		}
		cout << "Nu a putut fi gasita o carte cu ID-ul " << id << "." << endl;
		return NULL_CARTE;
	}

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
		cout << c.get_titlu() << ", scrisa de " << c.get_nume() << ", avand " << c.get_pagini() << " pagini." << endl;
		return c;
	}

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
		cout << "Cartea cu cel mai apropiat ID de " << id << " este: ";
		cout << '"' << c.get_titlu() << '"' << ", scrisa de " << c.get_nume() << ", avand " << c.get_pagini() << " pagini.";
		return c;
	}

	carte get_carte_by_index(int index) {
		return this->carti[index];
	}

	int get_spatiu_biblioteca() {
		return this->size_biblioteca;
	}

	int get_index(carte c) {
		for (int i = 0; i < this->size_biblioteca; i++) {
			if (this->carti[i].equals(c)) return i;
		}
		return NULL_INDEX;
	}

	void add_carte(carte c) {
		this->carti.push_back(c);
		this->size_biblioteca++;
	}

	void remove_carte(carte c) {
		if (get_index(c) == NULL_INDEX) return;
		this->remove_carte_at(get_index(c));
	}

	void remove_carte_at(int index) {
		if (index > this->size_biblioteca) return;
		this->carti.erase(this->carti.begin() + index);
		this->size_biblioteca--;
	}

	void remove_all() {
		if (this->carti.size() == 0) return;
		this->carti.erase(this->carti.begin(), this->carti.end());
	}

	bool id_already_exists(int id) {
		for (int i = 0; i < this->carti.size(); i++) {
			carte c = this->carti[i];
			if (c.get_id() == id) return true;
		}
		return false;
	}
};

bool is_number(char s) {
	return s >= '0' && s <= '9';
}

bool is_number_string(string str) {
	for (int i = 0; i < str.length(); i++) {
		char s = str.at(i);
		if (!is_number(s)) return false;
	}
	return true;
}

int string_to_int(string str) {
	int nr = 0;
	for (int i = 0; i < str.length(); i++) {
		char ch = str.at(i) - 48;
		nr *= 10;
		nr += ch;
	}
	return nr;
}

vector<string> titles, authors;
vector<int> pages, ids;
biblioteca b = biblioteca();

void afisare_numar_carti() {
	cout << "Aceasta biblioteca contine un numar de: " << b.get_spatiu_biblioteca() << " carti!" << endl;
}

void afisare_carti() {
	int gasite = 0;
	for (int i = 0; i < b.get_carti().size(); i++) {
		carte c = b.get_carte_by_index(i);
		cout << "Cartea #" << (i + 1) << " -> " << '"' << c.get_titlu() << '"' << ", scrisa de " << c.get_nume() << " (" << c.get_pagini() << " pagini - ID: " << c.get_id() << ")" << endl;
		gasite++;
	}
	if (gasite == 0) cout << "Nu a fost gasita nicio carte in biblioteca!";
}

bool contains(vector<string> v, string s) {
	for (int i = 0; i < v.size(); i++) {
		if (v[i] == s) return true;
	}
	return false;
}

void afisare_autori() {
	vector<string> autori;
	for (int i = 0; i < b.get_carti().size(); i++) {
		carte c = b.get_carte_by_index(i);
		if (!contains(autori, c.get_nume())) autori.push_back(c.get_nume());
	}
	cout << "Autorii din biblioteca sunt: ";
	int gasiti = 0;
	for (int i = 0; i < autori.size(); i++) {
		if (i == autori.size() - 1) cout << autori[i] << "." << endl;
		else cout << autori[i] << ", ";
		gasiti++;
	}
	if (gasiti == 0) cout << "- (NICIUN AUTOR NU A FOST GASIT - BIBLIOTECA GOALA?)";
}

void afisare_cea_mai_apropiata_de_id(int id) {
	b.get_carte_with_closest_id_to(id);
}

void afisare_cea_mai_apropiata_de_pagini(int pagini) {
	b.get_carte_with_closest_pages_to(pagini);
}

void cleanup_console() {
	system("CLS");
}

void display_message() {
	cout << "Bun venit in meniu!" << endl << "Acesta poate fi utilizat cu urmatoarele controale:" << endl
		<< "TASTA 0 -> Opreste executia programului" << endl
		<< "TASTA 1 -> Adauga/inregistreaza noi carti in biblioteca" << endl
		<< "TASTA 2 -> Afiseaza autorii disponibili din biblioteca" << endl
		<< "TASTA 3 -> Afiseaza toate cartile disponibile in biblioteca" << endl
		<< "TASTA 4 -> Cauta o carte dupa un anumit ID" << endl
		<< "TASTA 5 -> Cauta o carte dupa un anumit numar de pagini" << endl
		<< "TASTA 6 -> Afiseaza toate cartile scrise de un autor" << endl
		<< "TASTA 7 -> Initializeaza biblioteca (adaugand cartile deja inregistrate la cu ajutorul tastei 1)" << endl
		<< "Alege o optiune: ";
	return;
}

void afisare_carte(carte c) {
	cout << "################################"
		<< endl
		<< "Se afiseaza detalii despre carte:" << endl
		<< "Titlu: " << c.get_titlu() << endl
		<< "Autor: " << c.get_nume() << endl
		<< "Numar de pagini: " << c.get_pagini() << endl
		<< "ID: #" << c.get_id() << endl
		<< "################################";
}

void afisare_carti_dupa_autor() {
	string autor;
	cout << "Introdu numele autorului dupa care doresti sa cauti: " << endl;
	cin >> autor;
	vector<carte> v = b.get_carti_by_autor(autor);
	for (int i = 0; i < v.size(); i++) {
		afisare_carte(v[i]);
	}
}

void register_book() {
	string titlu, autor;
	int pagini, id;
	cout << "################################" << endl;
	cout << "Titlul cartii: ";
	cin >> titlu;
	cout << "Autorul cartii: ";
	cin >> autor;
	cout << "Numarul de pagini ale cartii: ";
	cin >> pagini;
	cout << "ID-ul cartii: ";
	cin >> id;
	cout << "################################";
	if (b.id_already_exists(id)) {
		cout << endl << "O carte cu acest ID deja exista! Te rog sa introduci iar detaliile cartii.";
		register_book();
	}
	else {
		titles.push_back(titlu);
		authors.push_back(autor);
		pages.push_back(pagini);
		ids.push_back(id);
	}
}

void cauta_dupa_id() {
	int id;
	cout << endl << "Introdu ID-ul dupa care doresti sa executi query-ul: ";
	cin >> id;
	carte c = b.get_carte_by_id(id);
	if (c.get_id() == 0)
		return;
	afisare_carte(c);
}

void cauta_dupa_pagini() {
	int pagini;
	cout << endl << "Introdu numarul de pagini dupa care doresti sa executi query-ul: " << endl;
	cin >> pagini;
	vector<carte> gasite = b.get_carti_by_pagini(pagini);
	for (int i = 0; i < gasite.size(); i++)
		afisare_carte(gasite[i]);
}

void register_books() {
	cout << endl << "Introdu numarul de carti pe care doresti sa-l adaugi in biblioteca: ";
	int n;
	cin >> n;
	string titlu, autor;
	int pagini, id;
	int i = 0;
	for (i = 0; i < n; i++) {
		register_book();
	}
}

void setup_biblioteca() {
	//auto start = chrono::system_clock::now();
	b.remove_all();
	for (int i = 0; i < titles.size(); i++) {
		carte c = carte(titles[i], pages[i], ids[i], authors[i]);
		b.add_carte(c);
	}
	//auto end = chrono::system_clock::now();
	//std::chrono::duration<double> elapsed_seconds = end - start;
	cout << "Cartile au fost inregistrare cu succes in biblioteca!" << endl;
	afisare_numar_carti();
	afisare_carti();
}

void pause() {
	cout << endl << "Acest mesaj se va sterge automat dupa 5 secunde.";
	_sleep(5000);
}

void init() {
	display_message();
	int option;
	cin >> option;
	while (option != 0) {
		switch (option) {
		case 1:
			register_books();
			break;
		case 2:
			afisare_autori();
			break;
		case 3:
			afisare_carti();
			break;
		case 4:
			cauta_dupa_id();
			break;
		case 5:
			cauta_dupa_pagini();
			break;
		case 6:
			afisare_carti_dupa_autor();
			break;
		case 7:
			setup_biblioteca();
			break;
		}
		pause();
		cleanup_console();
		display_message();
		cin >> option;
	}
}

int main(void) {
	init();
}
