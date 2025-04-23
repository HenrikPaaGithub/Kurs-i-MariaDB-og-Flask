# MariaDB installasjon og oppstart (Homebrew)

## Installer Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Installer MariaDB
```bash
brew install mariadb
```

## Start MySQL-server (hvis nødvendig)
```bash
mysql.server start
```

## Kjør MariaDB som root
```bash
sudo mariadb -u root
```

## Start MariaDB som en tjeneste
```bash
brew service start mariadb
```
