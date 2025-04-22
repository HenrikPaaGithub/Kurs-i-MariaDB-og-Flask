# MariaDB installasjon og oppstart (Homebrew)

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
