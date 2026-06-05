# Projects

CLI para crear proyectos de Node.js, Python, Go y Bash con las frameworks más populares.

## Instalación

### Opción 1: Usar con UV (desarrollo)

```bash
uv sync
uv run main.py
```

### Opción 2: Ejecutable para Linux

Descarga el ejecutable desde `dist/projects` y ejecútalo directamente:

```bash
./dist/projects
```

## Uso

El CLI muestra un menú interactivo con las siguientes opciones:

```
Projects
? Seleccione una opción: (Use las teclas ←↑↓→ para navegar)
❯ Astro
  Vite
  Angular
  UV
  Rspack
  Flowbite
  Go
  Bun
  Bash
  Salir
```

## Frameworks disponibles

### Frontend / JavaScript

| Framework | Descripción | Tailwind CSS | Adaptador Node |
|-----------|-------------|:------------:|:--------------:|
| **Astro** | Framework estático con soporte islands | ✅ | ✅ |
| **Vite** | Build tool con HMR ultrarrápido | ✅ | ❌ |
| **Angular** | Framework completo de Google | ✅ | ❌ |
| **Rspack** | Bundler Rust-compatible con Webpack | ✅ | ❌ |
| **Flowbite** | React con componentes Tailwind | ❌ | ❌ |
| **Bun** | Runtime JavaScript alternativo | ❌ | ❌ |

### Backend / Otros

| Framework | Descripción |
|-----------|-------------|
| **UV** | Proyecto Python con gestor de paquetes UV |
| **Go** | Proyecto Go con módulos (auto-descarga de Go) |
| **Bash** | Script Bash ejecutable con permisos 755 |

## Características principales

- **Instalación automática de dependencias**: Detecta y instala herramientas faltantes (Angular CLI, Bun, Go)
- **Soporte Tailwind CSS**: Opción de instalar Tailwind en frameworks compatibles
- **Banner ASCII**: Interfaz visual con arte ASCII al iniciar
- **Spinners**: Indicadores de progreso durante instalaciones
- **Detección de shell**: Configura PATH automáticamente para Go (bash, zsh, fish)

## Dependencias

### Python

- [InquirerPy](https://github.com/kazhala/InquirerPy) - Interfaz de línea de comandos interactiva
- [Halo](https://github.com/manrajgrover/halo) - Spinner para terminal
- [PyFiglet](https://github.com/pwaller/pyfiglet) - Generación de banner ASCII
- [Requests](https://github.com/psf/requests) - HTTP client para descarga de Go

### Herramientas externas (instaladas automáticamente)

- Angular CLI (`@angular/cli`)
- Bun runtime
- Go language (desde go.dev)
- UV (se asume preinstalado)
