### Tips

# cmd python 

Installe les dépendances via Poetry
```
make -C app install
```
Met à  jour toutes les dépendances
```
make -C app update
```

Lance flake8 sur ton code (poetry run flake8 .)
```
make -C app lint
```

Supprime tous les fichiers de cache Python (__pycache__, etc.)
```
make -C app clean
```

Lance les tests unitaires (pytest) (quand tu en auras)
```
make -C app test
```