CREATE TABLE Participant (
	year INTEGER NOT NULL,
	medal TEXT NOT NULL,
	event TEXT NOT NULL,
	athlete_id INTEGER,
	PRIMARY KEY (year, medal, event),
	FOREIGN KEY (year) REFERENCES Location(year) ON DELETE RESTRICT,
	FOREIGN KEY (event) REFERENCES Event(event) ON DELETE RESTRICT,
	FOREIGN KEY (athlete_id) REFERENCES Athlete(athlete_id) ON DELETE RESTRICT
);

CREATE TABLE Location (
	year INTEGER PRIMARY KEY,
	city TEXT NOT NULL
);

CREATE TABLE Athlete (
	athlete TEXT NOT NULL,
	country TEXT NOT NULL,
	athlete_id INTEGER PRIMARY KEY AUTOINCREMENT,
	gender TEXT NOT NULL,
	UNIQUE (athlete, country, gender)
);

CREATE TABLE Event (
	event TEXT NOT NULL PRIMARY KEY,
	discipline TEXT NOT NULL,
	sport TEXT NOT NULL
);
