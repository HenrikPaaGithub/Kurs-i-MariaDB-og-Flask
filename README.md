# MariaDB installasjon og oppstart i terminalen (med Homebrew)

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
brew service start mariadb
```

## Kjør MariaDB som root
```bash
sudo mariadb -u root
```

# Oppretting av bruker
## Lage bruker
```bash
CREATE USER 'brukernavn'@'localhost' IDENTIFIED BY 'passord';
```

## Gi tilgang
```bash
GRANT ALL PRIVILEGES ON databasenavn.* TO 'brukernavn'@'localhost';
```

## "Refreshe" tilgang
```bash
FLUSH PRIVILEGES;
```
