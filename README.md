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

# MariaDB installasjon og oppstart i terminalen (med Homebrew)
## Lage bruker
```bash
CREATE USER 'brukernavn'@'localhost' IDENTIFIED BY 'passord';
```

## Gi tilgang
```bash
GRANT ALL PRIVILEGES ON minapp.* TO 'brukernavn'@'localhost';
```
