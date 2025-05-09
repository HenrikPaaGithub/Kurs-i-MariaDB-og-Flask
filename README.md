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
## Lage bruker
```bash
CREATE USER 'brukernavn'@'localhost' IDENTIFIED BY 'passord';
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

## Gi bruker tilgang til database
```bash
GRANT ALL PRIVILEGES ON databasenavn.* TO 'brukernavn'@'localhost';
```

## "Refreshe" tilgang
```bash
FLUSH PRIVILEGES;
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
