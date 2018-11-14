CREATE TABLE Location (
	year INT PRIMARY KEY,
	city VARCHAR(255) NOT NULL
); 

CREATE TABLE Athlete (
	athlete VARCHAR(255) NOT NULL,
	country VARCHAR(255) NOT NULL,
	athlete_id INT PRIMARY KEY AUTOINCREMENT,
	gender VARCHAR(255) NOT NULL,
	UNIQUE (athlete, country, gender)
);

CREATE TABLE Event (
	event VARCHAR(255) NOT NULL PRIMARY KEY,
	discipline VARCHAR(255) NOT NULL,
	sport VARCHAR(255) NOT NULL
);

CREATE TABLE Participant (
	year INT NOT NULL,
	medal VARCHAR(255) NOT NULL,
	event VARCHAR(255) NOT NULL,
	athlete_id INT,
	PRIMARY KEY (year, medal, event),
	FOREIGN KEY (year) REFERENCES Location(year) ON DELETE RESTRICT,
	FOREIGN KEY (event) REFERENCES Event(event) ON DELETE RESTRICT,
	FOREIGN KEY (athlete_id) REFERENCES Athlete(athlete_id) ON DELETE RESTRICT
);