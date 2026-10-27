# Ontología: árbol genealógico familiar

## Clases y personas

- **Persona**: clase general para representar a los integrantes de la familia.
- **Juan, Carlos, Ana, Luis, Sofía y Mateo**: instancias de `Persona`.

## Predicados y relaciones

| Predicado | Significado | Ejemplo |
|---|---|---|
| `padre(X, Y)` | X es padre de Y | `padre(juan, carlos)` |
| `hijo(X, Y)` | X es hijo de Y; relación inversa de `padre` | `hijo(carlos, juan)` |
| `abuelo(X, Y)` | X es abuelo de Y | `abuelo(juan, luis)` |
| `hermano(X, Y)` | X e Y comparten padre y son personas distintas | `hermano(luis, sofia)` |
| `ancestro(X, Y)` | X es padre, abuelo u otro antepasado de Y | `ancestro(juan, mateo)` |

## Hechos de la base de conocimiento

Los hechos declarados son:

```text
padre(juan, carlos)
padre(juan, ana)
padre(carlos, luis)
padre(carlos, sofia)
padre(luis, mateo)
```

Las relaciones `hijo`, `abuelo`, `hermano` y `ancestro` se obtienen aplicando reglas a los hechos declarados.

## Reglas de inferencia

- **R1 — Hijo:** si `padre(X, Y)`, entonces `hijo(Y, X)`.
- **R2 — Abuelo:** si `padre(X, Y)` y `padre(Y, Z)`, entonces `abuelo(X, Z)`.
- **R3 — Hermanos:** si `padre(Z, X)` y `padre(Z, Y)` y `X` es distinto de `Y`, entonces `hermano(X, Y)`.
- **R4 — Ancestro:** si `padre(X, Y)`, entonces `ancestro(X, Y)`. Si `ancestro(X, Y)` y `padre(Y, Z)`, entonces `ancestro(X, Z)`.

## Diagrama de la ontología

<img width="1401" height="2473" alt="Diagrama en blanco" src="https://github.com/user-attachments/assets/83d210bd-dcd0-4022-bdc1-9018c4ebbff5" />
