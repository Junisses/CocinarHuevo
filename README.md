# 🥚 Cocina tu Huevo - App con Tkinter

**Cocina tu Huevo** es una aplicación de escritorio hecha en Python con Tkinter que permite al usuario seleccionar diferentes tipos de huevo y visualizar los ingredientes y tiempo de cocción correspondiente.

> ⚠️ Este proyecto está en una **fase inicial de desarrollo**, por lo que aún hay bugs por corregir y muchas mejoras por implementar.

---

## 🚧 Estado del proyecto

- ✅ Funciona la navegación entre pantallas (selección y detalle del huevo).
- ✅ Se muestra el tiempo y los ingredientes del huevo seleccionado.
- ✅ Cuenta con un temporizador funcional por tipo de huevo.
- 🐞 **Faltan mejoras importantes:**
  - Mejorar el diseño de la interfaz (estética básica por ahora).
  - Añadir animaciones o transiciones entre pantallas.
  - Incorporar sonidos al finalizar la cocción.
  - Mejorar manejo de errores (como el temporizador que pare o inicie de 0 al dar a volver).

---

## 🧠 ¿Cómo funciona?

1. Al ejecutar la app, se muestra una pantalla con botones por tipo de huevo (duro, frito, a la copa, revuelto).
2. Al seleccionar un tipo, se abre una nueva pantalla que muestra:
   - Ingredientes necesarios.
   - Tiempo estimado de cocción.
   - Un botón para iniciar el temporizador.
3. Al terminar el tiempo, se muestra una alerta indicando que el huevo está listo.

---

## ▶️ Ejecución del proyecto

### 1. Requisitos

- Python 3.6 instalado (también lo probe con python 3.8 y funciona)
- No requiere librerías externas, solo `tkinter` (incluido con Python)
- Proximamente incluira librerias externas.

### 2. Estructura del proyecto
```
CocinarHuevo/
├── assets/
│ ├── duro.png
│ ├── frito.png
│ ├── copa.png
│ └── revuelto.png
├── backend/
│ ├── huevo_data.py
│ └── timer_logic.py
├── frontend/
│ └── components/
│    ├── egg_select_page.py
│    └── egg_detail_page.py
│ └── main_ui.py
├── main.py
├── requirements.txt
└── README.md
```

### 3. Ejecutar

Desde la raíz del proyecto, corre el siguiente comando:

```
python main.py
```
---
## ✨ Próximas mejoras (por implementar)
 - Estilos y diseño más atractivo (fuentes, colores, disposición).
 - Animaciones al cambiar de pantalla.
 - Sonidos personalizados al terminar la cocción.
 - Empaquetar como aplicación ejecutable (.exe o .app).

## 📬 Contribuciones

Este proyecto es educativo y experimental. Si deseas aportar mejoras, sugerencias o correcciones, hablemos: https://www.linkedin.com/in/junisse-campos-aa9038198/

---
🧑‍💻 Desarrollado por Junisse Campos — 2025
