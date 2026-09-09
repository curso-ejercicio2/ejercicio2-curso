# Ejercicio 2 - Git (Todo el curso)

Repositorio compartido por todos los equipos de Ingeniería de Software (is_6) para practicar:

- Workflow de ramas (main, develop, feature)
- Pull Requests hacia develop
- Resolución de conflictos de merge
- Code review por líderes

## Estructura

- `main.py`: menú principal
- `operaciones/`: una función por archivo (suma.py, resta.py, multiplicacion.py, modulo.py, division.py, etc.)

## Flujo de trabajo

1. Crear rama `feature/<equipo>-<nombre>` desde `develop`
2. Trabajar en tu operación
3. Commit atómico con mensaje descriptivo
4. Push y abrir Pull Request hacia `develop`
5. Un líder aprueba y mergea

## Reglas

- No commitear directo a `main` ni `develop`
- Antes de pushear, traer cambios de `develop` a tu rama
- Resolver conflictos localmente antes de pushear
- Mínimo 8 commits por equipo