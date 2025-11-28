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

