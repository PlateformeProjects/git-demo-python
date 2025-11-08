# git-demo-python

Projet de démonstration Python avec :
- Fonctions mathématiques simples
- Tests unitaires avec **pytest**
- Pipeline **CI/CD GitHub Actions** qui exécute les tests à chaque push / pull request
- Protection de la branche `main`
- Vérification via deux comptes GitHub (accès + restrictions)

## Installation

```bash
git clone git@github.com:PlateformeProjects/git-demo-python.git
cd git-demo-python
pip install -r requirements.txt
pytest -vv
```

## Structure

```
git-demo-python/
├── src/
│   └── calculator.py
├── tests/
│   └── test_calculator.py
├── requirements.txt
├── main.py
└── .github/workflows/ci.yml
```


## Protection de la branche `main`

GitHub → Repository → Settings → Branches → Add rule :

- `main`
- Require a pull request before merging
- Require status checks to pass before merging
- Sélectionner : `CI Tests / test`
- (Optionnel) Include administrators

## Utiliser deux comptes GitHub en local

### Générer une clé SSH pour le second compte

```bash
ssh-keygen -t ed25519 -C "u4672563718@gmail.com" -f ~/.ssh/id_ed25519_b
```

Ajouter la clé publique dans GitHub :
Settings → SSH and GPG keys → New SSH key

### Configurer `~/.ssh/config`

```bash
nano ~/.ssh/config
```

```
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519

Host github-b
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_b
```