# DEL 1: MariaDB installasjon og oppstart i terminalen (med Homebrew)

## Installer Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Installer MariaDB
```bash
brew install mariadb
```

## Start MariaDB som en tjeneste
```bash
brew services start mariadb
```

## Kjør MariaDB som root
```bash
sudo mariadb -u root
```

# DEL 2: Oppretting av bruker
## Lage bruker (bytt 'brukernavn' og 'passord' med noe enkelt)
```bash
CREATE USER "brukernavn"@"localhost" IDENTIFIED BY "passord";
```

## Gi bruker tilgang til database
```bash
GRANT ALL PRIVILEGES ON *.* TO "brukernavn"@"localhost";
```

## "Refreshe" tilgang
```bash
FLUSH PRIVILEGES;
```

# DEL 3: Vanlige SQL-spørringer og kommandoer
## Lage database
```bash
CREATE DATABASE databasenavn;
```

## Vise alle databaser
```bash
SHOW DATABASES;
```

## Lage tabell
```bash
CREATE TABLE tabellnavn(kolonne1 VARCHAR(255), kolonne2 INT);
```

## Se strukturen til tabellen
```bash
DESCRIBE tabellnavn;
```

## Legge inn data i tabellen
```bash
INSERT INTO tabellnavn VALUES('verdi1', 'verdi2');
```

## Hente data fra tabellen
```bash
SELECT * FROM tabellnavn;
```

## Gå ut av MariaDB
```bash
EXIT;
```

# DEL 4: Instalasjon av Flask
## Installer python med brew
```bash
brew install python
```


## Skjekk om python er installert?
```bash
python3 --version
pip3 --version
```
## Hvis pip ikke funker
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

## Installere flask fra terminal
```bash
pip install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator virtualenv flask pymysql
```
